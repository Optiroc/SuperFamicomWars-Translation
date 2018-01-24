#!/usr/bin/python
# -*- coding: utf-8 -*-

def offset_from_lorom_addr(address):
  bank = (address >> 16) & 0x7f
  return (bank * 0x8000) + (address & 0x7fff)

def offset_to_lorom_addr(offset):
  bank = (offset >> 15) + 0x80
  return (bank << 16) + (offset & 0x7fff) + 0x8000


class Rom(object):
  def __init__(self, rom_path):
    file = open(rom_path, mode="rb")
    self.bytes = bytearray(file.read())
    file.close()
    self.offset = 0

  def seek_offset(self, offset):
    self.offset = offset

  def seek_address(self, address):
    self.offset = offset_from_lorom_addr(address)

  def get_offset(self):
    return self.offset

  def end(self):
    return self.offset >= len(self.bytes)

  def fwd(self, amount=1):
    self.offset += amount

  def bwd(self, amount=1):
    self.offset -= amount

  def get_byte(self):
    if self.offset >= len(self.bytes):
      return None
    else:
      return self.bytes[self.offset]

  def get_word(self, big_endian=False):
    if self.offset >= len(self.bytes) - 1:
      return None
    else:
      if big_endian is False:
        return (self.bytes[self.offset] << 8) + self.bytes[self.offset + 1]
      else:
        return self.bytes[self.offset] + (self.bytes[self.offset + 1] << 8)

  def get_long(self, addr=None):
    if addr is not None:
      self.seek_address(addr)
    if self.offset >= len(self.bytes) - 2:
      return None
    else:
      return self.bytes[self.offset] + (self.bytes[self.offset + 1] << 8) + (self.bytes[self.offset + 2] << 16)

  def get_range(self, p):
    start = end = length = None
    if "start" in p:
      start = p["start"]
    if "end" in p:
      end = p["end"]
    if "length" in p:
      length = p["length"]
    if start and end:
      return self.bytes[offset_from_lorom_addr(start):offset_from_lorom_addr(end)+1]
    if start and length:
      return self.bytes[offset_from_lorom_addr(start):offset_from_lorom_addr(start)+length]
    return None

