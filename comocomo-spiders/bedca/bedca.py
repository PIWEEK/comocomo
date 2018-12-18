import time
import json
import requests
from lxml import etree
from random import randint

######################
###### CONSTANTS #####
######################

API_ENDPOINT = 'http://www.bedca.net/bdpub/procquery.php'
REQ_HEADERS = {'Content-Type': 'text/xml'}

######################
###### FUNCTIONS #####
######################

def put_to_sleep(message):
    print(message)
    # always waits politely between 2 and 6 seconds
    # before doing anything
    seconds = randint(2, 6)
    time.sleep(seconds)

def load_xml_with_id_and_payload(payload, id=None):
    xml_payload = open(f"xml/{payload}.xml", "r").read()

    if id:
        xml_payload = xml_payload.replace('%IDENTIFIER%', str(id))

    request = requests.post(API_ENDPOINT, data=xml_payload, headers=REQ_HEADERS)
    request.encoding = 'utf-8-sig' # BOM
    raw = request.text.replace('<?xml version="1.0" encoding="utf-8"?>', '')
    xml = etree.fromstring(raw)

    return xml

def extract_attr(food, attribute_name):
    return food.xpath(attribute_name)[0].text

def extract_group_info(food):
    return {'id': extract_attr(food, 'fg_id'),
            'ori_name': extract_attr(food, 'fg_ori_name'),
            'eng_name': extract_attr(food, 'fg_eng_name')}

def extract_product_info(product):
    return {'id': extract_attr(product, 'f_id'),
            'ori_name': extract_attr(product, 'f_ori_name'),
            'eng_name': extract_attr(product, 'f_eng_name')}

def extract_product_values(value):
    return {'eur_name': extract_attr(value, 'eur_name'),
            'u_description': extract_attr(value, 'u_description'),
            'c_ori_name': extract_attr(value, 'c_ori_name'),
            'c_eng_name': extract_attr(value, 'c_eng_name'),
            'best_location': extract_attr(value, 'best_location')}

def dump_to_file(group):
    file_name = f"data/{group['id']}.json"
    group_json = json.dumps(group)

    with open(file_name, "w") as group_file:
        group_file.write(group_json)

######################
####### GROUPS #######
######################

put_to_sleep('extracting groups')
groups = load_xml_with_id_and_payload('groups').xpath('//food')
groups = [extract_group_info(food) for food in groups]

######################
###### PRODUCTS ######
######################

for group in groups:
    put_to_sleep(f"extracting products for group {group['ori_name']}")
    products = load_xml_with_id_and_payload('group', group['id']).xpath('//food')
    products = [extract_product_info(product) for product in products]

    for product in products:
        put_to_sleep(f"extracting values for product {product['ori_name']}")
        values = load_xml_with_id_and_payload('product_simple', 933).xpath('//foodvalue')
        values = [extract_product_values(value) for value in values]
        product['values'] = values

    group['products'] = products
    dump_to_file(group)
