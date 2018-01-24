#!/usr/bin/python
# -*- coding: utf-8 -*-

# scan rom.Rom() for null terminated SJIS strings

import sys

sys.path.insert(0, "../../common")
from py_lib import rom_reader, sjis

MIN_LENGTH = 2

def scan(rom):
  print "#!/usr/bin/python"
  print "# -*- coding: utf-8 -*-"
  print "strings = {"
  start_offset = rom.get_offset()
  while True:
    char = sjis.to_utf8(rom.get_word())
    if char is not None:
      string = char
      start_offset = rom.get_offset()
      while True:
        rom.fwd(2)
        if rom.get_word() == 0:
          break
        char = sjis.to_utf8(rom.get_word())
        if char is None:
          break
        string += char

      if rom.get_word() == 0 and len(string) >= MIN_LENGTH * 2:
        length = rom.get_offset() - start_offset
        start = rom_reader.offset_to_lorom_addr(start_offset)
        end = start + length
        print "  0x{:06X}: {{ b:0x{:06X}, e:0x{:06X}, l:{:<3} ja:\"{}\"  }},".format(start, start, end, "{},".format(length), string)
        rom.fwd(1)
      else:
        rom.seek_offset(start_offset)

    rom.fwd(1)
    if rom.end():
      print "}"
      break

def main():
  try:
    scan(rom_reader.Rom("../../rom/Super Famicom Wars (Japan) (NP).sfc"))
  except Exception as e:
    sys.exit(e)

if __name__ == "__main__":
    main()
