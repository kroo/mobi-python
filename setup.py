#!/usr/bin/env python

import os
from setuptools import setup, find_packages


setup(
    name = 'mobi-python',
    version = "0.1",
    description = 'A library for reading (unencrypted) mobi-reader files in Python.',
    url = 'https://github.com/kroo/mobi-python',
    classifiers = [
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries',
        ],
    packages = ['mobi']
)
            
