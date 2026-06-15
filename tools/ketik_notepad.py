import subprocess
import time
import pyautogui
pyautogui.FAILSAFE = False

# Launch Notepad
subprocess.Popen(['C:\\Windows\\System32\\notepad.exe'])
time.sleep(2)

# Type the text
pyautogui.write('Halo ini jenny', interval=0.15)
time.sleep(0.5)

print("SUCCESS: Done")
