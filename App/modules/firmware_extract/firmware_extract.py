from ..DroneModuleFrame import DroneModuleFrame
from . import firmwareextract

class DroneModule(DroneModuleFrame):

    def __init__(self):
        name = "Firmware_Extract"
        options = {'firmware_extract': 
                    {'value': 'firmware.bin', 'description': 'The firmware from vendor'},
                  'output_folder': 
                  {'value': 'datastore/', 'description': 'The folder to write extracted firmware to'}}
        
        DroneModuleFrame.__init__(self, name, options)

    def Analyze(self):
        #import firmwareextract
        fe_obj = firmwareextract.firmwareExtract(self.options['firmware_extract']['value'])
        fe_obj.run(self.options['output_folder']['value'])


