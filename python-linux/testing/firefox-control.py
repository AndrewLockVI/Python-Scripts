from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
import time
driver = webdriver.Firefox()
driver.get("https://www.google.com")

driver.find_element(by=By.CLASS_NAME, value='gLFyf').send_keys('testing')
time.sleep(3)
driver.close()

import requests

req = requests.get("https://google.com")

print(req.content)

