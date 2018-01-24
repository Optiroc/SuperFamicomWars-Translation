#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
from _lib_ import cg, sfw, rom_reader

#-----------------------------------------------------------------------------
# Sprite def manipulation

rom = rom_reader.Rom("{}/../../rom/Super Famicom Wars (Japan) (NP).sfc".format(os.path.dirname(os.path.realpath(__file__))))

class spritedef(object):
  def __init__(self, address):
    self.spr_defs = []
    self.address = address
    rom.seek_address(address)
    self.length = rom.get_word()
    rom.fwd(2)
    for i in range(self.length):
      spr_def = []
      spr_def.append(rom.get_word())
      rom.fwd(2)
      spr_def.append(rom.get_byte())
      rom.fwd(1)
      spr_def.append(rom.get_word())
      rom.fwd(2)
      self.spr_defs.append(spr_def)

  def adjust_pos(self, xd, yd):
    for i, spr_def in enumerate(self.spr_defs):
      cg.data_section({ "at":(self.address + 2 + i * 5) + 0, "w":(spr_def[0] & 0xf000) + (((spr_def[0] & 0x0fff) + xd) & 0x0fff) }) # x-position
      cg.data_section({ "at":(self.address + 2 + i * 5) + 2, "b":(spr_def[1] + yd) & 0xff }) # y-position


#-----------------------------------------------------------------------------
# Intro

# Title screen OAM table
cg.insert(at=0x8ea19e, name="OAMTABLE_title_start", d=sfw.oam_table([
  sfw.oam_entry(0x1d1+16*0, 0xff, 0x000, 0, 1, 3),
  sfw.oam_entry(0x1d1+16*1, 0xff, 0x002, 0, 1, 3),
  sfw.oam_entry(0x1d1+16*2, 0xff, 0x004, 0, 1, 3),
  sfw.oam_entry(0x1d1+16*3, 0xff, 0x006, 0, 1, 3),
  sfw.oam_entry(0x1d1+16*4, 0xff, 0x008, 0, 1, 3),
  sfw.oam_entry(0x1d1+16*5, 0xff, 0x00a, 0, 1, 3)
]))


#-----------------------------------------------------------------------------
# Initial load/config menus

# New game box width
new_game_boxdef      = 0x87E5A4
new_game_boxdim      = 0x87E59B
sfw.boxdim_set_width(new_game_boxdim, 10)

# Select mode box width
select_mode_boxdef   = 0x87EE18
select_mode_boxdim   = 0x87EE0F
sfw.boxdim_set_width(select_mode_boxdim, 17)

# Load game
# Map name column
cg.insert(at=0x87F228, d={"b":0x04})

# Game config
# Auto supply toggle column
cg.insert(at=0x87DAB4, d={"b":0x09})
# CO Profile
cg.insert(at=0x87C4F8, d={"b":0x10}) # Window width
cg.insert(at=0x87C4F9, d={"b":0x12}) # Window height
cg.insert(at=0x87C50C, d={"b":0x04}) # Window y-pos
cg.insert(at=0x8AA602, d={"b":0x38 - 2}) # Level stars y-pos

# Diplomatic Relations
cg.insert(at=0x8BE95D, d={"b":0x0C - 2}) # Level stars y-pos
cg.insert(at=0x8BEA75, d={"b":0xFF})     # D-pad y-pos

# Map select
cg.insert(at=0x87faca, d={"b":0x03}) # "Unoccupied Territory" x-pos
cg.insert(at=0x87fb17, d={"b":0x01}) # "Occupied by" x-pos
cg.insert(at=0x87fade, d={"b":0x05}) # Occupying army x-pos
cg.insert(at=0x87fb2e, d={"b":0x01}) # "Duration" x-pos
cg.insert(at=0x87fb00, d={"b":0x07}) # Days # x-pos
cg.insert(at=0x87fb45, d={"b":0x09}) # "days" x-pos


#-----------------------------------------------------------------------------
# In-game menues

# Main menu width
ingame_menu_boxdef   = 0x87CA56
ingame_menu_boxdim   = 0x87CA4D
sfw.boxdim_set_width(ingame_menu_boxdim, 8)

# Player command menu width
capture_menu1_boxdef = 0x87CC23
capture_menu1_boxdim = 0x87CC1A
sfw.boxdim_set_width(capture_menu1_boxdim, 8)

# AI command menu width
cg.insert(at=0x87c399, d={"b":0x04})

attack_menu_boxdef = 0x87C34A
attack_menu_boxdim = 0x87C341
sfw.boxdim_set_width(attack_menu_boxdim, 8)

