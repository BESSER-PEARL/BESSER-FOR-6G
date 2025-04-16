import os
import json
from pathlib import Path
from openai import OpenAI
from dotenv import load_dotenv
# Load environment variables from .env file
load_dotenv()
# Config
SCHEMA_ROOT = Path("generatedsmartdata")
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Lecture de tous les schémas
def load_all_schemas():
    schemas = {}
    for file in SCHEMA_ROOT.rglob("schema.json"):
        try:
            with open(file, "r") as f:
                content = json.load(f)
                schemas[file] = content
        except Exception as e:
            print(f"❌ Erreur lecture {file}: {e}")
    return schemas

# Resolves custom types (by name)
def find_custom_type_definition(type_name, all_schemas):
    for schema_path, content in all_schemas.items():
        defs = content.get("definitions", {}) or content.get("$defs", {})
        if type_name in defs:
            return defs[type_name]
    return None

# Integrate custom type definitions into the prompt
def enrich_schema_with_known_types(schema, all_schemas):
    def collect_custom_defs(schema_part):
        defs_found = {}
        for part in schema_part.get("allOf", []):
            props = part.get("properties", {})
            for prop_name, prop_schema in props.items():
                t = prop_schema.get("type")
                if t and not isinstance(t, list) and t not in ("string", "number", "integer", "boolean", "array", "object"):
                    custom_def = find_custom_type_definition(t, all_schemas)
                    if custom_def:
                        defs_found[t] = custom_def
        return defs_found

    defs = collect_custom_defs(schema)
    return defs

# Call OpenAI API to generate an example
def ask_gpt_to_generate_example(schema_json, custom_defs, filename):
    defs_text = "\n".join([
        f"Type personnalisé '{k}':\n```json\n{json.dumps(v, indent=2)}\n```"
        for k, v in custom_defs.items()
    ])

    prompt = f"""
Tu es un expert en schémas JSON. Voici un schéma JSON extrait de {filename}. Génère un exemple JSON valide et plausible qui instancie ce schéma.

Voici le schéma :
```json
{json.dumps(schema_json, indent=2)}
```

{defs_text}

Donne uniquement le JSON d'exemple, sans aucune explication.
"""

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2
    )
    content = response.choices[0].message.content
    
    # Clean output from markdown code block markers
    content = content.strip()
    if content.startswith("```json"):
        content = content[7:]
    if content.endswith("```"):
        content = content[:-3]
    content = content.strip()
    
    return content

# globale function to generate examples for all schemas
def generate_examples():
    all_schemas = load_all_schemas()
    for schema_path, schema_content in all_schemas.items():
        print(f"📄 Traitement : {schema_path}")
        try:
            custom_defs = enrich_schema_with_known_types(schema_content, all_schemas)
            example = ask_gpt_to_generate_example(schema_content, custom_defs, str(schema_path))
            output_path = schema_path.parent / "example.json"
            with open(output_path, "w") as f:
                f.write(example)
            print(f"✅ Exemple généré : {output_path}")
        except Exception as e:
            print(f"❌ Erreur génération pour {schema_path}: {e}")

if __name__ == "__main__":
    generate_examples()
