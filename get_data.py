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
            
            return xml_dict

def filter_xml(xml):
    result = []
    xml = xml['offers']['o']

    for product in xml:
        if int(product['avail']) > 0:
            result += [product]
        else:
            continue
    return result

def group_xml(xml, group):
    return [product for product in xml if product['cat']['text'] in group]

def save_xml(xml):
    json_str = json.dumps(xml, indent=4, ensure_ascii=False)
    with open('xml_data.txt', 'w', encoding='utf-8') as file:
        file.write(json_str)

groups = [
    ['/FIRANY/FIRANY GOTOWE/ŻAKARDOWE'], # Firany gotowe
    ['/FIRANY/FIRANY GOTOWE/MAKRAMY', '/FIRANY/FIRANY GOTOWE/PANELE'], #Makramy i Panele
    ['/KOCE I NARZUTY/NARZUTY'], # Narzuty
    ['/OBRUSY I BIEŻNIKI/OBRUSY', '/OBRUSY I BIEŻNIKI/BIEŻNIKI I SERWETY'], # Obrusy i bierzniki
    ['POSZEWKI I PODUSZKI/POSZEWKI', 'POSZEWKI I PODUSZKI/PODUSZKI'], # Poszewki i poduszki
    ['/POŚCIEL I PRZEŚCIERADŁA/POŚCIEL', '/POŚCIEL I PRZEŚCIERADŁA/PRZEŚCIERADŁA'], # Pościele i prześcieradła
    ['/RĘCZNIKI I ŚCIERKI/RĘCZNIKI', '/RĘCZNIKI I ŚCIERKI/ŚCIERKI KUCHENNE'], # Ręczniki i ścierki
    ['/TKANINY I ZASŁONY/ZASŁONY GOTOWE/JEDNOBARWNE'] # Zasłony gotowe
]

def separate_desc(desc: str, name: str) -> dict:
    desc = desc.split('<br>')
    desc_result = {}
    for x in desc:
        temp = x.split(':')
        match temp[0][1:]:
            case 'Kolor':
                desc_result['color'] = temp[1]
            case 'Skład':
                desc_result['sklad'] = temp[1]
            case 'Gramatura': 
                desc_result['gramatura'] = temp[1]
    name = name.split(',')
    size = name[1].split('x')
    name_result = {}
    for x in size:
        temp = x.split()
        match temp[0]:
            case 'wysokość':
                name_result['height'] = temp[1][:-2]
            case 'szerokość':
                name_result['width'] = temp[1]
    
    return desc_result, name_result


# xml = get_xml()
# xml = filter_xml(xml)
# xml = group_xml(xml, groups[0])
# print(len(xml))