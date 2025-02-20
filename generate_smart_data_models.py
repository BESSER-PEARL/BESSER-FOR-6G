import os
import sys
import importlib
import traceback
from besser_generator.json_schema_generator import JSONSchemaGenerator

def process_model_file(model_file, models_dir, output_base_dir):
    model_name = os.path.splitext(model_file)[0]
    model_output_dir = os.path.join(output_base_dir, model_name)

    try:
        # Add the models directory to Python path if not already there
        if models_dir not in sys.path:
            sys.path.append(os.path.dirname(models_dir))

        # Import the domain model dynamically
        module = importlib.import_module(f"generated_models.{model_name}")

        if hasattr(module, 'domain_model'):
            os.makedirs(model_output_dir, exist_ok=True)
            generator = JSONSchemaGenerator(module.domain_model, model_output_dir)
            generator.generate()
            print(f"Successfully generated schema for {model_name}")
            return True
        else:
            print(f"Skipping {model_name} - no domain_model found")
            return False

    except ImportError as e:
        # Skip files with missing dependencies for now
        print(f"Skipping {model_name} - missing dependency: {str(e)}")
        return False
    except Exception as e:
        print(f"Error processing {model_name}: {str(e)}")
        print(traceback.format_exc())
        return False

def create_smart_data_models():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    models_dir = os.path.join(current_dir, "generated_models")
    output_base_dir = os.path.join(current_dir, "generatedsmartdata")

    os.makedirs(output_base_dir, exist_ok=True)

    # Process core type modules first
    core_modules = [
        '_3gpp_common_yang_types.py',
        '_3gpp_5g_common_yang_types.py'
    ]

    model_files = [f for f in os.listdir(models_dir) 
                  if f.endswith('.py') and not f.startswith('__')]

    # Process core modules first
    for core_module in core_modules:
        if core_module in model_files:
            process_model_file(core_module, models_dir, output_base_dir)
            model_files.remove(core_module)

    # Then process remaining modules
    for model_file in model_files:
        process_model_file(model_file, models_dir, output_base_dir)

if __name__ == "__main__":
    create_smart_data_models()
