from consolemenu import *
from consolemenu.items import *
import sys
from termcolor import colored

def list_drone_wifi():

    print("Press any key to continue...")
    sys.stdin.read(1)

def list_modules():
    print("Press any key to continue...")
    sys.stdin.read(1)

def print_list_usage():
    return

def print_run_usage():
    return

# List Modules
# List Drone Available Wifi
# use <module>
# run ||  in module setting

def start_menu():
    module_loaded = False
    loaded_module = ""
    drone_inf = ""
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
            drone_inf = DroneInterface(loaded_module)
        elif arguments[0] == "run":
            if arguments[1] == "analyze":
                drone_inf.Analyze()
                pass
            elif arguments[1] == "exploit":
                drone_inf.Exploit()
                pass
            else:
                print_run_usage()
        elif arguments[0] == "quit":
            break
        else:
            print_usage()