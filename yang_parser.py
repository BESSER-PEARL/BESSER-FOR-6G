import json
from typing import Any, Dict, List
from besser.BUML.metamodel.structural import (Class, DataType, DomainModel, Property, Method,
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
        
        # Add module description as a synonym for the model if it exists
        if 'description' in module:
            desc = module.get('description', {}).get('text', '')
            if desc:
                self.current_model.synonyms = [desc]

        # Parse imports first to build prefix map
        if 'import' in module:
            imports = module['import']
            if not isinstance(imports, list):
                imports = [imports]
            for imp in imports:
                prefix = imp.get('prefix', {}).get('@value')
                module_ref = imp.get('@module')
                if prefix and module_ref:
                    self.prefix_map[prefix] = module_ref

        # Parse typedefs first as they define types used by other elements
        if 'typedef' in module:
            typedefs = module['typedef']
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

        # Parse lists and containers which define the main classes
        if 'list' in module:
            lists = module['list']
            if isinstance(lists, list):
                for list_def in lists:
                    self.parse_list(list_def)
            else:
                self.parse_list(lists)

        # Parse any augments
        if 'augment' in module:
            augments = module['augment']
            if isinstance(augments, list):
                for augment in augments:
                    self.parse_augment(augment)
            else:
                self.parse_augment(augments)

        return self.cleanup_grp_classes(self.current_model)

    def parse_typedef(self, typedef: Dict[str, Any]) -> None:
        """Parse a typedef definition and create an enumeration if it defines one."""
        type_info = typedef.get('type', {})
        if isinstance(type_info, dict) and type_info.get('@name') == 'enumeration':
            enum_name = typedef.get('@name')
            
            # Skip if we've already processed this type
            if enum_name in self.processed_types:
                return
            
            enum_type = Enumeration(name=enum_name)
            
            # Add description as a synonym if available
            if 'description' in typedef:
                desc = typedef.get('description', {}).get('text', '')
                if desc:
                    enum_type.synonyms = [desc]
            
            # Add enumeration literals
            if 'enum' in type_info:
                enums = type_info['enum'] if isinstance(type_info['enum'], list) else [type_info['enum']]
                for enum in enums:
                    literal_name = enum.get('@name', '')
                    if literal_name:  # Only add if we have a valid name
                        literal = EnumerationLiteral(name=literal_name, owner=enum_type)
                        
                        # Add description as a synonym for the literal if available
                        if 'description' in enum:
                            literal_desc = enum.get('description', {}).get('text', '')
                            if literal_desc:
                                literal.synonyms = [literal_desc]
                                
                        enum_type.add_literal(literal)
            
            # Add the enumeration to the model
            self.current_model.add_type(enum_type)
            self.processed_types.add(enum_name)

    def parse_grouping(self, grouping: Dict[str, Any]) -> None:
        """Parse a grouping definition and create a class."""
        class_name = grouping['@name']
        
        # Skip if we've already processed this type
        if class_name in self.processed_types:
            return
        
        # Get description if available
        desc = grouping.get('description', {}).get('text', '')
        
        # Create new class
        new_class = Class(name=class_name)
        
        # Add description as a synonym if available
        if desc:
            new_class.synonyms = [desc]
            
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
            
            # Add description as a synonym if available
            if class_desc:
                new_class.synonyms = [class_desc]
                
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
        
        # Handle special types with hyphens
        if isinstance(type_name, str) and '-' in type_name:
            type_name = type_name.replace('-', '_')

        # Map YANG types to primitive types
        type_mapping = {
            'string': 'StringType',
            'boolean': 'BooleanType',
            'uint8': 'IntegerType',
            'uint16': 'IntegerType',
            'uint32': 'IntegerType',
            'uint64': 'IntegerType',
            'int8': 'IntegerType',
            'int16': 'IntegerType',
            'int32': 'IntegerType',
            'int64': 'IntegerType',
            'decimal64': 'FloatType',
            'integer': 'IntegerType',
            'integer_percentage': 'IntegerType',
            'DistinguishedName': 'StringType',
            'DateAndTime': 'DateTimeType',
            'DateTime': 'DateTimeType',
            'Duration': 'TimeDeltaType',
            'Float': 'FloatType',
            'domain_name': 'StringType',
            'ip_address': 'StringType',
            'host': 'StringType',
            'date_and_time': 'DateTimeType',
            'instance_identifier': 'StringType',
            'enumeration': 'EnumerationType'
        }
        
        # Try to map the type
        if type_name not in type_mapping:
            # For unknown types, create a StringType
            type_name = 'StringType'
        else:
            type_name = type_mapping[type_name]

        # Create property with proper type
        prop = Property(
            name=name,
            type=type_name,
            owner=self.current_class,
            is_read_only=not mandatory
        )
        
        # Add description as a synonym if available
        if desc:
            prop.synonyms = [desc]

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
        
        # Add description as a synonym if available
        if desc:
            prop.synonyms = [desc]

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

    def cleanup_grp_classes(self, model: DomainModel) -> DomainModel:
        """Merge *Grp classes into their base classes and remove the Grp classes."""
        classes_to_remove = set()
        classes_to_update = {}

        # Find all classes ending with 'Grp'
        for type_obj in model.types:
            if isinstance(type_obj, Class) and type_obj.name.endswith('Grp'):
                base_name = type_obj.name[:-3]  # Remove 'Grp' suffix
                
                # Find the corresponding base class
                base_class = next(
                    (c for c in model.types 
                     if isinstance(c, Class) and c.name == base_name), 
                    None
                )

                if base_class:
                    # Merge attributes from Grp class into base class
                    for attr in type_obj.attributes:
                        base_class.add_attribute(attr)
                    classes_to_remove.add(type_obj)
                else:
                    # If no base class exists, rename this class by removing 'Grp'
                    classes_to_update[type_obj] = base_name

        # Update class names for those without a base class
        for cls, new_name in classes_to_update.items():
            cls.name = new_name

        # Remove merged Grp classes
        model.types = {t for t in model.types if t not in classes_to_remove}
        
        return model
