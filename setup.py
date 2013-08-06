from distutils.core import setup
import re
import os
import sys

def get_packages(package):
    """
    Return root package and all sub-packages.
    """
    return [dirpath
            for dirpath, dirnames, filenames in os.walk(package)
            if os.path.exists(os.path.join(dirpath, '__init__.py'))]

setup(name='mongo-migrate',
        version='0.1.0',
        description='a python tool for mongo migation',
        author='Arthur',
        author_email='largetalk@gmail.com',
        url='',
        packages=get_packages('mongo_migrate'),
        scripts=['mongo_migrate/bin/mongration.py'],
        install_requires=[],
        )