# Retreat dialogue width
retreat_dialogue_boxdef   = 0x87F63E
retreat_dialogue_boxdim   = 0x87F635
sfw.boxdim_set_width(retreat_dialogue_boxdim, 14)


#-----------------------------------------------------------------------------
# Terrain / unit info boxes

# BG plate sprites added at 8A87C6
# - Only terrain at 8A87F8

# Terrain box
# Drawn at 87BC8C
# Strings/stats drawn at 8A8735
# Width
cg.insert(at=0x87bd12, d={"b":0x07})
# Stat columns
cg.insert(at=0x8A8781, d={"b":0x04})
cg.insert(at=0x8A878B, d={"b":0x04})
# OAM table
cg.insert(at=0x8A87F9, d={"label_word":"OAMTABLE_terrain_box"})
cg.insert(bank=0x8a, name="OAMTABLE_terrain_box", d=sfw.oam_table([
  sfw.oam_entry( 0,  0, 0x0da, 2, 1, 3), # terrain icon
  sfw.oam_entry(17,  0, 0x0f8, 0, 0, 3), # def
  sfw.oam_entry(24,  0, 0x0f4, 0, 0, 3), # def-star
  sfw.oam_entry(17,  8, 0x0f6, 0, 0, 3), # cap
  sfw.oam_entry( 0, 16, 0x0d6, 3, 1, 3), # bg-plates...
  sfw.oam_entry(16,  0, 0x0d6, 3, 1, 3),
  sfw.oam_entry(16, 16, 0x0d6, 3, 1, 3),
  sfw.oam_entry(24,  0, 0x0d6, 3, 1, 3),
  sfw.oam_entry(24, 16, 0x0d6, 3, 1, 3),
]))


# Unit box
# Strings/stats drawn at 8A852B
# String position at 8A8543
# Width
cg.insert(at=0x87BCE9, d={"b":0x0B})
# Width with loaded transport
cg.insert(at=0x87BCF1, d={"b":0x0E})
# OAM tables
cg.insert(at=0x8A87DD, d={"label_word":"OAMTABLE_unit_box"})
cg.insert(bank=0x8a, name="OAMTABLE_unit_box", d=sfw.oam_table([
  sfw.oam_entry(25,  0, 0x0f0, 0, 0, 3), # heart
  sfw.oam_entry(25,  8, 0x0f1, 0, 0, 3), # boot
  sfw.oam_entry(25, 16, 0x0f2, 0, 0, 3), # gas
  sfw.oam_entry(25, 24, 0x0f3, 0, 0, 3), # ammo
  sfw.oam_entry(49, 16, 0x0f8, 0, 0, 3), # def
  sfw.oam_entry(56, 16, 0x0f4, 0, 0, 3), # def-star
  sfw.oam_entry(49, 24, 0x0f6, 0, 0, 3), # cap
  sfw.oam_entry(16,  0, 0x0d6, 3, 1, 3), # bg-plates...
  sfw.oam_entry(16, 16, 0x0d6, 3, 1, 3),
  sfw.oam_entry(24,  0, 0x0d6, 3, 1, 3),
  sfw.oam_entry(24, 16, 0x0d6, 3, 1, 3)
]))
cg.insert(at=0x8A87E4, d={"label_word":"OAMTABLE_unit_box_loaded"})
cg.insert(bank=0x8a, name="OAMTABLE_unit_box_loaded", d=sfw.oam_table([
  sfw.oam_entry(56,  0, 0x0da, 2, 1, 3), # terrain icon
  sfw.oam_entry(56, 16, 0x0d6, 3, 1, 3), # bg-plates...
  sfw.oam_entry(40,  0, 0x0d6, 3, 1, 3),
  sfw.oam_entry(40, 16, 0x0d6, 3, 1, 3)
]))


# Unit stats
cg.insert(at=0x8A8565, d={"b":0x05}) # HP
cg.insert(at=0x8A8583, d={"b":0x05}) # Move range
cg.insert(at=0x8A8557, d={"b":0x05}) # Gas
cg.insert(at=0x8A856F, d={"b":0x05}) # Ammo

# Clear strings
cg.insert(at=0x8A859A, d={"b":0x07})
cg.insert(at=0x8A85B1, d={"b":0x07})

# Def/capture stats
cg.insert(at=0x8A85DF, d={"b":0x08})
cg.insert(at=0x8A85E9, d={"b":0x08})

# Unit sprite position on terrain + unit box
# Function at 8A8804: loads pointer to OAM table for unit sprite, offset list at 8A8812:
# .DW $8830, $8841, $8852, $8863

