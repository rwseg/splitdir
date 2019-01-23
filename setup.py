# -*- coding: utf-8 -*-
from setuptools import setup
from os import path
# io.open is needed for projects that support Python 2.7
# It ensures open() defaults to text mode with universal newlines,
# and accepts an argument to specify the text encoding
# Python 3 only projects can skip this import
from io import open

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


setup(
    name='splitdir',  # Required
    version='1.0.0',  # Required
    description='split your directory to given number of sub directories',  # Optional
    long_description=long_description,  # Optional
    long_description_content_type='text/markdown',  # Optional (see note above)
    url='https://github.com/rwseg/splitdir',  # Optional
    author='rwseg',  # Optional
    author_email='rwsieng@gmail.com',  # Optional
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    keywords='split large directory sub directories',  # Optional
    py_modules=['splitdir'],
    entry_points={  # Optional
        'console_scripts': [
            'splitdir=splitdir:split',
        ],
    },
)