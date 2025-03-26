import os
from jinja2 import Environment, FileSystemLoader
from besser.BUML.metamodel.structural import (
    DomainModel, IntegerType, StringType, Class, 
    BooleanType, FloatType, Enumeration
)
from besser.generators import GeneratorInterface

class JSONSchemaGenerator(GeneratorInterface):
    def __init__(self, model: DomainModel, output_dir: str = None):
        super().__init__(model, output_dir)

    def _get_property_type(self, property_type):
        type_mapping = {
            IntegerType: "integer",
            StringType: "string",
            BooleanType: "boolean",
            FloatType: "number",
            list: "array"
        }
        
        if isinstance(property_type, Enumeration):
            return "string"
        return type_mapping.get(property_type, "string")

    def generate(self, *args):
        schema_data = {
            "type": "object",
            "properties": {},
            "required": []
        }

        # Add model description
        if hasattr(self.model, 'synonyms') and self.model.synonyms:
            schema_data["description"] = ". ".join(self.model.synonyms) if isinstance(self.model.synonyms, list) else self.model.synonyms

        # Process all types in the model
        for type_def in self.model.types:
            if isinstance(type_def, Enumeration):
                # Handle enumeration
                enum_values = [lit.name for lit in type_def.literals]
                schema_data["properties"][type_def.name] = {
                    "type": "string",
                    "enum": enum_values
                }
                if hasattr(type_def, 'synonyms') and type_def.synonyms:
                    schema_data["properties"][type_def.name]["description"] = (
                        ". ".join(type_def.synonyms) if isinstance(type_def.synonyms, list) 
                        else type_def.synonyms
                    )
            
            elif isinstance(type_def, Class):
                # Handle class properties
                for attr in type_def.attributes:
                    prop_type = self._get_property_type(attr.type)
                    prop_def = {
                        "type": prop_type,
                        "description": "Property"
                    }

                    if hasattr(attr, 'synonyms') and attr.synonyms:
                        prop_def["description"] = (
                            ". ".join(attr.synonyms) if isinstance(attr.synonyms, list)
                            else attr.synonyms
                        )

                    if isinstance(attr.type, Enumeration):
                        prop_def["enum"] = [lit.name for lit in attr.type.literals]

                    if prop_type == "array":
                        prop_def["items"] = {"type": "string"}

                    schema_data["properties"][attr.name] = prop_def

        templates_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "templates")
        env = Environment(loader=FileSystemLoader(templates_path))
        template = env.get_template('json_schema_template.json.j2')

        file_path = self.build_generation_path(file_name="schema.json")
        with open(file_path, mode="w", encoding='utf-8') as f:
            generated_schema = template.render(schema=schema_data)
            f.write(generated_schema)
            # print(f"Schema generated successfully at: {file_path}")
