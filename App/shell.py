import sys, os
from termcolor import colored
sys.path.insert(0, '.')
from interface import DroneInterface

# List Modules
# List Drone Available Wifi
# use <module>
# run ||  in module setting

import os
import re
import readline
from getch import getch

COMMANDS = ['use', 'run', 'list', 'help', 'quit']
RE_SPACE = re.compile('.*\s+$', re.M)

# https://stackoverflow.com/questions/5637124/tab-completion-in-pythons-raw-input
class Completer(object):

    def _listdir(self, root):
        "List directory 'root' appending the path separator to subdirs."
        res = []
        for name in os.listdir(root):
            path = os.path.join(root, name)
            if os.path.isdir(path):
                name += os.sep
            res.append(name)
        return res

    def _complete_path(self, path=None):
        "Perform completion of filesystem path."
        if not path:
            return self._listdir('.')
        dirname, rest = os.path.split(path)
        tmp = dirname if dirname else '.'
        res = [os.path.join(dirname, p)
                for p in self._listdir(tmp) if p.startswith(rest)]
        # more than one match, or single match which does not exist (typo)
        if len(res) > 1 or not os.path.exists(path):
            return res
        # resolved to a single directory, so return list of files below it
        if os.path.isdir(path):
            return [os.path.join(path, p) for p in self._listdir(path)]
        # exact file match terminates this completion
        return [path + ' ']

    def complete_extra(self, args):
        "Completions for the 'extra' command."
        if not args:
            return self._complete_path('.')
        # treat the last arg as a path and complete it
        return self._complete_path(args[-1])

    def complete(self, text, state):
        "Generic readline completion entry point."
        buffer = readline.get_line_buffer()
        line = readline.get_line_buffer().split()
        # show all commands
        if not line:
            return [c + ' ' for c in COMMANDS][state]
        # account for last argument ending in a space
        if RE_SPACE.match(buffer):
            line.append('')
        # resolve command to the implementation function
        cmd = line[0].strip()
        if cmd in COMMANDS:
            impl = getattr(self, 'complete_%s' % cmd)
            args = line[1:]
            if args:
                return (impl(args) + [None])[state]
            return [cmd + ' '][state]
        results = [c + ' ' for c in COMMANDS if c.startswith(cmd)] + [None]
        return results[state]

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
    getch()

def list_wifi(wifi_intrfce):
    """ Detect network card/list interfaces and disconnect if needed """
    yn = subprocess.Popen(['sudo','nmcli','c'],stdout=subprocess.PIPE)
    ynout = yn.stdout.read().decode('utf-8')
    if wifi_intrfce in ynout:
        subprocess.run(['sudo','nmcli','d','disconnect', wifi_intrfce])


    # list all interfaces and choose which you want
    subprocess.run(['sudo', 'nmcli', 'd', 'wifi', 'rescan'])
    netlist = subprocess.Popen(['sudo', 'nmcli', 'd', 'wifi'], stdout=subprocess.PIPE)
    output = netlist.stdout.read().decode('utf-8')
    print(output)

def wifi_connnect(ssid, password):
    """ Connect to drone using creds you found"""
    subprocess.run(['sudo','nmcli','d','wifi','connect',ssid,'password',password,'ifname',netiface])

    print("Success.")

def print_wifi_usage():
    print("Available Commands:")
    print("\t\tlist <interface> - List available wifi on <interface>")
    print("\t\tconnect <ssid> <password> - Connects to <ssid> using <password>")
    print("\t\thelp - Displays this menu help")

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
    print("\t\set - Access and Manipulate loaded module")
    print("\t\tshow - Displays fields of loaded module")
    print("\t\trun - Execute module behavior of argument")
    

def start_menu():
    module_loaded = False
    loaded_module = ""
    drone_inf = ""
    valid_modules = check_modules()
    comp = Completer()
    # we want to treat '/' as part of a worlist_wifi delimiters
    readline.set_completer_delims(' \t\n;')
    readline.parse_and_bind("tab: complete")
    readline.set_completer(comp.complete)
    while True:
        try:
            module_prompt = " exploit(%s)"%(colored(loaded_module, 'red'))
            cmd = input("hackdrones%s>>>"%(module_prompt if module_loaded else ""))
            arguments = cmd.split(" ")
            if arguments[0] == "list":
                list_modules()
            elif arguments[0] == "wifi":
                if len(arguments) ==  2 and arguments[1] == "help":
                    print_wifi_usage()
                elif len(arguments) ==  3 and arguments[1] == "list":
                    list_wifi(arguments[2])
                elif len(arguments) ==  4 and arguments[1] == "connect":
                    wifi_connnect(arguments[2], arguments[3])
                else:
                    print_wifi_usage()
            elif arguments[0] == "use":
                if arguments[1] in valid_modules:
                    loaded_module = arguments[1]
                    module_loaded = True
                    drone_inf = DroneInterface(loaded_module)
                    COMMANDS.append("set")
                    COMMANDS.append("show")
                else:
                    print("Module was not a valid DroneModule")
            elif loaded_module and arguments[0] == "set":
                drone_inf.set_option(arguments[1], arguments[2])
            elif arguments[0] == "show":
                drone_inf.get_options()
            elif arguments[0] == "run":
                if arguments[1] == "analyze":
                    drone_inf.Analyze()
                elif arguments[1] == "exploit":
                    drone_inf.Exploit()
                elif arguments[1] == "help":
                    print_run_usage()
                else:
                    print_run_usage()
            elif arguments[0] == "help":
                print_menu_usage()
            elif arguments[0] == "quit":
                break
            else:
                print_menu_usage()
        
        except KeyboardInterrupt:
            print("")
            if module_loaded == True:
                loaded_module = ""
                module_loaded = False
                drone_inf = ""
                COMMANDS.remove("set")
                COMMANDS.remove("show")
        except:
            print("Invalid Command.")
    
