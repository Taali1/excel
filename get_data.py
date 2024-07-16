import requests
import json
import xml.etree.ElementTree as ET
import pandas as pd

# Load the configuration file
with open('config.json', 'r') as file:
    config = json.load(file)

# Function to fetch XML data from the provided URL
def get_data(url: str):
    response = requests.get(url)
    return response.content

# Function to parse XML data into an ElementTree
def parse_xml(xml_data):
    root = ET.fromstring(xml_data)
    return root

# Recursive function to convert an XML element and its children into a dictionary
def element_to_dict(element):
    elem_dict = {}
    if element.attrib:
        elem_dict.update(element.attrib)
    if element.text and element.text.strip():
        elem_dict['text'] = element.text.strip()
    
    for child in element:
        child_dict = element_to_dict(child)
        if child.tag not in elem_dict:
            elem_dict[child.tag] = child_dict
        else:
            if not isinstance(elem_dict[child.tag], list):
                elem_dict[child.tag] = [elem_dict[child.tag]]
            elem_dict[child.tag].append(child_dict)
    
    return elem_dict

# Function to convert the entire XML tree to a dictionary
def xml_to_dict(root):
    return {root.tag: element_to_dict(root)}

# Function to fetch, parse, convert XML to dict, print it, and save to a text file
def get_xml():
    xml_data = get_data(config['url'])
    if xml_data:
        root = parse_xml(xml_data)
        if root is not None:
            xml_dict = xml_to_dict(root)
            # Print the dictionary as a nicely formatted JSON string
            json_str = json.dumps(xml_dict, indent=4, ensure_ascii=False)
            
            # Save the dictionary to a text file
            with open('xml_data.txt', 'w', encoding='utf-8') as file:
                file.write(json_str)
            
            return xml_dict

# Run the function to fetch and print XML data as a dictionary
