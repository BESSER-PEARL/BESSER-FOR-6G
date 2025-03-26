import os
from yang_parser import YangParser
from besser.BUML.metamodel.structural import Class, Enumeration
from buml_code_builder import domain_model_to_code

"""Generate B-UML models from JSON converted 3GPP YANG specifications 
and save them to the output directory."""


def convert_filename(name):
    """Convert hyphenated filename to underscore format"""
    return name.replace('-', '_')

def main():
    parser = YangParser()
    json_dir = "json_3gpp"
    output_dir = "buml_generated_models_brut"
    
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # List of files to prioritize processing
    priority_files = ["_3gpp-nr-nrm-desmanagementfunction.json"]
    
    # Process priority files first
    for json_file in priority_files:
        if json_file in os.listdir(json_dir):
            file_path = os.path.join(json_dir, json_file)
            model_name = json_file.replace('.json', '')
            output_name = convert_filename(model_name)
            
            print(f"Processing priority file: {json_file}")
            model = parser.parse_file(file_path, model_name, base_dir=json_dir)
            
            # Debug output
            print(f"Model {model_name} has {len(model.types)} types")
            for t in model.types:
                print(f" - Type: {t.name} ({t.__class__.__name__})")
                if hasattr(t, 'attributes'):
                    print(f"   with {len(t.attributes)} attributes")
            
            output_file = os.path.join(output_dir, f"{output_name}.py")
            domain_model_to_code(model, output_file, parser.prefix_map, parser.imported_models)
    
    # Process remaining files
    for json_file in os.listdir(json_dir):
        if json_file.endswith('.json') and json_file not in priority_files:
            file_path = os.path.join(json_dir, json_file)
            model_name = json_file.replace('.json', '')
            output_name = convert_filename(model_name)
            
            model = parser.parse_file(file_path, model_name, base_dir=json_dir)
            print(f"Model {model_name} has {len(model.types)} types")
            
            output_file = os.path.join(output_dir, f"{output_name}.py")
            domain_model_to_code(model, output_file, parser.prefix_map, parser.imported_models)

if __name__ == "__main__":
    main()