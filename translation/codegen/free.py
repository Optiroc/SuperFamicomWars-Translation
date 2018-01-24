#!/usr/bin/python
# -*- coding: utf-8 -*-

from _lib_ import cg

# Bank padding
cg.mark_ranges_free([
  {"start": 0x80c200, "end": 0x80efff},
  {"start": 0x818b00, "end": 0x81a7ff},
  {"start": 0x81fa00, "end": 0x81ffff},
  {"start": 0x828600, "end": 0x82bfff},
  {"start": 0x82c600, "end": 0x82dfff},
  {"start": 0x82f400, "end": 0x82ffff},
  {"start": 0x83f800, "end": 0x83ffff},
  {"start": 0x85f800, "end": 0x85ffff},
  {"start": 0x86c100, "end": 0x86ffff},
  {"start": 0x87fd70, "end": 0x87ffff},
  {"start": 0x89f400, "end": 0x89ffff},
  {"start": 0x8afb10, "end": 0x8affff},
  {"start": 0x8bf600, "end": 0x8bffff},
  {"start": 0x8cf400, "end": 0x8cffff},
  {"start": 0x8ef600, "end": 0x8effff},
  {"start": 0x8de200, "end": 0x8dffff},
  {"start": 0x8fd200, "end": 0x8fffff},
  {"start": 0x90fa00, "end": 0x90ffff},
  {"start": 0x91f600, "end": 0x91ffff},
  {"start": 0x93f000, "end": 0x93ffff},
  {"start": 0x94f000, "end": 0x94ffff},
  {"start": 0x9ad000, "end": 0x9affff},
  {"start": 0x9bd400, "end": 0x9bffff},
  {"start": 0x9e9800, "end": 0x9effff},
  {"start": 0xabaa00, "end": 0xabffff},
  {"start": 0xb69200, "end": 0xb6ffff}
])

# Relocated assets, etc
#
# Something went awry when freeing up these, so I decided not to
# bother until free space is actually a concern (which won't happen).

#cg.mark_ranges_free([
#  # boot_logo
#  {"start": 0x98DE57, "length": 0x02DA},
#  # title_sprites
#  {"start": 0x9DE1BB, "length": 0x02CF},
#  {"start": 0x9DE48A, "length": 0x01FF},
#  # S-JIS look-up-table
#  # S-JIS dictionary
#  {"start": 0x87A92B, "length": 0x047D}
#])
