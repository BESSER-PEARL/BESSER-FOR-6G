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

        schema_data = {
            "class_name": types_list[0].name,
            "properties": {}
        }

        # Now we're sure we're working with a Class object
        for attr in types_list[0].attributes:
            prop_type = self._get_property_type(attr.type)
            schema_data["properties"][attr.name] = {
                "type": prop_type,
                "description": f"Property. Model:'https://schema.org/{prop_type.capitalize()}'"
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
