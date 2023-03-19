import pyautogui
import time
count = 0
# This goes through my email when on the right side of the screen and deletes the second page
# while (count < 10):  
#     pyautogui.click(1804,199)
#     pyautogui.click(1242,199)
#     pyautogui.click(1390,201)
#     count += 1
#     time.sleep(2)

# Deletes 300 pages when search is being used
while (count < 300):  
    pyautogui.click(1246,251)
    pyautogui.click(1387,243)
    count += 1
    time.sleep(1.5)