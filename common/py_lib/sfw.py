#!/usr/bin/python
# -*- coding: utf-8 -*-

# Super Famicom Wars specific code generation functions

import codegen as cg, util

#-----------------------------------------------------------------------------
#

# generate pointer replacement section (2x lda/sta statement)
# d = { "at": callsite, "ptr": pointer_location, "obj": object_pointed_to }
def inject_setpointer(d):
  cg.section_start(d["at"], "inject_setpointer")
  if "obj" in d:
    print "  lda.w #:{}<<8"       .format(d["obj"])
    print "  sta.b ${:02x}"       .format(d["ptr"] + 1)
    print "  lda.w #{}"           .format(d["obj"])
    print "  sta.b ${:02x}"       .format(d["ptr"])
  elif "addr" in d:
    print "  lda.w #${:04x}"      .format((d["addr"] >> 8) & 0xff00)
    print "  sta.b ${:02x}"       .format(d["ptr"] + 1)
    print "  lda.w #${:04x}"      .format(d["addr"] & 0xffff)
    print "  sta.b ${:02x}"       .format(d["ptr"])
  cg.section_end()

# generate pointer replacement sections (2x lda/sta statement)
def inject_setpointers(arr):
  for d in arr:
    inject_setpointer(d)
  print("")


#-----------------------------------------------------------------------------
# Graphics / UX struct stuff

# boxdef/boxim struct manipulation
def boxdim_set_width(struct_ptr, width):
  cg.insert(at=struct_ptr, name="boxdim_set_width", d={"b":width})

def boxdim_set_height(struct_ptr, height):
  cg.insert(at=struct_ptr+1, name="boxdim_set_height", d={"b":height})


# create OAM table
def oam_table(entries):
  data = cg.db_word(len(entries))
  for e in entries:
    data += "\n\n" + cg.db_word(e[0])
    data += "\n" + cg.db_byte(e[1])
    data += "\n" + cg.db_word(e[2])
  return data

# create OAM table entry
def oam_entry(xc, yc, tile, palette=0, size=0, prio=0, hf=0, vf=0):
  entry = []
  entry.append(((xc & 0xfff) + ((size & 0x1) << 15)) & 0xffff)
  entry.append(yc & 0xff)
  entry.append(((tile & 0x1ff) + ((palette & 0x7) << 9) + ((prio & 0x3) << 12) + ((hf & 0x1) << 14) + ((vf & 0x1) << 15)  ) & 0xffff)
  return entry


# create icon list
# 0  W  icon id
# 2  B  x-pos
# 3  B  y-pos
def icon_list(name, bank, list):
  cg.free_section_start(bank, name)
  print "{}:".format(name)
  for b in list:
    print cg.db_byte(b)
  print cg.db_word(0xffff)
  cg.section_end()


#-----------------------------------------------------------------------------
# String transformation

# tokenize string
def tokenize_string(s):
  t = []
  lc = None
  for c in unicode(s, "utf-8"):
    if isinstance(lc, list):
      # Handle special token handle parameters
      #print t[-1]
      if lc[0] == 0x23ee:
        # [0x23ee] = ⏮n   Negative kerning
        t[-1] = 0xfa
        t.append(util.clamp(int(c), 0, 7))
        lc = None

      elif lc[0] == 0x23eb:
        # [0x23eb] = ⏫nn  Set VWF buffer offset
        # high nybble
        t[-1] = 0xfb
        t.append(int("0x{}".format(c), 16))
        lc = [0x23ec]

      elif lc[0] == 0x23ec:
        # ⏫nn low nybble
        t[-1] = (t[-1] << 4) + int("0x{}".format(c), 16)
        lc = None

      elif lc[0] == 0x23fa:
        # [0x23fa] = ⏺nn  Extended character
        # high nybble
        t[-1] = 0x7f
        t.append(int("0x{}".format(c), 16))
        lc = [0x23fb]

      elif lc[0] == 0x23fb:
        # ⏫nn low nybble
        t[-1] = (t[-1] << 4) + int("0x{}".format(c), 16)
        lc = None

      else:
        t[-1] = "$"
        lc = None

    else:
      if ord(c) >= 0x20 and ord(c) <= 0x7e:
        # ascii range: replace '_', leave other as is
        if ord(c) == 0x5f:
          # underscore = short tab ($FD)
          t.append(0xfd)
        else:
          t.append(ord(c))
      else:
        # non-ascii, append special token
        t.append([(ord(c))])
      lc = t[-1]

  return t


# generate string replacement section
# (this house of cards have been ripe for a rebuild since the second feature was added, but hey!)
# d = { "name": label, "at": address, "str": string, "len": length }
def inject_string(d):
  terminator = None

  str_loc = d["at"]
  new_str = d["str"]
  token_str = tokenize_string(new_str)
  org_len = d["len"]
  new_len = len(token_str)

  print "; org_len={}, new_len={}, new_str=\"{}\"".format(org_len, new_len, new_str)
  print "; tokenized={}".format(token_str)

  if "trlf" in d:
    terminator = [ 0x0000, 0xffff ]
  elif "tr" in d:
    terminator = [ 0x0000, 0x0000 ]
  if terminator is not None:
    cg.insert(at=str_loc + org_len, d={"w": terminator})

  if new_len == org_len:
    cg.insert(at=str_loc, name="inject_string", d=cg.db_string(token_str))

  elif new_len < org_len:
    if org_len - new_len > 0x1f:
      diff = org_len - new_len - 0x1f
      new_len += diff
      token_str.extend([0xfe] * diff)
    cg.insert(at=str_loc, name="inject_short_string", d='\n'.join([cg.db_string(token_str), cg.db_byte(org_len - new_len)]))

  else:
    cont_label = "longstr_cont_{:06x}".format(str_loc)
    print "; long_str_org_len={}, token_str_len={}".format(org_len, len(token_str))
    base_str = ""
    if org_len - 4 > 0 and (len(token_str) > org_len - 6):
      # special token on boundary? (except if argument...)
      if token_str[org_len-5] >= 0x7e and token_str[org_len-6] != 0xfb:
        base_str = cg.db_string(token_str[0:org_len-5] + [0xfe])
      else:
        base_str = cg.db_string(token_str[0:org_len-4])
    cg.insert(at=str_loc, name="inject_long_string", d='\n'.join([base_str, cg.db_byte(0xfc), cg.db_label_long(cont_label)]))

    cont_data = []
    if token_str[org_len-5] >= 0x7e and token_str[org_len-6] != 0xfb:
      cont_data = util.str_to_arr(token_str[max(org_len-5,0):])
    else:
      cont_data = util.str_to_arr(token_str[max(org_len-4,0):])
    cont_data.append(0)
    cg.insert(name="longstr_cont {:06x}".format(str_loc), label=cont_label, d={"b":cont_data})



# generate string replacement sections
def inject_strings(arr):
  for d in arr:
    inject_string(d)
  print("")
