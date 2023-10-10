import pyautogui as pag
import time
import random

while True:
    x = random.randint(600,700)
    y = random.randint(200,700)
    pag.moveTo(x,y,1)
    pag.click()
    time.sleep(30)