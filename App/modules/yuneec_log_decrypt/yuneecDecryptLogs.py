#!/usr/bin/python3

from pyDes import *
import binascii

def usage():
	print("usage: python3 yuneecDecryptLogs.py [encrypted Log File Path]")

if len(sys.argv) != 2:
	usage()
	exit(1)

# password similar to ks Yuneec...
key = des("ksYuN2eC", CBC, "\0\0\0\0\0\0\0\0", pad=None, padmode=PAD_PKCS5)

with open(sys.argv[1], 'rb') as f:
	data = f.read()

print(key.decrypt(data).decode("UTF-8"))
