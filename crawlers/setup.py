#!/usr/bin/env python
# -*- coding:utf-8 -*-

from __future__ import print_function
import os, sys


if sys.version_info[:2] < (2, 7) or (3, 0) <= sys.version_info[:2] < (3, 4):
    raise RuntimeError("Python version 2.7 or >= 3.4 required.")

try:
    from setuptools import setup, find_packages
except ImportError:
    print('# Error: you don\'t have "setuptools" installed!')
    print('# Before install: $ pip install setuptools')
    print('# Or visit https://pypi.org/project/setuptools/')


def rd(filename):
    f = open(filename)
    r = f.read()
    f.close()
    return r

if sys.argv[-1] == "publish":
    os.system("python setup.py sdist upload")
    sys.exit()

setup(name='crawlers',
    version='0.1',
    description=('A tool to monitor the trendings of Reddit'),
    url='https://github.com/dbednarski/desafios/tree/master/crawlers',
    author='Daniel Bednarski',
    author_email='daniel.bednarski.ramos@gmail.com',
    license='GNU GPLv3.0',      
    packages=['crawlers'],
    scripts=[os.path.join('scripts', f) for f in os.listdir('scripts')],
    long_description=rd('README.md'),
    long_description_content_type="text/markdown",
    install_requires=['numpy', 'requests', 'telegram'],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Others",
        "License :: OSI Approved :: GNU General Public License v3 or later" + \
        " (GPLv3+)",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
    ],
    keywords=['reddit', 'crawlers', 'trending', 'subreddit'],
    zip_safe=True
)