# Clear strings
cg.insert(at=0x8A8605, d={"b":0x0A})
cg.insert(at=0x8A861C, d={"b":0x0A})

# Patch first sprite position
cg.insert(at=0x8A8832, d={"b":0x03})
cg.insert(at=0x8A8843, d={"b":0x03})
cg.insert(at=0x8A8854, d={"b":0x03})
cg.insert(at=0x8A8865, d={"b":0x03})

# Extra sprites on loaded unit box
# Branch for adding extra sprites at 8A87EF
# Function at 8a881a: loads pointer to OAM table for unit sprite, offset list at 8A882A:
# .DW $8874, $8894, $88b4, $88d4

# Patch positions of unit sprites and background plates
# 8A8874, length 6:
cg.insert(at=0x8A8876 + 0*5, d={"b":0x48 + 7})  # unit 1
cg.insert(at=0x8A8876 + 1*5, d={"b":0x48 + 8})  # plate 2:1
cg.insert(at=0x8A8876 + 2*5, d={"b":0x48 + 7})  # unit 2
cg.insert(at=0x8A8876 + 3*5, d={"b":0x48 + 8})  # plate 2:2
cg.insert(at=0x8A8876 + 4*5, d={"b":0x40 + 8})  # plate 1:1
cg.insert(at=0x8A8876 + 5*5, d={"b":0x40 + 8})  # plate 1:2
# 8A8894, length 6:
cg.insert(at=0x8A8896 + 0*5, d={"b":0x48 + 7})  # unit 1
cg.insert(at=0x8A8896 + 1*5, d={"b":0x48 + 8})  # plate 2:1
cg.insert(at=0x8A8896 + 2*5, d={"b":0x48 + 7})  # unit 2
cg.insert(at=0x8A8896 + 3*5, d={"b":0x48 + 8})  # plate 2:2
cg.insert(at=0x8A8896 + 4*5, d={"b":0x40 + 8})  # plate 1:1
cg.insert(at=0x8A8896 + 5*5, d={"b":0x40 + 8})  # plate 1:2
# 8A88B4, length 6:
cg.insert(at=0x8A88B6 + 0*5, d={"b":0x48 + 7})  # unit 1
cg.insert(at=0x8A88B6 + 1*5, d={"b":0x48 + 8})  # plate 2:1
cg.insert(at=0x8A88B6 + 2*5, d={"b":0x48 + 7})  # unit 2
cg.insert(at=0x8A88B6 + 3*5, d={"b":0x48 + 8})  # plate 2:2
cg.insert(at=0x8A88B6 + 4*5, d={"b":0x40 + 8})  # plate 1:1
cg.insert(at=0x8A88B6 + 5*5, d={"b":0x40 + 8})  # plate 1:2
# 8A88D4, length 6:
cg.insert(at=0x8A88D6 + 0*5, d={"b":0x48 + 7})  # unit 1
cg.insert(at=0x8A88D6 + 1*5, d={"b":0x48 + 8})  # plate 2:1
cg.insert(at=0x8A88D6 + 2*5, d={"b":0x48 + 7})  # unit 2
cg.insert(at=0x8A88D6 + 3*5, d={"b":0x48 + 8})  # plate 2:2
cg.insert(at=0x8A88D6 + 4*5, d={"b":0x40 + 8})  # plate 1:1
cg.insert(at=0x8A88D6 + 5*5, d={"b":0x40 + 8})  # plate 1:2


#-----------------------------------------------------------------------------
# Unit info window

# Weapon strings x-position
cg.insert(at=0x8AC591, d={"b":0x0a})
cg.insert(at=0x8AC5A5, d={"b":0x0a})
# HP stat x-position
cg.insert(at=0x8AC729, d={"b":0x0a})

# OAM positions: code at 8AC88F, OAM table at 8ACB19
cg.insert(at=0x8ACB1B + 0*5 + 0, d={"b":0x3e - 8})  # Main weapon x-pos
cg.insert(at=0x8ACB1B + 1*5 + 0, d={"b":0x3e - 8})  # Sub weapon x-pos
cg.insert(at=0x8ACB1B + 2*5 + 0, d={"b":0x80 - 1})  # Main range x-pos #1
cg.insert(at=0x8ACB1B + 3*5 + 0, d={"b":0x88 - 1})  # Main range x-pos #2
cg.insert(at=0x8ACB1B + 4*5 + 0, d={"b":0x80 - 1})  # Sub range x-pos #1
cg.insert(at=0x8ACB1B + 5*5 + 0, d={"b":0x88 - 1})  # Sub range x-pos #2
cg.insert(at=0x8ACB1B + 6*5 + 0, d={"b":0xb0 - 0})  # Main ammo x-pos
cg.insert(at=0x8ACB1B + 6*5 + 2, d={"b":0x08 + 1})  # Main ammo y-pos
cg.insert(at=0x8ACB1B + 7*5 + 0, d={"b":0xb0 - 0})  # Sub ammo x-pos
cg.insert(at=0x8ACB1B + 7*5 + 2, d={"b":0x18 + 1})  # Sub ammo y-pos
cg.insert(at=0x8ACB1B + 8*5 + 0, d={"b":0x38 - 1})  # HP heart x-pos
cg.insert(at=0x8ACB1B + 9*5 + 0, d={"b":0x5c + 3})  # Move type x-pos

