"""setup.py: setuptools control."""
import re
from os import path
from setuptools import setup


# -*- coding: utf-8 -*-


# Get the actual path
HERE = path.abspath(path.dirname(__file__))


# Get version from main script
VERSION = re.search(
    r'^__version__\s*=\s*"(.*)"',
    open('reporter/reporter.py').read(), flags=re.M).group(1)


# Get the long description from the README file
try:
    import pypandoc
    LONG_DESCRIPTION = pypandoc.convert('README.md', 'rst')
except (IOError, ImportError):
    LONG_DESCRIPTION = open('README.md').read()


setup(
    name='cmdline-reporter',

    version=VERSION,

    description='Python command line application to extract .',
    long_description=LONG_DESCRIPTION,

    url="https://github.com/pablovilchis",

    author="Juan Pablo Vilchis",
    author_email="pablo.vilchis@gmail.com",

    # Choose your license
    license='MIT',

    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.

        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],

    packages=['reporter'],
    # List run-time dependencies here.  These will be installed by pip when
    # your project is installed. For an analysis of "install_requires" vs pip's
    # requirements files see:
    # https://packaging.python.org/en/latest/requirements.html
    install_requires=['pypandoc', 'mypy', 'googlemaps', 'tabulate'],
    entry_points={
        "console_scripts": ['reporter = reporter.reporter:main']
    },

)
