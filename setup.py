
import os
import sys
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand

# Establish a consistent base directory relative to the setup.py file
os.chdir(os.path.abspath(os.path.dirname(__file__)))

setup(
    name='classcafe',
    version='0.0.1',
    description='',
    long_description='',
    author='CafeHub',
    author_email='cloud-cafe@lists.rackspace.com',
    url='http://opencafe.readthedocs.org',
    install_requires=[],
    packages=find_packages(),
    license="",
    classifiers=(
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: Other/Proprietary License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7'))