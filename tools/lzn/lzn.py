#!/usr/bin/python

import sys, os
sys.path.insert(0, "{}/../../common".format(os.path.dirname(os.path.realpath(__file__))))
from py_lib import lzn

if __name__ == "__main__":
    lzn.main()
