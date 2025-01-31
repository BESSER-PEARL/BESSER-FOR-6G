import json
from typing import Any, Dict, List
from structural import (Class, DataType, DomainModel, Property, Method,
                       PrimitiveDataType, Enumeration, EnumerationLiteral)

class YangParser:
    def __init__(self):
        self.model = DomainModel("YangModel")
        self.current_class = None

    def parse_file(self, filepath: str) -> DomainModel:
        """Parse a YANG JSON file and return a DomainModel."""
        with open(filepath, 'r') as f:
            data = json.load(f)
        return self.parse_module(data['module'])

    def parse_module(self, module: Dict[str, Any]) -> DomainModel:
        """Parse the module section and create corresponding model elements."""
        module_name = module.get('@name', '')
        self.model.name = module_name

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

        return self.model

    def parse_typedef(self, typedef: Dict[str, Any]) -> None:
        """Parse a typedef definition and create an enumeration if it defines one."""
        type_info = typedef.get('type', {})
        if type_info.get('@name') == 'enumeration':
            enum_name = typedef['@name']
            enum_type = Enumeration(name=enum_name)
            
            # Add enumeration literals
            if 'enum' in type_info:
                enums = type_info['enum'] if isinstance(type_info['enum'], list) else [type_info['enum']]
                for enum in enums:
                    literal_name = enum.get('@name', '')
                    literal = EnumerationLiteral(name=literal_name, owner=enum_type)
                    enum_type.add_literal(literal)
            
            self.model.add_type(enum_type)

    def parse_grouping(self, grouping: Dict[str, Any]) -> None:
        """Parse a grouping definition and create a class."""
        class_name = grouping['@name']
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

        self.model.add_type(new_class)

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

            self.model.add_type(new_class)

    def parse_leaf(self, leaf: Dict[str, Any]) -> None:
        """Parse a leaf definition and create a property."""
        name = leaf['@name']
        desc = leaf.get('description', {}).get('text', '')
        mandatory = leaf.get('mandatory', {}).get('@value', 'false') == 'true'

        # Determine type
        type_info = leaf.get('type', {})
        type_name = type_info.get('@name', 'string')

        # Handle enumeration types
        if type_name == 'enumeration':
            enum_name = f"{self.current_class.name}_{name}_enum"
            enum_type = Enumeration(name=enum_name)
            
            # Add enumeration literals
            if 'enum' in type_info:
                enums = type_info['enum'] if isinstance(type_info['enum'], list) else [type_info['enum']]
                for enum in enums:
                    literal_name = enum.get('@name', '')
                    literal = EnumerationLiteral(name=literal_name, owner=enum_type)
                    enum_type.add_literal(literal)
            
            self.model.add_type(enum_type)
            type_name = enum_name
        else:
            # Map YANG types to primitive types
            type_mapping = {
                'int32': 'int',
                'uint32': 'int',
                'string': 'str',
                'boolean': 'bool'
            }
            type_name = type_mapping.get(type_name, type_name)

        # Create property
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
        referenced_class = self.model.get_class_by_name(grouping_name)
        if referenced_class and self.current_class:
            # Copy attributes from referenced class
            for attr in referenced_class.attributes:
                self.current_class.add_attribute(attr)
