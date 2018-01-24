#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import os
import struct

sys.path.insert(0, "../../common")
from py_lib import lzn, rom_reader

rom = rom_reader.Rom("../../rom/Super Famicom Wars (Japan) (NP).sfc")
superfamiconv = "../../tools/superfamiconv/bin/superfamiconv"

# TODO
# Investigate viability to scan for valid LZN streams

uncompressed_graphics = [
  { "name":"ui/icons.4bpp.bin",                         "start":0x959900, "length":0x1E00 },
  { "name":"ui/speech_bubbles.4bpp.bin",                "start":0x90F100, "length":0x0400 },
  { "name":"ui/logo_small.4bpp.bin",                    "start":0x90F500, "length":0x0400 },
  { "name":"ui/icon_g.4bpp.bin",                        "start":0x8A945B, "length":0x0080 },
  { "name":"terrain/icons.4bpp.bin",                    "start":0x958000, "length":0x0C00 },
  { "name":"terrain/animated_1.4bpp.bin",               "start":0x928000, "length":0x6000 },
  { "name":"terrain/animated_2.4bpp.bin",               "start":0x938000, "length":0x6000 },
  { "name":"units/animated.4bpp.bin",                   "start":0x948000, "length":0x4800 },
  { "name":"units/more.4bpp.bin",                       "start":0x9B8000, "length":0x1B00 },
  { "name":"misc/explosion_big.4bpp.bin",               "start":0x81BA40, "length":0x0400 },
]

compressed_graphics = [
  { "name":"title/boot_logo.4bpp.bin.lzn",              "start":0x98DE57 },
  { "name":"title/title_logo.4bpp.bin.lzn",             "start":0x9DCBB4 },
  { "name":"title/title_logo.tilemap.bin.lzn",          "start":0x9DE024 },
  { "name":"title/sprites_1.4bpp.bin.lzn",              "start":0x9DE1BB },
  { "name":"title/sprites_2.4bpp.bin.lzn",              "start":0x9DE48A },
  { "name":"ui/font.2bpp.bin.lzn",                      "start":0x95B700 },
  { "name":"ui/icons_menu_extra.4bpp.bin.lzn",          "start":0x98E274 },
  { "name":"ui/icons_stats_extra.4bpp.bin.lzn",         "start":0x96B577 },
  { "name":"ui/day_banner.4bpp.bin.lzn",                "start":0xAE8409 },
  { "name":"ui/day_banner.tilemap.bin.lzn",             "start":0xAE8826 },
  { "name":"ui/menu_bg.4bpp.bin.lzn",                   "start":0x95DD7A },
  { "name":"ui/battle_numbers.4bpp.bin.lzn",            "start":0xA9E08F },
  { "name":"ui/rival_config.4bpp.bin.lzn",              "start":0x96C9F1 },
  { "name":"ui/alertbox/00_borders.4bpp.bin.lzn",       "start":0xB5D9DC },
  { "name":"ui/alertbox/03_phew.4bpp.bin.lzn",          "start":0xB5DAB4 },
  { "name":"ui/alertbox/06_red_star.4bpp.bin.lzn",      "start":0xB5DCC4 },
  { "name":"ui/alertbox/09_blue_moon.4bpp.bin.lzn",     "start":0xB5DEE9 },
  { "name":"ui/alertbox/0C_green_earth.4bpp.bin.lzn",   "start":0xB5E12C },
  { "name":"ui/alertbox/0F_yellow_comet.4bpp.bin.lzn",  "start":0xB5E3B5 },
  { "name":"ui/alertbox/12_proto_tank.4bpp.bin.lzn",    "start":0xB5E64D },
  { "name":"ui/alertbox/15_unknown.4bpp.bin.lzn",       "start":0xB5E8CD },
  { "name":"ui/alertbox/18_unknown.4bpp.bin.lzn",       "start":0xB5EAD7 },
  { "name":"ui/alertbox/1B_hq_captured.4bpp.bin.lzn",   "start":0xB5EDA3 },
  { "name":"ui/alertbox/1E_supply.4bpp.bin.lzn",        "start":0xB5F057 },
  { "name":"ui/alertbox/21_domination.4bpp.bin.lzn",    "start":0xB5F282 },
  { "name":"ui/alertbox/24_fuel_check.4bpp.bin.lzn",    "start":0xB5F5B7 },
  { "name":"ui/alertbox/27_acquired.4bpp.bin.lzn",      "start":0xB5F83B },
  { "name":"ui/alertbox/2A_captured.4bpp.bin.lzn",      "start":0xB5F9B8 },
  { "name":"ui/co/anim_1_1.4bpp.bin.lzn",               "start":0xA8E624 },
  { "name":"ui/co/anim_1_2.4bpp.bin.lzn",               "start":0xA8F4B6 },
  { "name":"ui/co/anim_1_3.4bpp.bin.lzn",               "start":0xA981DA },
  { "name":"ui/co/anim_1_4.4bpp.bin.lzn",               "start":0xA98DFA },
  { "name":"ui/co/anim_1_5.4bpp.bin.lzn",               "start":0xA99BB3 },
  { "name":"ui/co/anim_1_6.4bpp.bin.lzn",               "start":0xA9A763 },
  { "name":"ui/co/anim_1_7.4bpp.bin.lzn",               "start":0xA9B582 },
  { "name":"ui/co/anim_1_8.4bpp.bin.lzn",               "start":0xA9C05D },
  { "name":"terrain/static.4bpp.bin.lzn",               "start":0x96D546 },
  { "name":"intro/tiles_1.4bpp.bin.lzn",                "start":0x9D9945 },
  { "name":"intro/tiles_2.4bpp.bin.lzn",                "start":0x9DA246 },
  { "name":"intro/sprites_1.4bpp.bin.lzn",              "start":0xB48137 },
  { "name":"intro/sprites_2.4bpp.bin.lzn",              "start":0xB4883D },
  { "name":"intro/sprites_3.4bpp.bin.lzn",              "start":0xB58BE1 },
  { "name":"intro/sprites_4.4bpp.bin.lzn",              "start":0xB1CFED },
  { "name":"intro/sprites_5.4bpp.bin.lzn",              "start":0xB1D406 },
  { "name":"ending/end.2bpp.bin.lzn",                   "start":0x9D9511 },
  { "name":"ending/end.4bpp.bin.lzn",                   "start":0x9D8847 },
  { "name":"ending/end_4bpp.tilemap.bin.lzn",           "start":0x9D92D8 },

]


