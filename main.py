import winreg
import os
import sys
import win32com.shell.shell as shell
ASADMIN = 'asadmin'

if sys.argv[-1] != ASADMIN:
    script = os.path.abspath(sys.argv[0])
    params = ' '.join([script] + sys.argv[1:] + [ASADMIN])
    shell.ShellExecuteEx(lpVerb='runas', lpFile=sys.executable, lpParameters=params)





class Task:
    def __init__(self):
        self.register_path = ""
        self.description = ""
        self.key_name = ""
        self.key_value=None
        self.key_type=None
        self.mode = None

    def run(self):
        try:
            key = winreg.CreateKey(self.mode, self.register_path)

            winreg.SetValueEx(key, self.key_name, 0, self.key_type, self.key_value)

            winreg.CloseKey(key)
        except:
            print(self.register_path)
            print(self.description)
            print(self.key_name)
            print(self.key_value)
            print(self.mode)
            print(self.key_type)
            print("----------------------------------------------")


        

class Tweaker:
    def __init__(self, path):
        self.file_path=path
        self.file_data=self.read_file(self.file_path).split("\n\n")
        self.tasks = []
        self.winreg_types = {
            "HKEY_CLASSES_ROOT":winreg.HKEY_CLASSES_ROOT,
            "HKEY_LOCAL_MACHINE":winreg.HKEY_LOCAL_MACHINE,
            "HKEY_USERS": winreg.HKEY_USERS,
            "HKEY_CURRENT_USER":winreg.HKEY_CURRENT_USER,
        }
        self.winreg_modes = {
            "dword":winreg.REG_DWORD,
            "string":winreg.REG_SZ
        }
    def read_file(self, path):
        with open(path, 'r') as file:
            return file.read()
    def createTasks(self):
        for i in self.file_data:
            tmp_task = Task()
            
            g = i.replace(";", "").split("\n")

            tmp_task.description = g[0]
            
            tmp_task.key_name = g[2].split("=")[0].replace("\"", "")
            
            if(len(g[2].split("=")[1].split(":")) > 1):
                b1=g[2].split("=")[1].split(":")[0]
                b2=g[2].split("=")[1].split(":")[1]
                try:
                    tmp_task.key_value=int(b2, 16)
                    tmp_task.key_type=self.winreg_modes[b1]

                except:
                    print("Error")
                

            else:
                tmp_task.key_value=g[2].replace("\"", "").split("=")[1]
                tmp_task.key_type=self.winreg_modes['string']
            
            g[1]=g[1][:-1]
            g[1]=g[1][1:]

            
            tmp_task.mode=self.winreg_types[g[1][:g[1].find("\\")]]
            tmp_task.register_path = g[1][g[1].find("\\")+1:]
            
            self.tasks.append(tmp_task)
    def runAllTasks(self):
        for i in self.tasks:    
            i.run()

tweaker = Tweaker("data\\mega_tweak_registry_pack.txt")
tweaker.createTasks()
for i in tweaker.tasks:
            print(i.register_path)
            print(i.description)
            print(i.key_name)
            print(i.key_value)
            print(i.mode)
            print(i.key_type)
tweaker.runAllTasks()