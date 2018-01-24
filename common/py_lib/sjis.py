#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

SHIFTJIS_TXT = "{}/sjis_data/SHIFTJIS.TXT".format(os.path.dirname(os.path.realpath(__file__)))

sjis_dict = {}
for line in open(SHIFTJIS_TXT):
  try:
    s = line.split("\t")
    if len(s) == 3:
      sjis_dict[int(s[0], 16)] = unichr(int(s[1], 16)).encode("utf-8")
  except Exception as e:
    continue

def to_utf8(codepoint):
  if codepoint in sjis_dict:
    return sjis_dict[codepoint]
  else:
    return None
