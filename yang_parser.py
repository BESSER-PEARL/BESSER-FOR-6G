import json
from typing import Any, Dict, List
from structural import (Class, DataType, DomainModel, Property, Method,
                       PrimitiveDataType, Enumeration, EnumerationLiteral)

class YangParser:
    def __init__(self):
        self.model = DomainModel("3GPPModel")
        self.current_model = None
        self.current_class = None
        self.prefix_map = {}  # Maps prefixes to their module names
        self.processed_types = set()  # Keep track of processed type names

    def parse_file(self, filepath: str, model_name: str) -> DomainModel:
        """Parse a YANG JSON file and create a new model."""
        self.current_model = DomainModel(model_name)
        try:
            with open(filepath, 'r') as f:
                data = json.load(f)
            
            # Check if data is a dictionary and contains 'module'
            if not isinstance(data, dict):
                print(f"Warning: File {filepath} does not contain a valid JSON object")
                return self.current_model
            
            # Extract module if it exists
            module = data.get('module')
            if not module:
                print(f"Warning: File {filepath} does not contain a 'module' key")
                return self.current_model
            
            # Extract module name and prefix mappings from imports
            module_name = module.get('@name', '')
            
            # Store prefix mappings
            if 'import' in module:
                imports = module['import']
                if not isinstance(imports, list):
                    imports = [imports]
                for imp in imports:
                    prefix = imp.get('prefix', {}).get('@value')
                    module_ref = imp.get('@module')
                    if prefix and module_ref:
                        self.prefix_map[prefix] = module_ref
            
            return self.parse_module(module)
        except json.JSONDecodeError:
            print(f"Warning: File {filepath} is not a valid JSON file")
            return self.current_model
        except Exception as e:
            print(f"Warning: Error processing file {filepath}: {str(e)}")
            return self.current_model

    def parse_module(self, module: Dict[str, Any]) -> DomainModel:
        """Parse the module section and create corresponding model elements."""
        module_name = module.get('@name', '')
        self.current_model.name = module_name

        # Parse typedefs first as they can define enums
        if 'typedef' in module:
            typedefs = module['typedef']
            # Handle both single typedef and list of typedefs
            if isinstance(typedefs, list):
                for typedef in typedefs:
                    self.parse_typedef(typedef)
            else:
                self.parse_typedef(typedefs)

        # Parse groupings as they define types
        if 'grouping' in module:
            groupings = module['grouping']
            if isinstance(groupings, list):
                for grouping in groupings:
                    self.parse_grouping(grouping)
            else:
                self.parse_grouping(groupings)

        # Parse augments which contain the main class definitions
        if 'augment' in module:
            self.parse_augment(module['augment'])

        return self.current_model

    def parse_typedef(self, typedef: Dict[str, Any]) -> None:
        """Parse a typedef definition and create an enumeration if it defines one."""
        type_info = typedef.get('type', {})
        if type_info.get('@name') == 'enumeration':
            enum_name = typedef['@name']
            
            # Skip if we've already processed this type
            if enum_name in self.processed_types:
                return
            
            enum_type = Enumeration(name=enum_name)
            
            # Add enumeration literals
            if 'enum' in type_info:
                enums = type_info['enum'] if isinstance(type_info['enum'], list) else [type_info['enum']]
                for enum in enums:
                    literal_name = enum.get('@name', '')
                    literal = EnumerationLiteral(name=literal_name, owner=enum_type)
                    enum_type.add_literal(literal)
            
            self.current_model.add_type(enum_type)
            self.processed_types.add(enum_name)

    def parse_grouping(self, grouping: Dict[str, Any]) -> None:
        """Parse a grouping definition and create a class."""
        class_name = grouping['@name']
        
        # Skip if we've already processed this type
        if class_name in self.processed_types:
            return
        
        class_desc = grouping.get('description', {}).get('text', '')
        
        # Create new class
        new_class = Class(name=class_name)
        self.current_class = new_class
        
        # Add attributes from leaves
        if 'leaf' in grouping:
            leaves = grouping['leaf'] if isinstance(grouping['leaf'], list) else [grouping['leaf']]
            for leaf in leaves:
                self.parse_leaf(leaf)

        # Add attributes from lists
        if 'list' in grouping:
            lists = grouping['list'] if isinstance(grouping['list'], list) else [grouping['list']]
            for list_def in lists:
                self.parse_list(list_def)

        self.current_model.add_type(new_class)
        self.processed_types.add(class_name)

    def parse_augment(self, augment: Dict[str, Any]) -> None:
        """Parse augment section which contains the main class definitions."""
        if 'list' in augment:
            list_def = augment['list']
            class_name = list_def['@name']
            class_desc = list_def.get('description', {}).get('text', '')

            new_class = Class(name=class_name)
            self.current_class = new_class

            # Parse attributes container if it exists
            if 'container' in list_def:
                container = list_def['container']
                if 'uses' in container:
                    self.parse_uses(container['uses'])

            self.current_model.add_type(new_class)

    def parse_leaf(self, leaf: Dict[str, Any]) -> None:
        """Parse a leaf definition and create a property."""
        name = leaf['@name']
        desc = leaf.get('description', {}).get('text', '')
        mandatory = leaf.get('mandatory', {}).get('@value', 'false') == 'true'

        # Determine type
        type_info = leaf.get('type', {})
        type_name = type_info.get('@name', 'string')
        
        # Map YANG types to primitive types
        type_mapping = {
            'string': 'string',
            'boolean': 'boolean',
            'uint8': 'integer',
            'uint16': 'integer',
            'uint32': 'integer',
            'uint64': 'integer',
            'int8': 'integer',
            'int16': 'integer',
            'int32': 'integer',
            'int64': 'integer',
            'decimal64': 'float',
            'boolean': 'bool'
        }
        type_name = type_mapping.get(type_name, type_name)

        # Create property with proper type
        prop = Property(
            name=name,
            type=type_name,
            owner=self.current_class,
            is_read_only=not mandatory
        )

        self.current_class.add_attribute(prop)

    def parse_list(self, list_def: Dict[str, Any]) -> None:
        """Parse a list definition and create a property for it."""
        name = list_def['@name']
        desc = list_def.get('description', {}).get('text', '')

        # Lists are typically collections, so we make them a property of type list
        prop = Property(
            name=name,
            type='list',  # This could be refined based on the list contents
            owner=self.current_class
        )

        self.current_class.add_attribute(prop)

    def parse_uses(self, uses: Dict[str, Any]) -> None:
        """Parse uses statement which references a grouping."""
        grouping_name = uses.get('@name', '')
        # Find referenced class and inherit from it
        referenced_class = self.current_model.get_class_by_name(grouping_name)
        if referenced_class and self.current_class:
            # Copy attributes from referenced class
            for attr in referenced_class.attributes:
                self.current_class.add_attribute(attr)

    def resolve_type_reference(self, type_name: str) -> str:
        """Resolve type references with prefixes (e.g., types3gpp:DistinguishedName)"""
        if ':' in type_name:
            prefix, name = type_name.split(':')
            if prefix in self.prefix_map:
                # The type is defined in another module
                referenced_module = self.prefix_map[prefix]
                # Return the full type name
                return f"{referenced_module}.{name}"
        return type_name
