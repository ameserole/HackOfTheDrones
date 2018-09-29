from setuptools import setup
setup(
    name = 'hackdrones',
    version = '1.33.7',
    packages = ['App'],
    entry_points = {
        'console_scripts': [
            'hackdrones = App.hackdrones:main'
        ]
})