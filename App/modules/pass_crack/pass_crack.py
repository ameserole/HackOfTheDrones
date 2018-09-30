from ..DroneModuleFrame import DroneModuleFrame

class DroneModule(DroneModuleFrame):

    def __init__(self):
        name = "pass_crack"
        options = {'inputfile': {"value": "dumby.txt", "description": "descrp"}}
        options['wordlist'] = {"value": "dumby2.txt", "description": "descrp"}
        DroneModuleFrame.__init__(self, name, options)

    def Analyze(self):
        import os
        os.system("screen -d -m john %s %s" %(self.options["inputfile"]['value'],self.options["wordlist"]['value']))
