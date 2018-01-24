.SUFFIXES:
.PHONY: clean all toolchain run patch

# Base ROM input
base_rom	:= "../rom/Super Famicom Wars (Japan) (NP).sfc"

# Output
name 		:= mb-sfwe
rom		:= ../rom/$(name).sfc
patch_vcdiff	:= ../rom/$(name).vcdiff
patch_bps	:= ../rom/$(name).bps
patch_ips	:= ../rom/$(name).ips
build_dir	:= build

# Source
inc		:= include/header.i include/macros.i include/registers.i
src		:= src/globals.s src/init.s src/dma_system.s src/string_decoder.s src/print_stat.s src/quality_of_life.s src/title_screen.s
codegen_dir	:= codegen
codegen_src	:= free.s graphics.s font_fix.s layout.s extras.s

# Tools
tools_dir	:= ../tools
py_lib		:= ../common/py_lib
wla		:= $(tools_dir)/wla-dx/binaries/wla-65816
wlalink		:= $(tools_dir)/wla-dx/binaries/wlalink
sfcheck		:= $(tools_dir)/superfamicheck/bin/superfamicheck
sfconv		:= $(tools_dir)/superfamiconv/bin/superfamiconv
lzn		:= $(tools_dir)/lzn/lzn.py
flips		:= $(tools_dir)/flips/flips

# Variable width fonts
vwf_pp		:= $(tools_dir)/vwf/vwf_preprocess.py
vwf_org		:= data/font/vwf_font.png
vwf_out		:= data/font/vwf_font_out.png
vwf_shifts	:= 1 2 3 4 5 6 7
vwf_out_shift	:= $(foreach i,$(vwf_shifts),data/font/vwf_font_shift$(i)_out.png)
vwf_widths	:= $(build_dir)/vwf_widths.s
vwf_zlines	:= $(build_dir)/vwf_zlines.s
vwf_org_ext	:= data/font/vwf_font_ext.png
vwf_out_ext	:= data/font/vwf_font_ext_out.png
vwf_widths_ext	:= $(build_dir)/vwf_widths_ext.s

# Files
cfg_files	:= Makefile data.make $(vwf_pp) $(codegen_dir)/_data_.py $(codegen_dir)/_lib_.py $(py_lib)/codegen.py $(py_lib)/util.py $(py_lib)/sfw.py $(py_lib)/pxbuf.py $(py_lib)/vwf.py $(py_lib)/kerning.py
str_files	+= data/strings/game.py data/strings/options.py data/strings/maps.py data/strings/units.py data/strings/terrain.py data/strings/help.py data/strings/soundpark.py
link_file	:= $(build_dir)/linkfile
src_gen_out	:= $(addprefix $(build_dir)/,$(codegen_src))
str_gen_out	:= $(build_dir)/strings.s
src_gen_data	:= $(vwf_widths) $(vwf_zlines) $(vwf_widths_ext)
src_all		:= $(build_dir)/all.s
obj_all		:= $(build_dir)/all.o


# Rules
default: $(rom)

all: clean toolchain default

toolchain:
	@$(MAKE) -C .. toolchain

patch: $(patch_vcdiff) $(patch_bps) #$(patch_ips)


# Data
derived_files	:=
include data.make

# Main rules
$(derived_files): $(cfg_files)

$(patch_vcdiff): $(rom)
	xdelta3 -f -s $(base_rom) $< $@

$(patch_bps): $(rom)
	$(flips) --create --bps-delta $(base_rom) $< $@

$(patch_ips): $(rom)
	$(flips) --create --ips $(base_rom) $< $@

$(rom): $(obj) $(cfg_files) $(link_file)
	$(wlalink) -S $(link_file) $@
	@mv .sym $(basename $(@)).cpu.sym
	@cat $(basename $(@)).cpu.sym
	$(sfcheck) $@

$(src_all): $(inc) $(src) $(src_gen_data) $(src_gen_out) $(str_gen_out) $(cfg_files)
	$(info Concatenating source files: [${inc} ${src} $(str_gen_out) ${src_gen_out}])
	$(shell cat $(inc) $(str_gen_out) $(src_gen_data) $(src_gen_out) $(src) >$(src_all))

$(obj_all): $(src_all) $(derived_files) $(cfg_files)
	$(wla) -o $@ $<

$(link_file): $(obj_all)
	$(shell echo "[objects]" >$(link_file))
	$(foreach o, $(obj_all), $(shell echo "$(o)" >>$(link_file)))

run: $(rom)
	open -a ~/Game/bsnes/bsnes+.app --args $(realpath $(rom)) --show-debugger --break-on-wdm


all: clean patch

clean:
	rm -f $(rom) $(basename $(rom)).sym $(src_all) $(obj_all) $(src_gen_data) $(src_gen_out) $(str_gen_out) $(link_file) $(derived_files) $(vwf_out) $(vwf_out_shift) $(vwf_out_ext) $(patch_vcdiff) $(patch_bps) $(patch_ips)


# Generate VWF data
$(vwf_out): $(vwf_pp) $(vwf_org) $(cfg_files)
	$(vwf_pp) --in_png $(vwf_org) --out_png $(vwf_out)

$(filter data/font/vwf_font_shift%_out.png,$(vwf_out_shift)): data/font/vwf_font_shift%_out.png : $(vwf_pp) $(vwf_org) $(cfg_files)
	$(vwf_pp) --preshift $* --in_png $(vwf_org) --out_png $@

$(vwf_widths): $(vwf_pp) $(vwf_org) $(cfg_files)
	$(vwf_pp) --in_png $(vwf_org) --widths >$@

$(vwf_zlines): $(vwf_pp) $(vwf_org) $(cfg_files)
	$(vwf_pp) --in_png $(vwf_org) --zlines >$@

$(vwf_widths_ext): $(vwf_pp) $(vwf_org_ext) $(cfg_files)
	$(vwf_pp) --in_png $(vwf_org_ext) --widths >$@ --widths_label VWF_widths_ext

$(vwf_out_ext): $(vwf_pp) $(vwf_org_ext) $(cfg_files)
	$(vwf_pp) --in_png $(vwf_org_ext) --out_png $(vwf_out_ext)

# Generated source files
$(src_gen_out): $(build_dir)/%.s : $(patsubst $(build_dir)/%.s,%.s,$(codegen_dir)/%.py) $(derived_files) $(vwf_out)
	./$< >$@

$(str_gen_out): $(codegen_dir)/strings.py $(str_files) $(cfg_files)
	./$< >$@

# Derived file transformations
$(filter %.lzn,$(derived_files)): %.lzn : %
	$(lzn) -i $* -o $@
	@touch $@
