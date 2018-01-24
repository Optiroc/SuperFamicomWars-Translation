#!/usr/bin/python
# -*- coding: utf-8 -*-

from _lib_ import cg, sfw

# TODO
#
# Make compressed files a dependency of graphics.s, and check filesizes
# for included files with a "max_size" key set.
# Also make available a "reloc_func" key, ie. a function that includes the
# data in a relocatable way if need be.

#-----------------------------------------------------------------------------
# Fonts & Icons

cg.insert(arr=[
  {"name":"VWF_font_ext",    "d":cg.incbin("data/font/vwf_font_ext_out.tiles")},
  {"name":"VWF_font_shift0", "d":cg.incbin("data/font/vwf_font_out.tiles")},
  {"name":"VWF_font_shift1", "d":cg.incbin("data/font/vwf_font_shift1_out.tiles")},
  {"name":"VWF_font_shift2", "d":cg.incbin("data/font/vwf_font_shift2_out.tiles")},
  {"name":"VWF_font_shift3", "d":cg.incbin("data/font/vwf_font_shift3_out.tiles")},
  {"name":"VWF_font_shift4", "d":cg.incbin("data/font/vwf_font_shift4_out.tiles")},
  {"name":"VWF_font_shift5", "d":cg.incbin("data/font/vwf_font_shift5_out.tiles")},
  {"name":"VWF_font_shift6", "d":cg.incbin("data/font/vwf_font_shift6_out.tiles")},
  {"name":"VWF_font_shift7", "d":cg.incbin("data/font/vwf_font_shift7_out.tiles")}
])

# Overwritten graphics (uncompressed or compressed at smaller size than original asset)
cg.insert(arr=[
  {"at":0x95b700, "name":"base_font",      "d":cg.incbin("data/font/font_base.tiles.lzn", max_size=8290)},
  {"at":0x959900, "name":"icons_main",     "d":cg.incbin("data/ui/icons_main.tiles")},
  {"at":0x8aba95, "name":"icons_unitinfo", "d":cg.incbin("data/ui/icons_unitinfo_extra.tiles")},
  {"at":0x8a945b, "name":"icons_g",        "d":cg.incbin("data/ui/icons_g.tiles")},
  {"at":0x90f100, "name":"speech_bubbles", "d":cg.incbin("data/ui/speech_bubbles.tiles")}
])

# Relocated icons/ui graphics
cg.insert(arr=[
  {"name":"add_font_mapselect", "d":cg.incbin("data/font/font_add_mapselect.tiles.lzn")},
  {"name":"icons_menu",         "d":cg.incbin("data/ui/icons_menu_extra.tiles.lzn")},
  {"name":"icons_statistics",   "d":cg.incbin("data/ui/icons_stats_extra.tiles.lzn")},
  {"name":"rival_config",       "d":cg.incbin("data/ui/rival_config.tiles.lzn")}
])

sfw.inject_setpointers([
  {"at": 0x8699fb, "ptr": 0x2f, "obj": "add_font_mapselect"}, # font additions at map screen
  {"at": 0x8ab33b, "ptr": 0x2f, "obj": "icons_menu"},         # ui sprites at main menu
  {"at": 0x8b84fa, "ptr": 0x2f, "obj": "icons_statistics"},   # ui sprites at unit screen
  {"at": 0x8b9a30, "ptr": 0x2f, "obj": "icons_statistics"},   # ui sprites at end-of-game statistics, page 2/3
  {"at": 0x8bb321, "ptr": 0x2f, "obj": "icons_statistics"},   # ui sprites at end-of-game statistics, page 1
  {"at": 0x8bcfb3, "ptr": 0x2f, "obj": "icons_statistics"},   # ?
  {"at": 0x918137, "ptr": 0x2f, "obj": "icons_statistics"},   # ?
  {"at": 0x8bcf8e, "ptr": 0x2f, "obj": "rival_config"},       # Diplomatic relations sprites
])


#-----------------------------------------------------------------------------
# Boot/intro graphics

cg.insert(arr=[
  {"name":"boot_logo",          "d":cg.incbin("data/title/boot.tiles.lzn")},
  {"name":"title_sprites1",     "d":cg.incbin("data/title/sprites1.tiles.lzn")},
  {"name":"title_sprites2",     "d":cg.incbin("data/title/sprites2.tiles")},
  {"name":"title_logo_tilemap", "d":cg.incbin("data/title/title_logo.tilemap.bin.lzn")}
])

