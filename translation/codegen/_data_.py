#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys, os, importlib
sys.path.insert(0, "{}/../data".format(os.path.dirname(os.path.realpath(__file__))))

strings = [
  importlib.import_module("strings.game").strings,
  importlib.import_module("strings.options").strings,
  importlib.import_module("strings.maps").strings,
  importlib.import_module("strings.units").strings,
  importlib.import_module("strings.terrain").strings,
  importlib.import_module("strings.help").strings,
  importlib.import_module("strings.soundpark").strings
]
