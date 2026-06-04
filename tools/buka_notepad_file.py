import subprocess
import time
import pyautogui

pyautogui.FAILSAFE = False

# 1. Open the text file with Notepad
notepad_path = 'C:\\Windows\\System32\\notepad.exe'
file_path = 'C:\\AI-Agent\\outputs\\halo_ini_jenny.txt'
subprocess.Popen([notepad_path, file_path])
time.sleep(3)

# 2. Force Notepad to foreground using PowerShell
ps_script = '''
$wshell = New-Object -ComObject wscript.shell
$wshell.AppActivate("notepad")
Start-Sleep -Milliseconds 1000
'''
subprocess.run(['powershell', '-Command', ps_script], capture_output=True)
time.sleep(1)

print("SUCCESS: Done")
