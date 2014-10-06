#!/usr/bin/python

from distutils.core import setup

setup(
    name = 'consular-agent',
    version = '0.1',
    author = 'Vinicius Coque',
    author_email = 'vcoque@gmail.com',
    packages=['consularagent'],
    install_requires=['requests']
)
