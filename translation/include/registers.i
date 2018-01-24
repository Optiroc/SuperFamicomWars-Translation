; Super Famicom Wars Translation
;--------------------------------------------------------------------
; Hardware Registers

.DEFINE INIDISP                 $2100 ;Display Control
.DEFINE OBJSEL                  $2101 ;Object Size + Object Base
.DEFINE OAMADDL                 $2102 ;OAM Address (LSB)
.DEFINE OAMADDH                 $2103 ;OAM Address (MSB) + Priority Rotation
.DEFINE OAMDATA                 $2104 ;OAM Data Write (write-twice)
.DEFINE BGMODE                  $2105 ;BG Mode + BG Character Size
.DEFINE MOSAIC                  $2106 ;Mosaic Size + Mosaic Enable

.DEFINE BG1SC                   $2107 ;BG1 Screen Base + Screen Size
.DEFINE BG2SC                   $2108 ;BG2 Screen Base + Screen Size
.DEFINE BG3SC                   $2109 ;BG3 Screen Base + Screen Size
.DEFINE BG4SC                   $210a ;BG4 Screen Base + Screen Size
.DEFINE BG12NBA                 $210b ;BG1/2 Character Data Area Designation
.DEFINE BG34NBA                 $210c ;BG3/4 Character Data Area Designation

.DEFINE BG1HOFS                 $210d ;BG1 Horizontal Scroll (write-twice) / M7HOFS
.DEFINE BG1VOFS                 $210e ;BG1 Vertical Scroll (write-twice) / M7VOFS
.DEFINE BG2HOFS                 $210f ;BG2 Horizontal Scroll (write-twice)
.DEFINE BG2VOFS                 $2110 ;BG2 Vertical Scroll (write-twice)
.DEFINE BG3HOFS                 $2111 ;BG3 Horizontal Scroll (write-twice)
.DEFINE BG3VOFS                 $2112 ;BG3 Vertical Scroll (write-twice)
.DEFINE BG4HOFS                 $2113 ;BG4 Horizontal Scroll (write-twice)
.DEFINE BG4VOFS                 $2114 ;BG4 Vertical Scroll (write-twice)

.DEFINE VMAINC                  $2115 ;VRAM Address Increment Mode
.DEFINE VMADDL                  $2116 ;VRAM Address (LSB)
.DEFINE VMADDH                  $2117 ;VRAM Address (MSB)
.DEFINE VMDATAL                 $2118 ;VRAM Data Write (LSB)
.DEFINE VMDATAH                 $2119 ;VRAM Data Write (MSB)

.DEFINE M7SEL                   $211a ;Rotation/Scaling Mode Settings
.DEFINE M7A                     $211b ;Rotation/Scaling Parameter A (write-twice) / Maths 16-bit operand
.DEFINE M7B                     $211c ;Rotation/Scaling Parameter B (write-twice) / Maths 8-bit operand
.DEFINE M7C                     $211d ;Rotation/Scaling Parameter C (write-twice)
.DEFINE M7D                     $211e ;Rotation/Scaling Parameter D (write-twice)
.DEFINE M7X                     $211f ;Rotation/Scaling Center Coordinate X (write-twice)
.DEFINE M7Y                     $2120 ;Rotation/Scaling Center Coordinate Y (write-twice)

.DEFINE CGADD                   $2121 ;CGRAM Address
.DEFINE CGDATA                  $2122 ;CGRAM Data Write (write-twice)

.DEFINE W12SEL                  $2123 ;Window Mask Settings (BG1/2)
.DEFINE W34SEL                  $2124 ;Window Mask Settings (BG3/4)
.DEFINE WOBJSEL                 $2125 ;Window Mask Settings (OBJ/COLOR)

.DEFINE WH0                     $2126 ;Window 1 Left Position
.DEFINE WH1                     $2127 ;Window 1 Right Position
.DEFINE WH2                     $2128 ;Window 2 Left Position
.DEFINE WH3                     $2129 ;Window 2 Right Position
.DEFINE WBGLOG                  $212a ;Window 1/2 Mask Logic Settings (BG1-4)
.DEFINE WOBJLOG                 $212b ;Window 1/2 Mask Logic Settings (OBJ/MATH)

.DEFINE TM                      $212c ;Main Screen Designation
.DEFINE TS                      $212d ;Sub Screen Designation
.DEFINE TMW                     $212e ;Window Mask Designation for Main Screen
.DEFINE TSW                     $212f ;Window Mask Designation for Sub Screen

.DEFINE CGSWSEL                 $2130 ;Initial settings for fixed color/screen addition
.DEFINE CGADSUB                 $2131 ;Addition/Subtraction Designation
.DEFINE COLDATA                 $2132 ;Fixed Color Data

.DEFINE SETINI                  $2133 ;Display Control
.DEFINE MPYL                    $2134 ;PPU1 Signed Multiply Result (lower 8-bit)
.DEFINE MPYM                    $2135 ;PPU1 Signed Multiply Result (middle 8-bit)
.DEFINE MPYH                    $2136 ;PPU1 Signed Multiply Result (upper 8-bit)
.DEFINE SLHV                    $2137 ;PPU1 Latch H/V-Counter

