#!/usr/bin/env python3.7

from socket import*
import sys, time
from datetime import datetime

global officialport

host = ''
max_port=5000
min_port=1

def scan_host(host, port, r_code = 1):
	try:
		s = socket(AF_INET,SOCK_STREAM)
		code = s.connect_ext((host,port))
		
		if code == 0:
			r_code==code
		s.close()
	
	except Exception:
		pass
	
	return r_code
	

try:
	host = input("[*] Enter Target Host Address please. ")

except KeyboardInterrupt:
	print("\n\n[*] User Requested An interrupt.")
	print("Application is shutting down. :(")
	sys.exit(1)

hostip=gethostbyname(host)

print("\n[*] Host: %s	IP: %s " % (host, hostip))
print("\n[*] Scanning started at %s...  \n" % (time.strftime("%H:%M:%S")))

start_time = datetime.now()

for port in range(min_port,max_port):
	try:
		response = scan_host(host,port)
		
		if response == 0:
			
			officialport = port #This will be carried over to the SSH login
			
			print("[*] Port %d: is Wide Open! ATTACK!!!" % (port))
		
	except Exception:
		pass
				
stop_time = datetime.now()

total_time = stop_time - start_time

print("\n Scanning Finished at %s ... This took %s ... " % (time.strftime("%H:%M:%S"),total_time))	
print("Have a good day! \nI'm always watching you. - HAL")
