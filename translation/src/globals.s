; Super Famicom Wars Translation Project
; R&D by David Lindecrantz <optiroc@gmail.com>

;--------------------------------------------------------------------
; Global defines

; Destination banks for new code
.DEFINE main_code_bank      $80

; VWF renderer constants
.EQU VWF_tilebase_offset    $0C00
.EQU VWF_buffer_size        $2000
.EQU VWF_buffer_sizemask    $1FFF


;--------------------------------------------------------------------
; Global RAM usage
; Unused stack          001E30-001EFF (or so...)
; Unused WRAM           7EF300-7EFFFF
; Unused SRAM           703600-707FFF

.DEFINE VWF_buffer                    $F06000
.DEFINE SRAM_version_stamp            $F05FF0


; WRAM variables
; WLA RAMSECTIONs are terrible, let's just define the addresses
; (and then I couldn't even get WLA's macros to do the work for me...)

.DEFINE RAM_base                      $801E30
.DEFINE RAM_used                      0
.DEFINE RAM_loc                       RAM_base

.DEFINE VWF_VRAM_tilebase             RAM_loc
.DEFINE VWF_VRAM_tilebase_size        $2
.REDEFINE RAM_loc RAM_loc + VWF_VRAM_tilebase_size

.DEFINE VWF_buffer_head               RAM_loc
.DEFINE VWF_buffer_head_size          $2
.REDEFINE RAM_loc RAM_loc + VWF_buffer_head_size

.DEFINE VWF_buffer_dirty_start        RAM_loc
.DEFINE VWF_buffer_dirty_start_size   $2
.REDEFINE RAM_loc RAM_loc + VWF_buffer_dirty_start_size

.DEFINE VWF_buffer_dirty_end          RAM_loc
.DEFINE VWF_buffer_dirty_end_size     $2
.REDEFINE RAM_loc RAM_loc + VWF_buffer_dirty_end_size

.DEFINE VWF_block_move                RAM_loc
.DEFINE VWF_block_move_dst            RAM_loc + 1
.DEFINE VWF_block_move_src            RAM_loc + 2
.DEFINE VWF_block_move_rts            RAM_loc + 3
.DEFINE VWF_block_move_size           $4
.REDEFINE RAM_loc RAM_loc + VWF_block_move_size

.DEFINE VWF_should_clear              RAM_loc
.DEFINE VWF_should_clear_size         $2
.REDEFINE RAM_loc RAM_loc + VWF_should_clear_size

.DEFINE VWF_position                  RAM_loc
.DEFINE VWF_position_size             $2
.REDEFINE RAM_loc RAM_loc + VWF_position_size

.DEFINE VWF_neg_kern                  RAM_loc
.DEFINE VWF_neg_kern_size             $2
.REDEFINE RAM_loc RAM_loc + VWF_neg_kern_size

.DEFINE HDMA_FLAGS_last_value         RAM_loc
.DEFINE HDMA_FLAGS_last_value_size    $2
.REDEFINE RAM_loc RAM_loc + HDMA_FLAGS_last_value_size

.DEFINE TITLE_should_init             RAM_loc
.DEFINE TITLE_should_init_size        $2
.REDEFINE RAM_loc RAM_loc + TITLE_should_init_size

.DEFINE TITLE_counter                 RAM_loc
.DEFINE TITLE_counter_size            $2
.REDEFINE RAM_loc RAM_loc + TITLE_counter_size

.DEFINE TITLE_wait_period             RAM_loc
.DEFINE TITLE_wait_period_size        $2
.REDEFINE RAM_loc RAM_loc + TITLE_wait_period_size


;--------------------------------------------------------------------
; System memory locations

.EQU tmp_1                  $0B
.EQU tmp_2                  $0D
.EQU tmp_3                  $0F
.EQU tmp_4                  $11
.EQU tmp_5                  $13
.EQU tmp_6                  $15

.EQU source_ptr             $2F
.EQU source_ptr_H           $30
.EQU source_ptr_B           $31
.EQU dest_ptr               $3E
.EQU dest_ptr_H             $3F
.EQU dest_ptr_B             $40

.EQU ZP_INIDISP             $7B
.EQU ZP_HDMA_FLAGS          $C1
.EQU ZP_VBL_handler_flag    $D9
.EQU ZP_NMI_shtick          $DD

.EQU UX_SYS_boxdef_ptr_L    $0F51
.EQU UX_SYS_boxdef_ptr_H    $0F52
.EQU UX_SYS_boxdef_ptr_B    $0F53
.EQU UX_SYS_boxdim_ptr_L    $0F54
.EQU UX_SYS_boxdim_ptr_H    $0F55
.EQU UX_SYS_boxdim_ptr_B    $0F56

.EQU param_attribute        $0F5D
.EQU param_empty_char       $0F5F


;--------------------------------------------------------------------
; System calls

; Add DMA job
; Parameters
;   $2F      L  Source address
;   $0B      W  Length
;   $0D      W  Destination (VRAM word offset)
.DEFINE SYS_DMA_add           $80B4B6
.DEFINE SYS_DMA_add_deferred  $80B503

; Add UNPACK job (decode LZN stream)
; Parameters
;   $2F      L Source pointer
;   $32      L Destination pointer
.DEFINE SYS_UNPACK_add        $80B5C7

; OAM_buffer_add
; Add entries to OAM buffer (1C00-1E1F) from definition list
; Parameters
;   Y        W OBJ definition list offset
;   $0B      W Added to x-coordinate
;   $0D      W Added to y-coordinate
;   $13      W Added to "tile # / attributes" word
;   $15      W OR:ed to "tile # / attributes" word
;
; The definition list starts with one word specifying the number of definitions,
; followed by an array of definitions 5 bytes each.
;
; OBJ definition:
; 0  W X-coordinate     (lower 12 bits)
;      OBJ size         (bit 15)
; 2  B Y-coordinate
; 3  W Tile #           (lower 9 bits)
;      Palette #        (bits 10-12)
;      H-flip           (bit 14)
;      V-flip           (bit 15)
.DEFINE OAM_buffer_add        $808879

.DEFINE TXT_decode_string     $879E01
.DEFINE TXT_print_small_char  $8797D7
.DEFINE UX_TXT_print_strings  $87B538

.DEFINE MAIN_runloop_jump     $808B1E
.DEFINE SYS_PPU_screen_on     $8081A8
.DEFINE SYS_DMA_add_inline    $80B3EB
.DEFINE DMA_set_hdma          $80B253
.DEFINE DMA_set_offsets       $82C199
.DEFINE VBLTASKS_iterate      $80ABB5
.DEFINE VBLTASK3              $82C0F9
.DEFINE VBL_UP_smp            $808CCC

