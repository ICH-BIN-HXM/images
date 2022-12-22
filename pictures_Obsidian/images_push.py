import pyautogui
import time
import os
from datetime import datetime


Path = r'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Git\Git Bash.lnk'
os.startfile(Path)

coords = pyautogui.locateCenterOnScreen('C:/Users/Xiaomeng Huang/Pictures/Saved Pictures/MINGW64.png',confidence=0.8)

while coords is None:
    coords = pyautogui.locateCenterOnScreen('C:/Users/Xiaomeng Huang/Pictures/Saved Pictures/MINGW64.png',confidence=0.8)

with pyautogui.hold('alt'):
        pyautogui.press('2')

pyautogui.typewrite('cd D:/images_Github/pictures_Obsidian')
pyautogui.press('enter')

coords = pyautogui.locateCenterOnScreen('C:/Users/Xiaomeng Huang/Pictures/Saved Pictures/pictures_obsidian.png',confidence=0.8)

while coords is None:
    coords = pyautogui.locateCenterOnScreen('C:/Users/Xiaomeng Huang/Pictures/Saved Pictures/pictures_obsidian.png',confidence=0.8)




pyautogui.typewrite('git pull')
pyautogui.press('enter')
time.sleep(2)


pyautogui.typewrite('git add .')
pyautogui.press('enter')

time.sleep(2)
pyautogui.typewrite('git commit -m \'')


# Getting the current date and time
dt = datetime.now()
# getting the timestamp
ts = datetime.timestamp(dt)
# convert to datetime
date_time = datetime.fromtimestamp(ts)
# convert timestamp to string in dd-mm-yyyy HH:MM:SS
str_date_time = date_time.strftime("%d-%m-%Y_%H-%M-%S")

pyautogui.typewrite(str_date_time)

pyautogui.typewrite('\'')
pyautogui.press('enter')

time.sleep(2)
pyautogui.typewrite('git push')
pyautogui.press('enter')

time.sleep(2)
pyautogui.typewrite('git pull')
pyautogui.press('enter')