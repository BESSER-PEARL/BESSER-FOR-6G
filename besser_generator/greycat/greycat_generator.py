import os
from jinja2 import Environment, FileSystemLoader
from besser.BUML.metamodel.structural import (
    DomainModel, IntegerType, StringType, Class, 
    BooleanType, FloatType, Enumeration, Property,
    TimeDeltaType, TimeType, DateType, DateTimeType
)
from besser.generators import GeneratorInterface

class GreyCatGenerator(GeneratorInterface):
    def __init__(self, models: list, output_dir: str = None):
        """
        Initialize the GreyCat generator with one or more B-UML models.
        
        Args:
            models: List of DomainModel instances
            output_dir: Directory where the output file will be written
        """
        # Use the first model for the base initialization
        super().__init__(models[0] if isinstance(models, list) else models, output_dir)
        # Store all models
        self.models = models if isinstance(models, list) else [models]
        
    def _get_greycat_type(self, property_type):
        """Map B-UML property types to GreyCat types"""
        type_mapping = {
            IntegerType: "int",
            StringType: "String",
            BooleanType: "bool",
            FloatType: "float",
            TimeType: "time",
            DateType: "date",
            DateTimeType: "datetime",
            TimeDeltaType: "duration"
        }
        
        if isinstance(property_type, Enumeration):
            return property_type.name
        elif hasattr(property_type, 'name'):
            return property_type.name
        
        return type_mapping.get(property_type, "String")
    
    def _collect_enumerations(self):
        """Collect all enumerations from all models"""
        enums = []
        for model in self.models:
            for type_def in model.types:
                if isinstance(type_def, Enumeration):
                    enum_data = {
                        'name': type_def.name,
                        'literals': [lit.name for lit in type_def.literals],
                        'description': self._get_description(type_def)
                    }
                    enums.append(enum_data)
        return enums
    
    def _get_description(self, element):
        """Extract description from synonyms attribute"""
        if hasattr(element, 'synonyms') and element.synonyms:
            if isinstance(element.synonyms, list):
                return ". ".join(element.synonyms)
            return element.synonyms
        return ""
    
    def _process_properties(self, class_def):
        """Process a class's properties to GreyCat attributes"""
        properties = []
        for attr in class_def.attributes:
            prop_type = self._get_greycat_type(attr.type)
            
            # Handle references/nodes
            is_node = False
            if hasattr(attr.type, 'name'):
                # Check if it's not a primitive type by comparing class names
                primitive_type_names = ['IntegerType', 'StringType', 'BooleanType', 'FloatType', 
                                       'TimeType', 'DateType', 'DateTimeType', 'TimeDeltaType']
                type_class_name = attr.type.__class__.__name__
                
                if type_class_name not in primitive_type_names and not isinstance(attr.type, Enumeration):
                    is_node = True
            
            # Handle multiplicity for arrays
            is_array = False
            if hasattr(attr, 'multiplicity') and attr.multiplicity:
                # Check if it's a collection (upper bound > 1 or -1 for unbounded)
                # Use proper attribute name or check with hasattr to avoid AttributeError
                if hasattr(attr.multiplicity, 'upper'):
                    upper = attr.multiplicity.upper
                    # -1 or * often indicates unbounded collection
                    if upper != 1 and upper != '1':
                        is_array = True
                elif hasattr(attr.multiplicity, 'max'):
                    max_val = attr.multiplicity.max
                    if max_val != 1 and max_val != '1':
                        is_array = True
            
            prop_data = {
                'name': attr.name,
                'type': prop_type,
                'is_node': is_node,
                'is_array': is_array,
                'description': self._get_description(attr)
            }
            properties.append(prop_data)
        
        return properties
    
    def _process_classes(self):
        """Process all classes from all models"""
        classes = []
        for model in self.models:
            for type_def in model.types:
                if isinstance(type_def, Class):
                    class_data = {
                        'name': type_def.name,
                        'properties': self._process_properties(type_def),
                        'description': self._get_description(type_def)
                    }
                    classes.append(class_data)
        return classes
    
    def generate(self):
        """Generate the GreyCat file based on the B-UML models"""
        # Collect data from models
        data = {
            'enumerations': self._collect_enumerations(),
            'classes': self._process_classes()
        }
        
        # Set up Jinja2 environment
        templates_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "templates")
        env = Environment(loader=FileSystemLoader(templates_path))
        template = env.get_template('greycat_template.gcl.j2')
        
        # Generate file
        file_path = self.build_generation_path(file_name="network.gcl")
        with open(file_path, mode="w", encoding='utf-8') as f:
            generated_code = template.render(data=data)
            f.write(generated_code)
            print(f"GreyCat model generated successfully at: {file_path}")
            
        return file_path
