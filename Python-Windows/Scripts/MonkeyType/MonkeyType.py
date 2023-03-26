#Warning this does get flagged by monkeytype as bot behavior. I could probably get around this by sending single characters at a time, but the point is it works.




import selenium.webdriver as wd
import time
from selenium.webdriver.common.by import By
import random

options = wd.ChromeOptions()
options.add_argument("user-data-dir=C:\\Users\\andre\\AppData\\Local\\Google\\Chrome\\User Data")

driver = wd.Chrome(options=options)

driver.get("https://monkeytype.com/")


time.sleep(3)

running = True
lastList = []

firstTime = True



try:
    while running:
        textEle = driver.find_element(by=By.ID, value="words")
        textIn = driver.find_element(by=By.ID, value="wordsInput")



        wordList = textEle.text.replace('\n', ' ').split(' ') 

        print(wordList)
        if not firstTime:
            
            start = wordList.index(lastList[len(lastList) - 1])
            wordList = wordList[start + 1:]
            print(wordList)
        else:
            firstTime = False



        lastList = wordList

        

        for i in wordList:
            
            textIn.send_keys(i + " ")
            time.sleep(random.choice([.7, .6, .43, .54, .34 , .4, .3]))

except:
    time.sleep(4)

