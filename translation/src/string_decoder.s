; Super Famicom Wars Translation Project
; R&D by David Lindecrantz <optiroc@gmail.com>

;--------------------------------------------------------------------
; String decoder & variable width font renderer
;
; Redirects calls to TXT_decode_string (@879E01) and implements
; decoding and rendering of custom translated string format.

; Special characters
;
; $00      String terminator
;          For compatibility with old strings, which are terminated with #$0000,
;          new strings will not spill into the first byte of the old terminator.
;
;          The zero-word is checked by the TXT_UTIL_string_len function, and
;          quite possibly other functions too.
;
;          Also, when returning from the print function the read offset in
;          register X should point to the word after the terminator. If that
;          contains #$FFFF the string is considered part of a multiline string.
;
; $01-$1F  Fast forward terminator
;          The non-printable ASCII range is used as special terminators.
;          When encountered, the string is terminated like with $00, and
;          the value of the terminator is added to the read pointer.
;
; $7Fxx    Extended character
;          2-byte encoded special characters (ie. for hand drawn unit names).
;
; $FE      Dummy byte
;          No effect, used for padding when a two-byte character at a
;          "continuation boundary" would otherwise leave one byte unaccounted
;          for before the old string terminator.
;
; $FD      Move to next tile
;          Used for fast and aligned spacing (a short tab of sorts).
;
; $FC      Continuation pointer
;          Used for strings that don't fit in the original location.
;          $FE followed by 24-bit pointer to rest of string.
;          Terminated by $00, at which point $2F will be restored
;          to the address of the token + 4.
;
; $FB      Set VFW buffer offset
;          When encountered continue VWF tile rendering at specified offset.
;          $FE followed an 8-bit value (<< 5 = offset in the #$2000 buffer).
;
; $FA      Negative kerning
;          When encountered subtract the following 8-bit value from the
;          width of the character.
;
;
;           IP                      EP  Initial pointer / exit pointer
; original: 40 40 40 40 40 40 00 00 **
;   normal: 44 44 44 44 44 44 00
;   ffwd 3: 44 44 44 03
;   ffwd 2: 44 44 44 44 02
;   ffwd 1: 44 44 44 44 44 01
;     long: 44 44 44 44 FC 11 22 87     -> $872211: 44 44 44 44 44 44 44 44 00

;--------------------------------------------------------------------
; VWF renderer
;
; After messing around with a small VWF tile buffer in WRAM and implementing
; a fairly complicated DMA queue system, I decided that it's both easier and
; better to dedicate a buffer of equal size to the VRAM buffer in SRAM.
;
; Blitting of VWF tiles is performed using 8 preshifted versions of the font.
; The amount of ROM space dedicated for that is probably approaching that of
; storing prerendered tiles for all text in the game, but making a real time
; text renderer was way more fun!
;
; Variables:
; VWF_buffer_head               Current VWF buffer pointer
; VWF_buffer_dirty_start        Range of tiles changed in VWF buffer, will
; VWF_buffer_dirty_end          be synchronized at next DMA_process call
;
; Zero page pointers:
; VWF_tile_ptr                  Pointer to currently rendered tile data
; VWF_font_src                  Pointer to font data


;-----------------------------------------------------------------------------
.EQU TXT_decode_string_addr     $879E01

.EQU line_len                   tmp_3
.EQU org_ptr                    tmp_1
.EQU org_ptr_B                  tmp_2

.EQU BAD_CHAR                   $0045
.EQU EMPTY_CHAR                 $005F

; VWF
.EQU VWF_tile_ptr               tmp_4         ; $11,12,13
.EQU VWF_font_src               tmp_5 + 1     ; $14,15,16

;-----------------------------------------------------------------------------
; DMA/VWF buffer macros

; Increment VWF_buffer_head by @arg1
.MACRO VWF_buffer_advance
  lda.w   VWF_buffer_head & $ffff
  clc
  adc.w   #\1
  cmp.w   #(VWF_buffer_size - \1)
  bcc     +

  jsr     _vwf_copy_spill                 ; If buffer wrapped: copy last tile to start, set head/start to zero, end to max
  lda.w   #VWF_buffer_size
  sta.w   VWF_buffer_dirty_end & $ffff
  lda.w   #$0000
  sta.w   VWF_buffer_dirty_start & $ffff

+ and.w   #VWF_buffer_sizemask
  sta.w   VWF_buffer_head & $ffff

  cmp.w   VWF_buffer_dirty_end & $ffff    ; Set dirty range end if higher than previous value
  bcc     +
  sta.w   VWF_buffer_dirty_end & $ffff
+
.ENDM

; Set VWF_buffer_head to value in A
.MACRO VWF_set_buffer_offset
  asl     a
  asl     a
  asl     a
  asl     a
  asl     a
  sta.w   VWF_buffer_head & $ffff

  cmp.w   VWF_buffer_dirty_start & $ffff  ; If value < buffer_dirty_start: set buffer_dirty_start
  bcs     +
  sta.w   VWF_buffer_dirty_start & $ffff
+
.ENDM

; Set VWF_tile_ptr
.MACRO VWF_set_tile_ptr
  lda.w   VWF_buffer_head & $ffff
  clc
  adc.w   #(VWF_buffer & $ffff)
  sta.b   VWF_tile_ptr
.ENDM


;-----------------------------------------------------------------------------
; Decode 8x16 tiles to text buffer
; Parameters
;   $2F      L Source pointer
;   X(L)     B X-coordinate
;   X(H)     B Y-coordinate
;   $0F54    L Pointer to boxdim_struct:
;                ($0f54)+0 B Buffer width
;                ($0f54)+6 L Destination pointer
;   $0F5D    W Tile attribute
;   $0F5F    W Empty character

.BANK (TXT_decode_string_addr >> 16) & $7f SLOT ROMSLOT
.BASE (TXT_decode_string_addr >> 16) & $80
.ORGA TXT_decode_string_addr & $ffff
.SECTION "TXT_decode_string_patch" OVERWRITE
  jml TXT_decode_string_new
.ENDS

.BANK (main_code_bank) & $7f SLOT ROMSLOT
.BASE (main_code_bank) & $80
.SECTION "TXT_decode_string_new" FREE
.ACCU 16
.INDEX 16
TXT_decode_string_new:
  phb
  php
  phk
  plb
  lda.b   tmp_1
  pha
  lda.b   tmp_2
  pha
  lda.b   tmp_3
  pha
  lda.b   tmp_4
  pha
  lda.b   tmp_5
  pha
  lda.b   tmp_6
  pha
  phx
  phy

  lda.w   UX_SYS_boxdim_ptr_L           ; Calculate cursor position and line stride
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
  pha
  lda.w   $0000,y
  and.w   #$00FF
  asl     a
  sta.l   line_len

  ply                                   ; Source offset in X, bank in DB
  lda.l   source_ptr
  tax
  A8
  lda.l   source_ptr_B
  pha
  A16
  plb

  ; Init state
  stz.b   org_ptr_B                     ; Zero out variable used to stash original read pointer
                                        ; when jumping to continuation pointer
  stz.w   VWF_should_clear & $ffff
  stz.w   VWF_position & $ffff
  stz.w   VWF_neg_kern & $ffff

  lda.w   #((VWF_buffer >> 8) & $ffff)  ; Set bank tile pointer bank byte
  sta.b   VWF_tile_ptr + 1

  bra     _get_byte


/**
 * Skip dummy byte
 */
 _dummy_byte:
  plx
  bra     _next_byte


/**
 * Next word/byte
 *
 * Increment read offset and get next byte
 */
_next_word:
  inx
_next_byte:
  inx
  ; fall through


/**
 * Get byte
 *
 * Get next byte from encoded stream
 */
_get_byte:
  lda.w   $0000,x
  and.w   #$00FF
  phx
  pha
  asl     a
  tax
  pla
  jmp     (_chartype_jmptable,x)

_chartype_jmptable:
  JMPTABL $00,$00, _term              ; #$00       String terminator
  JMPTABL $01,$1F, _term_ffwd         ; #$01-#$1F  Fast forward terminator
  JMPTABL $20,$7E, _ascii_char        ; #$20-#$7E  ASCII character
  JMPTABL $7F,$7F, _ext_char          ; #$7F       Extended character
  JMPTABL $80,$EA, _bad_wchar         ; #$80-#$EA  Original 2-byte SJIS (-> print BAD_CHAR)
  JMPTABL $EB,$F9, _bad_wchar         ; #$EB-#$F9  Unused
  JMPTABL $FA,$FA, _set_neg_kerning   ; #$FA       Set negative kerning
  JMPTABL $FB,$FB, _set_vwf_offset    ; #$FB       Set VFW buffer offset
  JMPTABL $FC,$FC, _cont_ptr          ; #$FC       Continuation pointer
  JMPTABL $FD,$FD, _move_next_tile    ; #$FD       Short tab (move to next tile)
  JMPTABL $FE,$FF, _dummy_byte        ; #$FE-#$FF  Dummy byte


/**
 * Fast forward terminator
 *
 * Increase read pointer (X) by value in A
 */
_term_ffwd:
  plx
  stx.b   tmp_1
  clc
  adc.b   tmp_1
  tax
  bra     _done


/**
 * Terminator
 *
 * Set read pointer to end of string
 * (first byte after original 2-byte terminator)
 */
_term:
  plx

_term_check_stash:
  lda.b   org_ptr_B         ; Check stashed org_ptr
  beq     _done

  A8                        ; Restore stashed read pointer
  pha
  plb
  A16
  ldx.b   org_ptr
  inx
  inx
  ; fall through


/**
 * Done
 *
 * String decoded and terminated. Flush VWF and restore state.
 */
_done:
  jsr     _vwf_flush

  inx                       ; Set source pointer one word beyond string terminator
  inx
  txa
  sta.b   source_ptr

  ply
  plx
  pla
  sta.b   tmp_6
  pla
  sta.b   tmp_5
  pla
  sta.b   tmp_4
  pla
  sta.b   tmp_3
  pla
  sta.b   tmp_2
  pla
  sta.b   tmp_1
  plp
  plb
  rtl


/**
 * Continuation pointer (#$FC + long pointer)
 * Stash current read pointer and fetch continuation pointer
 *
 * Parameters
 *   X        W Read offset
 */
_cont_ptr:
  plx
  phy
  inx                           ; Stash final read ptr
  lda.w   $0000,x               ; Fetch continuation ptr
  tay
  inx                           ; Stash final ptr
  stx.b   org_ptr
  A8
  lda.b   source_ptr_B
  sta.b   org_ptr_B
  lda.w   $0001,x               ; Push continuation ptr bank
  pha
  A16
  tyx                           ; New read pointer in X and pull bank
  plb
  ply
  jmp     _get_byte


/**
 * Move to next tile (#$FD)
 * Flush VWF plotter and move one char forward
 */
_move_next_tile:
  plx
  lda.w   VWF_position & $ffff  ; If VWF_position == 0, write one space
  beq     +
  jsr     _vwf_flush
  jmp     _next_byte

+ phy                           ; Write one space
  lda.w   param_attribute
  clc
  adc.w   #EMPTY_CHAR
  sta.b   [dest_ptr],y
  tya
  adc.b   line_len
  tay
  lda.w   param_attribute
  adc.w   #EMPTY_CHAR
  adc.w   #$0010
  sta.b   [dest_ptr],y
  ply
  iny
  iny
  jmp     _next_byte


/**
 * Set VWF offset (#$FB + byte value)
 */
_set_vwf_offset:
  plx
  jsr     _vwf_flush
  inx
  lda.w   $0000,x
  and.w   #$00ff
  VWF_set_buffer_offset

  jmp     _next_byte


/**
 * Set negative kerning (#$FA + byte value)
 */
_set_neg_kerning:
  plx
  inx
  lda.w   $0000,x
  and.w   #$00ff
  sta.w   VWF_neg_kern & $ffff
  jmp     _next_byte


/**
 * ASCII character
 * VWF plot ASCII encoded character
 *
 * Parameters
 *   A        W Character
 */
_ascii_char:
  plx                               ; Restore read offset and put on stack
  phx

  sec                               ; Put character index on stack
  sbc     #$0020
  pha

  tax                               ; Put initial zero-lines for character on stack
  lda.l   VWF_zlines,x
  and.w   #$00ff
  pha

  lda.w   VWF_position & $ffff      ; Set VWF_font_src
  asl     a
  tax
  lda.l   _vwf_font_src_banks,x
  sta.b   VWF_font_src+1
  lda.l   _vwf_font_src_offsets,x
  sta.b   VWF_font_src


  lda.w   VWF_position & $ffff      ; Blit tiles
  beq     _ascii_blit_left
  jmp     _ascii_blit_both


_ascii_blit_left:                   ; If VWF_position == 0: OR blit left tile, clear right tile

  lda.w   VWF_should_clear & $ffff  ; Clear tile if it's the first to be rendered
  bne     +
  jsr     _vwf_clear_left
+
  VWF_set_tile_ptr                  ; Set tile pointer, and
  adc     1,s                       ; adjust for zero-lines optimization
  sta.b   VWF_tile_ptr

  lda     3,s
  asl     a
  asl     a
  asl     a
  asl     a
  asl     a
  adc     1,s
  adc.b   VWF_font_src
  sta.b   VWF_font_src

  lda     1,s                       ; Jump into unrolled loop, skipping zero-lines
  tax
  jmp     (_ascii_blit_left_unroll_jmptable,x)

_ascii_blit_left_unroll:            ; OR blit left tile
.REPEAT 16
  lda.b   [VWF_font_src]
  ora.b   [VWF_tile_ptr]
  sta.b   [VWF_tile_ptr]
  inc.b   VWF_tile_ptr
  inc.b   VWF_tile_ptr
  inc.b   VWF_font_src
  inc.b   VWF_font_src
.ENDR
_ascii_blit_left_unroll_length:

  stz.w   VWF_should_clear & $ffff  ; If next character is zero-aligned, tile must be cleared before ORing
  jmp     _blit_done


_ascii_blit_both:                   ; Else: OR blit both tiles

  VWF_set_tile_ptr                  ; Set tile pointer, and
  adc     1,s                       ; adjust for zero-lines optimization
  sta.b   VWF_tile_ptr

  lda     3,s
  asl     a
  asl     a
  asl     a
  asl     a
  asl     a
  asl     a
  adc     1,s
  adc.b   VWF_font_src
  sta.b   VWF_font_src

  lda     1,s                       ; Jump into unrolled loop, skipping zero-lines
  tax
  jmp     (_ascii_blit_both_unroll_jmptable,x)

_ascii_blit_both_unroll:            ; OR blit left tile
.REPEAT 16
  lda.b   [VWF_font_src]
  ora.b   [VWF_tile_ptr]
  sta.b   [VWF_tile_ptr]
  inc.b   VWF_tile_ptr
  inc.b   VWF_tile_ptr
  inc.b   VWF_font_src
  inc.b   VWF_font_src
.ENDR
_ascii_blit_both_unroll_length:

.REPEAT 16                          ; Copy blit right tile
  lda.b   [VWF_font_src]
  sta.b   [VWF_tile_ptr]
  inc.b   VWF_tile_ptr
  inc.b   VWF_tile_ptr
  inc.b   VWF_font_src
  inc.b   VWF_font_src
.ENDR

  inc.w   VWF_should_clear & $ffff  ; Next tile don't need to be cleared


_blit_done:
  plx
  plx                               ; Increment VWF_position
  lda.l   VWF_widths,x
  jsr     _vwf_advance

  plx
  jmp     _next_byte


/**
 * Extended character
 * 2-byte encoded special characters (ie. for hand drawn unit names).
 *
 * #$7F followed by char id
 */
_ext_char:
  plx                     ; Restore read offset, increment and put on stack
  inx
  phx

  lda.w   $0000,x         ; Get parameter byte
  and.w   #$00ff
  ;cmp.w  #$0040
  ;bcc    _ext_vwf2       ; #$00 - #$3F: Now unused
  cmp.w   #$0080
  bcc     _ext_vwf        ; #$40 - #$7F: 3 x tile VWF characters (Unit/terrain names)
  cmp.w   #$00c0
  bcc     _ext_base1      ; #$80 - #$BF: 1 x tile base font characters (Stats symbols)

  ;fall through           ; #$C0 - #$FF: 2 x tile base font characters (Icons)

_ext_base2:
  pha
  jsr     _vwf_flush
  pla
  and.w   #$003F
  asl     a
  asl     a
  asl     a
  tax

  phx
  lda.l   _ext_base2_chrtable+2,x
  pha
  lda.l   _ext_base2_chrtable+0,x
  plx
  jsr.w   _print_char
  iny
  iny
  plx

  lda.l   _ext_base2_chrtable+6,x
  pha
  lda.l   _ext_base2_chrtable+4,x
  plx
  jsr.w   _print_char
  iny
  iny

  plx
  jmp     _next_byte


_ext_base1:
  pha
  jsr     _vwf_flush
  pla
  and.w   #$003F
  asl     a
  asl     a
  tax

  lda.l   _ext_base1_chrtable+2,x
  pha
  lda.l   _ext_base1_chrtable+0,x
  plx
  jsr.w   _print_char
  iny
  iny

  plx
  jmp     _next_byte


_ext_vwf:
  jsr     _render_ext_glyph
  plx
  jmp     _next_byte


/**
 * Print BAD_CHAR and consume 2 bytes from stream
 */
_bad_wchar:
  plx
  phx
  phy
  lda.w   #BAD_CHAR
  ldx.w   #BAD_CHAR+$10
  jsr.w   _print_char
  ply
  plx
  iny
  iny
  jmp     _next_word


/**
 * Print character (tile numbers in A/X) + attribute
 */
_print_char:
  phy
  clc
  adc.w   param_attribute
  sta.b   [dest_ptr],y
  tya
  adc.b   line_len
  tay
  txa
  adc.w   param_attribute
  sta.b   [dest_ptr],y
  ply
  rts


/**
 * Advance VWF plotter
 *
 * Parameters
 *   A        W Pixels to advance
 *   Y        W Write offset
 */
_vwf_advance:
  and.w   #$000f                    ; Add A to position
  clc
  adc.w   VWF_position & $ffff
  sec
  sbc.w   VWF_neg_kern & $ffff
  sta.w   VWF_position & $ffff

  cmp.w   #8                        ; If VWF_position < 8 don't advance tile position
  bcc     _no_advance

  phy                               ; Write tile map entry
  lda.w   VWF_buffer_head & $ffff   ; (VWF_tilebase_offset + VWF_buffer_head)
  clc
  adc.w   #VWF_tilebase_offset
  lsr     a
  lsr     a
  lsr     a
  lsr     a
  tax
  adc.w   param_attribute
  sta.b   [dest_ptr],y
  tya
  adc.b   line_len
  tay
  txa
  inc     a
  adc.w   param_attribute
  sta.b   [dest_ptr],y

  VWF_buffer_advance $20

  ply                               ; Increment write offset
  iny
  iny

_no_advance:
  lda.w   VWF_position & $ffff      ; Truncate position
  and.w   #$0007
  sta.w   VWF_position & $ffff
  stz.w   VWF_neg_kern & $ffff      ; Reset kern value
  rts


/**
 * Flush current character in VWF plotter
 *
 */
_vwf_flush:
  lda.w   VWF_position & $ffff      ; If VWF_position != 0:
  beq     _no_flush

  phy
  stz.w   VWF_should_clear & $ffff
  stz.w   VWF_position & $ffff
  lda.w   VWF_buffer_head & $ffff   ; Set tile map entry (VWF_tilebase_offset + VWF_buffer_head)
  clc
  adc.w   #VWF_tilebase_offset
  lsr     a
  lsr     a
  lsr     a
  lsr     a
  pha
  clc
  adc.w   param_attribute
  sta.b   [dest_ptr],y
  tya
  adc.b   line_len
  tay
  pla
  inc     a
  adc.w   param_attribute
  sta.b   [dest_ptr],y

  VWF_buffer_advance $20

  ply
  iny
  iny
_no_flush:
  rts


/**
 * Clear left VWF tile
 */
_vwf_clear_left:
  VWF_set_tile_ptr
  lda.w   #$0000
.REPT 16
  sta.b   [VWF_tile_ptr]
  inc.b   VWF_tile_ptr
  inc.b   VWF_tile_ptr
.ENDR
  rts


/**
 * Copy last rendered tile to start of buffer
 */
_vwf_copy_spill:
  pha
  lda.b   VWF_tile_ptr + 1
  sta.b   VWF_font_src + 1
  pla
  clc
  adc.w   #(VWF_buffer & $ffff)
  sta.b   VWF_font_src

  lda.w   #(VWF_buffer & $ffff)
  sta.b   VWF_tile_ptr

.REPT 16
  lda.b   [VWF_font_src]
  sta.b   [VWF_tile_ptr]
  inc.b   VWF_font_src
  inc.b   VWF_font_src
  inc.b   VWF_tile_ptr
  inc.b   VWF_tile_ptr
.ENDR
  rts


/**
 * Render one EXT (3x tiles) glyph
 */
_render_ext_glyph:
  phy
  and.w   #$003F                          ; Put character data offset on stack
  asl     a
  asl     a
  asl     a
  asl     a
  asl     a
  pha
  asl     a
  clc
  adc     1,s
  tax
  pla
  phx

  jsr     _vwf_flush                      ; Always render tile-aligned

  stz.w   VWF_buffer_head & $ffff         ; Potential rare bug fix+optimization: always render these at VFW_buffer location 0
  stz.w   VWF_buffer_dirty_start & $ffff  ; (safe since they are always rendered alone)
  ldy.w   #(VWF_buffer & $ffff)

  A8                                      ; Source bank
  lda.b   #:VWF_font_ext
  sta.w   VWF_block_move_src & $ffff
  A16

  pla                                     ; Source offset
  clc
  adc.w   #(VWF_font_ext & $ffff)
  tax

  lda.w   #$005F                          ; Count & transfer
  phb
  jsr.w   VWF_block_move & $ffff
  plb

  ply                                     ; Tilemap offset
  phy                                     ; Write tile map entries
  lda.w   VWF_buffer_head & $ffff
  clc
  adc.w   #VWF_tilebase_offset
  lsr     a
  lsr     a
  lsr     a
  lsr     a

  tax                                     ; Upper tiles
  clc
  adc.w   param_attribute
  sta.b   [dest_ptr],y
  iny
  iny
  inc     a
  inc     a
  sta.b   [dest_ptr],y
  iny
  iny
  inc     a
  inc     a
  sta.b   [dest_ptr],y

  lda     1,s                             ; Lower tiles
  clc
  adc.b   line_len
  tay
  txa
  inc     a
  adc.w   param_attribute
  sta.b   [dest_ptr],y
  iny
  iny
  inc     a
  inc     a
  sta.b   [dest_ptr],y
  iny
  iny
  inc     a
  inc     a
  sta.b   [dest_ptr],y

  VWF_buffer_advance $60

  ply                                     ; Increment write offset
  iny
  iny

  stz.w   VWF_position & $ffff            ; Reset position
  stz.w   VWF_neg_kern & $ffff            ; and kern value
  rts


;-----------------------------------------------------------------------------
; Data

; Offsets to preshifted font data
_vwf_font_src_offsets:
.DW VWF_font_shift0 & $ffff, VWF_font_shift1 & $ffff, VWF_font_shift2 & $ffff, VWF_font_shift3 & $ffff
.DW VWF_font_shift4 & $ffff, VWF_font_shift5 & $ffff, VWF_font_shift6 & $ffff, VWF_font_shift7 & $ffff,

_vwf_font_src_banks:
.DW :VWF_font_shift0 << 8, :VWF_font_shift1 << 8, :VWF_font_shift2 << 8, :VWF_font_shift3 << 8
.DW :VWF_font_shift4 << 8, :VWF_font_shift5 << 8, :VWF_font_shift6 << 8, :VWF_font_shift7 << 8

; Jumptables for zero-lines optimization
_ascii_blit_left_unroll_jmptable:
.REDEF RI 0
.REPEAT 17
.DW _ascii_blit_left_unroll + ((_ascii_blit_left_unroll_length - _ascii_blit_left_unroll) / 16)  * RI
.REDEF RI RI+1
.ENDR

_ascii_blit_both_unroll_jmptable:
.REDEF RI 0
.REPEAT 17
.DW _ascii_blit_both_unroll + ((_ascii_blit_both_unroll_length - _ascii_blit_both_unroll) / 16)  * RI
.REDEF RI RI+1
.ENDR


;-----------------------------------------------------------------------------
; Character tables for statically allocated extended chars

; Character table for ext_base1
_ext_base1_chrtable:
.DW $0000, $0010 ; 80 = 0
.DW $0001, $0011 ; 81 = 1
.DW $0002, $0012 ; 82 = 2
.DW $0003, $0013 ; 83 = 3
.DW $0004, $0014 ; 84 = 4
.DW $0005, $0015 ; 85 = 5
.DW $0006, $0016 ; 86 = 6
.DW $0007, $0017 ; 87 = 7
.DW $0008, $0018 ; 88 = 8
.DW $0009, $0019 ; 89 = 9

.DW $005F, $002B ; 8A = + (8x8 aligned)
.DW $005F, $002C ; 8B = - (8x8 aligned)
.DW $005F, $003C ; 8C = x (8x8 aligned)
.DW $005F, $002A ; 8D = ∞ (8x8 aligned)
.DW $003E, $003F ; 8E = / (8x16 aligned)
.DW $005F, $002D ; 8F = - (8x16 aligned)

.DW $005F, $0074 ; 90 = Red Star 3
.DW $006E, $007E ; 91 = Green Earth 4
.DW $0044, $0054 ; 92 = Yellow Comet 4

.DW $00A4, $00A5 ; 93 = Rogenski 3
.DW $005F, $00B4 ; 94 = Caroline 3

.DW $005F, $004A ; 95 = Small 'P'
.DW $005F, $0046 ; 96 = .. (2x small dots, 8x16 aligned)
.DW $005F, $0056 ; 97 = -  (shorter 8x16 aligned)
.DW $0045, $0055 ; 98 = ?  (8x16 aligned)


; Character table for ext_base2
_ext_base2_chrtable:
.DW $000A, $001A, $000B, $001B ; C0 = O toggle
.DW $000C, $001C, $000D, $001D ; C1 = X toggle
.DW $005F, $002E, $005F, $002F ; C2 = ∞ (unit info ammo)
.DW $000E, $001E, $000F, $001F ; C3 = large ∞ (unit intel)

.DW $0060, $0070, $0061, $0071 ; C4 = Red Star 1
.DW $0062, $0072, $0063, $0073 ; C5 = Red Star 2

.DW $0065, $0075, $005F, $0064 ; C6 = Blue Moon 1
.DW $0066, $0076, $0067, $0077 ; C7 = Blue Moon 2
.DW $005F, $0078, $005F, $0068 ; C8 = Blue Moon 3

.DW $0069, $0079, $005F, $007A ; C9 = Green Earth 1
.DW $005F, $006A, $006B, $007B ; CA = Green Earth 2
.DW $006C, $007C, $006D, $007D ; CB = Green Earth 3

.DW $008C, $007F, $0040, $0050 ; CC = Yellow Comet 1
.DW $005F, $0051, $0042, $0052 ; CD = Yellow Comet 2
.DW $0043, $0053, $005F, $0041 ; CE = Yellow Comet 3

.DW $005F, $005F, $005F, $005F ; CF = Intentionally left blank

.DW $0080, $0081, $0082, $0083 ; D0 = Mr. Yamamoto 1
.DW $0084, $0085, $005F, $0086 ; D1 = Mr. Yamamoto 2
.DW $005F, $0087, $005F, $0088 ; D2 = Mr. Yamamoto 3
.DW $0089, $008A, $005F, $008B ; D3 = Mr. Yamamoto 4

.DW $008C, $008D, $005F, $008E ; D4 = Yuan Delta 1
.DW $005F, $008F, $0090, $0091 ; D5 = Yuan Delta 2
.DW $0092, $0093, $0094, $0095 ; D6 = Yuan Delta 3

.DW $0096, $0097, $005F, $0098 ; D7 = Von Rosso 1
.DW $0099, $009A, $009B, $009C ; D8 = Von Rosso 2
.DW $005F, $009D, $005F, $009E ; D9 = Von Rosso 3

.DW $009F, $00A0, $005F, $00A1 ; DA = Rogenski 1
.DW $005F, $00A2, $005F, $00A3 ; DB = Rogenski 2

.DW $00A6, $00A7, $00A8, $00A9 ; DC = Hetler 1
.DW $00AA, $00AB, $005F, $00AC ; DD = Hetler 2

.DW $00AD, $00AE, $005F, $00AF ; DE = Caroline 1
.DW $00B0, $00B1, $00B2, $00B3 ; DF = Caroline 2

.DW $00B5, $00B6, $00B7, $00B8 ; E0 = Billy Gates 1
.DW $00B9, $00BA, $00BB, $00BC ; E1 = Billy Gates 2
.DW $00BD, $00BE, $005F, $00BF ; E2 = Billy Gates 3

.ENDS
