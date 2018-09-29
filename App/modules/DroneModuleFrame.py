
class DroneModuleFrame(object):
    def __init__(self, name):
        self.name = name

    def Analyze(self):
        raise NotImplementedError()

    def Exploit(self):
        raise NotImplementedError()