sfw.inject_setpointers([
  {"at": 0x8ab43e, "ptr": 0x2f, "obj": "boot_logo"},
  {"at": 0x8e96ae, "ptr": 0x2f, "obj": "title_sprites1"},
  {"at": 0x8e9696, "ptr": 0x2f, "obj": "title_logo_tilemap"}
])

cg.nop_slide(0x8e96da, 4)                             # nop unpacking, replaced with uncompressed sprites
cg.insert(at=0x8e9765, d={"label":"title_sprites2"})  # source
cg.insert(at=0x8e9768, d={"w":0x0400})                # length

cg.insert(bank=0x8e, name="TITLE_oam_table1", d=sfw.oam_table([
  sfw.oam_entry(0x00, 0x00, 0x0c0, 7, 1, 0),
  sfw.oam_entry(0x10, 0x00, 0x0c2, 7, 1, 0),
  sfw.oam_entry(0x20, 0x00, 0x0c4, 7, 1, 0)
]))
cg.insert(bank=0x8e, name="TITLE_oam_table2", d=sfw.oam_table([
  sfw.oam_entry(0x00, 0x00, 0x0c6, 7, 1, 0),
  sfw.oam_entry(0x10, 0x00, 0x0c8, 7, 1, 0),
  sfw.oam_entry(0x20, 0x00, 0x0ca, 7, 1, 0),
  sfw.oam_entry(0x30, 0x00, 0x0cc, 7, 1, 0)
]))
cg.insert(bank=0x8e, name="TITLE_oam_table3", d=sfw.oam_table([
  sfw.oam_entry(0x00, 0x00, 0x0e0, 7, 1, 0),
  sfw.oam_entry(0x10, 0x00, 0x0e2, 7, 1, 0),
  sfw.oam_entry(0x20, 0x00, 0x0e4, 7, 1, 0)
]))

# Let's bounce!
def bounce(t, b, c, d):
  t = float(t) / float(d)
  if t < (1 / 2.75):
    return c * (7.5625 * t * t) + b;
  elif t < (2 / 2.75):
    t -= (1.5 / 2.75)
    return c * (7.5625 * t * t + 0.75) + b;
  elif t < (2.5 / 2.75):
    t -= (2.25 / 2.75)
    return c * (7.5625 * t * t + 0.9375) + b;
  else:
    t -= (2.625 / 2.75)
    return c * (7.5625 * t * t + 0.984375) + b;

bounce_apex = 0x1a
bounce_rest = 0x8e
bounce_length = 160
bounce_padding = 72
bounce_apex_index = int(bounce_length * 0.7)
bounce_table = []
for t in range (0,bounce_length):
  bounce_table.append(int(bounce(t, float(bounce_apex), float(bounce_rest - bounce_apex), bounce_length)) & 0xff)
trajectory = bounce_table[-bounce_apex_index::-1]
trajectory.extend(bounce_table)
trajectory.extend([bounce_rest] * bounce_padding)
trajectory.extend([0xff, 0xff])
trajectory.insert(0, 0x00)
trajectory.insert(0, bounce_length-bounce_apex_index)
cg.insert(name="TITLE_bounce_table", d={"b":trajectory})


#-----------------------------------------------------------------------------
# Start of day banner

# Graphics
cg.insert(at=0xae8409, name="day_banner_bg",      d=cg.incbin("data/day_banner/background.tiles.lzn", max_size=1053))
cg.insert(at=0xb3c5ca, name="day_banner_sprites", d=cg.incbin("data/day_banner/sprites.tiles.lzn",    max_size=438))

# Tilemap
cg.insert(name="day_banner_tilemap", d=cg.incbin("data/day_banner/tilemap.bin.lzn"))
cg.insert(at=0x89DCFF, d={"label":"day_banner_tilemap"})

# Day number x/y-coordinates
# Sprites are moved by a rather elaborate routine
# 89b419: b400 6f00 14 89 00 a4b4 0b 00f0 64b4 0b00 f06e b40d 22b4 78b4
#
# Offset
# 00 W Initial x-offset
# 02 W Initial y-offset
# 04 B Unknown lookup offset
# 05 B Unknown lookup offset
# 06 B Unknown lookup offset
# 07 W Unknown subroutine offset (possible routines (89)B4A4 (89)B4B3 (89)B4C2 (89)B4D1?)
# 09 B Movement type?

