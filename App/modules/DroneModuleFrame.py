
class DroneModuleFrame(object):
    def __init__(self, name, options):
        self.name = name
        self.info = "Help"
        self.options = options

    def get_options(self):
        print('-'*60)
        print('| Name | Value | Description |')
        for key, value in self.options.items():
            print('| {} | {} | {} |'.format(key, value['value'], value['description']))
        print('-'*60)

    def set_option(self, name, value):
        self.options[name]['value'] = value

    def Analyze(self):
        raise NotImplementedError()

    def Exploit(self):
        raise NotImplementedError()
