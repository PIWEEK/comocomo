import time
import json

from common import navigate_to_groups
from selenium import webdriver
from selenium.webdriver.support.ui import Select

def serialize_subgroups_to_json():
    subgroups = []

    try:
        driver = webdriver.Chrome()
        options = navigate_to_groups(driver)
        driver.implicitly_wait(10)

        for idx, option in enumerate(options):
            index = idx + 1
            option_name = option.text

            sleeping(5, f'next iteration {index}')
            select = Select(driver.find_element_by_xpath('//select[@id="fglist"]'))
            select.select_by_index(index)

            submit = driver.find_element_by_xpath('//input[@type="button" and @value="Consultar"]')
            submit.click()
            sleeping(5, 'next group elements')

            items = driver.find_elements_by_xpath('//tr[starts-with(@class, "row-")]')
            subgroup = create_subgroup(option_name, items)
            subgroups.append(subgroup)

            options = navigate_to_groups(driver)
    finally:
        driver.close()

    return subgroups

def sleeping(seconds, message):
    print(f"sleeping... {message}")
    time.sleep(seconds)

def create_subgroup(option, food_items):
    print(f"creating group {option}")
    import pdb; pdb.set_trace()
    food_list = [{'id': food.find_element_by_xpath('/td[position()=1]/a').text,
                  'name': food.find_element_by_xpath('/td[position()=2]/a').text,
                  'spanish_name': food.find_element_by_xpath('/td[position()=3]/a').text} for food in food_items]

    subgroup = {'name': option, 'items': food_list}
    print(subgroup)
    return subgroup

serialize_subgroups_to_json()