.DEFINE OAMDATAREAD             $2138 ;PPU1 OAM Data Read
.DEFINE VMDATALREAD             $2139 ;PPU1 VRAM Data Read (LSB)
.DEFINE VMDATAHREAD             $213a ;PPU1 VRAM Data Read (MSB)
.DEFINE CGDATAREAD              $213b ;PPU2 CGRAM Data Read (read-twice)
.DEFINE OPHCT                   $213c ;PPU2 Horizontal Counter Latch (read-twice)
.DEFINE OPVCT                   $213d ;PPU2 Vertical Counter Latch (read-twice)
.DEFINE STAT77                  $213e ;PPU1 Status/Versionr
.DEFINE STAT78                  $213f ;PPU2 Status/Version
.DEFINE APUIO0                  $2140 ;Sound CPU Communication Port 0
.DEFINE APUIO1                  $2141 ;Sound CPU Communication Port 1
.DEFINE APUIO2                  $2142 ;Sound CPU Communication Port 2
.DEFINE APUIO3                  $2143 ;Sound CPU Communication Port 4

.DEFINE WMDATA                  $2180 ;WRAM Data Read/Write
.DEFINE WMADDL                  $2181 ;WRAM Address (lower 8-bit)
.DEFINE WMADDM                  $2182 ;WRAM Address (middle 8-bit)
.DEFINE WMADDH                  $2183 ;WRAM Address (upper 1-bit)

.DEFINE JOYFCL                  $4016 ;Joypad Input Register (LSB)
.DEFINE JOYFCH                  $4017 ;Joypad Input Register (MSB)

.DEFINE NMITIMEN                $4200 ;Interrupt Enable / Joypad Request
.DEFINE WRIO                    $4201 ;Joypad Programmable I/O Port
.DEFINE WRMPYA                  $4202 ;Unsigned 8-bit Multiplicand
.DEFINE WRMPYB                  $4203 ;Unsigned 8-bit Multiplier
.DEFINE WRDIVL                  $4204 ;Unsigned 16-bit Dividend (LSB)
.DEFINE WRDIVH                  $4205 ;Unsigned 16-bit Dividend (MSB)
.DEFINE WRDIVB                  $4206 ;Unsigned 8-bit Divisor
.DEFINE HTIMEL                  $4207 ;H-Count Timer Setting (LSB)
.DEFINE HTIMEH                  $4208 ;H-Count Timer Setting (MSB)
.DEFINE VTIMEL                  $4209 ;V-Count Timer Setting (LSB)
.DEFINE VTIMEH                  $420a ;V-Count Timer Setting (MSB)
.DEFINE MDMAEN                  $420b ;General Purpose DMA Channel Designation & Trigger
.DEFINE HDMAEN                  $420c ;H-DMA Channel Designation
.DEFINE MEMSEL                  $420d ;Access Cycle Designation

.DEFINE RDNMI                   $4210 ;V-Blank NMI Flag / CPU Version Number
.DEFINE TIMEUP                  $4211 ;H/V-Timer IRQ Flag
.DEFINE HVBJOY                  $4212 ;H/V-Blank Flag / Joypad Busy Flag
.DEFINE RDIO                    $4213 ;Joypad Programmable I/O Port
.DEFINE RDDIVL                  $4214 ;Unsigned Division Result (Quotient) (LSB)
.DEFINE RDDIVH                  $4215 ;Unsigned Division Result (Quotient) (MSB)
.DEFINE RDMPYL                  $4216 ;Unsigned Division Remainder / Multiply Product (LSB)
.DEFINE RDMPYH                  $4217 ;Unsigned Division Remainder / Multiply Product (MSB)

.DEFINE JOY1L                   $4218 ;Joypad 1 (LSB)
.DEFINE JOY1H                   $4219 ;Joypad 1 (MSB)
.DEFINE JOY2L                   $421a ;Joypad 2 (LSB)
.DEFINE JOY2H                   $421b ;Joypad 2 (MSB)
.DEFINE JOY3L                   $421c ;Joypad 3 (LSB)
.DEFINE JOY3H                   $421d ;Joypad 3 (MSB)
.DEFINE JOY4L                   $421e ;Joypad 4 (LSB)
.DEFINE JOY4H                   $421f ;Joypad 4 (MSB)

.DEFINE DMAP0                   $4300 ;DMA Parameters
.DEFINE BBAD0                   $4301 ;DMA I/O-Bus Address (B-Bus)
.DEFINE A1T0L                   $4302 ;HDMA Table Start Address / DMA Current Address (LSB)
.DEFINE A1T0H                   $4303 ;HDMA Table Start Address / DMA Current Address (MSB)
.DEFINE A1B0                    $4304 ;HDMA Table Start Address / DMA Current Address (BANK)
.DEFINE DAS0L                   $4305 ;Indirect HDMA Address / DMA Byte-Counter (LSB)
.DEFINE DAS0H                   $4306 ;Indirect HDMA Address / DMA Byte-Counter (MSB)
.DEFINE DASB0                   $4307 ;Indirect HDMA Address (BANK)
.DEFINE A2A0L                   $4308 ;HDMA Table Current Address (LSB)
.DEFINE A2A0H                   $4309 ;HDMA Table Current Address (MSB)
.DEFINE NTRL0                   $430a ;HDMA Line-Counter

