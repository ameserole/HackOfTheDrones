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

def check_modules():
    modules_dir = os.path.abspath(os.path.dirname(__file__))
    modules = os.listdir(modules_dir + "/modules")
    invalid_modules = []
    for module in modules:
        if not os.path.isfile("App/modules/%s/__init__.py"%module):
            invalid_modules.append(module)
    modules = list(set(modules) - set(invalid_modules))
    return modules

def list_modules():
    modules = check_modules()
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
    print("Available Commands:")
    print("\t\tanalyze - Executes Analyze function of DroneModule")
    print("\t\texploit - Executes Exploit function of DroneModule")
    print("\t\thelp - Displays this menu help")

def print_module_usage():
    print("Available Commands:")
    print("\t\tset <name> <value> - Set <name> field of module with <value>")
    print("\t\tshow - Shows fields of module")
    print("\t\thelp - Displays this menu help")

def print_menu_usage():
    print("Available Commands:")
    print("\t\tlist - Display enumeration of arguement")
    print("\t\tuse - Loads module from modules directory")
    print("\t\tmodule - Access and Manipulate loaded module")
    print("\t\trun - Execute module behavior of argument")
    print("\t\tshow - Display this menu help")

def start_menu():
    module_loaded = False
    loaded_module = ""
    drone_inf = ""
    valid_modules = check_modules()
    while True:
        module_prompt = " exploit(%s)"%(colored(loaded_module, 'red'))
        cmd = input("hackdrones%s>>>"%(module_prompt if module_loaded else ""))
        arguments = cmd.split(" ")
        if arguments[0] == "list":
            if arguments[1] == "modules":
                list_modules()
            elif arguments[1] == "wifi":
                list_drone_wifi()
            else:
                print_list_usage()
        elif arguments[0] == "use":
            if arguments[1] in valid_modules:
                loaded_module = arguments[1]
                module_loaded = True
                drone_inf = DroneInterface(loaded_module)
            else:
                print("Module was not a valid DroneModule")
        elif arguments[0] == "module":
            if arguments[1] == "set":
                drone_inf.set_option(arguments[2], arguments[3])
            elif arguments[1] == "show":
                drone_inf.get_options()
            elif arguments[1] == "help":
                print_module_usage()
            else:
                print_module_usage()
        elif arguments[0] == "run":
            if arguments[1] == "analyze":
                drone_inf.Analyze()
            elif arguments[1] == "exploit":
                drone_inf.Exploit()
            elif arguments[1] == "help":
                print_run_usage()
            else:
                print_run_usage()
        elif arguments[0] == "show":
            print_menu_usage()
        elif arguments[0] == "quit":
            break
        else:
            print_menu_usage()