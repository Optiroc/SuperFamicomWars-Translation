romfile		:= ../../rom/Super\ Famicom\ Wars\ \(Japan\)\ \(NP\).sfc
symfile		:= ../../rom/Super\ Famicom\ Wars\ \(Japan\)\ \(NP\).cpu.sym
asmfile		:= sfw.asm
reportfile	:= sfw_report.txt
traces		:= traces/big.trace
labels		:= labels/system.labels labels/sram.labels labels/task_runner.labels labels/memory_map.labels labels/unknown.labels labels/wip.labels
labels		+= labels/game.labels labels/ux_system.labels labels/ux_text_system.labels
autolabels	:= labels/auto.labels

snestistics	:= bin/snestistics
flags		:= -romfile $(romfile) -predict functions -autoannotate true -asmlowercaseop true -asmprintpc true -asmprintbytes true -asmprintregistersizes true -asmprintdb true -asmprintdp true
trace_args	:= $(foreach f,$(traces),-tracefile $(f))
label_args	:= $(foreach f,$(labels),-labelsfile $(f))

.PHONY: clean purge tool

default: $(asmfile)

$(asmfile): $(labels) $(traces) $(snestistics) Makefile
	$(snestistics) $(trace_args) $(label_args) -autolabelsfile $(autolabels) -asmoutfile $@ -reportoutfile $(reportfile) -symbolfmaoutfile $(symfile) $(flags)

tools:
	rm -frd bin
	git submodule update --init --recursive
	cd snestistics && cmake . && make clean && make -j4
	mkdir -pv bin
	mv snestistics/source/snestistics $(snestistics)

clean:
	rm -rf $(asmfile) $(reportfile)

purge: clean
	rm -rf $(autolabels) $(symfile) captures/*.emulation_cache