.DEFINE DMAP1                   $4310
.DEFINE BBAD1                   $4311
.DEFINE A1T1L                   $4312
.DEFINE A1T1H                   $4313
.DEFINE A1B1                    $4314
.DEFINE DAS1L                   $4315
.DEFINE DAS1H                   $4316
.DEFINE DASB1                   $4317
.DEFINE A2A1L                   $4318
.DEFINE A2A1H                   $4319
.DEFINE NTRL1                   $431a

.DEFINE DMAP2                   $4320
.DEFINE BBAD2                   $4321
.DEFINE A1T2L                   $4322
.DEFINE A1T2H                   $4323
.DEFINE A1B2                    $4324
.DEFINE DAS2L                   $4325
.DEFINE DAS2H                   $4326
.DEFINE DASB2                   $4327
.DEFINE A2A2L                   $4328
.DEFINE A2A2H                   $4329
.DEFINE NTRL2                   $432a

.DEFINE DMAP3                   $4330
.DEFINE BBAD3                   $4331
.DEFINE A1T3L                   $4332
.DEFINE A1T3H                   $4333
.DEFINE A1B3                    $4334
.DEFINE DAS3L                   $4335
.DEFINE DAS3H                   $4336
.DEFINE DASB3                   $4337
.DEFINE A2A3L                   $4338
.DEFINE A2A3H                   $4339
.DEFINE NTRL3                   $433a

.DEFINE DMAP4                   $4340
.DEFINE BBAD4                   $4341
.DEFINE A1T4L                   $4342
.DEFINE A1T4H                   $4343
.DEFINE A1B4                    $4344
.DEFINE DAS4L                   $4345
.DEFINE DAS4H                   $4346
.DEFINE DASB4                   $4347
.DEFINE A2A4L                   $4348
.DEFINE A2A4H                   $4349
.DEFINE NTRL4                   $434a

.DEFINE DMAP5                   $4350
.DEFINE BBAD5                   $4351
.DEFINE A1T5L                   $4352
.DEFINE A1T5H                   $4353
.DEFINE A1B5                    $4354
.DEFINE DAS5L                   $4355
.DEFINE DAS5H                   $4356
.DEFINE DASB5                   $4357
.DEFINE A2A5L                   $4358
.DEFINE A2A5H                   $4359
.DEFINE NTRL5                   $435a

.DEFINE DMAP6                   $4360
.DEFINE BBAD6                   $4361
.DEFINE A1T6L                   $4362
.DEFINE A1T6H                   $4363
.DEFINE A1B6                    $4364
.DEFINE DAS6L                   $4365
.DEFINE DAS6H                   $4366
.DEFINE DASB6                   $4367
.DEFINE A2A6L                   $4368
.DEFINE A2A6H                   $4369
.DEFINE NTRL6                   $436a

.DEFINE DMAP7                   $4370
.DEFINE BBAD7                   $4371
.DEFINE A1T7L                   $4372
.DEFINE A1T7H                   $4373
.DEFINE A1B7                    $4374
.DEFINE DAS7L                   $4375
.DEFINE DAS7H                   $4376
.DEFINE DASB7                   $4377
.DEFINE A2A7L                   $4378
.DEFINE A2A7H                   $4379
.DEFINE NTRL7                   $437a


;--------------------------------------------------------------------
; Hardware Register Bitmasks & Constants

;INIDISP
.DEFINE DISP_BLANKING_MASK      $7f
.DEFINE DISP_BRIGHTNESS_MASK    $f0

.DEFINE DISP_BLANKING_SHIFT     $07
.DEFINE DISP_BLANKING_ON        $80
.DEFINE DISP_BLANKING_OFF       $00

;OBJSEL
.DEFINE OBJ_NAME_MASK           $e0
.DEFINE OBJ_SIZE_MASK           $1f

.DEFINE OBJ_NAME_SHIFT          $00
.DEFINE OBJ_SIZE_SHIFT          $05

.DEFINE OBJ_8x8_16x16           $00
.DEFINE OBJ_8x8_32x32           $20
.DEFINE OBJ_8x8_64x64           $40
.DEFINE OBJ_16x16_32x32         $60
.DEFINE OBJ_16x16_64x64         $80
.DEFINE OBJ_32x32_64x64         $a0

;BGMODE
.DEFINE BG_MODE_MASK            $f8
.DEFINE BG_BG3_MAX_PRIO_MASK    $f7
.DEFINE BG_SIZE_MASK            $0f

.DEFINE BG_MODE_SHIFT           $00
.DEFINE BG_BG3_MAX_PRIO_SHIFT   $03
.DEFINE BG_SIZE_SHIFT           $04

.DEFINE BG_MODE_0               $00
.DEFINE BG_MODE_1               $01
.DEFINE BG_MODE_2               $02
.DEFINE BG_MODE_3               $03
.DEFINE BG_MODE_4               $04
.DEFINE BG_MODE_5               $05
.DEFINE BG_MODE_6               $06
.DEFINE BG_MODE_7               $07
.DEFINE BG_BG3_MAX_PRIO         $08

;MOSAIC
.DEFINE MOS_ENBL_MASK           $f0
.DEFINE MOS_SIZE_MASK           $0f
.DEFINE MOS_BG1_ON_MASK         $fe
.DEFINE MOS_BG2_ON_MASK         $fd
.DEFINE MOS_BG3_ON_MASK         $fb
.DEFINE MOS_BG4_ON_MASK         $f7

