; Super Famicom Wars Translation Project
; R&D by David Lindecrantz <optiroc@gmail.com>

;-----------------------------------------------------------------------------
; DMA system
;
; Patched in at the start of SYS_DMA_process.
; Synchronizes the SRAM VWF_buffer_dirty_start..VWF_buffer_dirty_end range
; with VRAM. If it needs to go over the vblank time budget it will hog the
; game engine for as many frames as is needed to synchronize.

; A few screens use HDMA (Sound Park, Units list) which needs a subroutine
; being called each vblank to keep active, which also affects the raster
; line budget in those cases. Also, the HDMA system is patched up a bit to
; handle this without causing visual glitches.

; Constants
.EQU DMA_CHANNEL               7
.EQU DMA_SAFE_BYTES_PER_LINE   170
.EQU DMA_EXIT_SAFE_LINE        236
.EQU DMA_LAST_SAFE_LINE        259
.EQU HDMA_PENALTY_LINES        3


;-----------------------------------------------------------------------------
; SYS_DMA_process hook

.EQU SYS_DMA_process_hook       $80B27A
.BANK (SYS_DMA_process_hook >> 16) & $7f SLOT ROMSLOT
.BASE (SYS_DMA_process_hook >> 16) & $80
.ORGA SYS_DMA_process_hook & $ffff
.SECTION "SYS_DMA_process_patch" OVERWRITE
  jml SYS_DMA_process_new
.ENDS


;-----------------------------------------------------------------------------
; Custom DMA routine

.BANK (main_code_bank) & $7f SLOT ROMSLOT
.BASE (main_code_bank) & $80
.SECTION "SYS_DMA_process_new" FREE
.ACCU 16
.INDEX 16

/**
 * Hook into SYS_DMA_process at the very start...
 */
SYS_DMA_process_new:
  phb
  php
  phk
  plb

; ...and perform the VRAM synchronization
DMA_process:
  A16X16
  lda.w   VWF_buffer_dirty_start & $ffff
  cmp.w   VWF_buffer_dirty_end & $ffff
  bne     _DMA_process_loop
  jml     SYS_DMA_process_hook + $4               ; Exit early


_DMA_process_loop:                                ; Dirty range exists: transfer as much as possible in current VBlank
  jsr     _DMA_get_max_size
  cmp.w   #$0040
  bcs     +
  bra     _skip                                   ; Not enough vblanking time, skip a frame
+


  pha                                             ; Put max byte count on stack

  lda.w   #(((VWF_buffer) >> 8) & $ffff)          ; Set source
  sta.w   A1T0H + (DMA_CHANNEL * $10)
  lda.w   #((VWF_buffer) & $ffff)
  clc
  adc.w   VWF_buffer_dirty_start & $ffff
  sta.w   A1T0L + (DMA_CHANNEL * $10)

  lda.w   VWF_buffer_dirty_start & $ffff          ; Set VRAM destination
  lsr     a
  clc
  adc.w   VWF_VRAM_tilebase & $ffff
  sta.w   VMADDL


  lda.w   VWF_buffer_dirty_end & $ffff            ; Byte count
  sec
  sbc.w   VWF_buffer_dirty_start & $ffff
  cmp     1,s
  bcs     _xfer_part

_xfer_all:
  sta.w   DAS0L + (DMA_CHANNEL * $10)
  lda.w   VWF_buffer_head & $ffff
  and.w   #VWF_buffer_sizemask
  sta.w   VWF_buffer_dirty_end & $ffff
  sta.w   VWF_buffer_dirty_start & $ffff
  pla
  bra     _byte_count_done

_xfer_part:
  lda.w   VWF_buffer_dirty_start & $ffff
  clc
  adc     1,s
  sta.w   VWF_buffer_dirty_start & $ffff
  pla
  sta.w   DAS0L + (DMA_CHANNEL * $10)

_byte_count_done:


  lda.w   #$1801                                  ; Set DMA parameters
  sta.w   DMAP0 + (DMA_CHANNEL * $10)
  A8
  lda.b   #$80                                    ; Increment mode
  sta.w   VMAINC
  lda.b   #(1 << DMA_CHANNEL)                     ; Enable DMA
  sta.w   MDMAEN
  A16


  lda.w   VWF_buffer_dirty_start & $ffff          ; Done?
  cmp.w   VWF_buffer_dirty_end & $ffff
  beq     _transfer_done

_skip:
  jsr     DMA_wait_next_transfer
  jmp     _DMA_process_loop

_transfer_done:
  jsr     DMA_wait_safe_exit_vbl
  jml     SYS_DMA_process_hook + $4



/**
 * Get max bytes possible to transfer during current vblank interval
 */
_DMA_get_max_size:
  A8                                    ; Check forced blanking
  lda.w   INIDISP
  and.b   #%10000000
  beq     +
  A16
  lda     #$ffff                        ; Return with max value: forced blanking
  rts

  A8
+ lda.w   SLHV
  lda.w   OPVCT
  xba
  lda.w   OPVCT
  and.b   #$01
  xba
  A16
  cmp     #$00e1
  bpl     +
  lda.w   #$0000                        ; Return 0: not in vblank
  rts

