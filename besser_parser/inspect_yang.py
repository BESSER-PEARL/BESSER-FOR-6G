import json
import os
import sys

def print_groupings(data, indent=0):
    """Print all grouping definitions in the YANG file"""
    if isinstance(data, dict):
        if 'grouping' in data:
            groupings = data['grouping']
            if not isinstance(groupings, list):
                groupings = [groupings]
            print(f"{' ' * indent}Found {len(groupings)} groupings:")
            for grouping in groupings:
                name = grouping.get('@name', 'unknown')
                desc = grouping.get('description', {}).get('text', '').split('\n')[0]
                print(f"{' ' * (indent+2)}- {name}: {desc}")
                
                # Print leaves
                if 'leaf' in grouping:
                    leaves = grouping['leaf']
                    if not isinstance(leaves, list):
                        leaves = [leaves]
                    print(f"{' ' * (indent+4)}Leaves ({len(leaves)}):")
                    for leaf in leaves:
                        leaf_name = leaf.get('@name', 'unknown')
                        leaf_type = leaf.get('type', {}).get('@name', 'unknown')
                        print(f"{' ' * (indent+6)}- {leaf_name}: {leaf_type}")
        else:
            for key, value in data.items():
                if key == 'module':
                    print_groupings(value, indent)

def print_augments(data, indent=0):
    """Print all augment definitions in the YANG file"""
    if isinstance(data, dict):
        if 'augment' in data:
            augments = data['augment']
            if not isinstance(augments, list):
                augments = [augments]
            print(f"{' ' * indent}Found {len(augments)} augments:")
            for augment in augments:
                target = augment.get('@target-node', 'unknown')
                print(f"{' ' * (indent+2)}- Target: {target}")
                
                # Print uses
                if 'uses' in augment:
                    uses = augment['uses']
                    if not isinstance(uses, list):
                        uses = [uses]
                    for use in uses:
                        print(f"{' ' * (indent+4)}Uses: {use.get('@name', 'unknown')}")
        else:
            for key, value in data.items():
                if key == 'module':
                    print_augments(value, indent)

def main():
    if len(sys.argv) < 2:
        print("Usage: python inspect_yang.py <yang_json_file>")
        return
        
    filepath = sys.argv[1]
    if not os.path.exists(filepath):
        print(f"Error: File {filepath} does not exist")
        return
        
    try:
        with open(filepath, 'r') as f:
            data = json.load(f)
            
        print(f"Inspecting YANG file: {filepath}")
        print("\n=== Groupings ===")
        print_groupings(data)
        
        print("\n=== Augments ===")
        print_augments(data)
            
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