# EXP decoration sprite offset
cg.insert(at=0x8aca54, d={"w":0x01fe}) # x-offs
cg.insert(at=0x8aca5c, d={"w":0x0019}) # y-offs
cg.insert(at=0x8aca5a, d={"b":[0x38, 0xe9]}) # clc/sbc for y-offs

# Page indicator y-offset
cg.insert(at=0x8a8c78, d={"w":0x0007})

# Build cost amount x-position
cg.insert(at=0x8ac4c8, d={"b":0x06})

# Ammo cost x-position
cg.insert(at=0x8ac522, d={"b":0x10})
# Ammo cost amount n/a x-position
cg.insert(at=0x8ac50d, d={"b":0x16})

# Blue/Green/etc indicator row, OAM table at 8ACB5C
cg.insert(at=0x8ACB8E, d={"b":0xce})  # New id for last sprite of "red", remaining sprite used for small exp star border

# EXP
cg.insert(at=0x8ACAEE, d={"w":0x38 + 1}) # EXP big star y-offset
cg.insert(at=0x8ACAB0, d={"w":0x28 - 4}) # EXP small stars x-offset
# Fix border of first EXP star
cg.insert(at=0x8acaf7, d={"label_word":"OAMTABLE_unit_info_expstars"})
cg.insert(bank=0x8a, name="OAMTABLE_unit_info_expstars", d=sfw.oam_table([
  sfw.oam_entry( 0, 0, 0x0d9, 0, 1, 3), # big star
  sfw.oam_entry(20, 3, 0x0cf, 0, 0, 3), # fix outline of first small star
]))


#-----------------------------------------------------------------------------
# Terrain info window

# Name column
cg.insert(at=0x8acde0, d={"b":0x01})
# Income column
cg.insert(at=0x8ace47, d={"b":0x17})
# "Def:" string column
cg.insert(at=0x8ace0e, d={"b":0x08})
# "Def stars" x-offset
cg.insert(at=0x8acf73, d={"b":0x4c})

# Move cost title
cg.insert(at=0x8acf1d, d={"b":0x0c - 2}) # x-offset
cg.insert(at=0x8acf2e, d={"label_word":"OAMTABLE_terrain_info_movecost"}) # original table at 8acf35
cg.insert(bank=0x8a, name="OAMTABLE_terrain_info_movecost", d=sfw.oam_table([
  sfw.oam_entry( 0, 0, 0x0b4, 0, 1, 3),
  sfw.oam_entry(16, 0, 0x0b6, 0, 1, 3),
  sfw.oam_entry(32, 0, 0x0b8, 0, 1, 3),
]))


#-----------------------------------------------------------------------------
# Battle results

# 'Battle results' column
cg.insert(at=0x8bb674, d={"b":0x0d})
# 'Days:' column
cg.insert(at=0x8bb6b2, d={"b":0x16})
# Days number column
cg.insert(at=0x8bb6a1, d={"b":0x1a})
# 'Expenditure' column
cg.insert(at=0x8BB87B, d={"b":0x08})

# Battle statistics
# 'Statistics' column
cg.insert(at=0x8b9ff6, d={"b":0x0d})
# 'Days:' column
cg.insert(at=0x8ba007, d={"b":0x16})
# Defated 'Day:' column
cg.insert(at=0x8ba305, d={"b":0x16})
# Days number column
cg.insert(at=0x8ba023, d={"b":0x1a})
# Defeated day number column
cg.insert(at=0x8ba327, d={"b":0x1a})

# Deployed column
cg.insert(at=0x8BA6C8, d={"b":0x01})
# Destroyed column
cg.insert(at=0x8BA711, d={"b":0x01})

# Army logo x-pos
cg.insert(at=0x8bacba, d={"w":0x0010 - 2})
# D-Pad y-pos
cg.insert(at=0x8bace5, d={"w":0x00c9})


#-----------------------------------------------------------------------------
# Unit intel screen

