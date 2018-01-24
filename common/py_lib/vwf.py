#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import util, kerning, pxbuf, png

# Make list of widths by scanning row 17 for number of non-zero values per 8 pixel slice
# (also scans row 18 for "join" markers for wider than 8 pixel characters, which I decided not to use)
def make_widths_array(png_path):
  r = png.Reader(file=open(png_path, "r"))
  (width, height, pixels, meta) = r.read()
  if height < 18:
    raise Exception("Error: in_png not tall enough")
  widths = []
  acc = 0
  for row, join_row in zip(util.iter_chunk(pixels[16], 8), util.iter_chunk(pixels[17], 8)):
    join = reduce(lambda a,b: a + 1 if (b > 0) else a, join_row)
    acc += reduce(lambda a,b: a + 1 if (b > 0) else a, row)
    if join < 2:
      widths.append(acc)
      acc = 0
  return widths

# Make list of lines (x2), counting from the first line, that contain only zero-value pixels per 8 pixel slice
def make_zlines_array(png_path):
  r = png.Reader(file=open(png_path, "r"))
  (width, height, pixels, meta) = r.read()
  if height < 16:
    raise Exception("Error: in_png not tall enough")
  zlines = []
  for char in range(width / 8):
    c_pixels = pxbuf.create([8, 16])
    pxbuf.paste(pxbuf.copy(pixels, [char*8,0, 8,16]), c_pixels, [0,0])
    count = 0
    for row in c_pixels:
      if reduce(lambda a,b: a + 1 if (b > 0) else a, row) > 0:
        break
      count += 1
    zlines.append(count * 2)
  return zlines


# Make re-arranged image
def make_processed_png(png_path, out_path, preshift=-1):
  r = png.Reader(file=open(png_path, "r"))
  (r_width, r_height, r_pixels, meta) = r.read()
  if r_height < 16:
    raise Exception("Error: image not tall enough")

  if 0 <= preshift <= 7:
    # Make pre-shifted image
    (width, height) = (r_width * 4, 8)
    pixels = pxbuf.create([width, height])
    for t in range(r_width / 8):
      pxbuf.paste(pxbuf.shift_base(pxbuf.copy(r_pixels,  [t*8,0, 8,8]), preshift)[0:8], pixels, [t*16*2+0,0])
      pxbuf.paste(pxbuf.shift_base(pxbuf.copy(r_pixels,  [t*8,8, 8,8]), preshift)[0:8], pixels, [t*16*2+8,0])
      pxbuf.paste(pxbuf.shift_spill(pxbuf.copy(r_pixels, [t*8,0, 8,8]), preshift)[0:8], pixels, [t*16*2+16,0])
      pxbuf.paste(pxbuf.shift_spill(pxbuf.copy(r_pixels, [t*8,8, 8,8]), preshift)[0:8], pixels, [t*16*2+24,0])

  else:
    # Not pre-shifted image
    (width, height) = (r_width * 2, 8)
    pixels = pxbuf.create([width, height])
    for t in range(r_width / 8):
      pxbuf.paste(pxbuf.copy(r_pixels, [t*8,0, 8,8]), pixels, [t*8*2,0])
      pxbuf.paste(pxbuf.copy(r_pixels, [t*8,8, 8,8]), pixels, [t*8*2+8,0])

  f = open(out_path, "wb")
  w = png.Writer(width, height, palette=meta["palette"], bitdepth=meta["bitdepth"], planes=meta["planes"], greyscale=meta["greyscale"], alpha=meta["alpha"])
  w.write(f, pixels)
  return True


# Return (rendered_width, character_widths, character_bounds) for string
def strlen(s, widths_table):
  width = 0
  c_widths = c_bounds = ""
  last_boundary = -1
  for i, c in enumerate(s):
    try:
      c_width = widths_table[ord(c) - 0x20]
      if i < len(s) - 1:
        pair = c + s[i + 1]
        for p, n in kerning.pairs:
          if pair == p:
            c_width -= n
      c_widths += `c_width`
      width += c_width
      if int(width / 8) > last_boundary:
        last_boundary += 1
        c_bounds += "."
      else:
        c_bounds += " "
    except Exception as e:
      pass
  return width, c_widths, c_bounds

