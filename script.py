import argparse
import json
import yaml
import xml.etree.ElementTree as ET

def parse_arguments():
  parser = argparse.ArgumentParser(description="Process some files.")
  parser.add_argument('--load-json', type=str, help='Path to the JSON file to load')
  parser.add_argument('--save-json', type=str, help='Path to the JSON file to save')
  parser.add_argument('--load-yaml', type=str, help='Path to the YAML file to load')
  parser.add_argument('--save-yaml', type=str, help='Path to the YAML file to save')
  parser.add_argument('--load-xml', type=str, help='Path to the XML file to load')
  parser.add_argument('--save-xml', type=str, help='Path to the XML file to save')
  parser.add_argument('--data', type=str, help='Data to save (as JSON string)')
  args = parser.parse_args()
  return args

def load_json(file_path):
  try:
    with open(file_path, 'r') as file:
      data = json.load(file)
    print("JSON data loaded successfully.")
    return data
  except json.JSONDecodeError as e:
    print("Error decoding JSON: {e}")
  except FileNotFoundError:
    print("File not found.")

def save_json(data, file_path):
  try:
    with open(file_path, 'w') as file:
      json.dump(data, file, indent=4)
    print("Data saved to JSON file successfully.")
  except Exception as e:
    print("Error saving JSON: {e}")

def load_yaml(file_path):
  try:
    with open(file_path, 'r') as file:
      data = yaml.safe_load(file)
    print("YAML data loaded successfully.")
    return data
  except yaml.YAMLError as e:
    print("Error loading YAML: {e}")
  except FileNotFoundError:
    print("File not found.")

def save_yaml(data, file_path):
  try:
    with open(file_path, 'w') as file:
      yaml.dump(data, file, default_flow_style=False)
    print("Data saved to YAML file successfully.")
  except Exception as e:
    print("Error saving YAML: {e}")

def load_xml(file_path):
  try:
    tree = ET.parse(file_path)
    root = tree.getroot()
    print("XML data loaded successfully.")
    return root
  except ET.ParseError as e:
    print("Error parsing XML: {e}")
  except FileNotFoundError:
    print("File not found.")
  return None

def save_xml(data, file_path):
  try:
    root = ET.Element("root")
    for key, value in data.items():
      element = ET.SubElement(root, key)
      element.text = str(value)
    tree = ET.ElementTree(root)
    tree.write(file_path)
    print("Data saved to XML file successfully.")
  except Exception as e:
    print("Error saving XML: {e}")

def main():
  args = parse_arguments()
  data = None
  if args.data:
    data = json.loads(args.data)

  if args.load_json:
    data = load_json(args.load_json)
  if args.save_json and data is not None:
    save_json(data, args.save_json)

  if args.load_yaml:
    data = load_yaml(args.load_yaml)
  if args.save_yaml and data is not None:
    save_yaml(data, args.save_yaml)

  if args.load_xml:
    data = load_xml(args.load_xml)
  if args.save_xml and data is not None:
    if isinstance(data, ET.Element):
      data = {child.tag: child.text for child in data}
    save_xml(data, args.save_xml)

if __name__ == "__main__":
  main()
