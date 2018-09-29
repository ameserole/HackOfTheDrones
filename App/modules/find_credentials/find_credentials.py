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
                     {'value': '(((passw(or)?d)|(passphrase)|(pass)|(key)) *[:=] *.*)|(^[#]?\w+:[^\n]*)', 'description' : 'Set the Regex expression to be used for file scans'}}
        DroneModuleFrame.__init__(self, name, options)

    def Analyze(self):
        if self.options['outfile']['value'] == "None":
            self.options['outfile']['value'] = None
        if self.options['scan_all']['value'] == "True":
            self.options['scan_all']['value'] = True
        if self.options['scan_all']['value'] == "False":
            self.options['scan_all']['value'] = False
        findcreds.findcreds(self.options['firmware_dir']['value'], self.options['scan_all']['value'], self.options['regex']['value'], self.options['outfile']['value'])
