import os
import re
from besser.BUML.metamodel.structural.structural import DomainModel, Enumeration, Type, Multiplicity

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

def clean_description(desc):
    """Clean and format description for use in code"""
    if not desc:
        return ""
    # Replace newlines with space and handle quotes
    cleaned = desc.replace('\n', ' ').replace('\r', ' ').replace('"', '\\"')
    # Remove multiple spaces
    while '  ' in cleaned:
        cleaned = cleaned.replace('  ', ' ')
    return cleaned.strip()

def sanitize_module_name(module_name):
    """
    Convert a module name to a valid Python identifier
    - Replace hyphens with underscores
    - Add prefix '_' if it starts with a number
    """
    # Replace hyphens with underscores
    sanitized = module_name.replace('-', '_')
    
    # If the name starts with a number, prefix with underscore
    if sanitized[0].isdigit() or sanitized[0] == '-':
        sanitized = '_' + sanitized
    
    # Replace any other invalid characters with underscores
    sanitized = re.sub(r'[^a-zA-Z0-9_]', '_', sanitized)
    
    return sanitized

def sanitize_identifier(name: str) -> str:
    """
    Convert a name to a valid Python identifier:
    - Replace hyphens with underscores
    - Ensure name does not start with a number
    - Handle other invalid characters
    """
    # Replace hyphens with underscores
    sanitized = name.replace('-', '_')
    
    # If the name starts with a number, prefix with underscore
    if sanitized and (sanitized[0].isdigit() or sanitized[0] == '-'):
        sanitized = '_' + sanitized
    
    # Replace any other invalid characters with underscores
    sanitized = re.sub(r'[^a-zA-Z0-9_]', '_', sanitized)
    
    return sanitized

