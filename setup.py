#!/usr/bin/python

from distutils.core import setup

setup(
    name = 'consulrest',
    version = '0.1',
    author = 'Vinicius Coque',
    author_email = 'vcoque@gmail.com',
    packages=['consulrest'],
    install_requires=['requests']
)
