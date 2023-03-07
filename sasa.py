import winreg
import os
import sys
import win32com.shell.shell as shell
ASADMIN = 'asadmin'

if sys.argv[-1] != ASADMIN:
    script = os.path.abspath(sys.argv[0])
    params = ' '.join([script] + sys.argv[1:] + [ASADMIN])
    shell.ShellExecuteEx(lpVerb='runas', lpFile=sys.executable, lpParameters=params)
key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, "SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Explorer", 0, winreg.KEY_SET_VALUE)

# Set the value of the "Hidden" key to 1 (which means "show hidden files")
winreg.SetValueEx(key, "foo", 0, winreg.REG_SZ, "hidden")


winreg.CloseKey(key)

print(int('38C4', 16))
