import subprocess
import time
import pyautogui
import pyperclip
import os

pyautogui.FAILSAFE = False

# 1. Launch fresh Notepad
subprocess.Popen(['notepad.exe'], shell=True)
time.sleep(3)

# 2. Paste text via clipboard
pyperclip.copy('Halo ini jenny')
time.sleep(0.5)
pyautogui.hotkey('ctrl', 'v')
time.sleep(1)

# 3. Force Notepad to front using PowerShell AppActivate
ps_script = '''
$wshell = New-Object -ComObject wscript.shell
$wshell.AppActivate("notepad")
Start-Sleep -Seconds 1
'''
subprocess.run(['powershell', '-Command', ps_script], capture_output=True)
time.sleep(1)

print("SUCCESS: Done")
