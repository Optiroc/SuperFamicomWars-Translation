; Super Famicom Wars Translation Project
; R&D by David Lindecrantz <optiroc@gmail.com>

;-----------------------------------------------------------------------------
; Title Screen additions

.EQU TITLE_OAM_base_x    $32
.EQU TITLE_OAM_dist_1    $32
.EQU TITLE_OAM_dist_2    $74
.EQU TITLE_OAM_stagger_1 50
.EQU TITLE_OAM_stagger_2 25

.EQU TITLE_long_wait     32
.EQU TITLE_short_wait    1


.EQU TITLE_UFUNC_hook       $8E9551
.EQU TITLE_UFUNC_hook_exit  $8E9556
.BANK (TITLE_UFUNC_hook >> 16) & $7f SLOT ROMSLOT
.BASE (TITLE_UFUNC_hook >> 16) & $80
.ORGA TITLE_UFUNC_hook & $ffff
.SECTION "TITLE_UFUNC_patch" OVERWRITE
  jmp TITLE_LOGO_new_ufunc
.ENDS

.BANK ($8E) & $7f SLOT ROMSLOT
.BASE ($8E) & $80
.SECTION "TITLE_LOGO_new_ufunc" FREE
.ACCU 16
.INDEX 16

TITLE_LOGO_new_ufunc:
  phb
  php
  phk
  plb
  phx
  phy

  lda.w   TITLE_should_init & $ffff
  bne     +
  jsr     TITLE_init
+

  lda.w   TITLE_wait_period & $ffff
  beq     +
  dec     a
  sta.w   TITLE_wait_period & $ffff
  jmp     TITLE_return
+

  ; SUPER
  ldx.w   TITLE_counter & $ffff
  lda.l   TITLE_bounce_table+2,x               ; y-pos
  and.w   #$00ff
  sta.b   $0D

  txa                                          ; prio
  cmp.l   TITLE_bounce_table
  lda.w   #$2000
  bcc     +
  ora.w   #$1000
+ sta.b   $15

  lda.w   #TITLE_OAM_base_x                    ; x-pos
  sta.b   $0B
  stz.b   $13
  ldy.w   #TITLE_oam_table1 & $ffff
  jsl     OAM_buffer_add

  ; FAMICOM
  lda.w   TITLE_counter & $ffff
  sec
  sbc.w   #TITLE_OAM_stagger_1
  bpl     +
  lda.w   #0
+ tax
  lda.l   TITLE_bounce_table+2,x               ; y-pos
  and.w   #$00ff
  sta.b   $0D

  txa                                          ; prio
  cmp.l   TITLE_bounce_table
  lda.w   #$2000
  bcc     +
  ora.w   #$1000
+ sta.b   $15

  lda.w   #TITLE_OAM_base_x+TITLE_OAM_dist_1   ; x-pos
  sta.b   $0B
  stz.b   $13
  ldy.w   #TITLE_oam_table2 & $ffff
  jsl     OAM_buffer_add

  ; WARS
  lda.w   TITLE_counter & $ffff
  sec
  sbc.w   #TITLE_OAM_stagger_2
  bpl     +
  lda.w   #0
+ tax
  lda.l   TITLE_bounce_table+2,x               ; y-pos
  and.w   #$00ff
  sta.b   $0D

  txa                                          ; prio
  cmp.l   TITLE_bounce_table
  lda.w   #$2000
  bcc     +
  ora.w   #$1000
+ sta.b   $15

  lda.w   #TITLE_OAM_base_x+TITLE_OAM_dist_2   ; x-pos
  sta.b   $0B
  stz.b   $13
  ldy.w   #TITLE_oam_table3 & $ffff
  jsl     OAM_buffer_add


  ; Stop counter?
  ldx.w   TITLE_counter & $ffff
  lda.l   TITLE_bounce_table+TITLE_OAM_stagger_2-5,x
  cmp.w   #$ffff
  beq     +
  inc.w   TITLE_counter & $ffff
+


TITLE_return:
  ply
  plx
  plp
  plb
  lda.b   $E8
  bit.w   #$1080
  jmp.w   TITLE_UFUNC_hook_exit & $ffff


TITLE_init:
  inc.w   TITLE_should_init & $ffff

  ; Set wait period
  lda.w   $05FD
  bne     _long_wait
_short_wait:
  lda.w   #TITLE_short_wait
  bra     _store_wait
_long_wait:
  lda.w   #TITLE_long_wait
_store_wait:
  sta.w   TITLE_wait_period & $ffff

  ; Init counters
  stz.w   TITLE_counter & $ffff

  ; Copy palette
  ldx.w   #$000e
- lda.w   TITLE_palette,x
  sta.w   $02e0,x
  dex
  dex
  bpl     -

  ; DMA remaining sprite data
  jsl     SYS_DMA_add_inline                   ; Add SYS_DMA job
  .DB     $02                                  ;  command
  .DW     (title_sprites2+$400) & $ffff        ;  source offset
  .DB     :title_sprites2                      ;  source bank
  .DW     $0800-$0140                          ;  length
  .DB     $80                                  ;  vmain
  .DW     $5800>>1                             ;  destination

  rts


TITLE_palette:
  .DB $00, $38, $84, $10, $de, $7b, $39, $67, $53, $4e, $08, $21, $00, $00, $00, $00

.ENDS
