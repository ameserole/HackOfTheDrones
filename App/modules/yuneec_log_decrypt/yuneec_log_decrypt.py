#!/usr/bin/python3

from ..DroneModuleFrame import DroneModuleFrame
from pyDes import *
import binascii

class DroneModule(DroneModuleFrame):

	def __init__(self):
		name = "Yuneec Log Decryption"
		options = {'file': {'value':'gps.csv','description':'Encrypted Yuneec GPS Logs'}}
		DroneModuleFrame.__init__(self, name, options)

	def Exploit(self):
		# password similar to ks Yuneec...
		key = des("ksYuN2eC", CBC, "\0\0\0\0\0\0\0\0", pad=None, padmode=PAD_PKCS5)

		with open(self.options["file"]["value"], 'rb') as f:
			data = f.read()

		print(key.decrypt(data).decode("UTF-8"))
