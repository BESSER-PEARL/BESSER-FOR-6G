# BESSER-FOR-6G Project

## Overview

BESSER-FOR-6G is a research and development initiative focused on implementing enhanced security protocols for next-generation 6G wireless communication systems. The project transforms 3GPP network specifications into standardized data models to enable interoperability and advanced security analysis.

### Project Workflow

1. **From 3GPP YANG to B-UML**: Converts 3GPP YANG network specifications into B-UML models for object-oriented representation
2. **From B-UML to Smart Data Models**: Transforms the B-UML models into standardized NGSI-LD compatible Smart Data Models
3. **From B-UML to GreyCat**: Generates optimized GreyCat models for high-performance data processing and analysis

## Key Components

- **YANG Parser**: Processes 3GPP YANG specifications into machine-readable JSON
- **B-UML Model Generator**: Creates object-oriented models from YANG specifications
- **Smart Data Model Generator**: Produces NGSI-LD compatible schemas for interoperability
- **GreyCat Model Generator**: Builds high-performance data models for real-time analysis
- **Example Generator**: Creates realistic data examples based on the generated models

## Installation

### Prerequisites

- Python 3.8+
- Required libraries (see `requirements.txt`)
- Network testing tools

### Setup

```bash
# Clone the repository
git clone https://github.com/your-organization/BESSER-FOR-6G.git

# Navigate to the project directory
cd BESSER-FOR-6G

# Install dependencies
pip install -r requirements.txt

# Configure environment
cp .env.example .env
```

## Usage

```bash
# Convert YANG models to JSON
pwsh .\yang-yin_json.ps1

# Generate B-UML models from JSON
python generate_B-UML_model.py

# Generate Smart Data Models from B-UML
python generate_smart_data_models.py

# Generate GreyCat models from B-UML
python generate_greycat_model.py

# Generate example data for Smart Data Models
python generate_examples_smart_data.py
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.


