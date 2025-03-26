import xmltodict
import json
import sys

# Get file paths from arguments
if len(sys.argv) != 3:
    print("Usage: python convert_yin_to_json.py input.yin output.json")
    sys.exit(1)

yin_file = sys.argv[1]
json_file = sys.argv[2]

# Convert YIN (XML) to JSON
with open(yin_file, "r") as xml_file:
    xml_data = xml_file.read()

json_data = json.dumps(xmltodict.parse(xml_data), indent=4)

# Save JSON output
with open(json_file, "w") as json_out:
    json_out.write(json_data)

print(f"Converted: {yin_file} -> {json_file}")
