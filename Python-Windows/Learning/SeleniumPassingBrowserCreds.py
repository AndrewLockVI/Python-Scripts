#This is a POC file for the purpose of understanding how to use my default chrome profile with selenium. 
#An important note about this is that all chrome tabs must be closed before running otherwise it will just open 
#a blank page and then error out.

import selenium.webdriver as wd
import time
from selenium.webdriver.common.by import By

#Initializes options
options = wd.ChromeOptions()
options.add_argument("user-data-dir=C:\\Users\\andre\\AppData\\Local\\Google\\Chrome\\User Data")


driver = wd.Chrome(chrome_options=options)
driver.get('https://linkedin.com')



time.sleep(2)
searchBar = driver.find_element(by=By.CLASS_NAME, value="search-global-typeahead__input")
searchBar.send_keys("Testing")





time.sleep(4)