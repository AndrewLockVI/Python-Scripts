
from selenium import webdriver
from selenium.webdriver.chrome.options import Options 
from selenium.webdriver.common.by import By
import time
import pyautogui
from PIL import Image
import os
from dotenv import load_dotenv

load_dotenv()

password = os.getenv("type_racer_password")
username = os.getenv("type_racer_username")



def findText(itemList):
    for i in itemList:
        if(len(i) > 40):
            return i
    


while True:
    driver = webdriver.Chrome()

    driver.get("https://play.typeracer.com/")
    driver.maximize_window()






    time.sleep(1)

    driver.find_element(by=By.XPATH,value='//*[@id="userInfo"]/div/div[2]/div[2]/div[1]/a[2]').click()
    driver.find_element(by=By.XPATH, value='/html/body/div[5]/div/div/div[3]/div/div[1]/div/table[1]/tbody/tr[2]/td/div/table/tbody/tr[1]/td[2]/input').send_keys(username)
    driver.find_element(by=By.XPATH, value='/html/body/div[5]/div/div/div[3]/div/div[1]/div/table[1]/tbody/tr[2]/td/div/table/tbody/tr[2]/td[2]/table/tbody/tr[1]/td/input').send_keys(password)
    driver.find_element(by=By.XPATH, value='/html/body/div[5]/div/div/div[3]/div/div[1]/div/table[1]/tbody/tr[2]/td/div/table/tbody/tr[4]/td[2]/table/tbody/tr/td[1]/button').click()
    time.sleep(1)
    driver.find_element(by=By.XPATH, value='/html/body/div[6]/div/div/div[1]').click()

    time.sleep(2)


    startButton = driver.find_element(by=By.XPATH, value='//*[@id="gwt-uid-1"]/a')

    startButton.click()

    time.sleep(2)

    currentText =  driver.find_elements(by=By.TAG_NAME, value="table")

    alltext = ""

    for i in currentText:
        alltext += i.text


    allList = alltext.split("\n")

    iminput = Image.open('inputbar.png')
    imStart = Image.open('startRace.png')



    while True:
        if pyautogui.locateOnScreen(imStart) != None:
            print("starting")
            break

    while True:
        if pyautogui.locateOnScreen(iminput) != None:
            inputLocation = pyautogui.locateOnScreen(iminput)
            pyautogui.moveTo(inputLocation)
            break


    pyautogui.click()


    textAll = findText(allList)
    for i in textAll:
        pyautogui.write(i)
        

    time.sleep(5)
    driver.close()