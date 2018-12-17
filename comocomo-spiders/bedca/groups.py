import json
from common import navigate_to_groups
from selenium import webdriver

def serialize_groups_to_json():
    try:
        driver = webdriver.Chrome()
        options = navigate_to_groups(driver)
        # looping through options
        groups = [{'group_name': option.text,
                   'group_id': option.get_attribute('value')} for option in options]

        with open("groups.json", "w") as write_file:
            json.dump(groups, write_file)
    finally:
        driver.close()

serialize_groups_to_json()