# 0x89D156: 120 structs à 0x15 bytes with misc "event" sprite sheets
# +6 points to compressed sprite graphics. Let's build a list!
compressed_event_sprites = []
for i in range(120):
  offset = 0x89D156 + 0x15 * i + 0x06
  ptr = rom.get_long(offset)
  compressed_event_sprites.append({ "name":"event/sprites/{:02X}_{:06X}_{:06X}.4bpp.bin.lzn".format(i, offset, ptr), "start":ptr })

# 0x89DB31 + 0x3F: List of long pointers to structs where +6 points to compressed graphics
compressed_event_tiles = []
for i in range(0x3f, 0x71, 0x03):
  offset = 0x89DB2E + i
  offset = rom.get_long(offset) + 6
  ptr = rom.get_long(offset)
  compressed_event_tiles.append({ "name":"event/tiles/{:02X}_{:06X}_{:06X}.4bpp.bin.lzn".format(i, offset, ptr), "start":ptr })

# 0x81CC33: 24 structs à 0x6 bytes with map unit sprite sheets
compressed_unit_sprites = []
for i in range(24):
  offset = 0x81CC63 + 0x06 * i
  ptr = rom.get_long(offset)
  compressed_unit_sprites.append({ "name":"units/sprites/{:02X}_{:06X}_{:06X}.4bpp.bin.lzn".format(i, offset, ptr), "start":ptr })


# 0x8e8aea: 22 pointers to staff roll data
compressed_staffroll_tiles = []
for i in range(22):
  offset = 0x8e8aea + 0x03 * i
  ptr = rom.get_long(offset)
  compressed_staffroll_tiles.append({ "name":"ending/staffroll/{:02X}_{:06X}_{:06X}.2bpp.bin.lzn".format(i, offset, ptr), "start":ptr })


def make_dir(path):
  try:
    os.makedirs(os.path.dirname(path))
  except OSError:
    if not os.path.isdir(os.path.dirname(path)):
        raise

def write_bytearray(arr, path):
  make_dir(path)
  with open(path, 'wb') as f:
    for b in arr:
      f.write(struct.pack("B", b))
    f.close()

def extract(da):
  for d in da:
    if not "end" in d and not "length" in d and d["name"].endswith(".lzn"):
      try:
        d["length"] = len(lzn.decode(rom.get_range({"start": d["start"], "length":0x10000}))[1])
      except Exception as e:
        print "Extraction failed: {}".format(e)
        continue
    r = rom.get_range(d)
    if r is not None:
      path = "./out/{}".format(d["name"])
      write_bytearray(r, path)
      print "Extracted: {} (0x{:X} bytes)".format(path, len(r))
      if path.endswith(".lzn"):
        er, _ = lzn.decode(r)
        path = path[:-4]
        write_bytearray(er, path)
        print "Decoded LZN: {} (0x{:X} bytes)".format(path, len(er))
      if path.endswith(".4bpp.bin"):
        os.system("{} tiles -v --bpp 4 --in-data {} --out-image {}".format(superfamiconv, path, "{}.png".format(path[:-4])))
      if path.endswith(".2bpp.bin"):
        os.system("{} tiles -v --bpp 2 --in-data {} --out-image {}".format(superfamiconv, path, "{}.png".format(path[:-4])))
      print ""

def main():
  try:
    extract(uncompressed_graphics)
    extract(compressed_graphics)
    extract(compressed_event_sprites)
    extract(compressed_event_tiles)
    extract(compressed_unit_sprites)
    extract(compressed_staffroll_tiles)
  except Exception as e:
    sys.exit(e)

if __name__ == "__main__":
    main()
