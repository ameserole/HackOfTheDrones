from consolemenu import *
from consolemenu.items import *
import sys

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

def start_menu():
    # Create the menu
    menu = ConsoleMenu("HackDrones", "Modules")

    # Create some items

    # MenuItem is the base class for all items, it doesn't do anything when selected
    # A FunctionItem runs a Python function when selected
    # A CommandItem runs a console command
    # A SelectionMenu constructs a menu from a list of strings
    funct1 = FunctionItem("Firmware Extraction", mod_1, args=["test"])
    funct2 = FunctionItem("Wifi Default Cred Exploiter", mod_2, args=["test"])
    funct3 = FunctionItem("Password Extractor", mod_3, args=["test"])
    funct4 = FunctionItem("URL Extractor", mod_4, args=["test"])    
    funct5 = FunctionItem("Firmware Modificaiton and Repackage", mod_5, args=["test"])

    # A SubmenuItem lets you add a menu (the selection_menu above, for example)
    # as a submenu of another menu
    #submenu_item = SubmenuItem("Submenu item", selection_menu, menu)

    # Once we're done creating them, we just add the items to the menu
    menu.append_item(funct1)
    menu.append_item(funct2)
    menu.append_item(funct3)
    menu.append_item(funct4)
    menu.append_item(funct5)

    # Finally, we call show to show the menu and allow the user to interact
    menu.show()