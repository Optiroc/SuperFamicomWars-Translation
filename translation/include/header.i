; Super Famicom Wars Translation Project
;--------------------------------------------------------------------
; Memory map & header

.DEFINE ROMBANK $80
.DEFINE ROMSLOT 0
.DEFINE RAMSLOT 1

.MEMORYMAP
  DEFAULTSLOT ROMSLOT
  SLOTSIZE    $8000
  SLOT        ROMSLOT $8000
.ENDME

.ROMBANKMAP
  BANKSTOTAL  64
  BANKSIZE    $8000
  BANKS       64
.ENDRO

.SNESHEADER
  NAME "SUPERFAMICOMWARS-1.1E"
  LOROM
  FASTROM
  CARTRIDGETYPE $02
  ROMSIZE $0B
  SRAMSIZE $05
  COUNTRY $00
  LICENSEECODE $01
  VERSION 1
.ENDSNES

.BACKGROUND "../rom/Super Famicom Wars (Japan) (NP).sfc"
.EMPTYFILL $FF

.UNBACKGROUND $7FB0 $7FBF ;Extended header
.UNBACKGROUND $7FC0 $7FD4 ;Name
.UNBACKGROUND $7FD8 $7FDF ;Size, version, etc

; Extended header
.EQU HEADER_ext_flag $80FFDA
.BANK (HEADER_ext_flag >> 16) & $7F SLOT ROMSLOT
.BASE (HEADER_ext_flag >> 16) & $80
.ORGA HEADER_ext_flag & $FFFF
.SECTION "HEADER_ext_flag" OVERWRITE
.DB $33
.ENDS

.EQU HEADER_ext $80FFB0
.BANK (HEADER_ext >> 16) & $7F SLOT ROMSLOT
.BASE (HEADER_ext >> 16) & $80
.ORGA HEADER_ext & $FFFF
.SECTION "HEADER_ext" FORCE
.ASCIITABLE
MAP 0 TO 127 = 0
.ENDA

.ASC "MB"       ; $FFB0-$FFB1  Maker code
.ASC "SFWE"     ; $FFB2-$FFB5  Game code

.DB 0,0,0,0,0,0 ; $FFB6-$FFBB  Reserved

.DB $00         ; $FFBC        Expansion flash size
.DB $00         ; $FFBD        Expansion RAM size
.DB $00         ; $FFBE        Special version
.DB $00         ; $FFBF        Chipset sub-type

.ENDS


;--------------------------------------------------------------------
; For unique hashes, and used as stamp template for SRAM ID

.BANK (ROMBANK) & $7F SLOT ROMSLOT
.BASE (ROMBANK) & $80
.SECTION "VERSION STAMP" FREE

.ASCIITABLE
MAP 0 TO 127 = 0
.ENDA

VERSION_STAMP:
;    "0123456789ABCDEF"
.ASC "MB-SFWE-v1.1.0E "

.ENDS
