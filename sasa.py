import winreg

key = winreg.CreateKey(winreg.HKEY_CURRENT_USER, "SOFTWARE\\Microsoft\\.NETFramework")

# Set the value of the "Hidden" key to 1 (which means "show hidden files")
winreg.SetValueEx(key, "foo", 0, winreg.REG_SZ, "hidden")


winreg.CloseKey(key)

print(int('38C4', 16))
