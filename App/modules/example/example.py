from ..DroneModuleFrame import DroneModuleFrame

class DroneModule(DroneModuleFrame):

    def __init__(self):
        name = "Example"
        options = {'example': {'value': 'testvalue', 'description': 'I am a description'}}
        DroneModuleFrame.__init__(self, name, options)

    def Analyze(self):
        print("I am analyzing stuff")

    def Exploit(self):
        print("I am exploiting stuff")
