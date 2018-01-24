#!/usr/bin/python

# LZN [v.IS/SFW] Decoder/Encoder
# (Lempel-Ziv-Nintendo, Intelligent Systems / Super Famicom Wars)
#
# R&D by David Lindecrantz <optiroc@gmail.com>
#
# - Decoder only supports the opcodes used in data I've mined so far
# - Encoder logic not touched since 2013.01.29. There's room for improvement!

import sys
import os
import struct
import binascii
import argparse

verbose = False

# Bytearray wrapper with some conveniences
class Bytestream(object):
  def __init__(self, bytes):
    self.offset = 0
    self.bytes = bytearray(bytes)

  def at_end(self):
    return self.offset >= len(self.bytes)

  def read(self, n=1, always_array=False):
    if n == 1 and not always_array:
      t = self.bytes[self.offset]
      self.offset += 1
      return t
    else:
      t = self.bytes[self.offset:self.offset+n]
      self.offset += n
      return t

  def get(self, n=1, always_array=False):
    ofs = self.offset
    res = self.read(n, always_array)
    self.offset = ofs
    return res

  def append(self, bytes):
    if isinstance(bytes, bytearray):
      self.bytes += bytes
    elif isinstance(bytes, int):
      self.bytes.append(bytes)

  def append_rle(self, val, len):
    self.bytes += bytearray([val] * len)

  def append_slw(self, offset, len):
    for i in range(len):
      self.bytes.append(self.bytes[-offset])

  def length(self):
    return len(self.bytes)

  def seek(self, offset):
    self.offset = offset

  def fwd(self, length):
    self.offset += length

  def cut(self):
    self.bytes = self.bytes[0:self.offset]

  def is_equal(self, bytes):
    if isinstance(bytes, bytearray):
      return self.bytes == bytes
    elif isinstance(bytes, Bytestream):
      return self.bytes == bytes.bytes
    else:
      raise NameError("Bytestream.is_equal(): Not bytearray or Bytestream")


# Bytearray to string
def bytearray_to_string(ba):
  str = ""
  for b in ba:
    str += " {:02X}".format(b)
  return str


#-----------------------------------------------------------------------------
# Decoder

