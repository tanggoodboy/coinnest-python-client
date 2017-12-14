# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

setup_requires = []

install_requires = ['requests']

setup(
    name='coinnest-python-client',
    version='0.0.1',
    description='Client for Coinnest API',
    packages=find_packages(),
    include_package_data=True,
    install_requires=install_requires,
    setup_requires=setup_requires,
    author='Leop0ld',
    author_email='iam@leop0ld.org',
    url='https://github.com/Leop0ld/coinnest-python-client.git',
    long_description=open('README.md').read(),
    license='MIT',
)
