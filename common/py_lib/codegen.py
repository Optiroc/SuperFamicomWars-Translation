#!/usr/bin/python
# -*- coding: utf-8 -*-

# Code generation functions for WLA-DX ROM manipulation

#-----------------------------------------------------------------------------
# Main code/data insertion

def insert(at=None, bank=None, name=None, label=None, d=None, arr=None):
  if isinstance(arr, list):
    for e in arr: insert(**e)
    return

  if d is None:
    raise TypeError("codegen.insert(): No data")
  data = None
  if isinstance(d, dict):
    data = format_data(d)
  else:
    data = d

  if at is not None:
    if name is None: name = "insert_overwrite"
    section_start(at, name)
    insert_label(label)
    print data
    section_end()

  elif bank is not None and (name is not None or label is not None):
    if name is None: name = label
    if label is None: label = name
    free_section_start(bank, name)
    insert_label(label)
    print data
    section_end()

  elif name is not None or label is not None:
    if name is None: name = label
    if label is None: label = name
    superfree_section_start(name)
    insert_label(label)
    print data
    section_end()

  else:
    raise TypeError("codegen.insert(): invalid parameter(s)")


def insert_label(label):
  if label is not None:
    print "{}:".format(label)


#-----------------------------------------------------------------------------
# WLA style data formatters

def format_data(d):
  if "b" in d:
    if isinstance(d["b"], list):
      return db_bytes(d["b"])
    else:
      return db_byte(d["b"])
  elif "w" in d:
    if isinstance(d["w"], list):
      return '\n'.join(map(lambda v: db_word(v), d["w"]))
    else:
      return db_word(d["w"])
  elif "l" in d:
    if isinstance(d["l"], list):
      return '\n'.join(map(lambda v: db_long(v), d["l"]))
    else:
      return db_long(d["l"])
  elif "label" in d:
    if isinstance(d["label"], list):
      return '\n'.join(map(lambda v: db_label_long(v), d["label"]))
    else:
      return db_label_long(d["label"])
  elif "label_word" in d:
    if isinstance(d["label_word"], list):
      return '\n'.join(map(lambda v: db_label_word(v), d["label_word"]))
    else:
      return db_label_word(d["label_word"])
  elif "asm" in d:
    return d["asm"]
  elif "text" in d:
    return d["text"]
  else:
    raise TypeError("db() called without valid parameter")

# return .DB statement from byte
def db_byte(b):
  return "  .DB ${:02x}".format(b)

# return .DB statement from bytes
def db_bytes(bs):
  if len(bs) < 1:
    return ""
  dbstr = "  .DB "
  for b in bs:
    dbstr += "${:02x},".format(b)
  if dbstr.endswith(','):
    dbstr = dbstr[:-1]
  return dbstr

# return .DB statement from word
def db_word(w):
  return "  .DW ${:04x}".format(w)

# return .DB statement from long
def db_long(l):
  return "  .DB ${:02x},${:02x},${:02x}".format(l & 0xff, (l >> 8) & 0xff, (l >> 16) & 0xff)

# return .DB statement from label (long)
def db_label_long(label):
  return "  .DB <{}, >{}, :{}".format(label, label, label)

# return .DB statement from label (word)
def db_label_word(label):
  return "  .DB <{}, >{}".format(label, label)

# return .DB statement string
def db_string(s):
  if len(s) < 1:
    return ""
  dbstr = "  .DB "
  for c in s:
    if isinstance(c, list):
      # Skip multi-byte codepoints
      pass
    else:
      dbstr += "${:02x},".format(int(c))
  if dbstr.endswith(','):
    dbstr = dbstr[:-1]
  return dbstr

# return .incbin statement string
def incbin(file, max_size=None):
  #if max_size is not None:
  #  TODO!
  return "  .incbin \"{}\"".format(file)


#-----------------------------------------------------------------------------
# Section start/end

# generate overwrite section at addr
def section_start(addr, name):
  print ".BANK ${:02x} SLOT ROMSLOT"        .format((addr >> 16) & 0x7f)
  print ".BASE ${:02x}"                     .format((addr >> 16) & 0x80)
  print ".ORGA ${:04x}"                     .format(addr & 0xffff)
  print ".SECTION \"{} {:04x}\" OVERWRITE"  .format(name, addr)

# generate free section
def free_section_start(bank, name):
  print ".BANK ${:02x} SLOT ROMSLOT"        .format(bank & 0x7f)
  print ".BASE ${:02x}"                     .format(bank & 0x80)
  print ".SECTION \"free_section {}\" FREE" .format(name)

# generate superfree section
def superfree_section_start(name):
  print ".SECTION \"superfree_section {}\" SUPERFREE" .format(name)

# end section
def section_end():
  print ".ENDS"
  print("")


#-----------------------------------------------------------------------------
# Misc

# generate unbackground statement
# d = { "start": address, "end": address }
# d = { "start": address, "length": length }
def mark_range_free(d):
  if "end" in d or "length" in d:
    start = d["start"]
    if "length" in d:
      length = d["length"]
    else:
      length = d["end"] - start
    bank = (start >> 16) & 0x7f
    offset = (bank * 0x8000) + (start & 0x7fff)
    print ";${:04x} bytes at ${:06x}-{:04x} -> .BANK ${:02x} SLOT ROMSLOT".format(length + 1, start, (start + length) & 0xffff, bank & 0x7f)
    print ".UNBACKGROUND ${:06x} ${:06x}".format(offset, offset + length)
    print("")
  else:
    raise TypeError("free_section needs 'end' or 'length' key")

# generate unbackground statements
def mark_ranges_free(arr):
  for d in arr:
    mark_range_free(d)
  print("")

# generate nop slide
def nop_slide(at, length=1):
  section_start(at, "nop_slide")
  for _ in range(length):
    print db_byte(0xEA)
  section_end()