+ pha                                   ; Get lines left of vblank
  lda.w   #$0001
  cmp.w   HDMA_FLAGS_last_value & $ffff
  beq     +
  clc
  adc.w   #HDMA_PENALTY_LINES
+ clc
  adc.w   #DMA_LAST_SAFE_LINE - HDMA_PENALTY_LINES - 1
  sec
  sbc     1,s
  bpl     +

  pla                                   ; Too few
  lda.w   #$0000
  rts

+ plx                                   ; Multiply safe lines left by 170
  A8
  xba
  lda.b   #DMA_SAFE_BYTES_PER_LINE
  sta.w   M7A
  stz.w   M7A
  xba
  sta.w   M7B
  A16
  lda.w   MPYL
  and.w   #$fff8
  rts


/**
 * Return at the top of next vblank interval
 */
DMA_wait_next_vbl:
- jsr     DMA_get_raster
  cmp.w   #$00E1
  bcc     -
  cmp.w   #$00E5
  bcs     -
  rts


DMA_wait_next_transfer:
  jsr     DMA_perform_vbl_duties
  jsr     DMA_wait_next_vbl
+ rts


/**
 * Return when it's safe to exit DMA handler with enough
 * vblank left for the game engine to update OAM and CGRAM
 */
_DMA_delay_safe_exit
  jsr     DMA_perform_vbl_duties
  jsr     DMA_wait_next_vbl
DMA_wait_safe_exit_vbl:
- jsr     DMA_get_raster
  cmp.w   #$00E2
  bcc     _DMA_delay_safe_exit
  cmp.w   #DMA_EXIT_SAFE_LINE
  bcs     _DMA_delay_safe_exit
  rts


/**
 * Call in vblank once per "hogged" frame
 */
DMA_perform_vbl_duties:
  inc.b   ZP_NMI_shtick

  lda.w   HDMA_FLAGS_last_value & $ffff
  cmp.w   #1
  bne     +
  jsl     DMA_set_hdma
  A8
  lda.w   HDMA_FLAGS_last_value & $ffff
  sta.b   ZP_HDMA_FLAGS
  A16
+
  jsl     SYS_PPU_screen_on
  rts


/**
 * Return current raster line in A
 */
DMA_get_raster:
  A8
  lda.w   SLHV
  lda.w   OPVCT
  xba
  lda.w   OPVCT
  and.b   #$01
  xba
  A16
  rts

.ENDS


;-----------------------------------------------------------------------------
; Patched SYS_PPU_set_hdma
;  - Stash $C1, which is needed for HDMA to work when going over frame budget

.EQU SYS_PPU_set_hdma_end $80B272

.BANK (SYS_PPU_set_hdma_end >> 16) & $7f SLOT ROMSLOT
.BASE (SYS_PPU_set_hdma_end >> 16) & $80
.ORGA SYS_PPU_set_hdma_end & $ffff
.SECTION "SYS_PPU_set_hdma_patch" OVERWRITE
  jmp SYS_PPU_set_hdma_new
.ENDS

.BANK (SYS_PPU_set_hdma_end >> 16) & $7f SLOT ROMSLOT
.BASE (SYS_PPU_set_hdma_end >> 16) & $80
.SECTION "SYS_PPU_set_hdma_new" FREE
.ACCU 8
.INDEX 16
SYS_PPU_set_hdma_new:
  sta.w   HDMA_FLAGS_last_value & $ffff
  stz.b   ZP_HDMA_FLAGS
  stz.w   $0342
  plp
  plb
  rtl
.ENDS


;-----------------------------------------------------------------------------
; Patched SYS_PPU_set_parameters
; - Store VWF_VRAM_tilebase
; - Initialize VWF offsets

.EQU SYS_PPU_set_parameters_end   $80AEDA

.BANK (SYS_PPU_set_parameters_end >> 16) & $7f SLOT ROMSLOT
.BASE (SYS_PPU_set_parameters_end >> 16) & $80
.ORGA SYS_PPU_set_parameters_end & $ffff
.SECTION "SYS_PPU_set_parameters_patch" OVERWRITE
  jml SYS_PPU_set_parameters_new
.ENDS

.BANK (main_code_bank) & $7f SLOT ROMSLOT
.BASE (main_code_bank) & $80
.SECTION "SYS_PPU_set_parameters_new" FREE
.ACCU 8
.INDEX 16

SYS_PPU_set_parameters_new:
  asl     a                                     ; Set tile base and reset VWF variables
  asl     a
  asl     a
  asl     a
  A16
  xba
  and.w   #$f000
  clc
  adc.w   #VWF_tilebase_offset >> 1
  sta.w   VWF_VRAM_tilebase & $ffff
  stz.w   VWF_buffer_head & $ffff
  stz.w   VWF_buffer_dirty_start & $ffff
  stz.w   VWF_buffer_dirty_end & $ffff

  lda.w   #($54 + ((VWF_buffer >> 8) & $ff00))  ; Block move instruction, destination bank, rts
  sta.w   VWF_block_move & $ffff
  A8
  lda.b   #$60
  sta.w   VWF_block_move_rts & $ffff
  A16

  stz.w   TITLE_should_init & $ffff

  plp
  plb
  rtl

.ENDS
