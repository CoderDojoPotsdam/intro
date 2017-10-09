#!/usr/bin/env python

import os
import sys
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.version_info < (3, 4):
    raise NotImplementedError("Sorry, you need at least Python 3.4 to use intro_offline_server.")

__version__ = "1.0.2"
__author__ = 'Nicco Kunzmann'

HERE = os.path.abspath(os.path.dirname(__file__))
sys.path.insert(0, HERE)  # for package import


def read_file_named(file_name):
    file_path = os.path.join(HERE, file_name)
    with open(file_path) as file:
        return file.read()


def read_requirements_file(file_name):
    content = read_file_named(file_name)
    lines = []
    for line in content.splitlines():
        comment_index = line.find("#")
        if comment_index >= 0:
            line = line[:comment_index]
        line = line.strip()
        if not line:
            continue
        lines.append(line)
    return lines

required_packages = read_requirements_file("requirements.txt")

setup(name='intro_offline_server',
      version=__version__,
      install_requires=required_packages,
      description='Server for intro material.',
      long_description=read_file_named("README.md"),
      author=__author__,
      author_email='nicco' + "kunzmann" + "AT rambler.ru",
      url='https://github.com/CoderDojoPotsdam/intro',
      py_modules=['intro_offline_server'],
      scripts=['intro_offline_server.py'],
      license='AGPL',
      platforms='any',
      classifiers=['Development Status :: 4 - Beta',
                   'Intended Audience :: Developers',
                   'Programming Language :: Python :: 3.4',
                   'Programming Language :: Python :: 3.5',
                   ],
)
