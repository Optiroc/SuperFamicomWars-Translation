.SUFFIXES:
.PHONY: clean extract

# Rules
default: extract

all: clean tools default

extract:
	@./extract_graphics.py

tools:
	@$(MAKE) -C ../.. tools

clean:
	rm -rf out
