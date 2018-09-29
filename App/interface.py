import importlib
import os

class DroneInterface:
    def __init__(self, module_name):
        mod_name = 'App.modules.{}.{}'.format(module_name, module_name)
        module = importlib.import_module(mod_name)
        self.drone_module = module.DroneModule()

    def Analyze(self):
        self.drone_module.Analyze()

    def Exploit(self):
        self.drone_module.Exploit()

    
