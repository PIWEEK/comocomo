import time
import json
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

try:
    driver.get('http://www.bedca.net/bdpub/index.php')

    # clicks to get query page
    docs = driver.find_element_by_xpath('//div[@id="navigation"]/div[4]/a')
    docs.click()
    time.sleep(5)

    # clicks to get general groups
    groups = driver.find_element_by_xpath('//a[@id="General"]')
    groups.click()
    time.sleep(5)

    # dairy groups
    # import pdb; pdb.set_trace()
    select = driver.find_element_by_xpath('//select[@id="fglist"]')
    options = select.find_elements_by_tag_name("option")

    # looping through options
    groups = [{'group_name': option.text,
               'group_id': option.get_attribute('value')} for option in options]

    with open("groups.json", "w") as write_file:
        json.dump(groups, write_file)

except:
    print("WTF!")
finally:
    driver.close()
