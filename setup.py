#! /usr/bin/env python
from setuptools import find_packages, setup


setup(
    name='ot-api',
    version='0.1',
    author='Tomasz Roszko',
    author_email='tom@opentopic',
    description='Rest API Client for Opentopic service',
    long_description=open('README.rst').read(),
    url='https://github.com/Opentopic/ot-api',
    license='GNU GENERAL PUBLIC LICENSE',
    platforms=['OS Independent'],
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.x',
    ],
    install_requires=[
        'booby==0.4.0',
    ],
)