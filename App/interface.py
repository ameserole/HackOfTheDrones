import importlib
import os
import sys

class DroneInterface:
    def __init__(self, module_name):
        mod_name = 'App.modules.{}.{}'.format(module_name, module_name)
        module = importlib.import_module(mod_name)
        self.drone_module = module.DroneModule()

    def get_options(self):
        self.drone_module.get_options()

    def set_option(self, option, value):
        self.drone_module.set_option(option, value)

    def Analyze(self):
        self.drone_module.Analyze()

    def Exploit(self):
        self.drone_module.Exploit()

    
