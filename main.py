import os
from yang_parser import YangParser
from structural import Class, Enumeration
from buml_code_builder import domain_model_to_code

def main():
    # Initialize the parser
    parser = YangParser()
    
    # Get all JSON files from the json_3gpp directory
    json_dir = "json_3gpp"
    output_dir = "generated_models"
    json_files = [f for f in os.listdir(json_dir) if f.endswith('.json')]
    
    # Create output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # First pass: Parse all files to build type definitions
    for json_file in json_files:
        file_path = os.path.join(json_dir, json_file)
        model_name = json_file.replace('.json', '')
        parser.parse_file(file_path, model_name)
        
        # Generate BUML file for each model
        output_file = os.path.join(output_dir, f"{model_name}.py")
        domain_model_to_code(parser.current_model, output_file, parser.prefix_map)

if __name__ == "__main__":
    main()
