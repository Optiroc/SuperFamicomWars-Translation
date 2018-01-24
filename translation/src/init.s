; Super Famicom Wars Translation Project
; R&D by David Lindecrantz <optiroc@gmail.com>

;-----------------------------------------------------------------------------
; Initialization hook

.EQU INIT_hook $808AFA
.BANK (INIT_hook >> 16) & $7f SLOT ROMSLOT
.BASE (INIT_hook >> 16) & $80
.ORGA INIT_hook & $ffff
.SECTION "INIT_hook" OVERWRITE
  jmp.w   INIT_patch & $ffff
.ENDS

.BANK (INIT_hook >> 16) & $7f SLOT ROMSLOT
.BASE (INIT_hook >> 16) & $80
.SECTION "INIT_patch" FREE
.ACCU 16
.INDEX 16
INIT_patch:

  ; Write version stamp to SRAM
  ldx.w   #$000e
- lda.l   VERSION_STAMP,x
  sta.l   SRAM_version_stamp,x
  dex
  dex
  bpl     -

  ; Init variables
  stz.w   HDMA_FLAGS_last_value & $ffff

  ; Continue
  jmp.w   MAIN_runloop_jump & $ffff

.ENDS
