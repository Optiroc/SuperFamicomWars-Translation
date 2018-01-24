; Super Famicom Wars Translation Project
; R&D by David Lindecrantz <optiroc@gmail.com>

;-----------------------------------------------------------------------------
; TXT_print_small_stat alternative, smaller font, 0-199 range

.EQU HEX2DEC $879944 ; Hex -> Dec table, 0-99
.EQU DIGITS_OFFSET $02D0


.BANK (main_code_bank) & $7f SLOT ROMSLOT
.BASE (main_code_bank) & $80
.SECTION "TXT_print_small_stat_new" FREE
.ACCU 16
.INDEX 16

;-----------------------------------------------------------------------------
; Parameters
;   A        W Number (0-199, #$FFFF prints '-')
TXT_print_small_stat199_main_dmg:
  phx
  phy
  cmp.w   #$FFFF
  beq     _print_dash
  cmp.w   #200
  bcc     +
  lda.w   #199
+
  ldy.w   #$2000
  sty.w   param_attribute
  jsl     TXT_print_small_number199
  jmp     _done

_print_dash:
  inx
  lda.w   #DIGITS_OFFSET+$200A
  jsl     TXT_print_small_char

_done:
  ply
  plx
  rtl


TXT_print_small_stat199_sub_dmg:
  phx
  phy
  cmp.w   #$FFFF
  beq     _print_dash
  cmp.w   #200
  bcc     +
  lda.w   #199
+
  ldy.w   #$2800
  sty.w   param_attribute
  jsl     TXT_print_small_number199
  ply
  plx
  rtl


;-----------------------------------------------------------------------------
; Parameters
;   A        W Number
;   X(L)     B Y-offset
;   X(H)     B X-offset
;   $0F5D    W Tile attribute
;   $0F54    L Pointer to boxdim_struct:
;                ($0f54)+0 B Buffer width
;                ($0f54)+6 L Destination pointer
TXT_print_small_number199:
  phb
  php
  phk
  plb
  phx
  phy
  ldy.b   tmp_1
  phy

  and.w   #$00FF
  pha

  lda.w   UX_SYS_boxdim_ptr_L    ; Calculate cursor position and line stride
  tay
  A8
  lda.w   UX_SYS_boxdim_ptr_B
  pha
  A16
  plb
  lda.w   $0006,y
  sta.l   dest_ptr
  lda.w   $0007,y
  sta.l   dest_ptr_H
  lda.w   #$0000
  sta.l   tmp_1
  txa
  A8
  sta.l   tmp_1
  xba
  sta.l   WRMPYA
  lda.w   $0000,y
  sta.l   WRMPYB
  nop
  nop
  nop
  A16
  lda.l   RDMPYL
  clc
  adc.l   tmp_1
  asl     a
  clc
  adc.l   dest_ptr
  sta.l   dest_ptr

  pla
  cmp.w   #100
  bcc     _first_tile
  bra     _first_tile_x

_first_tile:            ; First tile 0-99
  asl     a
  tax
  lda.l   HEX2DEC+1,x
  and.w   #$00FF
  beq     _blank
  clc
  adc.l   param_attribute
  adc.w   #DIGITS_OFFSET
  ora.w   #$2000
  sta.b   [dest_ptr]
  bra     _second_tile

_blank:
  lda.l   $000F61
  ora.w   #$2000
  sta.b   [dest_ptr]

_second_tile:
  ldy.w   #$0002
  lda.l   HEX2DEC,x
  and.w   #$00FF
  clc
  adc.l   param_attribute
  clc
  adc.w   #DIGITS_OFFSET+$10
  ora.w   #$2000
  sta.b   [dest_ptr],y

  pla
  sta.b   tmp_1
  ply
  plx
  plp
  plb
  clc
  rtl

_first_tile_x:          ; First tile 100-199
  sec
  sbc.w   #100
  asl     a
  tax
  lda.l   HEX2DEC+1,x
  and.w   #$00FF
  clc
  adc.l   param_attribute
  adc.w   #DIGITS_OFFSET+$20
  ora.w   #$2000
  sta.b   [dest_ptr]
  bra     _second_tile

.ENDS

