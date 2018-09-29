from ..DroneModuleFrame import DroneModuleFrame
from . import findcreds

class DroneModule(DroneModuleFrame):
    
    def __init__(self):
        name = "Find_Credentials"
        options = {'firmware_dir':
                    {'value': 'rootfs', 'description' : 'The root of the pulled firmware file structure'},
                   'scan_all':
                     {'value': False, 'description' : 'Set True to scan the whole filesystem'},
                   'outfile':
                     {'value': None, 'description' : 'Set the output file location'},
                   'regex':
                     {'value': None, 'description' : 'Set the Regex expression to be used for file scans'}}
        DroneModuleFrame.__init__(self, name, options)

    def Analyze(self):
        if self.options['outfile']['value'] is not None:
            findcreds.setOutfile(self.options['outfile']['value']
        if self.options['regex']['value'] is not None:
            findcreds.setRegex(self.options['outfile']['value']
        findcreds.findcreds(self.options['outfile']['value'], self.options['scan_all']['value'])
