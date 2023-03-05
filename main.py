import winreg

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
            print("Error")


        

class Tweaker:
    def __init__(self, path):
        self.file_path=path
        self.file_data=self.read_file(self.file_path).split("\n\n")
        self.tasks = []
        self.winreg_types = {
            "HKEY_CLASSES_ROOT":winreg.HKEY_CLASSES_ROOT,
            "HKEY_LOCAL_MACHINE":winreg.HKEY_LOCAL_MACHINE,
            "HKEY_USERS": winreg.HKEY_USERS,
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
            print(g)
            tmp_task.description = g[0]
            
            tmp_task.key_name = g[2].split("=")[0].replace("\"", "")
            if(len(g[2].split("=")[1].split(":")) > 1):
                b1=g[2].split("=")[1].split(":")[0]
                b2=g[2].split("=")[1].split(":")[1]

            else:
                
                print(g[2].replace("\"", "").split("=")[1])

            try:
                tmp_task.key_value=int(b2)

            except:
                tmp_task.key_value=int(b2)

            tmp_task.key_type=self.winreg_modes[b1]
            
            g[1]=g[1][:-2]
            g[1]=g[1][1:]

            
            tmp_task.mode=self.winreg_types[g[1][:g[1].find("\\")]]
            tmp_task.register_path = g[1][g[1].find("\\"):]
            
            self.tasks.append(tmp_task)


tweaker = Tweaker("data\\mega_tweak_registry_pack.txt")
tweaker.createTasks()
print(tweaker.tasks[0].key_name)