.DEFINE MOS_SIZE_SHIFT          $04
.DEFINE MOS_BG1_ON_SHIFT        $00
.DEFINE MOS_BG2_ON_SHIFT        $01
.DEFINE MOS_BG3_ON_SHIFT        $02
.DEFINE MOS_BG4_ON_SHIFT        $03

.DEFINE BG1_MOS_ON              $01
.DEFINE BG2_MOS_ON              $02
.DEFINE BG3_MOS_ON              $04
.DEFINE BG4_MOS_ON              $08

;BGSC (BG1SC/BG2SC/BG3SC/BG4SC)
.DEFINE SC_SIZE_MASK            $fc
.DEFINE SC_BASE_MASK            $03
.DEFINE SC_SIZE_SHIFT           $00
.DEFINE SC_BASE_SHIFT           $02

.DEFINE SC_SIZE_0               $00
.DEFINE SC_SIZE_1               $01
.DEFINE SC_SIZE_2               $02
.DEFINE SC_SIZE_3               $03

;BGNBA (BG12NBA/BG34NBA)
.DEFINE BG_NBA1_MASK            $f0
.DEFINE BG_BNA2_MASK            $0f
.DEFINE BG_NBA1_SHIFT           $00
.DEFINE BG_NBA2_SHIFT           $04

;VMAINC
.DEFINE VMA_TIMING_MASK         $7f
.DEFINE VMA_MODE_MASK           $f0
.DEFINE VMA_TIMING_SHIFT        $07
.DEFINE VMA_MODE_SHIFT          $00

.DEFINE VMA_TIMING_0            $00
.DEFINE VMA_TIMING_1            $80
.DEFINE VMA_MODE_1x1            $00
.DEFINE VMA_MODE_32x32          $01
.DEFINE VMA_MODE_64x64          $02
.DEFINE VMA_MODE_128x128        $03
.DEFINE VMA_MODE_8x32           $04
.DEFINE VMA_MODE_8x64           $05
.DEFINE VMA_MODE_8x128          $06

;M7SEL
.DEFINE M7_FLIP_MASK            $fc
.DEFINE M7_OVER_MASK            $3f

.DEFINE M7_FLIP_SHIFT           $00
.DEFINE M7_OVER_SHIFT           $06

.DEFINE M7_FLIP_NONE            $00
.DEFINE M7_FLIP_H               $01
.DEFINE M7_FLIP_V               $02
.DEFINE M7_FLIP_HV              $03
.DEFINE M7_OVER_SC_REP          $00
.DEFINE M7_OVER_CHR_REP         $80
.DEFINE M7_OVER_COL             $c0

;WSEL (W12SEL/W34SEL/WOBJSEL)
.DEFINE WM1_W1_AREA_MASK        $fe
.DEFINE WM1_W1_ON_MASK          $fd
.DEFINE WM1_W2_AREA_MASK        $fb
.DEFINE WM1_W2_ON_MASK          $f7
.DEFINE WM2_W1_AREA_MASK        $ef
.DEFINE WM2_W1_ON_MASK          $df
.DEFINE WM2_W2_AREA_MASK        $bf
.DEFINE WM2_W2_ON_MASK          $7f

.DEFINE WM1_W1_AREA_SHIFT       $00
.DEFINE WM1_W1_ON_SHIFT         $01
.DEFINE WM1_W2_AREA_SHIFT       $02
.DEFINE WM1_W2_ON_SHIFT         $03
.DEFINE WM2_W1_AREA_SHIFT       $04
.DEFINE WM2_W1_ON_SHIFT         $05
.DEFINE WM2_W2_AREA_SHIFT       $06
.DEFINE WM2_W2_ON_SHIFT         $07

.DEFINE WM1_W1_AREA_IN          $00
.DEFINE WM1_W1_AREA_OUT         $01
.DEFINE WM1_W1_ON               $02
.DEFINE WM1_W1_OFF              $00
.DEFINE WM1_W2_AREA_IN          $00
.DEFINE WM1_W2_AREA_OUT         $04
.DEFINE WM1_W2_ON               $08
.DEFINE WM1_W2_OFF              $00

.DEFINE WM2_W1_AREA_IN          $00
.DEFINE WM2_W1_AREA_OUT         $10
.DEFINE WM2_W1_ON               $20
.DEFINE WM2_W1_OFF              $00
.DEFINE WM2_W2_AREA_IN          $00
.DEFINE WM2_W2_AREA_OUT         $40
.DEFINE WM2_W2_ON               $80
.DEFINE WM2_W2_OFF              $00

;WBGLOG/WOBJLOG
.DEFINE WL_BG1_MASK             $fc
.DEFINE WL_BG2_MASK             $f3
.DEFINE WL_BG3_MASK             $cf
.DEFINE WL_BG4_MASK             $3f
.DEFINE WL_OBJ_MASK             $fc
.DEFINE WL_COLR_MASK            $f3

.DEFINE WL_BG1_SHIFT            $00
.DEFINE WL_BG2_SHIFT            $02
.DEFINE WL_BG3_SHIFT            $04
.DEFINE WL_BG4_SHIFT            $06
.DEFINE WL_OBJ_SHIFT            $00
.DEFINE WL_COLR_SHIFT           $02

