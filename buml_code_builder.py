import os
from besser.BUML.metamodel.structural.structural import DomainModel, Enumeration
from besser.utilities import sort_by_timestamp as sort

PRIMITIVE_TYPE_MAPPING = {
    'str': 'StringType',
    'string': 'StringType', 
    'int': 'IntegerType',
    'integer': 'IntegerType',
    'float': 'FloatType',
    'bool': 'BooleanType',
    'boolean': 'BooleanType',
    'time': 'TimeType',
    'date': 'DateType',
    'datetime': 'DateTimeType',
    'timedelta': 'TimeDeltaType'
}
def domain_model_to_code(model: DomainModel, file_path: str, prefix_map: dict):
    """
    Generates Python code for a B-UML model and writes it to a specified file.

    Parameters:
    model (DomainModel): The B-UML model object containing classes, enumerations, 
        associations, and generalizations.
    file_path (str): The path where the generated code will be saved.
    prefix_map (dict): A dictionary mapping prefixes to module names.

    Outputs:
    - A Python file containing the base code representation of the B-UML domain model.
    """
    output_dir = os.path.dirname(file_path)
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir)
    if not file_path.endswith('.py'):
        file_path += '.py'

    with open(file_path, 'w', encoding='utf-8') as f:
        # Write minimal imports
        f.write("# Generated B-UML Model\n")
        f.write("from besser.BUML.metamodel.structural import (\n")
        f.write("    Class, Property, DomainModel,\n")
        f.write("    IntegerType, Enumeration, EnumerationLiteral\n")
        f.write(")\n\n")
        
        # Add only needed imports from referenced models
        needed_imports = set()
        for prefix, module_name in prefix_map.items():
            if module_name.startswith('_3gpp'):
                module_path = module_name.replace('-', '_')
                if prefix in ['types3gpp', 'types5g3gpp']:  # Only import essential types
                    needed_imports.add(f"from generated_models.{module_path} import domain_model as {prefix}_model")
        
        if needed_imports:
            f.write("# Import referenced models\n")
            for import_stmt in sorted(needed_imports):
                f.write(f"{import_stmt}\n")
            f.write("\n")

        # Write enumerations
        enums = [t for t in model.types if isinstance(t, Enumeration)]
        if enums:
            f.write("# Enumerations\n")
            for enum in sort(enums):
                f.write(f"{enum.name} = Enumeration(name=\"{enum.name}\")\n")
                for literal in sort(enum.literals):
                    f.write(f"{enum.name}_{literal.name} = EnumerationLiteral(")
                    f.write(f"name=\"{literal.name}\", owner={enum.name})\n")
                f.write(f"{enum.name}.literals = {{{', '.join(f'{enum.name}_{lit.name}' for lit in sort(enum.literals))}}}\n\n")

        # Write classes
        f.write("# Classes\n")
        for cls in sort(model.get_classes()):
            f.write(f"{cls.name} = Class(name=\"{cls.name}\")\n")
            f.write("\n")

            # Write class attributes
            f.write(f"# {cls.name} class attributes and methods\n")
            for attr in sort(cls.attributes):
                attr_type = "IntegerType" if attr.type == "int32" else attr.type
                f.write(f"{cls.name}_{attr.name}: Property = Property(name=\"{attr.name}\", type={attr_type})\n")
            
            # Write attributes set
            attrs = [f"{cls.name}_{attr.name}" for attr in sort(cls.attributes)]
            if attrs:
                f.write(f"{cls.name}.attributes={{{', '.join(attrs)}}}\n\n")

        # Write domain model
        # f.write("# Domain Model with References\n")
        # f.write("domain_model = DomainModel(\n")
        # f.write(f"    name=\"{model.name}\",\n")
        # f.write(f"    types={{{', '.join(cls.name for cls in sort(model.get_classes()))}}},\n")
        # f.write("    associations={},\n")
        # f.write("    generalizations={}\n")
        # f.write(")\n")

    print(f"BUML model saved to {file_path}")