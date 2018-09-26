import os, shutil

# -------------------------------------------
def main():
    """Creates the new wheel, publish it to PYPI and delete output folders"""
    os.system('py setup.py bdist_wheel')
    os.system('twine upload dist/*')

    shutil.rmtree('dist')
    shutil.rmtree('build')
    shutil.rmtree('horasCLI.egg-info')

main()