.DEFINE WL_OR                   $00
.DEFINE WL_AND                  $01
.DEFINE WL_XOR                  $02
.DEFINE WL_XNOR                 $03

.DEFINE WL_BG1_OR               WL_OR<<WL_BG1_SHIFT
.DEFINE WL_BG1_AND              WL_AND<<WL_BG1_SHIFT
.DEFINE WL_BG1_XOR              WL_XOR<<WL_BG1_SHIFT
.DEFINE WL_BG1_XNOR             WL_XNOR<<WL_BG1_SHIFT

.DEFINE WL_BG2_OR               WL_OR<<WL_BG2_SHIFT
.DEFINE WL_BG2_AND              WL_AND<<WL_BG2_SHIFT
.DEFINE WL_BG2_XOR              WL_XOR<<WL_BG2_SHIFT
.DEFINE WL_BG2_XNOR             WL_XNOR<<WL_BG2_SHIFT

.DEFINE WL_BG3_OR               WL_OR<<WL_BG3_SHIFT
.DEFINE WL_BG3_AND              WL_AND<<WL_BG3_SHIFT
.DEFINE WL_BG3_XOR              WL_XOR<<WL_BG3_SHIFT
.DEFINE WL_BG3_XNOR             WL_XNOR<<WL_BG3_SHIFT

.DEFINE WL_BG4_OR               WL_OR<<WL_BG4_SHIFT
.DEFINE WL_BG4_AND              WL_AND<<WL_BG4_SHIFT
.DEFINE WL_BG4_XOR              WL_XOR<<WL_BG4_SHIFT
.DEFINE WL_BG4_XNOR             WL_XNOR<<WL_BG4_SHIFT

.DEFINE WL_OBJ_OR               WL_OR<<WL_OBJ_SHIFT
.DEFINE WL_OBJ_AND              WL_AND<<WL_OBJ_SHIFT
.DEFINE WL_OBJ_XOR              WL_XOR<<WL_OBJ_SHIFT
.DEFINE WL_OBJ_XNOR             WL_XNOR<<WL_OBJ_SHIFT

.DEFINE WL_COLR_OR              WL_OR<<WL_COLR_SHIFT
.DEFINE WL_COLR_AND             WL_AND<<WL_COLR_SHIFT
.DEFINE WL_COLR_XOR             WL_XOR<<WL_COLR_SHIFT
.DEFINE WL_COLR_XNOR            WL_XNOR<<WL_COLR_SHIFT

;TM
.DEFINE TM_BG1_MASK             $fe
.DEFINE TM_BG2_MASK             $fd
.DEFINE TM_BG3_MASK             $fb
.DEFINE TM_BG4_MASK             $f7
.DEFINE TM_OBJ_MASK             $ef

.DEFINE TM_BG1_SHIFT            $00
.DEFINE TM_BG2_SHIFT            $01
.DEFINE TM_BG3_SHIFT            $02
.DEFINE TM_BG4_SHIFT            $03
.DEFINE TM_OBJ_SHIFT            $04

.DEFINE TM_BG1_ON               $01
.DEFINE TM_BG1_OFF              $00
.DEFINE TM_BG2_ON               $02
.DEFINE TM_BG2_OFF              $00
.DEFINE TM_BG3_ON               $04
.DEFINE TM_BG3_OFF              $00
.DEFINE TM_BG4_ON               $08
.DEFINE TM_BG4_OFF              $00
.DEFINE TM_OBJ_ON               $10
.DEFINE TM_OBJ_OFF              $00

;TS
.DEFINE TS_BG1_MASK             $fe
.DEFINE TS_BG2_MASK             $fd
.DEFINE TS_BG3_MASK             $fb
.DEFINE TS_BG4_MASK             $f7
.DEFINE TS_OBJ_MASK             $ef

.DEFINE TS_BG1_SHIFT            $00
.DEFINE TS_BG2_SHIFT            $01
.DEFINE TS_BG3_SHIFT            $02
.DEFINE TS_BG4_SHIFT            $03
.DEFINE TS_OBJ_SHIFT            $04

.DEFINE TS_BG1_ON               $01
.DEFINE TS_BG1_OFF              $00
.DEFINE TS_BG2_ON               $02
.DEFINE TS_BG2_OFF              $00
.DEFINE TS_BG3_ON               $04
.DEFINE TS_BG3_OFF              $00
.DEFINE TS_BG4_ON               $08
.DEFINE TS_BG4_OFF              $00
.DEFINE TS_OBJ_ON               $10
.DEFINE TS_OBJ_OFF              $00

;TMW
.DEFINE TMW_BG1_MASK            $fe
.DEFINE TMW_BG2_MASK            $fd
.DEFINE TMW_BG3_MASK            $fb
.DEFINE TMW_BG4_MASK            $f7
.DEFINE TMW_OBJ_MASK            $ef

.DEFINE TMW_BG1_SHIFT           $00
.DEFINE TMW_BG2_SHIFT           $01
.DEFINE TMW_BG3_SHIFT           $02
.DEFINE TMW_BG4_SHIFT           $03
.DEFINE TMW_OBJ_SHIFT           $04