# Initial position
day_sprite_xoffs = 0x17F
day_sprite_xdist = 13
day_sprite_yoffs = 0x78


cg.insert(at=0x89b432, d={"w":day_sprite_xoffs})
cg.insert(at=0x89b419, d={"w":day_sprite_xoffs + day_sprite_xdist})
cg.insert(at=0x89b41b, d={"b":day_sprite_yoffs})
cg.insert(at=0x89b434, d={"b":day_sprite_yoffs})

# Speed curve
# Table at 89b464 controls tweened movement:
# 0000 80ff 0000 1000 1000 0000 8000 0000 f0ff 1000
# xs   ys   xa   ya             ys-  ya        pause

cg.insert(at=0x89B464, d={"w": [
  0x0750, # base x-speed
  0x0000, # base y-speed
  0x0000, #
  0x0000, #
  0x0020, # pause x-speed
  0x0080, # pause x-speed
  0x0000, #
  0x0000, #
  0x0000, #
  0x0042, # pause length
]})


#-----------------------------------------------------------------------------
# Game over graphics

# Compressed tiles at 89DD0E -> AE88E8 (length: 075F): 降伏 -> Surrendered
# Compressed tiles at 89DD17 -> AE90BB (length: 0745): 全滅 -> Annihilated
# Currently using the same graphic for both: "ARMY LOST"

cg.insert(at=0xae88e8, name="game_over_surrender",   d=cg.incbin("data/game_over/surrender.tiles.lzn",   max_size=1887))
cg.insert(at=0xae90bb, name="game_over_annihilated", d=cg.incbin("data/game_over/annihilated.tiles.lzn", max_size=1861))


#-----------------------------------------------------------------------------
# Alert box graphics
#
# Decrunching happens at 89A27B
# List of pointers at 89A398
#
# X   Ptr     Size  Translation
# 00  B5D9DC  00D8  (border graphics)
# 03  B5DAB4  0210  Destroyed!             ぜんめっ!!
# 06  B5DCC4  0225  Red Star Army
# 09  B5DEE9  0243  Blue Moon Army
# 0C  B5E12C  0289  Green Earth Army
# 0F  B5E3B5  0298  Yellow Comet Army
# 12  B5E64D  0280  Proto Tank             しんがたせんしゃ
# 15  B5E8CD  020A  Ambush!                そうぐう!! (Encounter in fog of war)
# 18  B5EAD7  02CC  Ambush!!               こうしゃそうぐう! (Encounter while dropping in fog of war)
# 1B  B5EDA3  02B4  HQ Captured!           しゅとせんりょう!
# 1E  B5F057  022B  Supply                 ぜんほきゅう
# 21  B5F282  0335  Domination!!           ゆうせいしょうり!!
# 24  B5F5B7  0284  Fuel Check             ガソリンチェック
# 27  B5F83B  017D  Acquired!              ゲット!!!
# 2A  B5F9B8  021A  Captured!              せんりょう！

