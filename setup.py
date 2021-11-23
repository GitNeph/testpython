#!/usr/bin/env python
import re

from setuptools import setup, find_packages

__version__ = ''
with open('testpython/__init__.py', 'r') as fd:
    reg = re.compile(r'__version__ = [\'"]([^\'"]*)[\'"]')
    for line in fd:
        m = reg.match(line)
        if m:
            __version__ = m.group(1)
            break

if not __version__:
    raise RuntimeError('Cannot find version information')

setup(
    name='testpython',
    version=__version__,
    description='Test package for python',
    author='KlutzyBubbles',
    author_email='LTzilantois@gmail.com',
    url='https://github.com/KlutzyBubbles/testpython',
    packages=find_packages(include=['testpython']),
    entry_points={
        'console_scripts': [
          'tp-one=testpython.one:main',
          'tp-two=testpython.two:main',
          'tp-three=testpython.three:main',
          'tp-four=testpython.four:main'
        ]
    }
)
