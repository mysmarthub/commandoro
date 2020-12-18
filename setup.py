#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Copyright © 2020 Aleksandr Suvorov
# Licensed under the terms of the MIT License
# (see LICENSE.txt for details)
# -----------------------------------------------------------------------------
# Email: myhackband@yandex.ru
# Github: https://github.com/mysmarthub/komandoro/
# PyPi: https://pypi.org/project/komandoro/
# -----------------------------------------------------------------------------
from setuptools import setup, find_packages
from os.path import join, dirname

PACKAGE = "komandoro"
VERSION = __import__(PACKAGE).__version__
AUTHOR = __import__(PACKAGE).__author__
AUTHOR_EMAIL = "myhackband@yandex.ru"
DESCRIPTION = "Utility for automatic command execution." \
              " Aleksandr Suvorov | https://github.com/mysmarthub/ | Donate: 4276 4417 5763 7686"
NAME = "komandoro"
URL = "https://github.com/mysmarthub/komandoro"
LICENSE = 'MIT'
LONG_DESCRIPTION = open(join(dirname(__file__), 'README.md')).read()
INSTALL_REQUIRES = []
PLATFORM = ['Linux', 'Windows']
CLASSIFIERS = [
    "Development Status :: 5 - Production/Stable",
    "Environment :: Console",
    "Intended Audience :: End Users/Desktop",
    "Intended Audience :: System Administrators",
    "License :: OSI Approved :: MIT License",
    "Natural Language :: English",
    "Operating System :: OS Independent",
    "Operating System :: Microsoft :: Windows",
    "Operating System :: POSIX :: Linux",
    "Programming Language :: Python :: 3 :: Only",
    "Topic :: Scientific/Engineering :: Electronic Design Automation (EDA)",
    "Topic :: Software Development :: Libraries :: Python Modules",
    "Topic :: Utilities"
]
KEYWORDS = [
    'komandoro',
    'automatic command execution',
]
setup(
    name=NAME,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    url=URL,
    description=DESCRIPTION,
    version=VERSION,
    license=LICENSE,
    platforms=PLATFORM,
    packages=find_packages(),
    long_description_content_type='text/markdown',
    long_description=LONG_DESCRIPTION,
    install_requires=INSTALL_REQUIRES,
    include_package_data=True,
    zip_safe=False,
    keywords=KEYWORDS,
    entry_points={
        'console_scripts':
            ['komandoro = komandoro.start:main']
        }
)
