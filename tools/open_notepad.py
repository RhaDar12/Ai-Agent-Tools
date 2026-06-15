import subprocess
import time
import pyautogui

# Launch Notepad
subprocess.Popen(['C:\\Windows\\System32\\notepad.exe'])
time.sleep(2)

# Type the text
pyautogui.write('halo ini jenny', interval=0.1)
print("SUCCESS: Text typed successfully")
