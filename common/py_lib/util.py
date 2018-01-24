#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

# check if file exists
def is_valid_file(parser, arg):
  if not os.path.exists(arg):
    parser.error("The file %s does not exist!" % arg)
  else:
    return arg

# chunk iterator
def iter_chunk(seq, size):
    return (seq[pos:pos + size] for pos in xrange(0, len(seq), size))

# clamp number
def clamp(n, smallest, largest):
  return max(smallest, min(n, largest))

# byte-array from string
def str_to_arr(s):
  arr = []
  if len(s) < 1:
    return arr
  for c in s:
    if isinstance(c, list):
      # Skip multi-byte codepoints
      pass
    else:
      arr.append(int(c))
  return arr
