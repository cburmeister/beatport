#!/usr/bin/env python

from setuptools import setup

setup(
        name='beatport',
        version='0.0.1',
        description='Unofficial Python API client for Beatport.com',
        url='https://github.com/cburmeister/beatport',
        author='cburmeister',
        author_email='burmeister.corey@gmail.com',
        install_requires=[
            'requests',
            ],
        py_modules=[
            'beatport'
            ],
        )