# Help bar sprite positions
cg.insert(at=0x8B928F, d={"w":0x0047}) # "Select" icon x-position
cg.insert(at=0x8B9294, d={"w":0x0001}) # "Select" icon y-position
cg.insert(at=0x8B92AC, d={"w":0x0001}) # "A" icon y-position
cg.insert(at=0x8B92BF, d={"w":0x00C9}) # "B" icon x-position
cg.insert(at=0x8B92C4, d={"w":0x0001}) # "B" icon y-position
cg.insert(at=0x8B9264, d={"w":0x0020}) # "G" icon y-position

cg.insert(at=0x8B952A, d={"w":0x0048}) # "Unit type" selection marker x-position
cg.insert(at=0x8B945C, d={"w":0x005B}) # "Unit type" sort marker x-position


#-----------------------------------------------------------------------------
# Ally/rival select screen

# Change help bar sprite positions
cg.insert(at=0x8BE9CC, d={"b":0xca})


#-----------------------------------------------------------------------------
# Help Browser

# Change help bar sprite positions
cg.insert(at=0x918ABA, d={"w":0x0047}) # Base x-pos
cg.insert(at=0x918ABF, d={"w":0x00C9}) # Base y-pos
cg.insert(at=0x918AED, d={"w":0x0040}) # X-distanceset

# B-button y-offset += 1
cg.insert(at=0x918AF3, d={"asm":"""
  A16X16
  inc a
  sta.b $0D
  nop
  nop
  stz.b $13
"""})

# Help Browser icons
class ICON(object):
  Void   = 0x00
  Hammer = 0x01
  Wrench = 0x02
  CursrT = 0x03
  CursrR = 0x04
  CursrG = 0x05
  HQ     = 0x06
  Base   = 0x07
  City   = 0x08
  Airprt = 0x09
  Port   = 0x0a
  Depot  = 0x0b
  Lab    = 0x0c
  Gold   = 0x0d
  Income = 0x0e
  DPad   = 0x0f
  ButtnA = 0x10
  ButtnB = 0x11
  ButtnX = 0x12
  Select = 0x13
  Start  = 0x14
  WRange = 0x15
  HP     = 0x16
  Fuel   = 0x17
  Vision = 0x18
  Rounds = 0x19
  Wood   = 0x1a
  Plain  = 0x1b
  Mountn = 0x1c
  Rail   = 0x1d
  Road   = 0x1e
  Sea    = 0x1f
  Fort   = 0x20
  Shoal  = 0x21
  Bridge = 0x22
  River  = 0x23
  Lake   = 0x24
  Sky    = 0x25 # Sky?!
  Kanji1 = 0x26
  Cross  = 0x27
  Kanji2 = 0x28
  Kanji3 = 0x29
  ButtnL = 0x2a
  ButtnR = 0x2b
  Plus   = 0x2c
  ButtnY = 0x2d
  Inftry = 0x40
  Mech   = 0x41
  HvTank = 0x42
  MdTank = 0x43
  LtTank = 0x44
  Recon  = 0x45
  APC    = 0x46
  PrTank = 0x47
  Supply = 0x48
  Artly  = 0x49
  Rocket = 0x4a
  Train  = 0x4b
  AAGun  = 0x4c
  Vulcan = 0x4d
  Missil = 0x4e
  Fightr = 0x4f
  Bomber = 0x50
  Strikr = 0x51
  BCoptr = 0x52
  TCoptr = 0x53
  BShip  = 0x54
  Cruisr = 0x55
  Lander = 0x56
  Sub    = 0x57

# Icon list pointers
cg.insert(at=0x918B9E, d={"label_word":[
  "icons_a0",  "icons_a1",  "icons_a2",  "icons_a3",  "icons_a4",
  "icons_a5",  "icons_a6",  "icons_a7",  "icons_a8",  "icons_a9",
  "icons_a10", "icons_a11", "icons_a12", "icons_a13", "icons_a14",
  "icons_a15",
  "icons_b0",  "icons_b1",  "icons_b2",  "icons_b3",  "icons_b4",
  "icons_b5",  "icons_b6",  "icons_b7",  "icons_b8",  "icons_b9",
  "icons_b10", "icons_b11", "icons_b12", "icons_b13", "icons_b14",
  "icons_null",
  "icons_c0",  "icons_c1",  "icons_c2",  "icons_c3",  "icons_c4",
  "icons_c5",  "icons_c6",  "icons_c7",  "icons_c8",  "icons_c9",
  "icons_c10", "icons_c11", "icons_c12"
]})

sfw.icon_list("icons_null", 0x91, [])


