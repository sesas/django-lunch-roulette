#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    :copyright: Copyright 2014 by Gabriel Reyla
    :contact: gabreyla@gmail.com
"""


from setuptools import setup
from os.path import join, dirname

LONG_DESCRIPION = """
Lunch roulette app for django. Have more fun at lunch!
"""

def long_description():
    """Return long description from README.rst if it's present
    because it doesn't get installed."""
    try:
        return open(join(dirname(__file__), 'README.md')).read()
    except IOError:
        return LONG_DESCRIPTION

setup(
    name='django-lunch-roulette',
    version='0.1.0',
    description='Django-powered Lunch Roulette',
    long_description=long_description(),
    author='Gabriel Reyla, Henry Zhu, Jessica S',
    author_email='gabreyla@gmail.com',
    packages = ['lunch_roulette'],
    install_requires=['Django', 'djangorestframework', 'django-crispy-forms'],
    classifiers=[
        'Intended Audience :: Lunch Eaters :: Organizations :: Employees :: Fun :: Social Eating',
        'Programming Language :: Python',
        'Topic :: Eating :: Social :: Libraries :: Python Modules',
        'Framework :: Django',
        'License :: OSI Approved :: MIT License',
        'Development Status :: 3 - Alpha',
    ],
    platforms=['any'],
)
