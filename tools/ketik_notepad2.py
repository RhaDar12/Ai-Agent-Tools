import subprocess
import time
import pyautogui
import pyperclip

pyautogui.FAILSAFE = False

# Launch Notepad using full path
proc = subprocess.Popen(['notepad.exe'], shell=True)
time.sleep(3)

# Bring Notepad to foreground
pyautogui.hotkey('alt', 'tab')
time.sleep(0.5)

# Use clipboard to paste clean text
pyperclip.copy('Halo ini jenny')
time.sleep(0.3)
pyautogui.hotkey('ctrl', 'v')
time.sleep(0.5)

print("SUCCESS: Done")