# Page A0
sfw.icon_list("icons_a0", 0x91, [
  ICON.Mech,   0, 0x4b, 0x68,
  ICON.Missil, 0, 0xe0, 0x68,
  ICON.DPad,   0, 0x95, 0xa9
])

# Page A1
sfw.icon_list("icons_a1", 0x91, [
  # Empty
])

# Page A2
sfw.icon_list("icons_a2", 0x91, [
  ICON.HQ,     0, 0x90, 0x58,
  ICON.HQ,     0, 0x5c, 0xb8
])

# Page A3
sfw.icon_list("icons_a3", 0x91, [
  ICON.HQ,     0, 0x72, 0x58,
  ICON.ButtnA, 0, 0xb2, 0x5a,
  ICON.Wrench, 0, 0xa0, 0x69,
  ICON.CursrG, 0, 0x9f, 0x69,
  ICON.Gold,   0, 0xe1, 0x7a,
  ICON.Inftry, 0, 0x7c, 0xb8,
  ICON.Mech,   0, 0xb5, 0xb8
])

# Page A4
sfw.icon_list("icons_a4", 0x91, [
  ICON.Inftry, 0, 0x6f, 0x38,
  ICON.Mech,   0, 0x69, 0x48,
  ICON.ButtnX, 0, 0x59, 0x8a
])


# Page A5
sfw.icon_list("icons_a5", 0x91, [
  ICON.ButtnA, 0, 0x72, 0x3a,
  ICON.Inftry, 0, 0xc5, 0x68,
  ICON.Mech,   0, 0x6a, 0x78
])

# Page A6
sfw.icon_list("icons_a6", 0x91, [
  ICON.APC,    0, 0x7d, 0x57,
  ICON.Lander, 0, 0xbb, 0x59,
  ICON.TCoptr, 0, 0x7b, 0x69,
  ICON.Inftry, 0, 0x6f, 0x78,
  ICON.TCoptr, 0, 0xca, 0x79,
  ICON.TCoptr, 0, 0xe0, 0x99
])

# Page A7
sfw.icon_list("icons_a7", 0x91, [
  ICON.Inftry, 0, 0xbe, 0x38,
  ICON.Mech,   0, 0x64, 0x48,
  ICON.Inftry, 0, 0x7c, 0x98,
  ICON.Mech,   0, 0xb5, 0x98,
  ICON.HP,     0, 0x73, 0xa8
])

# Page A8
sfw.icon_list("icons_a8", 0x91, [
  ICON.ButtnX, 0, 0x94, 0x6a,
  ICON.Artly,  0, 0xc6, 0x88
])

# Page A9
sfw.icon_list("icons_a9", 0x91, [
  ICON.ButtnY, 0, 0x49, 0x4a,
  ICON.HP,     0, 0x8d, 0x48,
  ICON.ButtnL, 0, 0x46, 0x68,
  ICON.CursrR, 0, 0xda, 0x68,
  ICON.ButtnR, 0, 0x46, 0x88,
  ICON.CursrR, 0, 0xda, 0x88,
  ICON.HQ,     0, 0xd3, 0x78,
  ICON.ButtnL, 0, 0x46, 0xa8,
  ICON.Plus,   0, 0x57, 0xa9,
  ICON.ButtnR, 0, 0x5f, 0xa8,
  ICON.Plus,   0, 0x70, 0xa9,
  ICON.Select, 0, 0x7d, 0xaa,
  ICON.Plus,   0, 0x9b, 0xa9,
  ICON.Start,  0, 0xa8, 0xaa
])

# Page A10
sfw.icon_list("icons_a10", 0x91, [
  ICON.Vision, 0, 0x4a, 0x68,
  ICON.Inftry, 0, 0x6f, 0x98,
  ICON.Mech,   0, 0xae, 0x98,
  ICON.Mountn, 0, 0x4b, 0xb8
])

# Page A11
sfw.icon_list("icons_a11", 0x91, [
  ICON.Sub,    0, 0x9f, 0x79,
  ICON.Port,   0, 0xd1, 0xb8
])

# Page A12
sfw.icon_list("icons_a12", 0x91, [
  ICON.HQ,     0, 0xc0, 0x68
])

# Page A13
sfw.icon_list("icons_a13", 0x91, [
  # Empty
])

# Page A14
sfw.icon_list("icons_a14", 0x91, [
  ICON.HP,     0, 0x6f, 0xa8
])

# Page A15
sfw.icon_list("icons_a15", 0x91, [
  ICON.Vision, 0, 0x61, 0x98,
  ICON.Recon,  0, 0x49, 0xa8,
  ICON.Cruisr, 0, 0x95, 0xa9
])



