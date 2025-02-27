import json
import os
from typing import Any, Dict, List, Set, Optional
from besser.BUML.metamodel.structural import (Class, DataType, DomainModel, Property, Method,
                       PrimitiveDataType, Enumeration, EnumerationLiteral, Multiplicity)

class YangParser:
    def __init__(self):
        self.model = DomainModel("3GPPModel")
        self.current_model = None
        self.current_class = None
        self.prefix_map = {}  # Maps prefixes to their module names
        self.processed_types = set()  # Keep track of processed type names
        self.imported_models = {}  # Maps module names to their domain models

    def parse_file(self, filepath: str, model_name: str, base_dir: Optional[str] = None) -> DomainModel:
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
            
            # Store prefix mappings and try to load imported models
            if 'import' in module:
                imports = module['import']
                if not isinstance(imports, list):
                    imports = [imports]
                for imp in imports:
                    prefix = imp.get('prefix', {}).get('@value')
                    module_ref = imp.get('@module')
                    if prefix and module_ref:
                        self.prefix_map[prefix] = module_ref
                        
                        # Try to load the imported model if we have a base directory
                        if base_dir and module_ref not in self.imported_models:
                            imported_file = os.path.join(base_dir, f"{module_ref}.json")
                            if os.path.exists(imported_file):
                                try:
                                    imported_model = YangParser().parse_file(imported_file, module_ref, base_dir)
                                    self.imported_models[module_ref] = imported_model
                                    print(f"Imported model {module_ref} from {imported_file}")
                                except Exception as e:
                                    print(f"Failed to import model {module_ref}: {e}")
            
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

    def find_type_in_imported_models(self, type_name: str) -> Any:
        """Find a type in imported models by name"""
        # Split type reference into module and type name if it contains a prefix
        if ':' in type_name:
            prefix, local_name = type_name.split(':', 1)
            if prefix in self.prefix_map:
                module_name = self.prefix_map[prefix]
                if module_name in self.imported_models:
                    imported_model = self.imported_models[module_name]
                    return imported_model.get_type_by_name(local_name)
        return None

    def resolve_type_reference(self, type_name: str) -> str:
        """Resolve type references with prefixes (e.g., types3gpp:DistinguishedName)"""
        # First check if it's a prefixed reference
        if ':' in type_name:
            prefix, name = type_name.split(':')
            if prefix in self.prefix_map:
                # The type is defined in another module
                referenced_module = self.prefix_map[prefix]
                
                # Try to find the actual type in imported models
                referenced_type = self.find_type_in_imported_models(type_name)
                if referenced_type:
                    return referenced_type
                
                # Fall back to constructing a string reference
                return f"{referenced_module}.{name}"
        
        # If it's not prefixed or we can't resolve it, return as is
        return type_name

    def parse_typedef(self, typedef: Dict[str, Any]) -> None:
        """Parse a typedef definition and create an enumeration if it defines one."""
        type_info = typedef.get('type', {})
        if isinstance(type_info, dict) and type_info.get('@name') == 'enumeration':
            # Get enum name and replace hyphens with underscores
            enum_name = typedef.get('@name', '').replace('-', '_')
            
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
        # Replace hyphens with underscores in class name
        class_name = grouping['@name'].replace('-', '_')
        
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
            # Replace hyphens with underscores in class name
            class_name = list_def['@name'].replace('-', '_')
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
        # Replace hyphens with underscores in property name
        name = leaf['@name'].replace('-', '_')
        desc = leaf.get('description', {}).get('text', '')
        mandatory = leaf.get('mandatory', {}).get('@value', 'false') == 'true'

        # Determine type
        type_info = leaf.get('type', {})
        raw_type_name = type_info.get('@name', 'string')
        
        # Check if it's a prefixed type reference
        if ':' in raw_type_name:
            # Try to resolve it to an actual type object first
            resolved_type = self.find_type_in_imported_models(raw_type_name)
            if resolved_type:
                # We found the actual type in imported models
                type_name = resolved_type
            else:
                # Fall back to type mapping
                type_name = self.resolve_type_reference(raw_type_name)
        else:
            # Handle special types with hyphens
            if isinstance(raw_type_name, str) and '-' in raw_type_name:
                raw_type_name = raw_type_name.replace('-', '_')

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
            if raw_type_name not in type_mapping:
                # For unknown types, create a StringType
                type_name = 'StringType'
            else:
                type_name = type_mapping[raw_type_name]

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
        # Replace hyphens with underscores in property name
        name = list_def['@name'].replace('-', '_')
        desc = list_def.get('description', {}).get('text', '')
        
        # Set multiplicity based on min-elements if available
        min_elements = int(list_def.get('min-elements', {}).get('@value', '0')) if 'min-elements' in list_def else 0
        max_elements = "*"  # Use "*" as unlimited max
        multiplicity = Multiplicity(min_elements, max_elements)
        
        # Check if the list has a specific type through 'uses' directive
        item_type = None
        if 'uses' in list_def:
            uses_info = list_def['uses']
            if isinstance(uses_info, dict):
                type_ref = uses_info.get('@name')
                if type_ref and ':' in type_ref:
                    # This is a reference to a type in another module
                    prefix, type_name = type_ref.split(':')
                    # Replace hyphens with underscores in type name
                    type_name = type_name.replace('-', '_')
                    if prefix in self.prefix_map:
                        module_name = self.prefix_map[prefix]
                        item_type = f"{module_name}.{type_name}"
        
        # Create property with proper type and multiplicity
        prop = Property(
            name=name,
            # Use the specific item type if available, otherwise use generic list
            type=item_type if item_type else 'list',
            owner=self.current_class,
            multiplicity=multiplicity
        )
        
        # Add description as a synonym if available
        if desc:
            prop.synonyms = [desc]

        self.current_class.add_attribute(prop)

    def parse_uses(self, uses: Dict[str, Any]) -> None:
        """Parse uses statement which references a grouping."""
        # Replace hyphens with underscores in grouping name
        grouping_name = uses.get('@name', '').replace('-', '_')
        # Find referenced class and inherit from it
        referenced_class = self.current_model.get_class_by_name(grouping_name)
        if referenced_class and self.current_class:
            # Copy attributes from referenced class
            for attr in referenced_class.attributes:
                self.current_class.add_attribute(attr)

    def cleanup_grp_classes(self, model: DomainModel) -> DomainModel:
        """Merge *Grp classes into their base classes and remove the Grp classes."""
        classes_to_remove = set()
        
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
                        # Check if the attribute already exists in the base class
                        existing_attr = next((a for a in base_class.attributes if a.name == attr.name), None)
                        if not existing_attr:
                            # Only add if it doesn't exist
                            base_class.add_attribute(attr)
                    classes_to_remove.add(type_obj)
                else:
                    # If no base class exists, rename the Grp class by removing 'Grp'
                    type_obj.name = base_name

        # Remove merged Grp classes
        model.types = {t for t in model.types if t not in classes_to_remove}
        
        return model
