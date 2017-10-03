#!/usr/bin/env python

import sys
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.version_info < (3, 4):
    raise NotImplementedError("Sorry, you need at least Python 3.4 to use intro_offline_server.")

__version__ = "1.0.0"

setup(name='intro_offline_server',
      version=intro_offline_server.__version__,
      description='Server for intro material.',
      long_description=bottle.__doc__,
      author=bottle.__author__,
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