# Page B0
sfw.icon_list("icons_b0", 0x91, [
  ICON.DPad,   0, 0x95, 0xa9
])

# Page B1
sfw.icon_list("icons_b1", 0x91, [
  ICON.ButtnA, 0, 0x64, 0x4a,
  ICON.HQ,     0, 0x4b, 0x78,
  ICON.Base,   0, 0x4b, 0x88,
  ICON.Airprt, 0, 0x4b, 0x98,
  ICON.Port,   0, 0x4b, 0xa8,
  ICON.Depot,  0, 0x4b, 0xb8,
  ICON.Train,  0, 0xb0, 0xb8
])

# Page B2
sfw.icon_list("icons_b2", 0x91, [
  # Empty
])

# Page B3
sfw.icon_list("icons_b3", 0x91, [
  ICON.Base,   0, 0xc9, 0x48,
  ICON.Airprt, 0, 0x71, 0x58,
  ICON.Port,   0, 0xa2, 0x58,
  ICON.Depot,  0, 0xe1, 0x58
])

# Page B4
sfw.icon_list("icons_b4", 0x91, [
  ICON.Select, 0, 0x60, 0x7a,
  ICON.HP,     0, 0xab, 0x88,
  ICON.Fuel,   0, 0xd6, 0x88,
  ICON.Rounds, 0, 0x64, 0x98,
  ICON.DPad,   0, 0x7b, 0xa9,
  ICON.ButtnA, 0, 0xac, 0xaa
])

# Page B5
sfw.icon_list("icons_b5", 0x91, [
  ICON.HP,     0, 0x99, 0x58,
  ICON.Fuel,   0, 0x4a, 0x68,
  ICON.Rounds, 0, 0x65, 0x68,
  ICON.HQ,     0, 0x4b, 0x88,
  ICON.Base,   0, 0x4b + 15 * 1, 0x88,
  ICON.City,   0, 0x4b + 15 * 2, 0x88,
  ICON.Lab,    0, 0x4b + 15 * 3, 0x88,
  ICON.Airprt, 0, 0x4b, 0x98,
  ICON.Port,   0, 0x4b, 0xa8,
  ICON.Depot,  0, 0x4b, 0xb8,
  ICON.Train,  0, 0xb0, 0xb8
])

# Page B6
sfw.icon_list("icons_b6", 0x91, [
  ICON.Gold,   0, 0x9d, 0x6a,
  ICON.HP,     0, 0x48, 0x88,
  ICON.Fuel,   0, 0x48, 0x98,
  ICON.Gold,   0, 0x6c, 0x9a,
  ICON.Rounds, 0, 0x48, 0xa8,
  ICON.ButtnX, 0, 0x65, 0xba
])

# Page B7
sfw.icon_list("icons_b7", 0x91, [
  ICON.Fuel,   0, 0xdb, 0x48,
  ICON.Rounds, 0, 0x54, 0x58,
  ICON.BCoptr, 0, 0x91, 0x69,
  ICON.TCoptr, 0, 0xa2, 0x69,
  ICON.BCoptr, 0, 0xa6, 0x79,
  ICON.TCoptr, 0, 0xb7, 0x79,
  ICON.Cruisr, 0, 0x8b, 0x89
])

# Page B8
sfw.icon_list("icons_b8", 0x91, [
  ICON.Gold,   0, 0x49, 0x7a,
  ICON.Income, 0, 0x49, 0x8a,
  ICON.DPad,   0, 0x5e, 0xb9,
])

# Page B9
sfw.icon_list("icons_b9", 0x91, [
  # Empty
])

# Page B10
sfw.icon_list("icons_b10", 0x91, [
  ICON.CursrR, 0, 0x97, 0x88,
  ICON.Hammer, 0, 0xd4, 0x83,
  ICON.CursrG, 0, 0xd4, 0x88,
  ICON.ButtnA, 0, 0xb7, 0xaa

])

# Page B11
sfw.icon_list("icons_b11", 0x91, [
  # Empty
])

# Page B12
sfw.icon_list("icons_b12", 0x91, [
  # Empty
])

# Page B13
sfw.icon_list("icons_b13", 0x91, [
  # Empty
])

# Page B14
sfw.icon_list("icons_b14", 0x91, [
  # Empty
])



# Page C0
sfw.icon_list("icons_c0", 0x91, [
  ICON.DPad,   0, 0x95, 0xa9
])

# Page C1
sfw.icon_list("icons_c1", 0x91, [
  ICON.WRange, 0, 0xa1, 0x78,
  ICON.WRange, 0, 0x98, 0x98,
  ICON.ButtnX, 0, 0x66, 0xba,
  ICON.WRange, 0, 0xd0, 0xb8
])

