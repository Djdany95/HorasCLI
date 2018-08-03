from setuptools import setup
setup(
    name = 'horas',
    version = '0.3.0',
    packages = ['horas'],
    scripts = ['horas/utils.py'],
    entry_points = {
        'console_scripts': [
            'horas = horas.__main__:main'
        ]
    })