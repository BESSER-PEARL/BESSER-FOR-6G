import os
from yang_parser import YangParser
from structural import Class, Enumeration
from buml_code_builder import domain_model_to_code

def main():
    parser = YangParser()
    json_dir = "json_3gpp"
    output_dir = "generated_models"
    
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Process each JSON file
    for json_file in os.listdir(json_dir):
        if json_file.endswith('.json'):
            file_path = os.path.join(json_dir, json_file)
            model_name = json_file.replace('.json', '')
            
            # Parse and generate model
            model = parser.parse_file(file_path, model_name)
            output_file = os.path.join(output_dir, f"{model_name}.py")
            domain_model_to_code(model, output_file, parser.prefix_map)

if __name__ == "__main__":
    main()
