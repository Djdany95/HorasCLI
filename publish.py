import os

# -------------------------------------------
def main():
    """Creates the new wheel and publish it to PYPI"""
    os.system('py setup.py bdist_wheel')
    os.system('twine upload dist/*')

main()