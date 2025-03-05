import os
from jinja2 import Environment, FileSystemLoader
from besser.BUML.metamodel.structural import DomainModel, IntegerType, StringType, Class
from besser.generators import GeneratorInterface

class JSONSchemaGenerator(GeneratorInterface):
    def __init__(self, model: DomainModel, output_dir: str = None):
        super().__init__(model, output_dir)

    def _get_property_type(self, property_type):
        type_mapping = {
            IntegerType: "number",
            StringType: "string",
            list: "array"
        }
        return type_mapping.get(property_type, "string")

    def generate(self, *args):
        # Filter for Class types only
        types_list = [t for t in self.model.types if isinstance(t, Class)]
        
        if not types_list:
            raise ValueError("No valid class types found in the model")

        main_class = types_list[0]
        
        schema_data = {
            "class_name": main_class.name,
            "properties": {}
        }

        # Add model description if available
        if hasattr(self.model, 'synonyms') and self.model.synonyms:
            # If synonyms is a list, join them; otherwise use as is
            if isinstance(self.model.synonyms, list):
                schema_data["model_description"] = ". ".join(self.model.synonyms)
            else:
                schema_data["model_description"] = self.model.synonyms

        # Now we're sure we're working with a Class object
        for attr in main_class.attributes:
            prop_type = self._get_property_type(attr.type)
            
            # Extract description from synonyms if available
            description = "Property. Model:'https://schema.org/{}'".format(prop_type.capitalize())
            if hasattr(attr, 'synonyms') and attr.synonyms:
                if isinstance(attr.synonyms, list):
                    # Join multiple synonyms if it's a list
                    attr_description = ". ".join(attr.synonyms)
                else:
                    # Use the single synonym as is
                    attr_description = attr.synonyms
                description = f"Property. {attr_description}. Model:'https://schema.org/{prop_type.capitalize()}'"
            
            schema_data["properties"][attr.name] = {
                "type": prop_type,
                "description": description
            }
            if prop_type == "array":
                schema_data["properties"][attr.name]["items"] = {"type": "string"}

        templates_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "templates")
        env = Environment(loader=FileSystemLoader(templates_path))
        template = env.get_template('json_schema_template.json.j2')

        file_path = self.build_generation_path(file_name="schema.json")
        with open(file_path, mode="w", encoding='utf-8') as f:
            generated_schema = template.render(schema=schema_data)
            f.write(generated_schema)
            print("Schema generated in the location: " + file_path)
