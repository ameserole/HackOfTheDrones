#!/usr/bin/python3

from os.path import basename

from ..DroneModuleFrame import DroneModuleFrame
from pyDes import *
from .gpx import yuneec_to_gpx


class DroneModule(DroneModuleFrame):

    def __init__(self):
        name = "Yuneec Log Decryption"
        options = {
            'in_file': {'value': 'encrypted_track.log', 'description':'Path to encrypted Yuneec GPS log file'},
            'out_file': {'value': 'decrypted_track.gpx', 'description': 'Destination file path to write decrypted GPS log'},
            'format': {'value': 'gpx', 'description': 'output format, either "raw" or "gpx"'}
        }
        DroneModuleFrame.__init__(self, name, options)

    def Exploit(self):
        # password similar to ks Yuneec...
        key = des("ksYuN2eC", CBC, "\0\0\0\0\0\0\0\0", pad=None, padmode=PAD_PKCS5)

        in_file = self.options["in_file"]["value"]

        with open(in_file, 'rb') as f:
            data = f.read()

        output = key.decrypt(data).decode("UTF-8")

        if self.options['format']['value'] == 'gpx':
            output = yuneec_to_gpx(output, skip_headers=True, title=basename(in_file))

        with open(self.options['out_file']['value'], 'w') as f:
            f.write(output)

        print('success!')

