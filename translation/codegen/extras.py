#!/usr/bin/python
# -*- coding: utf-8 -*-

from _lib_ import cg

#-----------------------------------------------------------------------------
# Quality of Life

# Key repeat delay
# Written to $E0 during scene init, default 0x10
cg.insert(at=0x80A53E, d={"w":0x000e}) # In-game wait period

# Key repeat speed
# Written to $E2 during scene init, default 0x04
# Special case made for deploy unit menu in src/quality_of_life.s
cg.insert(at=0x80a8d0, d={"w":0x0002}) # Load/options repeat speed
cg.insert(at=0x8b80d1, d={"w":0x0003}) # Units overview repeat speed
cg.insert(at=0x92e2a1, d={"w":0x0002}) # Sound Park repeat speed

# Change default choice in Retreat dialogue
cg.insert(at=0x87f62d, d={"l":0x87f618})
cg.insert(at=0x87f632, d={"l":0x87f60b})

# Unit damage stat max printed number
print_unitdmg_max = 199
cg.insert(at=0x83D8DC, d={"b":print_unitdmg_max+1})
cg.insert(at=0x83D8E0, d={"b":print_unitdmg_max+1})
cg.insert(at=0x8AC838, d={"w":print_unitdmg_max+1})
cg.insert(at=0x8AC83F, d={"w":print_unitdmg_max})
cg.insert(at=0x8AC7FD, d={"label":"TXT_print_small_stat199_main_dmg"})
cg.insert(at=0x8AC80D, d={"label":"TXT_print_small_stat199_sub_dmg"})
cg.insert(at=0x8AC81D, d={"label":"TXT_print_small_stat199_main_dmg"})
cg.insert(at=0x8AC82D, d={"label":"TXT_print_small_stat199_sub_dmg"})
# Fixed damage stats OAM color (bpl -> bcs because of underflow with >127 values)
cg.insert(at=0x8ACBF2, d={"b":0xb0})


#-----------------------------------------------------------------------------
# Secret stuff

# Enable "CO" debug menu (cli -> sec)
# - Currently a black screen, need to patch some number/char printing functions
#   for it to work in conjunction with patched text rendering system...
# TODO:
# - Regenerate source with CP menu excercised! Code around 869033
cg.insert(at=0x87C9DA, d={"b":0x38})

# Enable SOUND PARK secret code without appropriate SRAM condition
# (up, down, left, right, up, a)
cg.nop_slide(0x92E04C, 9)


#-----------------------------------------------------------------------------
# Cheats

# Free units
#cg.nop_slide(0x83A641, 2)

# Skip save game validation
# Use only when fooling around with the Units arrays!
#cg.nop_slide(0x85aa7a, 2)
