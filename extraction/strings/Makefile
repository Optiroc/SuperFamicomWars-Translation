.SUFFIXES:
.PHONY: clean extract

# Rules
default: extract

all: clean default

extract:
	@mkdir -pv out
	@./extract_strings.py >out/strings.py

clean:
	rm -rf out
