from yang_parser import YangParser
from structural import Class
from besser.utilities.buml_code_builder import domain_model_to_code

def main():
    # Initialize the parser
    parser = YangParser()
    
    # Parse the JSON file
    json_file = "example/nrcellcu.json"
    json_file = "json_3gpp/_3gpp-nr-nrm-beam.json"
    json_file = "json_3gpp/_3gpp-common-yang-types.json"

    model = parser.parse_file(json_file)
    
    # Print the results
    print(f"Model name: {model.name}")
    print("\nClasses:")
    for class_type in model.types:
        if isinstance(class_type, Class):
            print(f"\nClass: {class_type.name}")
            print("Attributes:")
            for attr in class_type.attributes:
                print(f"  - {attr.name}: {attr.type}")

if __name__ == "__main__":
    main()