# Page C2
sfw.icon_list("icons_c2", 0x91, [
  # Empty
])

# Page C3
sfw.icon_list("icons_c3", 0x91, [
  ICON.HQ,     0, 0xcf, 0x98,
  ICON.Income, 0, 0x49, 0xba,
  ICON.Gold,   0, 0x80, 0xba
])

# Page C4
sfw.icon_list("icons_c4", 0x91, [
  ICON.Lab,    0, 0x7b, 0x78,
  ICON.PrTank, 0, 0xbe, 0x88,
  ICON.Lab,    0, 0xe8, 0x88,
  ICON.Gold,   0, 0xa4, 0x9a,
  ICON.PrTank, 0, 0x5c, 0xa8
])

# Page C5
sfw.icon_list("icons_c5", 0x91, [
  ICON.HP,     0, 0xc3, 0x78,
  ICON.Fuel,   0, 0xc2, 0x88,
  ICON.Rounds, 0, 0xde, 0x88,
  ICON.HP,     0, 0xcf, 0x98
])

# Page C6
sfw.icon_list("icons_c6", 0x91, [
  ICON.Supply, 0, 0x8a, 0x48,
  ICON.TCoptr, 0, 0x49, 0x69,
  ICON.BCoptr, 0, 0x5b, 0x69,
  ICON.Fuel,   0, 0x83, 0x68,
  ICON.Rounds, 0, 0x9e, 0x68,
  ICON.BCoptr, 0, 0x96, 0x98,
  ICON.Inftry, 0, 0x86, 0xa7,
  ICON.Supply, 0, 0x96, 0xa7,
  ICON.HvTank, 0, 0xa8, 0xa7,
  ICON.Train,  0, 0x96, 0xb8
])

# Page C7
sfw.icon_list("icons_c7", 0x91, [
  ICON.Fuel,   0, 0xb1, 0x38,
  ICON.Fuel,   0, 0x49, 0x78,
  ICON.Fuel,   0, 0xb7, 0x88,
  ICON.ButtnX, 0, 0x9d, 0x9a,
  ICON.Fuel,   0, 0x8e, 0xa8
])

# Page C8
sfw.icon_list("icons_c8", 0x91, [
  ICON.APC,    0, 0x49, 0x77,
  ICON.Inftry, 0, 0xa9, 0x77,
  ICON.Mech,   0, 0xca, 0x77,
  ICON.TCoptr, 0, 0x48, 0x88,
  ICON.Inftry, 0, 0xa9, 0x88,
  ICON.Mech,   0, 0xca, 0x88,
  ICON.Lander, 0, 0x48, 0x99,
  ICON.Cruisr, 0, 0x49, 0xa9,
  ICON.BCoptr, 0, 0xa9, 0xa9,
  ICON.TCoptr, 0, 0xca, 0xa9,
  ICON.Train,  0, 0x49, 0xb8
])

# Page C9
TCoptr_x = 0x8b
sfw.icon_list("icons_c9", 0x91, [
  ICON.APC,    0, 0x49, 0x77,
  ICON.APC,    0, 0x9a, 0x77,
  ICON.TCoptr, 0, 0x48, 0x88,
  ICON.Mountn, 0, TCoptr_x + 0 * 0x0f, 0x88,
  ICON.River,  0, TCoptr_x + 1 * 0x0f, 0x88,
  ICON.Wood,   0, TCoptr_x + 2 * 0x0f, 0x88,
  ICON.Sea,    0, TCoptr_x + 3 * 0x0f, 0x88,
  ICON.Lake,   0, TCoptr_x + 4 * 0x0f, 0x88,
  ICON.Shoal,  0, TCoptr_x + 2 + 6 * 0x0f, 0x88,
  ICON.Lander, 0, 0x48, 0x99,
  ICON.Shoal,  0, 0xb2, 0x98,
  ICON.Port,   0, 0xc1, 0x98,
  ICON.Cruisr, 0, 0x49, 0xa9,
  ICON.Cruisr, 0, 0x99, 0xa9,
  ICON.Train,  0, 0x49, 0xb8,
  ICON.Depot,  0, 0x8e, 0xb8
])

# Page C10
sfw.icon_list("icons_c10", 0x91, [
  ICON.HP,     0, 0x5d, 0x38,
  ICON.HP,     0, 0x82, 0x48
])

# Page C11
sfw.icon_list("icons_c11", 0x91, [
  # Empty
])

# Page C12
sfw.icon_list("icons_c12", 0x91, [
  # Empty
])
