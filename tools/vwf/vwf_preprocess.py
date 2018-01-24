#!/usr/bin/python
# -*- coding: utf-8 -*-

# 8x16px variable width font preprocessor, serving two functions:
# - Export width table
# - Re-arrange font image
#
# The input font image is a horizontal strip of at least 16px (+2 for width encoding):
# AtBtCtDt ...
# AbBbCbDb ... (?t = top tile, ?b = bottom tile)
#
# Which is re-arranged to an 8px tall strip arranged like so:
# AtAbBtBbCtCbDtDb ...
#
# Rows 17 and 18 contain width encoding:
# - Row 17 should contain as many non-zero pixel as the width of its corresponding character
# - If row 18 contains more than 1 non-zero pixel its willidth will be joined with the next character

from argparse import ArgumentParser
import sys, os
sys.path.insert(0, "{}/../../common".format(os.path.dirname(os.path.realpath(__file__))))
from py_lib import util, codegen, vwf

def main():
  parser = ArgumentParser()
  parser.add_argument("--in_png", dest="in_png", required=True, metavar="FILE", type=lambda x: util.is_valid_file(parser, x))
  parser.add_argument("--out_png", dest="out_png", metavar="FILE")
  parser.add_argument("--widths", dest="widths", action="store_true")
  parser.add_argument("--widths_label", dest="widths_label", default="VWF_widths")
  parser.add_argument("--zlines", dest="zlines", action="store_true")
  parser.add_argument("--zlines_label", dest="zlines_label", default="VWF_zlines")
  parser.add_argument("--preshift", dest="preshift", type=int, default=-1)

  try:
    args = parser.parse_args()
    if args.out_png:
      vwf.make_processed_png(args.in_png, args.out_png, args.preshift)

    if args.widths:
      print "; {}".format(vwf.make_widths_array(args.in_png))
      codegen.insert(name=args.widths_label, bank=0x82, d={"b":vwf.make_widths_array(args.in_png)})

    if args.zlines:
      codegen.insert(name=args.zlines_label, bank=0x82, d={"b":vwf.make_zlines_array(args.in_png)})

  except Exception as e:
    sys.exit(e)

if __name__ == "__main__":
    main()
