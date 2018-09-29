from consolemenu import *
from consolemenu.items import *
import sys
from termcolor import colored

def mod_1(stringring):
    print("module 1")
    print("Press any key to continue...")
    sys.stdin.read(1)

def mod_2(stringring):
    print("module 2")
    print("Press any key to continue...")
    sys.stdin.read(1)

def mod_3(stringring):
    print("module 3")
    print("Press any key to continue...")
    sys.stdin.read(1)

def mod_4(stringring):
    print("module 4")
    print("Press any key to continue...")
    sys.stdin.read(1)

def mod_5(stringring):
    print("module 5")
    print("Press any key to continue...")
    sys.stdin.read(1)

def mod_6(stringring):
    print("module 6")
    print("Press any key to continue...")
    sys.stdin.read(1)

def list_drone_wifi():
    print("Press any key to continue...")
    sys.stdin.read(1)

def list_modules():
    print("Press any key to continue...")
    sys.stdin.read(1)

def print_list_usage():
    return

# List Modules
# List Drone Available Wifi
# use <module>
# run ||  in module setting

def start_menu():
    module_loaded = False
    loaded_module = ""
    while True:
        module_prompt = " exploit(%s)"%(colored(loaded_module, 'red'))
        cmd = raw_input("hackdrones%s>>>"%(module_prompt if module_loaded else ""))
        arguments = cmd.split(" ")
        if arguments[0] == "list":
            if arguments[1] == "modules":
                list_modules()
                pass
            elif arguments[1] == "wifi":
                list_drone_wifi()
                pass
            else:
                print_list_usage()
        elif arguments[0] == "use":
            loaded_module = arguments[1]
            module_loaded = True
        elif arguments[0] == "quit":
            break
        else:
            print_usage()
        
    
   
