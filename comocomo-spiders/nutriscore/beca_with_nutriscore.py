import os
import json

from nutriscore import nutriscore

for filename in os.listdir('data'):
    roo_file = filename.replace('.json', '')
    ori_file = f"./data/{filename}"
    des_file = f"./data/{roo_file}_with_nutriscore.json"
    products = []

    with open(ori_file, "r") as group_file:
        print(f"transforming file {filename}")
        file_text = group_file.read()
        file_json = json.loads(file_text)
        for product in file_json['products']:
            product_data = {'name': product['ori_name'],
                            'nutriscore': nutriscore(product, False, False)}
            products.append(product_data)

        with open(des_file, "w") as dest_file:
            dest_file.write(json.dumps(products))
