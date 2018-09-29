import importlib.util
import os

class DroneInterface:
    def __init__(self, module_name):
        mod = os.path.abspath("modules") + os.sep + module_name
        if os.path.isdir(mod) and os.path.exists(mod + os.sep + "__init__.py"):
            self.drone_module = __import__(module_name, fromlist=[''])
        else:
            raise Exception('Module {} not found'.format(module_name)

    def Analyze(self):
        self.drone_module.Analyze()

    def Exploit(self):
        self.drone_module.Exploit()

    
