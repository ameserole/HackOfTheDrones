from ..DroneModuleFrame import DroneModuleFrame

class DroneModule(DroneModuleFrame):

    def __init__(self):
        name = "Example"
        DroneModuleFrame.__init__(self, name)

    def Analyze(self):
        print("I am analyzing stuff")

    def Exploit(self):
        print("I am exploiting stuff")
