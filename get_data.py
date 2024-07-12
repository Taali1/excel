import requests
import json
import xml.etree.ElementTree as ET
import pandas as pd

with open('config.json', 'r') as file:
    config = json.load(file)

def get_data(url: str):
    response = requests.get(url)
    return response.content

def parse_xml(xml_data):
    root = ET.fromstring(xml_data)
    return root

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

def xml_to_dict(root):
    return {root.tag: element_to_dict(root)}


xml_data = get_data(config['url'])

if xml_data:
    root = parse_xml(xml_data)
    
    if root is not None:
        xml_dict = xml_to_dict(root)
        print(json.dumps(xml_dict, indent=4, ensure_ascii=False))