.DEFINE TMW_BG1_ON              $01
.DEFINE TMW_BG1_OFF             $00
.DEFINE TMW_BG2_ON              $02
.DEFINE TMW_BG2_OFF             $00
.DEFINE TMW_BG3_ON              $04
.DEFINE TMW_BG3_OFF             $00
.DEFINE TMW_BG4_ON              $08
.DEFINE TMW_BG4_OFF             $00
.DEFINE TMW_OBJ_ON              $10
.DEFINE TMW_OBJ_OFF             $00

;TSW
.DEFINE TSW_BG1_MASK            $fe
.DEFINE TSW_BG2_MASK            $fd
.DEFINE TSW_BG3_MASK            $fb
.DEFINE TSW_BG4_MASK            $f7
.DEFINE TSW_OBJ_MASK            $ef

.DEFINE TSW_BG1_SHIFT           $00
.DEFINE TSW_BG2_SHIFT           $01
.DEFINE TSW_BG3_SHIFT           $02
.DEFINE TSW_BG4_SHIFT           $03
.DEFINE TSW_MASK_SHIFT          $04

.DEFINE TSW_BG1_ON              $01
.DEFINE TSW_BG1_OFF             $00
.DEFINE TSW_BG2_ON              $02
.DEFINE TSW_BG2_OFF             $00
.DEFINE TSW_BG3_ON              $04
.DEFINE TSW_BG3_OFF             $00
.DEFINE TSW_BG4_ON              $08
.DEFINE TSW_BG4_OFF             $00
.DEFINE TSW_OBJ_ON              $10
.DEFINE TSW_OBJ_OFF             $00

;CGSWSEL
.DEFINE CG_DIRECT_SELECT_MASK   $fe
.DEFINE CG_ENABLE_MASK          $fd
.DEFINE CG_SUB_MASK             $cf
.DEFINE CG_MAIN_MASK            $3f

.DEFINE CG_DIRECT_SELECT_SHIFT  $00
.DEFINE CG_ENABLE_SHIFT         $01
.DEFINE CG_SUB_SHIFT            $04
.DEFINE CG_MAIN_SHIFT           $06

.DEFINE CG_DIRECT_SELECT_ON     $01
.DEFINE CG_DIRECT_SELECT_OFF    $00
.DEFINE CG_ENABLE_FIXED_COL     $00
.DEFINE CG_ENABLE_SUB_SC        $02

.DEFINE CG_SUB_ALL              $00
.DEFINE CG_SUB_INSIDE           $10
.DEFINE CG_SUB_OUTSIDE          $20
.DEFINE CG_SUB_OFF              $30

.DEFINE CG_MAIN_ALL             $00
.DEFINE CG_MAIN_INSIDE          $40
.DEFINE CG_MAIN_OUTSIDE         $80
.DEFINE CG_MAIN_OFF             $c0

;CGADSUB
.DEFINE CG_BG1_MASK             $fe
.DEFINE CG_BG2_MASK             $fd
.DEFINE CG_BG3_MASK             $fb
.DEFINE CG_BG4_MASK             $f7
.DEFINE CG_OBJ_MASK             $ef
.DEFINE CG_BACK_MASK            $df
.DEFINE CG_HALF_MASK            $bf
.DEFINE CG_MODE_MASK            $7f

.DEFINE CG_BG1_SHIFT            $00
.DEFINE CG_BG2_SHIFT            $01
.DEFINE CG_BG3_SHIFT            $02
.DEFINE CG_BG4_SHIFT            $03
.DEFINE CG_OBJ_SHIFT            $04
.DEFINE CG_BACK_SHIFT           $05
.DEFINE CG_HALF_SHIFT           $06
.DEFINE CG_MODE_SHIFT           $07

.DEFINE CG_BG1_ON               $01
.DEFINE CG_BG1_OFF              $00
.DEFINE CG_BG2_ON               $02
.DEFINE CG_BG2_OFF              $00
.DEFINE CG_BG3_ON               $04
.DEFINE CG_BG3_OFF              $00
.DEFINE CG_BG4_ON               $08
.DEFINE CG_BG4_OFF              $00
.DEFINE CG_OBJ_ON               $10
.DEFINE CG_OBJ_OFF              $00
.DEFINE CG_BACK_ON              $20
.DEFINE CG_BACK_OFF             $00
.DEFINE CG_HALF_ON              $40
.DEFINE CG_HALF_OFF             $00
.DEFINE CG_MODE_ADD             $00
.DEFINE CG_MODE_SUB             $80

;COLDATA
.DEFINE CDAT_CONST_COL_MASK     $e0
.DEFINE CDAT_RED_MASK           $df
.DEFINE CDAT_GREEN_MASK         $bf
.DEFINE CDAT_BLUE_MASK          $7f

.DEFINE CDAT_CONST_SHIFT        $00
.DEFINE CDAT_RED_SHIFT          $05
.DEFINE CDAT_GREEN_SHIFT        $06
.DEFINE CDAT_BLUE_SHIFT         $07

.DEFINE CDAT_RED                $20
.DEFINE CDAT_GREEN              $40
.DEFINE CDAT_BLUE               $80

