from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='joelRFMPackage',
description='Calculate RFM Scores',
version='1.0',
py_modules=['calculateRFMscores'],
install_requires=['pandas','numpy'],
author='not me',
packages=['joelRFMPackage'])
