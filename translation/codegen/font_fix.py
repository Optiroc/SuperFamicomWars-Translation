#!/usr/bin/python
# -*- coding: utf-8 -*-

from _lib_ import cg

# These patches modify tile indices/attributes for the purged BG3 base font

empty_char = 0x005f

#-----------------------------------------------------------------------------
# Patch TXT_print_number

print_number_char_offset   = 0x0000
print_number_basechar      = 0x2000

# Patch base character offsets in TXT_print_number
cg.insert(at=0x879D11, d={"w":print_number_char_offset})
cg.insert(at=0x879D3B, d={"w":print_number_char_offset})
cg.insert(at=0x879D86, d={"w":print_number_char_offset})
cg.insert(at=0x879DD2, d={"w":print_number_char_offset})

# Patch base character offsets in TXT_print_number_uint24
cg.insert(at=0x87C7A2, d={"w":print_number_char_offset})
cg.insert(at=0x87C7AF, d={"w":print_number_char_offset + 0x10})

# Patch base character for TXT_print_number in load game selector
cg.insert(at=0x87F275, d={"w":print_number_char_offset})
cg.insert(at=0x87F28F, d={"w":print_number_char_offset})

# Patch base character for TXT_print_number in map select
cg.insert(at=0x87F945, d={"w":print_number_basechar})
cg.insert(at=0x87FAFA, d={"w":print_number_basechar})

# Patch base character for TXT_print_number in unit info
cg.insert(at=0x8B87DE, d={"w":print_number_basechar})
cg.insert(at=0x8B8806, d={"w":print_number_basechar})
cg.insert(at=0x8B88D2, d={"w":print_number_basechar})
cg.insert(at=0x8B8929, d={"w":print_number_basechar})
cg.insert(at=0x8B89AB, d={"w":print_number_basechar})
cg.insert(at=0x8B89F0, d={"w":print_number_basechar})
cg.insert(at=0x8B8A22, d={"w":print_number_basechar})

# Patch base character for TXT_print_number in quick battle screen
cg.insert(at=0x87C19E, d={"w":print_number_basechar})
cg.insert(at=0x87C1BD, d={"w":print_number_basechar})
cg.insert(at=0x87C231, d={"w":print_number_basechar})
cg.insert(at=0x87C261, d={"w":print_number_basechar})


#-----------------------------------------------------------------------------
# Patch TXT_print_small_number/stat functions

print_small_number_chardist   = 0x0010
print_small_stat_basechar     = 0x2020
print_small_stat_dashchar     = 0x001D
print_small_stat_unitdmg_attr = 0x0800

# Charset distance between "low" and "high" number tiles
cg.insert(at=0x879A9F, d={"w":print_small_number_chardist})

# Patch charset base character for TXT_print_small_stat
cg.insert(at=0x87BD32, d={"w":print_small_stat_basechar})

# Patch null/dash character for TXT_print_small_stat
cg.insert(at=0x87BD3F, d={"w":(print_small_stat_basechar + print_small_stat_dashchar)})

# Patch charset base character/attr for TXT_print_small_stat_unitdmg
cg.insert(at=0x8A84F7, d={"w":(print_small_stat_basechar | print_small_stat_unitdmg_attr)})

# Patch null/dash character for TXT_print_small_stat_unitdmg
cg.insert(at=0x8A8504, d={"w":((print_small_stat_basechar + print_small_stat_dashchar) | print_small_stat_unitdmg_attr)})

# Patch charset base character/attr for TXT_print_small_stat_movecost
cg.insert(at=0x8A8515, d={"w":print_small_stat_basechar})

# Patch dash character for TXT_print_small_stat_movecost
cg.insert(at=0x8A8522, d={"w":(print_small_stat_basechar + print_small_stat_dashchar)})

