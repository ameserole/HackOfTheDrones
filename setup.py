from setuptools import setup
setup(
    name = 'hackdrones',
    version = '1.33.7',
    packages = ['src'],
    entry_points = {
        'console_scripts': [
            'hackdrones = src.hackdrones:main'
        ]
})