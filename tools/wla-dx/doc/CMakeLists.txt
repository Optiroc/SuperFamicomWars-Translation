project(DOCS)

option(GEN_DOC_MAN "Generate Manpages" ON)
option(GEN_DOC_SINGLEHTML "Generate single HTML documentation" ON)
option(GEN_DOC_SINGLETEXT "Generate text documentation" ON)

set(DOC_OUT "${CMAKE_RUNTIME_OUTPUT_DIRECTORY}/doc")
set(DOC_SRC "${CMAKE_CURRENT_SOURCE_DIR}")
set(DOC_DEPS )

find_program(SPHINX_EXECUTABLE
    NAMES sphinx-build
    HINTS $ENV{SPHINX_DIR}
    PATH_SUFFIXES bin
    DOC "Sphinx documentation generator"
)

if (SPHINX_EXECUTABLE)
    message(STATUS "Found sphinx-build: ${SPHINX_EXECUTABLE}")
    option(GEN_DOC "Generate documentation (Requires sphinx)" ON)
else()
    message(STATUS "Couldn't find sphinx-build")
    option(GEN_DOC "Generate documentation (Requires sphinx)" OFF)
endif (SPHINX_EXECUTABLE)

if (NOT GEN_DOC)
    return()
endif (NOT GEN_DOC)

if (NOT SPHINX_EXECUTABLE)
    message(FATAL_ERROR "sphinx-build not found")
    return()
endif (NOT SPHINX_EXECUTABLE)

add_custom_target(doc ALL)

set(DOC_MAN_SRCS "man/wlab.rst" "man/wla-cpu.rst"
    "man/wlad.rst" "man/wlalink.rst"
    "wla-dx.rst")
set(DOC_SRCS
    "archoverview.rst"
    "arithmetics.rst"
    "asmdiv.rst"
    "asmsyntax.rst"
    "bintodb.rst"
    "bugs.rst"
    "codetoknow.rst"
    "compiling.rst"
    "disassembling.rst"
    "errormsg.rst"
    "extraflags.rst"
    "files.rst"
    "gb-support.rst"
    "goodtoknow.rst"
    "introduction.rst"
    "legal.rst"
    "linking.rst"
    "tempfiles.rst"
    "wla-dx.rst"
    "wlaflags.rst"
    )
set(DOC_META_SRCS
    "conf.py"
    "sphinx/globalindex.py"
    )

if (GEN_DOC_MAN)
    set(DOC_MAN_CPUFILES "${DOC_OUT}/wla-gb.1" "${DOC_OUT}/wla-65c02.1"
        "${DOC_OUT}/wla-6502.1" "${DOC_OUT}/wla-6510.1" "${DOC_OUT}/wla-65816.1"
        "${DOC_OUT}/wla-huc6280.1" "${DOC_OUT}/wla-spc700.1"
        "${DOC_OUT}/wla-z80.1"
    )
    set(DOC_MAN_FILES "${DOC_OUT}/wla-dx.7" "${DOC_OUT}/wlalink.1"
        "${DOC_OUT}/wlad.1" "${DOC_OUT}/wlab.1" ${DOC_MAN_CPUFILES})
    add_custom_command(
        OUTPUT ${DOC_MAN_FILES}
        COMMAND "${SPHINX_EXECUTABLE}" -q -b man
            -d "${CMAKE_CURRENT_BINARY_DIR}/man.doctree"
            "${DOC_SRC}" "${CMAKE_CURRENT_BINARY_DIR}/gen-man"
        COMMAND "${CMAKE_COMMAND}" -E copy_directory
            "${CMAKE_CURRENT_BINARY_DIR}/gen-man/"
            "${DOC_OUT}"
        DEPENDS ${DOC_SRCS} ${DOC_MAN_SRCS} ${DOC_META_SRCS}
        COMMENT "Generating man pages"
    )
    add_custom_target(doc-man DEPENDS ${DOC_MAN_FILES})
    add_dependencies(doc doc-man)
    install(FILES "${DOC_OUT}/wla-dx.7" DESTINATION "man/man7")
    list(REMOVE_ITEM DOC_MAN_FILES "${DOC_OUT}/wla-dx.7")
    install(FILES ${DOC_MAN_FILES} DESTINATION "man/man1")
    set_property(DIRECTORY APPEND PROPERTY ADDITIONAL_MAKE_CLEAN_FILES
        "gen-man" "man.doctree")
endif (GEN_DOC_MAN)

if (GEN_DOC_SINGLEHTML)
    add_custom_command(
        OUTPUT "${DOC_OUT}/wla-dx.html"
        COMMAND "${SPHINX_EXECUTABLE}" -q -b singlehtml
            -d "${CMAKE_CURRENT_BINARY_DIR}/shtml.doctree"
            "${DOC_SRC}" "${CMAKE_CURRENT_BINARY_DIR}/gen-shtml"
        COMMAND "${CMAKE_COMMAND}" -E copy
            "${CMAKE_CURRENT_BINARY_DIR}/gen-shtml/wla-dx.html"
            "${DOC_OUT}/wla-dx.html"
        DEPENDS ${DOC_SRCS} ${DOC_META_SRCS} theme/layout.html theme/theme.conf
        COMMENT "Generating single HTML page documentation"
    )
    list(APPEND DOC_DEPS "${DOC_OUT}/wla-dx.html")
    add_custom_target(doc-shtml DEPENDS "${DOC_OUT}/wla-dx.html")
    add_dependencies(doc doc-shtml)
    install(FILES "${DOC_OUT}/wla-dx.html" DESTINATION "share/doc/wla-dx")
    set_property(DIRECTORY APPEND PROPERTY ADDITIONAL_MAKE_CLEAN_FILES
        "gen-shtml" "shtml.doctree")
endif (GEN_DOC_SINGLEHTML)

if (GEN_DOC_SINGLETEXT)
    add_custom_command(
        OUTPUT "${DOC_OUT}/wla-dx.txt"
        COMMAND "${SPHINX_EXECUTABLE}" -q -b singletext
            -d "${CMAKE_CURRENT_BINARY_DIR}/stext.doctree"
            "${DOC_SRC}" "${CMAKE_CURRENT_BINARY_DIR}/gen-stext"
        COMMAND "${CMAKE_COMMAND}" -E copy
            "${CMAKE_CURRENT_BINARY_DIR}/gen-stext/wla-dx.txt"
            "${DOC_OUT}/wla-dx.txt"
        DEPENDS ${DOC_SRCS} ${DOC_META_SRCS} sphinx/singletext.py
        COMMENT "Generating simple text documentation"
    )
    add_custom_target(doc-stext DEPENDS "${DOC_OUT}/wla-dx.txt")
    add_dependencies(doc doc-stext)
    install(FILES "${DOC_OUT}/wla-dx.txt" DESTINATION "share/doc/wla-dx")
    set_property(DIRECTORY APPEND PROPERTY ADDITIONAL_MAKE_CLEAN_FILES
        "gen-stext" "stext.doctree")
endif (GEN_DOC_SINGLETEXT)

