# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='asgs-msgr',
    version='0.1.0',
    description='Sends amqp messages for asgs process',
    long_description=readme,
    author='Brian Blanton',
    author_email='bblanton@renci.org',
    url='https://github.com/lstillwe/asgs-msgr',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
