from besser_parser.yang_parser import YangParser
from structural import Class, Enumeration
from besser.utilities.buml_code_builder import domain_model_to_code

def main():
    # Initialize the parser
    parser = YangParser()

    # Parse the JSON file
    json_file = "example/nrcellcu.json"
    json_file = "json_3gpp/_3gpp-nr-nrm-beam.json"
    json_file = "json_3gpp/_3gpp-common-yang-types.json"


    json_file = "json_3gpp/_3gpp-5gc-nrm-configurable5qiset.json"
    json_file = "json_3gpp/_3gpp-5gc-nrm-nfprofile.json"
    json_file = "example/nrcellcu.json"
    
    model = parser.parse_file(json_file)

    # Print the results
    print(f"Model name: {model.name}")

    # Print Classes
    print("\nClasses:")
    for class_type in model.types:
        if isinstance(class_type, Class):
            print(f"\nClass: {class_type.name}")
            print("Attributes:")
            for attr in class_type.attributes:
                print(f"  - {attr.name}: {attr.type}")

    # Print Enumerations
    print("\nEnumerations:")
    for type_element in model.types:
        if isinstance(type_element, Enumeration):
            print(f"\nEnumeration: {type_element.name}")
            print("Literals:")
            for literal in type_element.literals:
                print(f"  - {literal.name}")

if __name__ == "__main__":
    main()
