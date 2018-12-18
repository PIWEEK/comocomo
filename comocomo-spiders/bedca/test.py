import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import time
import json

from selenium import webdriver

def get_kaleiders():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get('http://www.kaleidos.net')

    kaleiders = []

    try:
        kaleider_divs = driver.find_elements_by_xpath('//div[@class="kaleiders"]/div[@class="square"]')
        print(len(kaleider_divs))
        kaleiders = [{'name': get_kaleider_name(kaleider)} for kaleider in kaleider_divs]
    finally:
        driver.close()

    print(kaleiders)


def get_kaleider_name(kaleider):
    return kaleider.find_element_by_xpath('a').get_attribute('alt')

get_kaleiders()
