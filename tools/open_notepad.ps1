# Open Notepad, bring to foreground, and type text
Start-Process 'C:\Windows\System32\notepad.exe'
Start-Sleep -Seconds 3

# Bring Notepad window to foreground
$wshell = New-Object -ComObject wscript.shell
$wshell.AppActivate('notepad')
Start-Sleep -Seconds 1

# Type the text
Add-Type -AssemblyName System.Windows.Forms
[System.Windows.Forms.SendKeys]::SendWait('halo ini jenny')
