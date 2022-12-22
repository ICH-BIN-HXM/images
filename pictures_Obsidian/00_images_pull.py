import pyautogui
import time
import os
#from datetime import datetime


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