def domain_model_to_code(model: DomainModel, file_path: str, prefix_map: dict, imported_models: dict = None):
    """
    Generates Python code for a B-UML model and writes it to a specified file.

    Parameters:
    model (DomainModel): The B-UML model object containing classes, enumerations, 
        associations, and generalizations.
    file_path (str): The path where the generated code will be saved.
    prefix_map (dict): A dictionary mapping prefixes to module names.
    imported_models (dict): A dictionary mapping module names to domain models.

    Outputs:
    - A Python file containing the base code representation of the B-UML domain model.
    """
    imported_models = imported_models or {}
    output_dir = os.path.dirname(file_path)
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir)
    if not file_path.endswith('.py'):
        file_path += '.py'

    # First, analyze the model to determine which imports are needed
    imports_needed = _analyze_imports_needed(model, prefix_map)

    with open(file_path, 'w', encoding='utf-8') as f:
        # Write minimal imports
        f.write("# Generated B-UML Model\n")
        f.write("from besser.BUML.metamodel.structural import (\n")
        f.write("    Class, Property, DomainModel, Multiplicity,\n")
        f.write("    IntegerType, StringType, BooleanType, FloatType,\n")
        f.write("    TimeType, DateType, DateTimeType, TimeDeltaType,\n")
        f.write("    PrimitiveDataType, Enumeration, EnumerationLiteral\n")
        f.write(")\n\n")
        
        # Add imports for referenced models
        if imports_needed:
            f.write("# Import referenced models\n")
            for prefix in sorted(imports_needed):
                module_name = prefix_map.get(prefix)
                if (module_name):
                    # Generate a valid Python module name
                    module_path = sanitize_module_name(module_name)
                    f.write(f"from buml_generated_models.{module_path} import domain_model as {prefix}_model\n")
            f.write("\n")

        # Write enumerations
        enums = [t for t in model.types if isinstance(t, Enumeration)]
        if enums:
            f.write("# Enumerations\n")
            # Sort by name instead of timestamp for enumerations
            for enum in sorted(enums, key=lambda x: x.name):
                f.write(f"{enum.name} = Enumeration(name=\"{enum.name}\")\n")
                # Sort literals by name as well
                for literal in sorted(enum.literals, key=lambda x: x.name):
                    # Include synonyms if available
                    if literal.synonyms and len(literal.synonyms) > 0:
                        desc = clean_description(literal.synonyms[0])
                        f.write(f"{enum.name}_{literal.name} = EnumerationLiteral(")
                        f.write(f"name=\"{literal.name}\", owner={enum.name}, synonyms=[\"{desc}\"])\n")
                    else:
                        f.write(f"{enum.name}_{literal.name} = EnumerationLiteral(")
                        f.write(f"name=\"{literal.name}\", owner={enum.name})\n")
                        
                f.write(f"{enum.name}.literals = {{{', '.join(f'{enum.name}_{lit.name}' for lit in sorted(enum.literals, key=lambda x: x.name))}}}\n")
                
                # Add synonyms to enum if available
                if enum.synonyms and len(enum.synonyms) > 0:
                    desc = clean_description(enum.synonyms[0])
                    f.write(f"{enum.name}.synonyms = [\"{desc}\"]\n")
                f.write("\n")

        # Write classes
        f.write("# Classes\n")
        # Sort classes by name instead of timestamp
        for cls in sorted(model.get_classes(), key=lambda x: x.name):
            # Skip classes ending with Grp
            if cls.name.endswith('Grp'):
                continue
                
            # Include synonyms if available
            if cls.synonyms and len(cls.synonyms) > 0:
                desc = clean_description(cls.synonyms[0])
                f.write(f"{cls.name} = Class(name=\"{cls.name}\", synonyms=[\"{desc}\"])\n")
            else:
                f.write(f"{cls.name} = Class(name=\"{cls.name}\")\n")
            f.write("\n")

            # Write class attributes
            f.write(f"# {cls.name} class attributes and methods\n")
            # Sort attributes by name
            for attr in sorted(cls.attributes, key=lambda x: x.name):
                # Handle different type scenarios
                if isinstance(attr.type, str):
                    # Check if it's a reference to an imported model
                    if '.' in attr.type:
                        module_name, type_name = attr.type.split('.', 1)
                        # Find the prefix for this module
                        prefix = next((p for p, m in prefix_map.items() if m == module_name), None)
                        if prefix:
                            # Ensure we're using a valid Python identifier for the type name
                            safe_type_name = sanitize_identifier(type_name)
                            type_name = f"{prefix}_model.get_type_by_name('{safe_type_name}')"
                        else:
                            type_name = f"'{attr.type}'"  # Fallback to string if not found
                    elif attr.type in PRIMITIVE_TYPE_MAPPING:
                        type_name = PRIMITIVE_TYPE_MAPPING[attr.type]
                    elif attr.type == 'list':
                        type_name = 'list'  # Special case for lists
                    else:
                        # Check if it's already a defined primitive type name
                        if attr.type.endswith('Type'):
                            type_name = attr.type
                        else:
                            # For custom types, reference them directly
                            type_name = attr.type
                elif isinstance(attr.type, Type):
                    # If it's an actual Type instance, use its name
                    type_name = attr.type.name
                else:
                    type_name = str(attr.type)
                
                # Include multiplicity information if available
                if hasattr(attr, 'multiplicity') and attr.multiplicity and (attr.multiplicity.min != 1 or attr.multiplicity.max != 1):
                    # Format multiplicity for code generation
                    min_val = attr.multiplicity.min
                    # Make sure the "*" is a string literal in quotes
                    if attr.multiplicity.max >= 9999:
                        max_val = '"*"'  # Properly quoted as a string
                    else:
                        max_val = attr.multiplicity.max
                    
                    # Include synonyms if available
                    if attr.synonyms and len(attr.synonyms) > 0:
                        desc = clean_description(attr.synonyms[0])
                        f.write(f"{cls.name}_{attr.name}: Property = Property(name=\"{attr.name}\", type={type_name}, "
                               f"multiplicity=Multiplicity({min_val}, {max_val}), synonyms=[\"{desc}\"])\n")
                    else:
                        f.write(f"{cls.name}_{attr.name}: Property = Property(name=\"{attr.name}\", type={type_name}, "
                               f"multiplicity=Multiplicity({min_val}, {max_val}))\n")
                else:
                    # Regular property without custom multiplicity
                    if attr.synonyms and len(attr.synonyms) > 0:
                        desc = clean_description(attr.synonyms[0])
                        f.write(f"{cls.name}_{attr.name}: Property = Property(name=\"{attr.name}\", type={type_name}, synonyms=[\"{desc}\"])\n")
                    else:
                        f.write(f"{cls.name}_{attr.name}: Property = Property(name=\"{attr.name}\", type={type_name})\n")
            
            # Write attributes set
            attrs = [f"{cls.name}_{attr.name}" for attr in sorted(cls.attributes, key=lambda x: x.name)]
            if attrs:
                f.write(f"{cls.name}.attributes={{{', '.join(attrs)}}}\n\n")

        # Write domain model
        f.write("# Domain Model with References\n")
        f.write("domain_model = DomainModel(\n")
        f.write(f"    name=\"{model.name}\",\n")
        
        # Get all types including both classes and enumerations
        all_types = set()
        all_types.update(sorted(model.get_classes(), key=lambda x: x.name))  # Add classes
        all_types.update(sorted((t for t in model.types if isinstance(t, Enumeration)), key=lambda x: x.name))  # Add enums
        
        # Sort all types by name
        f.write(f"    types={{{', '.join(t.name for t in sorted(all_types, key=lambda x: x.name))}}},\n")
        f.write("    associations={},\n")
        f.write("    generalizations={}\n")
        f.write(")\n")
        
        # Add synonyms to model if available
        if model.synonyms and len(model.synonyms) > 0:
            desc = clean_description(model.synonyms[0])
            f.write(f"domain_model.synonyms = [\"{desc}\"]\n")

    print(f"BUML model saved to {file_path}")

def _analyze_imports_needed(model: DomainModel, prefix_map: dict):
    """
    Analyze the model to determine which imports are needed.
    
    Args:
        model: The domain model to analyze
        prefix_map: Dictionary mapping prefixes to module names
        
    Returns:
        Set of prefixes that need to be imported
    """
    imports_needed = set()
    reverse_prefix_map = {v: k for k, v in prefix_map.items()}
    
    # Check all classes for attributes with types from other models
    for cls in model.get_classes():
        for attr in cls.attributes:
            if isinstance(attr.type, str):
                if '.' in attr.type:
                    module_name = attr.type.split('.')[0]
                    if module_name in reverse_prefix_map:
                        imports_needed.add(reverse_prefix_map[module_name])
    
    return imports_needed