cg.insert(arr=[
  {"at":0xb5dab4, "name":"alertbox_x03", "d":cg.incbin("data/alert_box/03_B5DAB4_destroyed.tiles.lzn",    max_size=528)},
  {"at":0xb5dcc4, "name":"alertbox_x06", "d":cg.incbin("data/alert_box/06_B5DCC4_red_star.tiles.lzn",     max_size=549)},
  {"at":0xb5dee9, "name":"alertbox_x09", "d":cg.incbin("data/alert_box/09_B5DEE9_blue_moon.tiles.lzn",    max_size=579)},
  {"at":0xb5e12c, "name":"alertbox_x0C", "d":cg.incbin("data/alert_box/0C_B5E12C_green_earth.tiles.lzn",  max_size=649)},
  {"at":0xb5e3b5, "name":"alertbox_x0F", "d":cg.incbin("data/alert_box/0F_B5E3B5_yellow_comet.tiles.lzn", max_size=664)},
  {"at":0xb5e64d, "name":"alertbox_x12", "d":cg.incbin("data/alert_box/12_B5E64D_proto_tank.tiles.lzn",   max_size=640)},
  {"at":0xb5e8cd, "name":"alertbox_x15", "d":cg.incbin("data/alert_box/15_B5E8CD_ambush.tiles.lzn",       max_size=522)},
  {"at":0xb5ead7, "name":"alertbox_x18", "d":cg.incbin("data/alert_box/18_B5EAD7_drop_ambush.tiles.lzn",  max_size=716)},
  {"at":0xb5eda3, "name":"alertbox_x1B", "d":cg.incbin("data/alert_box/1B_B5EDA3_hq_captured.tiles.lzn",  max_size=692)},
  {"at":0xb5f057, "name":"alertbox_x1e", "d":cg.incbin("data/alert_box/1E_B5F057_supply.tiles.lzn",       max_size=555)},
  {"at":0xb5f282, "name":"alertbox_x21", "d":cg.incbin("data/alert_box/21_B5F282_domination.tiles.lzn",   max_size=821)},
  {"at":0xb5f5b7, "name":"alertbox_x24", "d":cg.incbin("data/alert_box/24_B5F5B7_fuel_check.tiles.lzn",   max_size=644)},
 #{"at":0xb5f83b, "name":"alertbox_x27", "d":cg.incbin("data/alert_box/27_B5F83B_acquired.tiles.lzn",     max_size=381)}, # Too big, relocate!
  {"at":0xb5f9b8, "name":"alertbox_x2A", "d":cg.incbin("data/alert_box/2A_B5F9B8_captured.tiles.lzn",     max_size=538)}

])

# Relocated alert box graphics
cg.insert(arr=[
  {"name":"alertbox_x27",  "d":cg.incbin("data/alert_box/27_B5F83B_acquired.tiles.lzn")},
  {"at":0x89a398 + 3 * 13, "d":{"label":"alertbox_x27"}}
])


#-----------------------------------------------------------------------------
# Game Over / Staff Roll graphics

cg.insert(arr=[
  {"name":"end_2bpp",    "d":cg.incbin("data/staff_roll/end.2bpp.tiles.lzn")},
  {"name":"end_4bpp",    "d":cg.incbin("data/staff_roll/end.4bpp.tiles.lzn")},
  {"name":"end_tilemap", "d":cg.incbin("data/staff_roll/end.tilemap.bin.lzn")}
])
sfw.inject_setpointers([
  {"at": 0x8e8453, "ptr": 0x2f, "obj": "end_2bpp"},
  {"at": 0x8e9c17, "ptr": 0x2f, "obj": "end_4bpp"},
  {"at": 0x8e9c2f, "ptr": 0x2f, "obj": "end_tilemap"}
])

# Staff Roll
#
# Ix  Ptr     Size  Translation
# 00  9E8694  01DD  Staff
# 01  9DEABA  01E7  Producer: Takehiro Izushi
# 02  9DE689  0214  Game Design: Shouzou Kaga
# 03  9DE89D  021D  Director: Tohru Narihiro
# 04  9DECA1  0287  System Program: Takafumi Kaneko
# 05  9DEF28  0211  Anime Program: Takanori Hino
# 06  9DF139  022E  Layout Program: Motomu Chikaraishi
# 07  9DF367  023F  Graphic Design: Masahiro Higuchi
# 08  9E8467  022D  Map Design: Chikara Yamamoto
# 09  9DF5A6  0214  Sound: Kenichi Nishimaki
# 0A  9E8871  01D6  Sound Assist: Yuka Tsujiyoko
# 0B  9E8A47  021C  Sound Assist: Atsuko Yamamoto
# 0C  9DFD73  02B3  Program Assist: Ryuichiro Koguchi
# 0D  9DF7BA  01E5  Graphic Assist: Sachiko Wada
# 0E  9DF99F  01EA  Graphic Assist: Sumiko Miki
# 0F  9DFB89  01EA  Graphic Assist: Ryou Hirata
# 10  9E8026  01F1  Graphic Assist: Maki Takemori
# 11  9E8217  0250  Graphic Assist: Junko Umehara
# 12  9E8C63  0223  Special Thanks: Takashi Kawaguchi
# 13  9E8E86  0254  Special Thanks: Yasuo Inoue
# 14  9E90DA  01FF  Special Thanks: Kohta Fukui
# 15  9E92D9  024C  Special Thanks: Super Mario Club

