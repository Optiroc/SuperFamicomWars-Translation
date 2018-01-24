; Super Famicom Wars Translation
;--------------------------------------------------------------------
; Set register widths

.MACRO A8
  sep #$20
.ENDM

.MACRO A16
  rep #$20
.ENDM

.MACRO X8
  sep #$10
.ENDM

.MACRO X16
  rep #$10
.ENDM

.MACRO A8X8
  sep #$30
.ENDM

.MACRO A16X16
  rep #$30
.ENDM

.MACRO A8X16
  A8
  X16
.ENDM

.MACRO A16X8
  A16
  X8
.ENDM


;--------------------------------------------------------------------
; Utilities

; Macro repeat indices
.DEFINE RI 0
.DEFINE RJ 0

; bsnes+ soft break (wdm #$00)
.MACRO BREAK
  .DB $42, $00
.ENDM

; @arg nops
.MACRO NOOP
  .REPEAT \1
    nop
  .ENDR
.ENDM

; Insert @arg2-@arg1+1 number of word offsets to @arg3
.MACRO JMPTABL
  .REPEAT \2 - \1 + 1
    .DW \3 & $FFFF
  .ENDR
.ENDM
