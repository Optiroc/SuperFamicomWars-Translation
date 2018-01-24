#!/usr/bin/python
# -*- coding: utf-8 -*-

from copy import copy as cp
from array import array

# Simple pixel buffer functions
def create(size):
  (w, h) = size
  pixels = []
  row = array("B", [0] * w)
  for i in range(h):
    pixels.append(cp(row))
  return pixels

def copy(pixels, area):
  (x, y, w, h) = area
  crop = []
  for row in range(h):
    crop.append(pixels[y+row][x:x+w])
  return crop

def paste(src_pixels, dest_pixels, coord):
  (x, y) = coord
  for i, row, in enumerate(src_pixels):
    dest_pixels[y+i][x:x+len(row)] = row

def shift(pixels, amount):
  h = len(pixels)
  w = len(pixels[0])
  shifted = []
  for i, row, in enumerate(pixels):
    tr = array("B", [])
    tr.extend([0] * amount)
    tr.extend(row)
    tr.extend([0] * (amount - w))
    shifted.append(tr[0:8])
    shifted.append(tr[8:16])
  return shifted

def shift_base(pixels, amount):
  h = len(pixels)
  w = len(pixels[0])
  shifted = []
  for i, row, in enumerate(pixels):
    tr = array("B", [])
    tr.extend([0] * amount)
    tr.extend(row)
    tr.extend([0] * (amount - w))
    shifted.append(tr[0:8])
  return shifted

def shift_spill(pixels, amount):
  h = len(pixels)
  w = len(pixels[0])
  shifted = []
  for i, row, in enumerate(pixels):
    tr = array("B", [])
    tr.extend([0] * amount)
    tr.extend(row)
    tr.extend([0] * (amount - w))
    shifted.append(tr[8:16])
  return shifted