;SETINI
.DEFINE SET_INTERLACE_MASK      $fe
.DEFINE SET_OBJ_V_MASK          $fd
.DEFINE SET_BG_V_MASK           $fb
.DEFINE SET_H_PSEUDO512_MASK    $f7
.DEFINE SET_EXT_BG_MASK         $bf
.DEFINE SET_EXT_SYNC_MASK       $7f

.DEFINE SET_INTERLACE_SHIFT     $00
.DEFINE SET_OBJ_V_SHIFT         $01
.DEFINE SET_BG_V_SHIFT          $02
.DEFINE SET_H_PSEUDO_SHIFT      $03
.DEFINE SET_EXT_BG_SHIFT        $06
.DEFINE SET_EXT_SYNC_SHIFT      $07

.DEFINE SET_INTERLACE_ON        $01
.DEFINE SET_INTERLACE_OFF       $00
.DEFINE SET_OBJ_V_ON            $02
.DEFINE SET_OBJ_V_OFF           $00
.DEFINE SET_BG_V_ON             $04
.DEFINE SET_BG_V_OFF            $00
.DEFINE SET_H_PSEUDO512_ON      $08
.DEFINE SET_H_PSEUDO512_OFF     $00
.DEFINE SET_EXT_BG_ON           $40
.DEFINE SET_EXT_BG_OFF          $00
.DEFINE SET_EXT_SYNC_ON         $80
.DEFINE SET_EXT_SYNC_OFF        $00

;STAT77
.DEFINE STAT77_5C77V_MASK       $f0
.DEFINE STAT77_MS_MODE_MASK     $df
.DEFINE STAT77_OBJSTAT_MASK     $3f

.DEFINE STAT77_5C77V_SHIFT      $00
.DEFINE STAT77_MS_MODE_SHIFT    $05
.DEFINE STAT77_OBJSTAT_SHIFT    $06

;STAT78
.DEFINE STAT78_5C78V_MASK       $f0
.DEFINE STAT78_VIDEOMODE_MASK   $ef
.DEFINE STAT78_EXT_MASK         $bf
.DEFINE STAT78_FIELD_MASK       $7f

.DEFINE STAT78_5C78V_SHIFT      $00
.DEFINE STAT78_VIDEOMODE_SHIFT  $04
.DEFINE STAT78_EXT_SHIFT        $06
.DEFINE STAT78_FIELD_SHIFT      $07

.DEFINE STAT78_VIDEOMODE_NTSC   $00
.DEFINE STAT78_VIDEOMODE_PAL    $01

;NMITIMEN
.DEFINE NMI_JOY_MASK            $fe
.DEFINE NMI_H_TIMER_MASK        $ef
.DEFINE NMI_V_TIMER_MASK        $df
.DEFINE NMI_HV_TIMER_MASK       $cf
.DEFINE NMI_NMI_MASK            $7f

.DEFINE NMI_JOY_SHIFT           $00
.DEFINE NMI_H_TIMER_SHIFT       $04
.DEFINE NMI_V_TIMER_SHIFT       $05
.DEFINE NMI_NMI_SHIFT           $07

.DEFINE NMI_JOY_ON              $01
.DEFINE NMI_JOY_OFF             $00
.DEFINE NMI_H_TIMER_ON          $10
.DEFINE NMI_H_TIMER_OFF         $00
.DEFINE NMI_V_TIMER_ON          $20
.DEFINE NMI_V_TIMER_OFF         $00
.DEFINE NMI_NMI_ON              $80
.DEFINE NMI_NMI_OFF             $00

;MDMAEN/HDMAEN
.DEFINE DMA0_ON                 $01
.DEFINE DMA0_OFF                $00
.DEFINE DMA1_ON                 $02
.DEFINE DMA1_OFF                $00
.DEFINE DMA2_ON                 $04
.DEFINE DMA2_OFF                $00
.DEFINE DMA3_ON                 $08
.DEFINE DMA3_OFF                $00
.DEFINE DMA4_ON                 $10
.DEFINE DMA4_OFF                $00
.DEFINE DMA5_ON                 $20
.DEFINE DMA5_OFF                $00
.DEFINE DMA6_ON                 $40
.DEFINE DMA6_OFF                $00
.DEFINE DMA7_ON                 $80
.DEFINE DMA7_OFF                $00

;MEMSEL
.DEFINE MEM_268_MHZ             $00
.DEFINE MEM_358_MHZ             $01

;RDNMI
.DEFINE RDNMI_5A22V_MASK        $f0
.DEFINE RDNMI_NMI_STAT_MASK     $7f

.DEFINE RDNMI_5A22V_SHIFT       $00
.DEFINE RDNMI_NMI_STAT_SHIFT    $07

;TIMEUP
.DEFINE TIME_STAT_MASK          $7f
.DEFINE TIME_STAT_SHIFT         $07

;HVBJOY
.DEFINE HVBJOY_JOY_STAT_MASK    $fe
.DEFINE HVBJOY_H_BLANK_MASK     $bf
.DEFINE HVBJOY_V_BLANK_MASK     $7f

.DEFINE HVBJOY_JOY_STAT_SHIFT   $00
.DEFINE HVBJOY_H_BLANK_SHIFT    $06
.DEFINE HVBJOY_V_BLANK_SHIFT    $07

.DEFINE HVBJOY_JOY_FREE         $00
.DEFINE HVBJOY_JOY_BUSY         $01

