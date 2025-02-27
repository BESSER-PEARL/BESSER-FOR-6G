import os
import json
import glob
import re
from yang_parser import YangParser
from buml_code_builder import domain_model_to_code, sanitize_module_name

class ModelProcessor:
    def __init__(self, json_dir, output_dir):
        """
        Initialize the ModelProcessor.
        
        Args:
            json_dir: Directory containing YANG JSON files
            output_dir: Directory to output the generated Python models
        """
        self.json_dir = json_dir
        self.output_dir = output_dir
        self.processed_models = {}  # Maps model names to DomainModel objects
        self.prefix_map = {}       # Maps prefixes to model names
        
        # Create output directory if it doesn't exist
        os.makedirs(output_dir, exist_ok=True)
        
        # Create __init__.py if it doesn't exist
        init_file = os.path.join(output_dir, "__init__.py")
        if not os.path.exists(init_file):
            with open(init_file, 'w') as f:
                f.write('"""Generated B-UML models from 3GPP YANG specifications."""\n')
    
    def process_all_files(self):
        """Process all JSON files in the specified directory"""
        # First pass: Load all files to build the complete prefix map
        json_files = glob.glob(os.path.join(self.json_dir, "*.json"))
        
        print(f"Found {len(json_files)} JSON files to process")
        
        # First pass - collect all prefix mappings
        for json_file in json_files:
            self._collect_prefixes(json_file)
            
        print(f"Collected prefix mappings: {self.prefix_map}")
            
        # Second pass - parse all files with complete prefix information
        for json_file in json_files:
            self._process_file(json_file)
            
        # Third pass - generate code with resolved references
        for model_name, model in self.processed_models.items():
            # Define the output file path - sanitize the model name for Python
            safe_name = sanitize_module_name(model_name)
            output_file = os.path.join(self.output_dir, f"{safe_name}.py")
            # Generate the code
            domain_model_to_code(model, output_file, self.prefix_map, self.processed_models)
    
    def _collect_prefixes(self, json_file):
        """First pass - collect all prefix mappings from the file"""
        try:
            with open(json_file, 'r') as f:
                data = json.load(f)
                
            if 'module' in data:
                module = data['module']
                module_name = module.get('@name', '')
                
                # Get the prefix for this module
                own_prefix = module.get('prefix', {}).get('@value')
                if own_prefix:
                    self.prefix_map[own_prefix] = module_name
                
                # Get all imported modules and their prefixes
                if 'import' in module:
                    imports = module['import']
                    if not isinstance(imports, list):
                        imports = [imports]
                    
                    for imp in imports:
                        prefix = imp.get('prefix', {}).get('@value')
                        module_ref = imp.get('@module')
                        if prefix and module_ref:
                            self.prefix_map[prefix] = module_ref
        except Exception as e:
            print(f"Error collecting prefixes from {json_file}: {e}")
                
    def _process_file(self, json_file):
        """Process a single JSON file and generate a model"""
        try:
            # Extract the model name from the filename
            model_name = os.path.splitext(os.path.basename(json_file))[0]
            
            print(f"Processing {model_name}...")
            
            # Create a parser with the full prefix map
            parser = YangParser()
            parser.prefix_map = self.prefix_map  # Use the complete map we've built
            
            # Parse the file to create a domain model
            model = parser.parse_file(json_file, model_name, self.json_dir)
            
            # Remove any remaining Grp classes that weren't correctly handled
            model = self._cleanup_grp_classes(model)
            
            # Store the model for future reference
            self.processed_models[model_name] = model
            
            print(f"Successfully processed {model_name}")
            
        except Exception as e:
            print(f"Error processing {json_file}: {e}")
    
    def _cleanup_grp_classes(self, model: DomainModel) -> DomainModel:
        """Additional cleanup to ensure all Grp classes are removed"""
        types_to_keep = set()
        for t in model.types:
            if not (hasattr(t, 'name') and t.name.endswith('Grp')):
                types_to_keep.add(t)
        model.types = types_to_keep
        return model


if __name__ == "__main__":
    # Directory paths
    json_dir = "/c:/Users/sulejmani/Desktop/BESSER-FOR-6G/json_3gpp"
    output_dir = "/c:/Users/sulejmani/Desktop/BESSER-FOR-6G/buml_generated_models"
    
    # Create and run the processor
    processor = ModelProcessor(json_dir, output_dir)
    processor.process_all_files()