def decode(in_bs):
  """
  Decodes an LZN stream.

  :param in_bs: LZN bytearray or Bytestream
  :return: (out_bytearray, in_bytearray)
  :rtype: (bytearray, bytearray)

  .. note:: Returns a tuple with both the decoded bytes and the input bytes
            trimmed to it's correct length. This is useful when not knowing
            the length ot the input beforehand.
  """

  if not isinstance(in_bs, Bytestream): in_bs = Bytestream(in_bs)
  out_bs = Bytestream([])

  while True:
    # Decode opcode
    try:
      opcode = in_bs.read()
    except Exception as e:
      raise NameError("LZN_ERR: Stream not terminated")

    # Opcode 00 / #$00-#$3f / %00xxxxxx [x+1 bytes]
    # Straight stream copy
    # Copy x+1 bytes straight from source stream
    #   x = #$00-#$3f (1-64)
    if opcode & 0xC0 == 0x00:
      length = (opcode & 0x3F) + 1
      out_bs.append(in_bs.read(length))

    # Opcode 0100 / #$40-#$4f / %0100xxxx uv.wyyyy [x/2 bytes]
    # Write x+(1|2) interleaved bytes
    # Different nybble patterns depending on parameters u/v/w
    #   u = Get constant nybble from parameter v or y (0 = constant y, 1 = constant v)
    #   w = Byte pattern (0 = stream:constant, 1 = constant:stream)
    #   If u=1 the first variable nybble is "yyyy"
    #   If u=0 the first variable nybble is the most significant bits of next byte

    # Opcode 0101 / #$50-#$5f / %0101xxxx [x+1 bytes]
    # Double pump stream copy
    # Copy x+1 bytes from source stream, write each byte two times
    #   x = #$0-#$f (1-16)
    elif opcode & 0xF0 == 0x50:
      length = (opcode & 0x0F) + 1
      for b in in_bs.read(length, True):
        out_bs.append(bytearray([b] * 2))

    # Opcode 011 / #$60-#$7f / %011wxxxx yyyyyyyy [x+1 bytes]
    # Interleaved word copy
    # Write x+2 interleaved words (constant byte:streamed byte, or vice versa)
    #   y = Constant byte
    #   w = Word pattern (0 = constant:stream, 1 = stream:constant)
    elif opcode & 0xE0 == 0x60:
      pattern = opcode & 0x10
      length = (opcode & 0x0F) + 2
      constant = in_bs.read()
      for b in in_bs.read(length, True):
        if pattern == 0:
          out_bs.append(constant); out_bs.append(b)
        else:
          out_bs.append(b); out_bs.append(constant)

    # Opcode 10 / #$80-#$bf / %10xxxxyy yyyyyyyy
    # Sliding window copy, 2-byte
    # Copy x+2 bytes from offset -y in decoded buffer
    #   x = #$0-#$f (2-17)
    #   y = #$000-#$3ff (0-1023)
    elif opcode & 0xC0 == 0x80:
      length = ((opcode & 0x3C) >> 2) + 2
      offset = in_bs.read() + ((opcode & 0x03) << 8)
      try:
        out_bs.append_slw(offset, length)
      except Exception as e:
        raise NameError("LZN_ERR: Sliding window copy out of bounds")

    # Opcode 110 / #$c0-#$df / %110xxxxx xyyyyyyy yyyyyyyy
    # Sliding window copy, 3-byte
    # Copy x+2 bytes from offset -y in decoded buffer
    #   x = #$00-#$3f (2-65)
    #   y = #$0000-#$7fff (0-32767)
    elif opcode & 0xE0 == 0xC0:
      opr1 = in_bs.read()
      length = ((opcode & 0x1F) << 1) + (opr1 >> 7) + 2
      offset = ((opr1 & 0x7F) << 8) + in_bs.read()
      try:
        out_bs.append_slw(offset, length)
      except Exception as e:
        raise NameError("LZN_ERR: Sliding window copy out of bounds")

    # Opcode 1110 / #$e0-#$ef / %1110xxxx xxxxxxxx yyyyyyyy
    # Byte RLE, 3-byte
    # Duplicate byte y x+3 times
    #   x = #$000-#$fff (3-4098)
    elif opcode & 0xF0 == 0xE0:
      length = ((opcode & 0x0F) << 8) + in_bs.read() + 3
      out_bs.append_rle(in_bs.read(), length)

    # Opcode 11110 / #$f0-#$f7 / %11110xxx yyyyyyyy
    # Byte RLE, 2-byte
    # Duplicate byte y x+3 times
    #   x = #$0-#$7 (3-10)
    elif opcode & 0xF8 == 0xF0:
      length = (opcode & 0x07) + 3
      out_bs.append_rle(in_bs.read(), length)

    # Opcode 111110 / #$f8-#$fb / %111110xx xxx.yyyy yyyyyyyy
    # Rewind stream pointer, 3-byte
    # Rewind to -y, decode x+3 bytes before returning
    #   x = #$00-#$1f (3-34)
    #   y = #$000-#$fff (0-4095)

    # Opcode 1111110 /#$fc-#$fd / %1111110x xxyyyyyy
    # Rewind stream pointer, 2-byte
    # Rewind to -y, decode x+3 bytes before returning
    #   x = #$0-#$7 (3-10)
    #   y = #$00-#$3f (0-63)

    # Opcode 1111111 / #$fe-#$ff / %1111111.
    # End of data
    elif opcode & 0xFE == 0xFE:
      break

    else:
      raise NameError("LZN_ERR: Opcode 0x{:02X} not implemented".format(opcode))


  # Done
  in_bs.cut()
  return out_bs.bytes, in_bs.bytes



#-----------------------------------------------------------------------------
# Encoder

