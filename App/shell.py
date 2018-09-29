import sys, os
from termcolor import colored
sys.path.insert(0, '.')
from interface import DroneInterface

# List Modules
# List Drone Available Wifi
# use <module>
# run ||  in module setting

def list_drone_wifi():
    print("Press any key to continue...")
    sys.stdin.read(1)

def list_modules():
    modules_dir = os.path.abspath(os.path.dirname(__file__))
    modules = os.listdir(modules_dir + "/modules")
    invalid_modules = []
    for module in modules:
        if not os.path.isfile("modules/%s/__init__.py"%module):
            invalid_modules.append(module)
    modules = list(set(modules) - set(invalid_modules))
    print("Modules available for loading...")
    print()
    for module in modules:
        print('\t\t'+module)
    print()
    print()
    print("Press any key to continue...")
    sys.stdin.read(1)

def print_list_usage():
    return

def print_run_usage():
    return

def start_menu():
    module_loaded = False
    loaded_module = ""
    drone_inf = ""
    while True:
        module_prompt = " exploit(%s)"%(colored(loaded_module, 'red'))
        cmd = input("hackdrones%s>>>"%(module_prompt if module_loaded else ""))
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