.DEFINE HVBJOY_H_BLANK          $40
.DEFINE HVBJOY_V_BLANK          $80

;DMAPx
.DEFINE DMA_TRANS_SELECT_MASK   $f8
.DEFINE DMA_INCDEC_MASK         $e7
.DEFINE DMA_TYPE_MASK           $bf
.DEFINE DMA_TRANS_DIR_MASK      $7f

.DEFINE DMA_TRANS_SELECT_SHIFT  $00
.DEFINE DMA_INCDEC_SHIFT        $03
.DEFINE DMA_TYPE_SHIFT          $06
.DEFINE DMA_TRANS_DIR_SHIFT     $07

.DEFINE DMA_TRANS_1             $00
.DEFINE DMA_TRANS_2_LH          $01
.DEFINE DMA_TRANS_1_LL          $02
.DEFINE DMA_TRANS_2_LLHH        $03
.DEFINE DMA_TRANS_4_LHLH        $04

.DEFINE HDMA_TRANS_1            $00
.DEFINE HDMA_TRANS_2_LH         $01
.DEFINE HDMA_TRANS_2_LL         $02
.DEFINE HDMA_TRANS_2_LLHH       $03
.DEFINE HDMA_TRANS_4_LHLH       $04

.DEFINE DMA_FIXED               $08
.DEFINE DMA_INCREMENT           $00
.DEFINE DMA_DECREMENT           $10

.DEFINE HDMA_ABSOLUTE           $00
.DEFINE HDMA_INDIRECT           $40

.DEFINE DMA_DIR_MEM_TO_PPU      $00
.DEFINE DMA_DIR_PPU_TO_MEM      $80


;--------------------------------------------------------------------
; VRAM Data Register Bitmasks & Constants

;Base Segment Sizes
.DEFINE SC_BASE_SIZE            $0800
.DEFINE BG_BASE_SIZE            $2000
.DEFINE OBJ_BASE_SIZE           $4000

;OAM Data
.DEFINE OAM_H_POS_MASK          $ff00
.DEFINE OAM_V_POS_MASK          $00ff
.DEFINE OAM_NAME_MASK           $fe00
.DEFINE OAM_COLR_MASK           $f1ff
.DEFINE OAM_PRIO_MASK           $cfff
.DEFINE OAM_FLIP_MASK           $3fff

.DEFINE OAM_H_POS_SHIFT         $00
.DEFINE OAM_V_POS_SHIFT         $08
.DEFINE OAM_NAME_SHIFT          $00
.DEFINE OAM_COLR_SHIFT          $09
.DEFINE OAM_PRIO_SHIFT          $0c
.DEFINE OAM_FLIP_SHIFT          $0e

.DEFINE OAM_H_FLIP              $4000
.DEFINE OAM_V_FLIP              $8000

;BG Screen Data
.DEFINE BG_SC_NAME_MASK         $fc00
.DEFINE BG_SC_COLR_MASK         $e3ff
.DEFINE BG_SC_PRIO_MASK         $dfff
.DEFINE BG_SC_FLIP_MASK         $3fff

.DEFINE BG_SC_NAME_SHIFT        $00
.DEFINE BG_SC_COLR_SHIFT        $0a
.DEFINE BG_SC_PRIO_SHIFT        $0d
.DEFINE BG_SC_FLIP_SHIFT        $0e

.DEFINE BG_SC_H_FLIP            $4000
.DEFINE BG_SC_V_FLIP            $8000

;Color data
.DEFINE COLR_RED_MASK           $ffe0
.DEFINE COLR_GREEN_MASK         $fc1f
.DEFINE COLR_BLUE_MASK          $83ff

.DEFINE COLR_RED_SHIFT          $00
.DEFINE COLR_GREEN_SHIFT        $05
.DEFINE COLR_BLUE_SHIFT         $10

.DEFINE COLR_BLACK              $0000
.DEFINE COLR_BLUE               $7c00
.DEFINE COLR_RED                $001f
.DEFINE COLR_MAGENTA            $7c1f
.DEFINE COLR_GREEN              $03e0
.DEFINE COLR_CYAN               $7fe0
.DEFINE COLR_YELLOW             $03ff
.DEFINE COLR_WHITE              $7fff


;--------------------------------------------------------------------
; Hardware Joypad Values

.DEFINE JOY_L                   $0010
.DEFINE JOY_R                   $0020
.DEFINE JOY_X                   $0040
.DEFINE JOY_A                   $0080
.DEFINE JOY_RIGHT               $0100
.DEFINE JOY_LEFT                $0200
.DEFINE JOY_DOWN                $0400
.DEFINE JOY_UP                  $0800
.DEFINE JOY_START               $1000
.DEFINE JOY_SELECT              $2000
.DEFINE JOY_Y                   $4000
.DEFINE JOY_B                   $8000

.DEFINE JOY_BUTTON_MASK         JOY_L+JOY_R+JOY_X+JOY_A+JOY_START+JOY_SELECT+JOY_Y+JOY_B
.DEFINE JOY_KEY_MASK            JOY_RIGHT+JOY_LEFT+JOY_DOWN+JOY_UP
.DEFINE JOY_ALL_MASK            JOY_BUTTON_MASK+JOY_KEY_MASK