def encode(in_bs):
  """
  Encodes an LZN stream.

  :param in_bs: bytearray or Bytestream
  :return: (out_bytearray)
  :rtype: bytearray
  """

  if not isinstance(in_bs, Bytestream): in_bs = Bytestream(in_bs)
  out_bs = Bytestream([])

  # Encode functions

  # Find identical sequence in already decoded stream (return length, offset)
  def search_slw(stream):
    MIN_LEN = 2
    MAX_LEN = 64
    MAX_OFFSET = 32767
    search_offset = max(0, stream.offset - MAX_OFFSET)
    forward_window = stream.bytes[stream.offset:stream.offset+MAX_LEN]
    if len(forward_window) < MIN_LEN or stream.offset - search_offset < MIN_LEN:
      return 0, 0

    length = MIN_LEN
    while True:
      if length > len(forward_window) or length > MAX_LEN:
        length -= 1
        break
      match_window = forward_window[0:length]
      search_window = stream.bytes[search_offset:stream.offset+length-2]
      if search_window[0:stream.offset+search_offset+length].count(match_window) > 0:
        length += 1
      else:
        length -= 1
        break

    if length >= MIN_LEN:
      return length, stream.offset - stream.bytes[search_offset:stream.offset+length].index(forward_window[0:length])
    return 0, 0

  # Get number of identical bytes in stream forward from current offset (max_len=4096)
  def search_rle(stream):
    MIN_LEN = 3
    MAX_LEN = 4096
    org_offset = stream.offset
    length = 1
    match_byte = stream.read()
    while stream.at_end() is not True:
      if length == MAX_LEN:
        break
      elif match_byte == stream.read():
        length += 1
      else:
        break
    if length < MIN_LEN:
      length = 0
    stream.offset = org_offset
    return length, match_byte

  # Get number of bytes until next RLE or SW match in stream forward from index (max 64 bytes)
  def get_literal_len(stream):
    org_offset = stream.offset
    length = 1
    while stream.at_end() is not True and search_rle(stream)[0] == 0 and search_slw(stream)[0] == 0:
      if length == 64:
        break
      length += 1
      stream.read()
    stream.offset = org_offset
    return length - 1


  # Encode
  while True:
    if in_bs.at_end():
      break

    # Look for Sliding Window and RLE matches
    slw_len, slw_offset = search_slw(in_bs)
    rle_len, rle_value = search_rle(in_bs)
    if rle_len >= slw_len: slw_len = 0

    # Append Sliding Window opcode
    if slw_len > 0:
      if verbose:
        print "{:06X}:{:06X} SLW sequence, 0x{:04X} bytes from offset 0x{:04X}".format(in_bs.offset, out_bs.length(), slw_len, slw_offset)
      if slw_len > 16 or slw_offset > 1023:
        # 3-byte SLW opcode, #$c0-#$df (%110xxxxx xyyyyyyy yyyyyyyy)
        out_bs.append(0xc0 | (((slw_len - 2) >> 1) & 0x1f))
        out_bs.append((((slw_len - 2) << 7) & 0x80) | ((slw_offset & 0x7f00) >> 8))
        out_bs.append(slw_offset & 0x00ff)
      else:
        # 2-byte SLW opcode, #$80-#$bf (%10xxxxyy yyyyyyyy)
        out_bs.append((0x80 | (slw_len - 2 & 0x0f) << 2) | ((slw_offset & 0x0300) >> 8))
        out_bs.append(slw_offset & 0xff)
      in_bs.fwd(slw_len)
      continue

    # Append RLE opcode
    if rle_len > 0:
      if verbose:
        print "{:06X}:{:06X} RLE sequence, 0x{:02X} * 0x{:X}".format(in_bs.offset, out_bs.length(), rle_value, rle_len)
      if rle_len > 9:
        # 3-byte RLE instruction, #$e0-#$ef (%1110xxxx xxxxxxxx yyyyyyyy)
        out_bs.append(0xe0 | ((rle_len - 3 >> 8) & 0x0f))
        out_bs.append((rle_len - 3) & 0xff)
        out_bs.append(rle_value)
      else:
        # 2-byte RLE instruction, #$f0-#$f7 (%11110xxx yyyyyyyy)
        out_bs.append(0xf0 | ((rle_len - 3) & 0x07))
        out_bs.append(rle_value)
      in_bs.fwd(rle_len)
      continue

    # Append literal
    lit_len = get_literal_len(in_bs)
    append_bytes = in_bs.get(lit_len, True)
    if verbose:
      print "{:06X}:{:06X} LIT sequence, 0x{:X} bytes".format(in_bs.offset, out_bs.length(), lit_len)
      #print "  Bytes:{}".format(bytearray_to_string(append_bytes))
    out_bs.append((lit_len - 1) & 0x3f)
    out_bs.append(append_bytes)
    in_bs.fwd(lit_len)


  # Done, terminate stream
  out_bs.append(0xff)
  if verbose:
    print "---"
    print "Original size     {:8d}B  (0x{:06X})".format(in_bs.length(), in_bs.length())
    print "Compressed size   {:8d}B  (0x{:06X})".format(out_bs.length(), out_bs.length())
    print "Compression ratio {:8.2f}%".format(100.0 * (float(out_bs.length()) / float(in_bs.length())))
  return out_bs.bytes


#-----------------------------------------------------------------------------
# Command Line Interface

def main():
  parser = argparse.ArgumentParser()
  parser.add_argument('-i', metavar='infile', type=argparse.FileType('rb'), help='Input path', required=True)
  parser.add_argument('-o', metavar='outfile', type=argparse.FileType('wb'), help='Output path')
  parser.add_argument('-x', action='store_true', default=False, dest='extract', help='Extract data')
  parser.add_argument('-v', action='store_true', default=False, dest='verbose', help='Verbose output')
  parser.add_argument('-t', action='store_true', default=False, dest='test', help='Test output')
  parser.add_argument('--version', action='version', version='%(prog)s 0.2.0')

  try:
    global verbose
    arguments = parser.parse_args()
    verbose = arguments.verbose
    inbytes = bytearray(arguments.i.read())
    arguments.i.close()

    if arguments.extract is True:
      outbytes, _ = decode(inbytes)
      if arguments.test is True:
        ref = encode(outbytes)
        print "Test = {}".format(ref == inbytes)
    else:
      outbytes = encode(inbytes)
      if arguments.test is True:
        ref, _ = decode(outbytes)
        print "Test = {}".format(ref == inbytes)

    if arguments.o is not None:
      for byte in outbytes:
        arguments.o.write(struct.pack("B", byte))
      arguments.o.close()

  except IOError, msg:
    parser.error(str(msg))

if __name__ == "__main__":
    main()
