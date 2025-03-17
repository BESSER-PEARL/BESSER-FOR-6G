#!/usr/bin/env python3
"""
Script to generate GreyCat models from B-UML models.
"""
import os
import sys
from pathlib import Path

# Add the project directory to the Python path
project_dir = str(Path(__file__).parent)
if project_dir not in sys.path:
    sys.path.append(project_dir)

# Import the GreyCat generator
from besser_generator.greycat.greycat_generator import GreyCatGenerator

# Import the domain models
from buml_generated_models._3gpp_nr_nrm_nrcelldu import domain_model as nrcelldu_model
from buml_generated_models._3gpp_nr_nrm_nrcellcu import domain_model as nrcellcu_model

def main():
    """
    Generate the GreyCat model from the imported B-UML models.
    """
    # Define the output directory
    output_dir = os.path.join(project_dir, "generated_models", "greycat")
    
    # Create the output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # Create the GreyCat generator with both models
    generator = GreyCatGenerator(
        models=[nrcellcu_model, nrcelldu_model],
        output_dir=output_dir
    )
    
    # Generate the GreyCat model
    output_path = generator.generate()
    
    # print(f"GreyCat model successfully generated at: {output_path}")

if __name__ == "__main__":
    main()
