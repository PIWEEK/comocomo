import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

def navigate_to_groups(driver):
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
    return options
