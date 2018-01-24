# Flags and convenience functions
2bpp_flags := --mode snes --bpp 2 --no-remap --no-flip --no-discard -v
4bpp_flags := --mode snes --bpp 4 --no-remap --no-flip --no-discard -v

define add_2bpp_tiles
derived_files += $(patsubst %.png,%.tiles,$(1))
$(patsubst %.png,%.tiles,$(1)): $(1)
	$(sfconv) tiles $(2bpp_flags) --in-image $(1) --out-data $(patsubst %.png,%.tiles,$(1))
endef

define add_compressed_2bpp_tiles
derived_files += $(patsubst %.png,%.tiles,$(1)) $(patsubst %.png,%.tiles.lzn,$(1))
$(patsubst %.png,%.tiles,$(1)): $(1)
	$(sfconv) tiles $(2bpp_flags) --in-image $(1) --out-data $(patsubst %.png,%.tiles,$(1))
endef

define add_4bpp_tiles
derived_files += $(patsubst %.png,%.tiles,$(1))
$(patsubst %.png,%.tiles,$(1)): $(1)
	$(sfconv) tiles $(4bpp_flags) --in-image $(1) --out-data $(patsubst %.png,%.tiles,$(1))
endef

define add_compressed_4bpp_tiles
derived_files += $(patsubst %.png,%.tiles,$(1)) $(patsubst %.png,%.tiles.lzn,$(1))
$(patsubst %.png,%.tiles,$(1)): $(1)
	$(sfconv) tiles $(4bpp_flags) --in-image $(1) --out-data $(patsubst %.png,%.tiles,$(1))
endef

# Font
$(eval $(call add_compressed_2bpp_tiles,data/font/font_base.png))
$(eval $(call add_compressed_2bpp_tiles,data/font/font_add_mapselect.png))

# Variable width fonts
$(eval $(call add_2bpp_tiles,$(vwf_out)))
$(eval $(call add_2bpp_tiles,$(vwf_out_ext)))
$(foreach out,$(vwf_out_shift),$(eval $(call add_2bpp_tiles,$(out))))

# Titles
$(eval $(call add_compressed_4bpp_tiles,data/title/boot.png))
$(eval $(call add_compressed_4bpp_tiles,data/title/sprites1.png))
$(eval $(call add_4bpp_tiles,data/title/sprites2.png))
derived_files += data/title/title_logo.tilemap.bin.lzn

# UI sprites
$(eval $(call add_4bpp_tiles,data/ui/icons_main.png))
$(eval $(call add_4bpp_tiles,data/ui/icons_unitinfo_extra.png))
$(eval $(call add_4bpp_tiles,data/ui/icons_g.png))
$(eval $(call add_4bpp_tiles,data/ui/speech_bubbles.png))
$(eval $(call add_compressed_4bpp_tiles,data/ui/icons_menu_extra.png))
$(eval $(call add_compressed_4bpp_tiles,data/ui/icons_stats_extra.png))
$(eval $(call add_compressed_4bpp_tiles,data/ui/rival_config.png))

# Alert Box sprites
$(eval $(call add_compressed_4bpp_tiles,data/alert_box/03_B5DAB4_destroyed.png))
$(eval $(call add_compressed_4bpp_tiles,data/alert_box/06_B5DCC4_red_star.png))
$(eval $(call add_compressed_4bpp_tiles,data/alert_box/09_B5DEE9_blue_moon.png))
$(eval $(call add_compressed_4bpp_tiles,data/alert_box/0C_B5E12C_green_earth.png))
$(eval $(call add_compressed_4bpp_tiles,data/alert_box/0F_B5E3B5_yellow_comet.png))
$(eval $(call add_compressed_4bpp_tiles,data/alert_box/12_B5E64D_proto_tank.png))
$(eval $(call add_compressed_4bpp_tiles,data/alert_box/15_B5E8CD_ambush.png))
$(eval $(call add_compressed_4bpp_tiles,data/alert_box/18_B5EAD7_drop_ambush.png))
$(eval $(call add_compressed_4bpp_tiles,data/alert_box/1B_B5EDA3_hq_captured.png))
$(eval $(call add_compressed_4bpp_tiles,data/alert_box/1E_B5F057_supply.png))
$(eval $(call add_compressed_4bpp_tiles,data/alert_box/21_B5F282_domination.png))
$(eval $(call add_compressed_4bpp_tiles,data/alert_box/24_B5F5B7_fuel_check.png))
$(eval $(call add_compressed_4bpp_tiles,data/alert_box/27_B5F83B_acquired.png))
$(eval $(call add_compressed_4bpp_tiles,data/alert_box/2A_B5F9B8_captured.png))

