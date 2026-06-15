import subprocess
import time
import pyautogui
import pyperclip

pyautogui.FAILSAFE = False

# 1. Launch fresh Notepad
subprocess.Popen(['notepad.exe'], shell=True)
time.sleep(2)

# 2. Paste text via clipboard
pyperclip.copy('Halo ini jenny')
time.sleep(0.3)
pyautogui.hotkey('ctrl', 'v')
time.sleep(0.5)

# 3. Bring Notepad to front - press Alt+Tab to cycle
for _ in range(5):
    pyautogui.hotkey('alt', 'tab')
    time.sleep(0.3)
time.sleep(1)

print("SUCCESS: Done")
