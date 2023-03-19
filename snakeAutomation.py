import pyautogui
import time
from PIL import Image
import pydirectinput

#This script can't work because my computer is too slow with the image recognition to change directions on the fly.


def vert(movingLeft):

    if movingLeft:
        pyautogui.press("up")
    else:
        pyautogui.press("down")
    
 




leftImg = Image.open('Left.png')
rightImg = Image.open('Right.png')
topImg = Image.open('Top.png')
bottomImg = Image.open('Bottom.png')

 
pyautogui.click(1402,690)
pyautogui.click(1402,690)

count = 0 
while True:
    sc1 = pyautogui.screenshot()

    if pyautogui.locateOnScreen(rightImg) != None:
        print("right")
        pydirectinput.press(['up', 'up'])
    






    


