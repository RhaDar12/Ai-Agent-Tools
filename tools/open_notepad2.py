import subprocess
import time
import pyautogui
pyautogui.FAILSAFE = False

# Launch Notepad
proc = subprocess.Popen(['C:\\Windows\\System32\\notepad.exe'])
time.sleep(2)

# Type with delay between each character
pyautogui.write('halo ini jenny', interval=0.2)
time.sleep(0.5)

print("SUCCESS: Done")
