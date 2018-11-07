from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='horasCLI',
    description='Simple CLI program to create a project hour schedule in markdown.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    platforms=['Windows', 'Linux', 'MacOS'],
    version='1.1.2',
    url='https://github.com/djdany01/horasCLI',
    author='Daniel J. Pérez Nieto',
    author_email='djdany.djesus@gmail.com',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Natural Language :: Spanish',
        'Operating System :: Microsoft',
        'Operating System :: MacOS',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Documentation',
        'Topic :: Office/Business :: Scheduling',
        'Topic :: Software Development :: Documentation',
        'Topic :: Terminals',
        'Topic :: Utilities',
        'Topic :: System :: Shells'
    ],
    license='MIT',
    packages=['horasCLI'],
    entry_points={
        'console_scripts': [
            'horasCLI = horasCLI.__main__:main'
        ]
    })