# Change to:
# 12  9E8C63  0223  Localization: David Lindecrantz
# 13  9E8E86  0254  Localization: Anders Lindqvist, Lee Hyde
# 14  9E90DA  01FF  Special Thanks: Takashi Kawaguchi, Yasuo Inoue
# 15  9E92D9  024C  Special Thanks: Kohta Fukui, Super Mario Club

# Category row scroll in/out flags
cg.insert(at=0x8e8a50, name="staffroll_flags1", d={"b": [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1] })
cg.insert(at=0x8e8a66, name="staffroll_flags2", d={"b": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0] })

# Relocated staff roll graphics
cg.insert(arr=[
  {"name":"staff_roll_i00", "d":cg.incbin("data/staff_roll/00_8E8AEA_9E8694.tiles.lzn")},
  {"name":"staff_roll_i01", "d":cg.incbin("data/staff_roll/01_8E8AED_9DEABA.tiles.lzn")},
  {"name":"staff_roll_i02", "d":cg.incbin("data/staff_roll/02_8E8AF0_9DE689.tiles.lzn")},
  {"name":"staff_roll_i03", "d":cg.incbin("data/staff_roll/03_8E8AF3_9DE89D.tiles.lzn")},
  {"name":"staff_roll_i04", "d":cg.incbin("data/staff_roll/04_8E8AF6_9DECA1.tiles.lzn")},
  {"name":"staff_roll_i05", "d":cg.incbin("data/staff_roll/05_8E8AF9_9DEF28.tiles.lzn")},
  {"name":"staff_roll_i06", "d":cg.incbin("data/staff_roll/06_8E8AFC_9DF139.tiles.lzn")},
  {"name":"staff_roll_i07", "d":cg.incbin("data/staff_roll/07_8E8AFF_9DF367.tiles.lzn")},
  {"name":"staff_roll_i08", "d":cg.incbin("data/staff_roll/08_8E8B02_9E8467.tiles.lzn")},
  {"name":"staff_roll_i09", "d":cg.incbin("data/staff_roll/09_8E8B05_9DF5A6.tiles.lzn")},
  {"name":"staff_roll_i0A", "d":cg.incbin("data/staff_roll/0A_8E8B08_9E8871.tiles.lzn")},
  {"name":"staff_roll_i0B", "d":cg.incbin("data/staff_roll/0B_8E8B0B_9E8A47.tiles.lzn")},
  {"name":"staff_roll_i0C", "d":cg.incbin("data/staff_roll/0C_8E8B0E_9DFD73.tiles.lzn")},
  {"name":"staff_roll_i0D", "d":cg.incbin("data/staff_roll/0D_8E8B11_9DF7BA.tiles.lzn")},
  {"name":"staff_roll_i0E", "d":cg.incbin("data/staff_roll/0E_8E8B14_9DF99F.tiles.lzn")},
  {"name":"staff_roll_i0F", "d":cg.incbin("data/staff_roll/0F_8E8B17_9DFB89.tiles.lzn")},
  {"name":"staff_roll_i10", "d":cg.incbin("data/staff_roll/10_8E8B1A_9E8026.tiles.lzn")},
  {"name":"staff_roll_i11", "d":cg.incbin("data/staff_roll/11_8E8B1D_9E8217.tiles.lzn")},
  {"name":"staff_roll_i12", "d":cg.incbin("data/staff_roll/12_8E8B20_9E8C63.tiles.lzn")},
  {"name":"staff_roll_i13", "d":cg.incbin("data/staff_roll/13_8E8B23_9E8E86.tiles.lzn")},
  {"name":"staff_roll_i14", "d":cg.incbin("data/staff_roll/14_8E8B26_9E90DA.tiles.lzn")},
  {"name":"staff_roll_i15", "d":cg.incbin("data/staff_roll/15_8E8B29_9E92D9.tiles.lzn")}
])

cg.insert(at=0x8e8aea, d={"label":[
  "staff_roll_i00", "staff_roll_i01", "staff_roll_i02", "staff_roll_i03",
  "staff_roll_i04", "staff_roll_i05", "staff_roll_i06", "staff_roll_i07",
  "staff_roll_i08", "staff_roll_i09", "staff_roll_i0A", "staff_roll_i0B",
  "staff_roll_i0C", "staff_roll_i0D", "staff_roll_i0E", "staff_roll_i0F",
  "staff_roll_i10", "staff_roll_i11", "staff_roll_i12", "staff_roll_i13",
  "staff_roll_i14", "staff_roll_i15"
]})
