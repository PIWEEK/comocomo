import json
from common import navigate_to_groups
from selenium import webdriver

def serialize_subgroups_to_json():
    try:
        driver = webdriver.Chrome()
        options = navigate_to_groups(driver)

        for option in options:
            option.select()
            submit = driver.find_element_by_xpath('//input[@type="button" && value="Consultar"]')
            submit.click()
            food_elements = driver.find_element_by_xpath('//tr[starts-with(@class, "row-")')
            for food in food_elements:
                name = food.find_element_by_xpath('//td[@id="foodname"]/a').text
                print(name)
                print('end loop')
            break

        print('end')
    finally:
        driver.close()


serialize_subgroups_to_json()
