from App import interface
import sys

i = interface.DroneInterface("example")
i.Exploit()
i.Analyze()
i.get_options()
i.set_option('example', 'new value')
i.get_options()
