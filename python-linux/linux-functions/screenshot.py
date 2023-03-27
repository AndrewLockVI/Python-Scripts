import pyautogui
import os


def copy_image(path):
	os.popen('scrot -F ' + path)




img_path = '/home/andrew/pictures/screenshot.png'
im1 = pyautogui.screenshot(img_path)
copy_image(img_path)
