from collections import defaultdict

from ..DroneModuleFrame import DroneModuleFrame

import subprocess

URL_PATTERN = 'https\\?://[a-zA-Z0-9./?&%=_-]\\+'

class DroneModule(DroneModuleFrame):

    def __init__(self):
        name = "URL_Extract"
        options = {
            'root_path': {'value': '/path/to/firmware.extracted', 'description': 'Path to the extracted firmware root'},
            'output_file': {'value': None, 'description': 'file to which extracted URLs should be written'}
        }
        DroneModuleFrame.__init__(self, name, options)

    def Analyze(self):
        grep = subprocess.Popen(['grep', '-aRo', '--null', URL_PATTERN, self.options['root_path']['value']], stdout=subprocess.PIPE)
        output = grep.communicate()[0]
        matches = defaultdict(set)
        last_path = None
        for match in output.decode('utf-8').splitlines():
            split = match.split('\0', 1)
            if len(split) == 1:
                url = split[0]
                path = last_path
            else:
                path, url = split
            if path is None:
                path = '__'
            matches[path].add(url)

        if self.options['output_file']['value'] is None:
            for path, urls in sorted(matches.items()):
                print(path.replace(self.options['root_path']['value'], ''))
                for url in sorted(urls):
                    print('    ' + url)
        else:
            with open(self.options['output_file']['value'], 'w') as f:
                for path, urls in sorted(matches.items()):
                    f.write(path.replace(self.options['root_path']['value'], '') + '\n')
                    for url in sorted(urls):
                        f.write('    ' + url + '\n')
