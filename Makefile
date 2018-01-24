VERSION := v1.1

.PHONY: output patch tools clean

default: output

all: clean tools patch

tools: superfamiconv superfamicheck flips wla

patch: tools
	@$(MAKE) -C translation patch -j4

output: patch
	@rm -rf release
	@mkdir -pv release
	@mv -f rom/mb-sfwe.vcdiff "release/mb-sfwe-$(VERSION).vcdiff"
	@mv -f rom/mb-sfwe.bps "release/mb-sfwe-$(VERSION).bps"
	@cp docs/release/mb-sfwe.txt release/readme.txt
	@cp docs/release/mb-sfwe.nfo release/mb-sfwe-$(VERSION).nfo
	@mkdir -pv release/comparison_gifs
	@cp graphics/screenshots/20171220/comparison_gifs/*.gif ./release/comparison_gifs
	cd release; zip -r -y -9 "mb-sfwe-$(VERSION).zip" ./*


superfamiconv:
	@$(MAKE) -C tools/superfamiconv -j4

superfamicheck:
	@$(MAKE) -C tools/superfamicheck -j4

flips:
	@$(MAKE) -C tools/flips -j4

wla:
	cd tools/wla-dx && cmake . && make -j4


clean:
	@rm -rf release
	@$(MAKE) clean -C translation
	@$(MAKE) clean -C tools/superfamiconv
	@$(MAKE) clean -C tools/superfamicheck
	@$(MAKE) clean -C tools/flips
	@rm -rf tools/wla-dx/binaries/* tools/wla-dx/cmake_install.cmake tools/wla-dx/CMakeCache.txt tools/wla-dx/CMakeFiles tools/wla-dx/Makefile
	@rm -rf tools/wla-dx/opcode_table_generator/cmake_install.cmake tools/wla-dx/opcode_table_generator/CMakeCache.txt tools/wla-dx/opcode_table_generator/CMakeFiles tools/wla-dx/opcode_table_generator/Makefile
	@rm -rf tools/wla-dx/wlab/cmake_install.cmake tools/wla-dx/wlab/CMakeCache.txt tools/wla-dx/wlab/CMakeFiles tools/wla-dx/wlab/Makefile
	@rm -rf tools/wla-dx/wlalink/cmake_install.cmake tools/wla-dx/wlalink/CMakeCache.txt tools/wla-dx/wlalink/CMakeFiles tools/wla-dx/wlalink/Makefile
