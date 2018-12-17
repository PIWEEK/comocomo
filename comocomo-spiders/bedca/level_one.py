import time
from selenium import webdriver
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
except:
    print("WTF!")
finally:
    driver.close()
