#!/usr/bin/python
# -*- coding: utf-8 -*-

import re
from _lib_ import cg, sfw, kerning
from _data_ import strings

#-----------------------------------------------------------------------------
# Compile strings

def kern_string(s):
  # Sneak in some glyph replacements here
  s = s.replace("  ", ">")
  s = s.replace("fi", "`")
  s = s.replace("fl", "^")
  kern = {}
  for p, n in kerning.pairs:
    for m in re.finditer(p, s):
      kern[m.start()] = n
  ks = ""
  for i, c in enumerate(s):
    if i in kern:
      ks += "⏮{}{}".format(kern[i], c)
    else:
      ks += c
  return ks

def compile_strings(d):
  for addr in d:
    entry = d[addr]
    if "en" in entry:
      if isinstance(entry["en"], list):
        new_len = None
        if "len" in entry:
          new_len = entry["len"]
          org_len = entry["org_len"]
          if org_len < new_len: org_len = new_len
        print "; multiline string at 0x{:06x}".format(addr)
        for i, s in enumerate(entry["en"]):
          str = {}
          if new_len is not None:
            if i == 0:
              line_addr = addr
              str["len"] = new_len
              token_len = len(sfw.tokenize_string(kern_string(s))) + 1
              pad_len = org_len - token_len
              if pad_len > 0:
                cg.insert(at=addr + org_len - pad_len, d={"b":[0xfe] * pad_len})
            else:
              line_addr = addr + new_len - 4 + i * 8
              str["len"] = 4
          else:
            line_addr = addr + i * 8
            str["len"] = 4
          str["name"] = "string 0x{:06x}".format(line_addr)
          str["at"] = line_addr
          str["str"] = kern_string(s)
          if i < len(entry["en"]) - 1:
            str["trlf"] = True
          else:
            str["tr"] = True
          sfw.inject_string(str)

      else:
        str = {}
        str["name"] = "string 0x{:06x}".format(addr)
        str["at"] = entry["b"]
        str["len"] = entry["l"]
        str["str"] = kern_string(entry["en"])
        if "trlf" in entry and entry["trlf"] is True:
          str["trlf"] = True
        elif "tr" in entry and entry["tr"] is True:
          str["tr"] = True
        sfw.inject_string(str)

for d in strings:
  compile_strings(d)

print("")

#-----------------------------------------------------------------------------
# Patches

# Relocate Help Page B14
cg.insert(at=0x919d16, d={"w":0xAC50})

print("")
