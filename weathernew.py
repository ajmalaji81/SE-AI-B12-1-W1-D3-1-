import pyautogui
import time
import pyscreeze
from datetime import datetime

pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0.5

print("Open the chrome browser...")
time.sleep(2)  

pyautogui.hotkey('win', 'r', interval=0.1)
time.sleep(1)
pyautogui.typewrite('chrome\n', interval=0.1)
time.sleep(2)
pyautogui.hotkey('alt', 'space')
time.sleep(1)
pyautogui.press('x')
time.sleep(2)

time.sleep(2)

# Move through the Chrome profile options
pyautogui.press('tab', presses=7,)

# Select the highlighted profile
pyautogui.press('enter')

print("Opening the website...")
# Open a new tab
pyautogui.hotkey("ctrl", "t")
time.sleep(1)

pyautogui.typewrite("https://www.accuweather.com/en/in/pondicherry/1-190056_1_al/current-weather/1-190056_1_al",interval=0.1)
time.sleep(1), 
pyautogui.press('enter', interval=0.5)

pyautogui.hotkey('ctrl', 'a', interval=0.1)

pyautogui.hotkey('ctrl', 'c', interval=0.1)
time.sleep(2)

print("Copying the data...")

import os
import subprocess
import time
import pyautogui

# 1. Launch Excel directly instead of typing into the system menu
subprocess.Popen(["start", "excel"], shell=True)
time.sleep(5)  # Wait for Excel to fully open

# 2. Select 'Blank workbook' (Enter typically opens the default selected blank template)
pyautogui.press('enter')
time.sleep(2)

# 3. Paste clipboard contents
pyautogui.hotkey('ctrl', 'v')
time.sleep(1)

# 4. Save file via F12 (opens the direct 'Save As' dialog, bypassing Backstage view)
pyautogui.press('f12')
time.sleep(2)

# 5. Type the filename and save
pyautogui.typewrite('weather_data.xlsx\n', interval=0.1)
filepath = os.path.abspath('weather_data.xlsx')
pyautogui.typewrite(filepath, interval=0.05)
time.sleep(0.5)
pyautogui.press('enter')
time.sleep(2)

# 6. Take screenshot and log
pyautogui.screenshot('weather_screenshot.png')
print(f"Data saved to {filepath}")
