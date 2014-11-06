#!/usr/bin/python

from distutils.core import setup

setup(
    name = 'consulri',
    version = '0.1',
    author = 'Vinicius Coque',
    author_email = 'vcoque@gmail.com',
    packages=['consulri'],
    install_requires=['requests']
)
