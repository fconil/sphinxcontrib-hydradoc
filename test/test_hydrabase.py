# -*- coding: utf-8 -*-
"""
This modules contains the units tests for the sphinxcontrib.hydradoc -module.
"""
import doctest
import os
import sys

from sphinxcontrib import hydradoc
from sphinxcontrib.hydradoc import toindex, toname


def test():
    """
    Run the tests of the module
    """
    sys.path = [os.path.join(os.path.dirname(__file__), '..')] + sys.path

    doctests()
    unittests()


def doctests():
    """
    Run doc tests
    """
    doctest.testmod()


def unittests():
    """
    Minimal verification of the module: run some
    unittests against the module
    """
    path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../doc/example/vocab.json-ld'))
    document = hydradoc.hydradoc(open(path, 'r+b'))

  
