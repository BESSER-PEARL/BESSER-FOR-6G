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

        # Parse groupings first as they define types
        if 'grouping' in module:
            self.parse_grouping(module['grouping'])

        # Parse augments which contain the main class definitions
        if 'augment' in module:
            self.parse_augment(module['augment'])

        return self.model

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
            self.parse_list(grouping['list'])

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

        # Map YANG types to primitive types
        type_mapping = {
            'int32': 'int',
            'string': 'str',
            'boolean': 'bool',
            'enumeration': 'str'
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
