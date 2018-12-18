import time
import json

from common import navigate_to_groups
from selenium import webdriver
from selenium.webdriver.support.ui import Select

def serialize_subgroups_to_json():
    subgroups = []

    try:
        driver = webdriver.Chrome()
        options = [opt.text for opt in navigate_to_groups(driver)]
        driver.implicitly_wait(10)

        for index, option_name in enumerate(options):
            # We need to navigate here again for each iteration to avoid
            # elements to get stale
            navigate_to_groups(driver)

            sleeping(5, f'next iteration {index}')
            select = Select(driver.find_element_by_xpath('//select[@id="fglist"]'))
            select.select_by_index(index)

            submit = driver.find_element_by_xpath('//input[@type="button" and @value="Consultar"]')
            submit.click()
            sleeping(5, 'next group elements')

            items = driver.find_elements_by_xpath('//tr[starts-with(@class, "row-")]')
            subgroup = create_subgroup(option_name, items)
            subgroups.append(subgroup)
    finally:
        driver.close()

    return subgroups

def sleeping(seconds, message):
    print(f"sleeping... {message}")
    time.sleep(seconds)

def create_subgroup(option, food_items):
    print(f"creating group {option}")
    food_list = [{'id': food.find_element_by_xpath('td[position()=1]/a').text,
                  'name': food.find_element_by_xpath('td[position()=2]/a').text,
                  'spanish_name': food.find_element_by_xpath('td[position()=3]/a').text} for food in food_items]

    return {'name': option, 'items': food_list}

serialize_subgroups_to_json()
