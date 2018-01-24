; Super Famicom Wars Translation Project
; R&D by David Lindecrantz <optiroc@gmail.com>

;-----------------------------------------------------------------------------
; Quality of Life additions


;-----------------------------------------------------------------------------
; Key repeat adjustments

.EQU ZP_KEYREPEAT $E2
.EQU KEYREPEAT_default 4
.EQU KEYREPEAT_deploymenu 1

; Deploy menu: Init
.EQU DEPLOYMENU_init_hook $87D23B
.BANK (DEPLOYMENU_init_hook >> 16) & $7f SLOT ROMSLOT
.BASE (DEPLOYMENU_init_hook >> 16) & $80
.ORGA DEPLOYMENU_init_hook & $ffff
.SECTION "DEPLOYMENU_init_patch" OVERWRITE
  jsr.w   DEPLOYMENU_init_new
.ENDS

.BANK (DEPLOYMENU_init_hook >> 16) & $7f SLOT ROMSLOT
.BASE (DEPLOYMENU_init_hook >> 16) & $80
.SECTION "DEPLOYMENU_init_new" FREE
.ACCU 16
.INDEX 16
DEPLOYMENU_init_new:
  pha
  lda.w   #KEYREPEAT_deploymenu
  sta.b   ZP_KEYREPEAT
  pla
  jmp.w   $BB39
.ENDS

; Deploy menu: Cancel
.EQU DEPLOYMENU_cancel_hook $87D2D8
.BANK (DEPLOYMENU_cancel_hook >> 16) & $7f SLOT ROMSLOT
.BASE (DEPLOYMENU_cancel_hook >> 16) & $80
.ORGA DEPLOYMENU_cancel_hook & $ffff
.SECTION "DEPLOYMENU_cancel_patch" OVERWRITE
  jmp.w   DEPLOYMENU_cancel_new
DEPLOYMENU_cancel_hook_exit:
.ENDS

.BANK (DEPLOYMENU_cancel_hook >> 16) & $7f SLOT ROMSLOT
.BASE (DEPLOYMENU_cancel_hook >> 16) & $80
.SECTION "DEPLOYMENU_cancel_new" FREE
.ACCU 16
.INDEX 16
DEPLOYMENU_cancel_new:
  lda.w   #KEYREPEAT_default
  sta.b   ZP_KEYREPEAT
  lda.w   #$001D
  jmp.w   DEPLOYMENU_cancel_hook_exit
.ENDS

; Deploy menu: Buy
.EQU DEPLOYMENU_buy_hook $87D510
.BANK (DEPLOYMENU_buy_hook >> 16) & $7f SLOT ROMSLOT
.BASE (DEPLOYMENU_buy_hook >> 16) & $80
.ORGA DEPLOYMENU_buy_hook & $ffff
.SECTION "DEPLOYMENU_buy_patch" OVERWRITE
  jmp.w   DEPLOYMENU_buy_new
DEPLOYMENU_buy_hook_exit:
.ENDS

.BANK (DEPLOYMENU_buy_hook >> 16) & $7f SLOT ROMSLOT
.BASE (DEPLOYMENU_buy_hook >> 16) & $80
.SECTION "DEPLOYMENU_buy_new" FREE
.ACCU 16
.INDEX 16
DEPLOYMENU_buy_new:
  lda.w   #KEYREPEAT_default
  sta.b   ZP_KEYREPEAT
  lda.w   #$0001
  jmp.w   DEPLOYMENU_buy_hook_exit
.ENDS

; Deploy menu: AI buy
.EQU DEPLOYMENU_ai_buy_hook $87D556
.BANK (DEPLOYMENU_ai_buy_hook >> 16) & $7f SLOT ROMSLOT
.BASE (DEPLOYMENU_ai_buy_hook >> 16) & $80
.ORGA DEPLOYMENU_ai_buy_hook & $ffff
.SECTION "DEPLOYMENU_ai_buy_patch" OVERWRITE
  jmp.w   DEPLOYMENU_ai_buy_new
DEPLOYMENU_ai_buy_hook_exit:
.ENDS

.BANK (DEPLOYMENU_ai_buy_hook >> 16) & $7f SLOT ROMSLOT
.BASE (DEPLOYMENU_ai_buy_hook >> 16) & $80
.SECTION "DEPLOYMENU_ai_buy_new" FREE
.ACCU 16
.INDEX 16
DEPLOYMENU_ai_buy_new:
  lda.w   #KEYREPEAT_default
  sta.b   ZP_KEYREPEAT
  lda.w   #$0001
  jmp.w   DEPLOYMENU_ai_buy_hook_exit
.ENDS
