from setuptools import setup
setup(
    name = 'horas',
    version = '0.1.0',
    packages = ['horas'],
    entry_points = {
        'console_scripts': [
            'horas = horas.__main__:main'
        ]
    })