# Patch character table used in unit HP fullscreen overlay
print_overlay_stat_basechar = 0x22C0
print_overlay_stat_t_char   = print_overlay_stat_basechar + 12
cg.insert(at=0x858db8, d={"w":[
  # Used at 858d78
  # 0x00 - 0x0a -> 0 - 10
  empty_char, print_overlay_stat_basechar + 0,
  empty_char, print_overlay_stat_basechar + 1,
  empty_char, print_overlay_stat_basechar + 2,
  empty_char, print_overlay_stat_basechar + 3,
  empty_char, print_overlay_stat_basechar + 4,
  empty_char, print_overlay_stat_basechar + 5,
  empty_char, print_overlay_stat_basechar + 6,
  empty_char, print_overlay_stat_basechar + 7,
  empty_char, print_overlay_stat_basechar + 8,
  empty_char, print_overlay_stat_basechar + 9,
  print_overlay_stat_basechar + 10, print_overlay_stat_basechar + 11,
  # 0x0b - 0x15 -> T0 - T10
  print_overlay_stat_t_char, print_overlay_stat_basechar + 0,
  print_overlay_stat_t_char, print_overlay_stat_basechar + 1,
  print_overlay_stat_t_char, print_overlay_stat_basechar + 2,
  print_overlay_stat_t_char, print_overlay_stat_basechar + 3,
  print_overlay_stat_t_char, print_overlay_stat_basechar + 15,
  print_overlay_stat_t_char, print_overlay_stat_basechar + 5,
  print_overlay_stat_t_char, print_overlay_stat_basechar + 6,
  print_overlay_stat_t_char, print_overlay_stat_basechar + 7,
  print_overlay_stat_t_char, print_overlay_stat_basechar + 8,
  print_overlay_stat_t_char, print_overlay_stat_basechar + 9,
  print_overlay_stat_t_char + 1, print_overlay_stat_t_char + 2
]})

# Patch base character for small numbers in battle results
cg.insert(at=0x8BA9B5, d={"w":print_small_stat_basechar})
cg.insert(at=0x8BA8A6, d={"w":print_small_number_chardist})
cg.insert(at=0x8BA94B, d={"w":print_small_number_chardist})


#-----------------------------------------------------------------------------
# Patch shadow tile indices for most windows

shadow_def_addr = 0x8A8392
shadow_tilebase = 0x4E

cg.insert(at=shadow_def_addr + 0x06, d={"b":shadow_tilebase + 0x00}) # top-right
cg.insert(at=shadow_def_addr + 0x0c, d={"b":shadow_tilebase + 0x10}) # right
cg.insert(at=shadow_def_addr + 0x14, d={"b":shadow_tilebase + 0x00}) # bottom-left
cg.insert(at=shadow_def_addr + 0x16, d={"b":shadow_tilebase + 0x01}) # bottom
cg.insert(at=shadow_def_addr + 0x18, d={"b":shadow_tilebase + 0x00}) # bottom-right


#-----------------------------------------------------------------------------
# Patch border definition for UX_draw_map_infobox_terrain

map_infobox_borderdef_attr = 0x3000
map_infobox_borderdef_base = map_infobox_borderdef_attr + 0x4C

cg.insert(at=0x8A8363, d={"w":[
  (map_infobox_borderdef_base + 0x11) | 0x0000, # top-left corner
  (map_infobox_borderdef_base + 0x00) | 0x0000, # top border
  (map_infobox_borderdef_base + 0x11) | 0x4000, # top-right corner
  (map_infobox_borderdef_base + 0x02) | 0x8000, # top-right shadow
  (map_infobox_borderdef_base + 0x01) | 0x0000, # left border
  (map_infobox_borderdef_base + 0x01) | 0x4000, # right border
  (map_infobox_borderdef_base + 0x12) | 0x0000, # right shadow
  (map_infobox_borderdef_base + 0x11) | 0x8000, # bottom-left corner
  (map_infobox_borderdef_base + 0x00) | 0x8000, # bottom border
  (map_infobox_borderdef_base + 0x11) | 0xC000, # bottom-right corner
  (map_infobox_borderdef_base + 0x02) | 0x4000, # bottom-left shadow
  (map_infobox_borderdef_base + 0x03) | 0x0000, # bottom shadow
  (map_infobox_borderdef_base + 0x02) | 0x0000  # bottom-right shadow
]})

#-----------------------------------------------------------------------------
# Patch tile number for "range overlay" in UX_MOVE_draw_overlay

move_overlay_attr = 0x3C00
move_overlay_char = 0x5C

cg.insert(at=0x83C16A, d={"w":move_overlay_attr | move_overlay_char}) # main fill
cg.insert(at=0x83E7CC, d={"w":move_overlay_attr | move_overlay_char}) # add fills
cg.insert(at=0x83E88D, d={"w":move_overlay_attr | move_overlay_char})