# Day Banner
$(eval $(call add_compressed_4bpp_tiles,data/day_banner/background.png))
$(eval $(call add_compressed_4bpp_tiles,data/day_banner/sprites.png))
derived_files += data/day_banner/tilemap.bin.lzn

# Game Over
$(eval $(call add_compressed_4bpp_tiles,data/game_over/surrender.png))
$(eval $(call add_compressed_4bpp_tiles,data/game_over/annihilated.png))

# Staff Roll
$(eval $(call add_compressed_2bpp_tiles,data/staff_roll/end.2bpp.png))
$(eval $(call add_compressed_4bpp_tiles,data/staff_roll/end.4bpp.png))
derived_files += data/staff_roll/end.tilemap.bin.lzn

$(eval $(call add_compressed_2bpp_tiles,data/staff_roll/00_8E8AEA_9E8694.png))
$(eval $(call add_compressed_2bpp_tiles,data/staff_roll/01_8E8AED_9DEABA.png))
$(eval $(call add_compressed_2bpp_tiles,data/staff_roll/02_8E8AF0_9DE689.png))
$(eval $(call add_compressed_2bpp_tiles,data/staff_roll/03_8E8AF3_9DE89D.png))
$(eval $(call add_compressed_2bpp_tiles,data/staff_roll/04_8E8AF6_9DECA1.png))
$(eval $(call add_compressed_2bpp_tiles,data/staff_roll/05_8E8AF9_9DEF28.png))
$(eval $(call add_compressed_2bpp_tiles,data/staff_roll/06_8E8AFC_9DF139.png))
$(eval $(call add_compressed_2bpp_tiles,data/staff_roll/07_8E8AFF_9DF367.png))
$(eval $(call add_compressed_2bpp_tiles,data/staff_roll/08_8E8B02_9E8467.png))
$(eval $(call add_compressed_2bpp_tiles,data/staff_roll/09_8E8B05_9DF5A6.png))
$(eval $(call add_compressed_2bpp_tiles,data/staff_roll/0A_8E8B08_9E8871.png))
$(eval $(call add_compressed_2bpp_tiles,data/staff_roll/0B_8E8B0B_9E8A47.png))
$(eval $(call add_compressed_2bpp_tiles,data/staff_roll/0C_8E8B0E_9DFD73.png))
$(eval $(call add_compressed_2bpp_tiles,data/staff_roll/0D_8E8B11_9DF7BA.png))
$(eval $(call add_compressed_2bpp_tiles,data/staff_roll/0E_8E8B14_9DF99F.png))
$(eval $(call add_compressed_2bpp_tiles,data/staff_roll/0F_8E8B17_9DFB89.png))
$(eval $(call add_compressed_2bpp_tiles,data/staff_roll/10_8E8B1A_9E8026.png))
$(eval $(call add_compressed_2bpp_tiles,data/staff_roll/11_8E8B1D_9E8217.png))
$(eval $(call add_compressed_2bpp_tiles,data/staff_roll/12_8E8B20_9E8C63.png))
$(eval $(call add_compressed_2bpp_tiles,data/staff_roll/13_8E8B23_9E8E86.png))
$(eval $(call add_compressed_2bpp_tiles,data/staff_roll/14_8E8B26_9E90DA.png))
$(eval $(call add_compressed_2bpp_tiles,data/staff_roll/15_8E8B29_9E92D9.png))
