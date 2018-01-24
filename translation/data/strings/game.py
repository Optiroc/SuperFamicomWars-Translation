#!/usr/bin/python
# -*- coding: utf-8 -*-

# Special characters:
# _   Fast short tab (moves the cursor forward to the next 8 pixel column without any tile rendering involved)
# |   Short space
# <   1 pixel space
# [   Opening quotation mark
# ]   Closing quotation mark

# Control code characters:
# Manual kerning          ⏮n
# Extended character      ⏺nn
# Set VWF buffer offset   ⏫nn

strings = {

# ARMY NAMES (in static tile area)
  0x8BC4B8: { "b":0x8BC4B8, "e":0x8BC4C8, "l":16, "en":"⏺C4⏺C5⏺90____",      "ja":"レッドスター　　"  },  # Red Star
  0x8BC4CA: { "b":0x8BC4CA, "e":0x8BC4DA, "l":16, "en":"⏺C6⏺C7⏺C8___",       "ja":"ブルームーン　　"  },  # Blue Moon
  0x8BC4DC: { "b":0x8BC4DC, "e":0x8BC4EC, "l":16, "en":"⏺C9⏺CA⏺CB⏺91_",     "ja":"グリーンアース　"  },  # Green Earth
  0x8BC4EE: { "b":0x8BC4EE, "e":0x8BC4FE, "l":16, "en":"⏺CC⏺CD⏺CE⏺92_",     "ja":"イエローコメット"  },  # Yellow Comet

# CO NAMES (in static tile area)
  0x8AB75D: { "b":0x8AB75D, "e":0x8AB76D, "l":16, "en":"⏺D0⏺D1⏺D2⏺D3_",    "ja":"ミスターヤマモト"  },  # Mr. Yamamoto
  0x8AB76F: { "b":0x8AB76F, "e":0x8AB77F, "l":16, "en":"⏺D4⏺D5⏺D6___",      "ja":"ヤン　デルタ　　"  },  # Yuan Delta
  0x8AB781: { "b":0x8AB781, "e":0x8AB791, "l":16, "en":"⏺D7⏺D8⏺D9___",      "ja":"フォン　ロッソ　"  },  # Von Rosso
  0x8AB793: { "b":0x8AB793, "e":0x8AB7A3, "l":16, "en":"⏺DA⏺DB⏺93____",     "ja":"ロジェンスキー　"  },  # Rogenski
  0x8AB7A5: { "b":0x8AB7A5, "e":0x8AB7B5, "l":16, "en":"⏺DC⏺DD_____",        "ja":"ヘットラー　　　"  },  # Hetler
  0x8AB7B7: { "b":0x8AB7B7, "e":0x8AB7C7, "l":16, "en":"⏺DE⏺DF⏺94____",     "ja":"キャロライン　　"  },  # Caroline
  0x8AB7C9: { "b":0x8AB7C9, "e":0x8AB7D9, "l":16, "en":"⏺E0⏺E1⏺E2___",      "ja":"ビリーゲーツ　　"  },  # Billy Gates


# CLEAR STRINGS

  # Game config
  0x87D9CC: { "b":0x87D9CC, "e":0x87D9CF, "l":2,  "en":"_",              "ja":"　"  },
  0x87D9D7: { "b":0x87D9D7, "e":0x87D9DA, "l":2,  "en":"_",              "ja":"　"  },
  0x8A86EE: { "b":0x8A86EE, "e":0x8A86F1, "l":2,  "en":"_",              "ja":"　"  },
  0x8A86F2: { "b":0x8A86F2, "e":0x8A86F8, "l":6,  "en":"___",            "ja":"　　　"  },
  # Quick battle window
  0x8A9646: { "b":0x8A9646, "e":0x8A9649, "l":2,  "en":"_",              "ja":"　"  },
  # Not sure
  0x87C2BA: { "b":0x87C2BA, "e":0x87C2BE, "l":4,  "en":"__",             "ja":"　　"  },
  0x87D835: { "b":0x87D835, "e":0x87D83B, "l":6,  "en":"___",            "ja":"　　　"  },


# NEW GAME / SAVE DATA MANAGEMENT

  0x87E51F: { "b":0x87E51F, "e":0x87E529, "l":10, "en":"⏫00_New Game",                "ja":"　　開戦　"  },
  0x87E50E: { "b":0x87E50E, "e":0x87E518, "l":10, "en":"⏫08_Load Game",               "ja":"　　再戦　"  },
  0x87E530: { "b":0x87E530, "e":0x87E53A, "l":10, "en":"⏫10_Copy Data",               "ja":"　　複写　"  },
  0x87E541: { "b":0x87E541, "e":0x87E54B, "l":10, "en":"⏫18_Delete Data",             "ja":"　　削除　"  },

  0x87F4DA: { "b":0x87F4DA, "e":0x87F4F2, "l":24, "en":"⏫20_| Select Saved Game",     "ja":"　　再戦データのせんたく"  },
  0x87E6CA: { "b":0x87E6CA, "e":0x87E6E2, "l":24, "en":"⏫20__ Select Data Slot",      "ja":"　　記録エリアのせんたく"  },
  0x87EB31: { "b":0x87EB31, "e":0x87EB47, "l":22, "en":"⏫30_Select Destination Slot", "ja":"　　複写さきのせんたく"  },
  0x87EB15: { "b":0x87EB15, "e":0x87EB2F, "l":26, "en":"⏫40__|Copy Saved Game",       "ja":"　複写するデータのせんたく"  },
  0x87EB49: { "b":0x87EB49, "e":0x87EB5D, "l":20, "en":"⏫50_ |Game Data Copied!_",    "ja":"　　　複写できました"  },
  0x87ECA3: { "b":0x87ECA3, "e":0x87ECBD, "l":26, "en":"⏫20__Delete Saved Game",      "ja":"　削除するデータのせんたく"  },
  0x87ECBF: { "b":0x87ECBF, "e":0x87ECD3, "l":20, "en":"⏫30_ |Game Data Deleted!_",   "ja":"　　　削除できました"  },

  0x87F2EB: { "b":0x87F2EB, "e":0x87F2F5, "l":10, "en":"⏫60_⏺81._",                  "ja":"　記録１　"  },
  0x87F2F7: { "b":0x87F2F7, "e":0x87F301, "l":10, "en":"⏫80_⏺82._",                  "ja":"　記録２　"  },
  0x87F303: { "b":0x87F303, "e":0x87F30D, "l":10, "en":"⏫A0_⏺83._",                  "ja":"　記録３　"  },

  0x87F2C1: { "b":0x87F2C1, "e":0x87F2D9, "l":24, "en":"No Game Data",                 "ja":"休戦データなし　　　　　"  },
  0x87F2DB: { "b":0x87F2DB, "e":0x87F2DF, "l":4,  "en":"|days",                        "ja":"日　"  },
  0x87F2E1: { "b":0x87F2E1, "e":0x87F2E9, "l":8,  "en":"_⏮2 Ended",                   "ja":"　終了　"  },

  0x87E8C3: { "b":0x87E8C3, "e":0x87E8DB, "l":24, "en":"⏫C0⏮1|Replace Saved Game?",  "ja":"この記録を削除しますか？"  },
  0x87E843: { "b":0x87E843, "e":0x87E849, "l":6,  "en":"⏫CD_OK",                          "ja":"　はい"  },
  0x87E850: { "b":0x87E850, "e":0x87E858, "l":8,  "en":"⏫D0_Cancel",                      "ja":"　いいえ"  },

  # Not sure when/if these are used...
  0x87F30F: { "b":0x87F30F, "e":0x87F319, "l":10, "en":"_Memo 1",             "ja":"　自記１　"  },
  0x87F31B: { "b":0x87F31B, "e":0x87F325, "l":10, "en":"_Memo 2",             "ja":"　自記２　"  },
  0x87F327: { "b":0x87F327, "e":0x87F331, "l":10, "en":"_Memo 3",             "ja":"　自記３　"  },
  0x87F333: { "b":0x87F333, "e":0x87F33D, "l":10, "en":"_Memo 4",             "ja":"　自記４　"  },

  # GAME MODE
  0x87EE66: { "b":0x87EE66, "e":0x87EE76, "l":16, "en":"⏫00____|Select Mode",         "ja":"　モードせんたく"  },
  0x87EDC2: { "b":0x87EDC2, "e":0x87EDCE, "l":12, "en":"⏫20_2_Player: Classic Maps",  "ja":"　２Ｐマップ"  },
  0x87EDD5: { "b":0x87EDD5, "e":0x87EDE7, "l":18, "en":"_2_Player: New Maps",          "ja":"　ニュー２Ｐマップ"  },
  0x87EDEE: { "b":0x87EDEE, "e":0x87EDFA, "l":12, "en":"_4_Player: Special Maps",      "ja":"　４Ｐマップ"  },



# DIALOGUES

  0x87F695: { "b":0x87F695, "e":0x87F6A3, "l":14, "en":"Retreat From Map?",   "ja":"降伏しますか？"  },
  0x87F610: { "b":0x87F610, "e":0x87F616, "l":6,  "en":"_Yes",                "ja":"　はい"  },
  0x87F61D: { "b":0x87F61D, "e":0x87F625, "l":8,  "en":"_No",                 "ja":"　いいえ"  },

  0x87F751: { "b":0x87F751, "e":0x87F75F, "l":14, "en":"|Save Game?",         "ja":"記録しますか？"  },
  0x87F6C7: { "b":0x87F6C7, "e":0x87F6CD, "l":6,  "en":"_OK",                 "ja":"　はい"  },
  0x87F6D4: { "b":0x87F6D4, "e":0x87F6DC, "l":8,  "en":"_Cancel",             "ja":"　いいえ"  },

  0x87F872: { "b":0x87F872, "e":0x87F880, "l":14, "en":"⏮1 Quick Load⏮1|?", "ja":"再戦しますか？"  },
  0x87F7ED: { "b":0x87F7ED, "e":0x87F7F3, "l":6,  "en":"_OK",                 "ja":"　はい"  },
  0x87F7FA: { "b":0x87F7FA, "e":0x87F802, "l":8,  "en":"_Cancel",             "ja":"　いいえ"  },



# MAIN MENU

  0x87C8FA: { "b":0x87C8FA, "e":0x87C902, "l":8,  "en":"_Deploy",       "ja":"　生産　"  },
  0x87C909: { "b":0x87C909, "e":0x87C911, "l":8,  "en":"_Arrange",      "ja":"　配置　"  },
  0x87C99F: { "b":0x87C99F, "e":0x87C9A7, "l":8,  "en":"_Help",         "ja":"　説明　"  },
  0x87C918: { "b":0x87C918, "e":0x87C920, "l":8,  "en":"_Units",        "ja":"　部隊　"  },
  0x87C936: { "b":0x87C936, "e":0x87C93E, "l":8,  "en":"_Intel",        "ja":"　状況　"  },
  0x87C945: { "b":0x87C945, "e":0x87C94D, "l":8,  "en":"_Supply",       "ja":"　全補　"  },
  0x87C954: { "b":0x87C954, "e":0x87C95C, "l":8,  "en":"_Options",      "ja":"　設定　"  },
  0x87C963: { "b":0x87C963, "e":0x87C96B, "l":8,  "en":"_Disband",      "ja":"　処分　"  },
  0x87C972: { "b":0x87C972, "e":0x87C97A, "l":8,  "en":"_Retreat",      "ja":"　降伏　"  },
  0x87C990: { "b":0x87C990, "e":0x87C998, "l":8,  "en":"_Load",         "ja":"　再戦　"  },
  0x87C981: { "b":0x87C981, "e":0x87C989, "l":8,  "en":"_Save",         "ja":"　休戦　"  },
  0x87C9AE: { "b":0x87C9AE, "e":0x87C9B6, "l":8,  "en":"_End Day",      "ja":"　終了　"  },
  # Secret debug item
  0x87C927: { "b":0x87C927, "e":0x87C92F, "l":8,  "en":"_Edit",         "ja":"　ＣＰ　"  },



# UNIT COMMANDS

  # Player commands
  0x87CB76: { "b":0x87CB76, "e":0x87CB7E, "l":8,  "en":"_Wait____",     "ja":"　待機　"  },
  0x87CB85: { "b":0x87CB85, "e":0x87CB8D, "l":8,  "en":"_Attack__",     "ja":"　攻撃　"  },
  0x87CB94: { "b":0x87CB94, "e":0x87CB9C, "l":8,  "en":"_Capture__",    "ja":"　占領　"  },
  0x87CBA3: { "b":0x87CBA3, "e":0x87CBAB, "l":8,  "en":"_Load____",     "ja":"　搭載　"  },
  0x87CBD0: { "b":0x87CBD0, "e":0x87CBD8, "l":8,  "en":"_Drop____",     "ja":"　降車　"  },
  0x87CBB2: { "b":0x87CBB2, "e":0x87CBBA, "l":8,  "en":"_Join_____",    "ja":"　合流　"  },
  0x87CBC1: { "b":0x87CBC1, "e":0x87CBC9, "l":8,  "en":"_Supply____",   "ja":"　補給　"  },
  # Not sure!
  0x87CBDF: { "b":0x87CBDF, "e":0x87CBE7, "l":8,  "en":"_Encounter_",   "ja":"　遭遇　"  },

  # AI(/2P?) commands
  0x868183: { "b":0x868183, "e":0x86818B, "l":8,  "en":"_Wait___",      "ja":"　待機　"  },
  0x86818D: { "b":0x86818D, "e":0x868195, "l":8,  "en":"_Attack__",     "ja":"　攻撃　"  },
  0x868197: { "b":0x868197, "e":0x86819F, "l":8,  "en":"_Capture__",    "ja":"　占領　"  },
  0x8681A1: { "b":0x8681A1, "e":0x8681A9, "l":8,  "en":"_Load____",     "ja":"　搭載　"  },
  0x8681BF: { "b":0x8681BF, "e":0x8681C7, "l":8,  "en":"_Drop____",     "ja":"　降車　"  },
  0x8681AB: { "b":0x8681AB, "e":0x8681B3, "l":8,  "en":"_Join_____",    "ja":"　合流　"  },
  0x8681B5: { "b":0x8681B5, "e":0x8681BD, "l":8,  "en":"_Supply____",   "ja":"　補給　"  },



# BATTLE RESULTS / INTEL

  # RESULTS
  # Rendering order (example when battle concluded, 2P, army 2 won):
  # - Army Name [1]
  #   - Player [1]
  #   - Expenditure [1]
  # - Army Name [2]
  #   - Player [2]
  #   - Expenditure [2]
  # * Map name
  # - Results (header)
  #   - Days: (header)
  # - Nav bar (footer)
  0x8BB5F8: { "b":0x8BB5F8, "e":0x8BB60C, "l":20, "en":"⏫00|Next____|Done",             "ja":"きりかえ　　　ぬける"  },
  0x8BB6DF: { "b":0x8BB6DF, "e":0x8BB6E9, "l":10, "en":"⏫10|Results",      "ja":"戦闘けっか"  },
  0x8BB8A9: { "b":0x8BB8A9, "e":0x8BB8B3, "l":10, "en":"⏫18Player",        "ja":"プレイヤー"  },
  0x8BB6EB: { "b":0x8BB6EB, "e":0x8BB6F3, "l":8,  "en":"⏫40Days:",         "ja":"戦闘日数"  },
  0x8BB8B5: { "b":0x8BB8B5, "e":0x8BB8BD, "l":8,  "en":"⏫60 Expenditure",  "ja":"総軍事費"  },

  # Not sure!
  0x8BB8BF: { "b":0x8BB8BF, "e":0x8BB8C3, "l":4,  "en":"⏫80Battle",        "ja":"戦闘"  },

  # STATISTICS
  # Rendering order (example when battle concluded, army 1 won):
  # - Neutral
  # - Army Name [1]
  #   - Units [1]
  # - Army Name [2]
  #   - Defeated [2]
  #   - Day:
  # * Map name
  # - Statistics (header)
  #   - Days: (header)
  # - Nav bar (footer)
  0x8B9F7B: { "b":0x8B9F7B, "e":0x8B9F8F, "l":20, "en":"⏫00|Next____|Done",             "ja":"きりかえ　　　ぬける"  },
  0x8BA062: { "b":0x8BA062, "e":0x8BA068, "l":6,  "en":"⏫10Statistics",    "ja":"の状況"  },
  0x8BA06A: { "b":0x8BA06A, "e":0x8BA074, "l":10, "en":"⏫18Days:",         "ja":"けいか日数"  },
  0x8BA17E: { "b":0x8BA17E, "e":0x8BA181, "l":4,  "en":"⏫20Neutral",       "ja":"中立"  },
  0x8BA352: { "b":0x8BA352, "e":0x8BA35E, "l":12, "en":"⏫28Defeated",      "ja":"全滅しました"  },

  0x8BA342: { "b":0x8BA342, "e":0x8BA348, "l":6,  "en":"⏫30Units",         "ja":"部隊数"  },
  0x8BA360: { "b":0x8BA360, "e":0x8BA368, "l":8,  "en":"⏫60Day:",          "ja":"全滅日数"  },
  0x8BA34A: { "b":0x8BA34A, "e":0x8BA350, "l":6,  "en":"__⏺98",            "ja":"　？？"  },

  # Empty
  0x8BC4A6: { "b":0x8BC4A6, "e":0x8BC4B6, "l":16, "en":"__",                "ja":"なし　　　　　　"  },
  0x8BB6F5: { "b":0x8BB6F5, "e":0x8BB6F7, "l":2,  "en":"",                  "ja":"日"  },
  0x8BA36A: { "b":0x8BA36A, "e":0x8BB6FC, "l":2,  "en":"",                  "ja":"日"  },
  0x8BA076: { "b":0x8BA076, "e":0x8BA078, "l":2,  "en":"",                  "ja":"日"  },



# UNIT SUMMARY

  0x8BA7E2: { "b":0x8BA7E2, "e":0x8BA804, "l":34, "en":"⏫00 Select____|Next____|Done",   "ja":"ほかの軍　　　きりかえ　　　ぬける"  },
  0x8BA7AE: { "b":0x8BA7AE, "e":0x8BA7B8, "l":10, "en":"⏫10 Deployed",     "ja":"生産部隊数"  },
  0x8BA7BA: { "b":0x8BA7BA, "e":0x8BA7C4, "l":10, "en":"⏫18 Casualties",   "ja":"全滅部隊数"  },
  0x8BA7C6: { "b":0x8BA7C6, "e":0x8BA7D2, "l":12, "en":"⏫20__Total",       "ja":"　　合計　　"  },
  0x8BA7D4: { "b":0x8BA7D4, "e":0x8BA7E0, "l":12, "en":"⏫20__Total",       "ja":"　　合計　　"  },



# NOT SURE / UNUSED?

  0x8AB57F: { "b":0x8AB57F, "e":0x8AB5A1, "l":34, "en:":"CP____/__/___VER._",             "ja":"ＣＰ　　　　／　　／　　　ＶＥＲ．"  },
  0x8AB5A3: { "b":0x8AB5A3, "e":0x8AB5C5, "l":34, "en:":"RAM___/__/___VER._",             "ja":"ＲＡＭ　　　／　　／　　　ＶＥＲ．"  },

  0x83D797: { "b":0x83D797, "e":0x83D7A5, "l":14, "en":"Top Results",                 "ja":"せんとうけっか"  },
  0x83D7A7: { "b":0x83D7A7, "e":0x83D7B5, "l":14, "en":"Attack Power",                "ja":"こうげきりょく"  },
  0x83D7B7: { "b":0x83D7B7, "e":0x83D7C5, "l":14, "en":"Defense Power",               "ja":"ぼうぎょりょく"  },
  0x83D7E5: { "b":0x83D7E5, "e":0x83D7EB, "l":6,  "en":"Level",                       "ja":"レベル"  },
  0x83D7ED: { "b":0x83D7ED, "e":0x83D7F5, "l":8,  "en":"Experience",                  "ja":"けいけん"  },
  0x83D7F7: { "b":0x83D7F7, "e":0x83D7FF, "l":8,  "en":"Capture",                     "ja":"かくとく"  },
  0x83D7C7: { "b":0x83D7C7, "e":0x83D7E3, "l":28, "en":"Push button to return",       "ja":"エイボタンをおすともどります"  },

  0x858C64: { "b":0x858C64, "e":0x858C80, "l":28, "en":"_Red Star Battle Start",      "ja":"　レッドスター軍　戦闘開始　"  },
  0x858C82: { "b":0x858C82, "e":0x858C9E, "l":28, "en":"_Blue Moon Battle Start",     "ja":"　ブルームーン軍　戦闘開始　"  },
  0x858CA0: { "b":0x858CA0, "e":0x858CBE, "l":30, "en":"_Green Earth Battle Start",   "ja":"　グリーンアース軍　戦闘開始　"  },
  0x858CC0: { "b":0x858CC0, "e":0x858CE0, "l":32, "en":"_Yellow Comet Battle Start",  "ja":"　イエローコメット軍　戦闘開始　"  },

  0x83BFDD: { "b":0x83BFDD, "e":0x83BFE3, "l":6,  "en":"Red",                         "ja":"レッド"  },
  0x83BFE5: { "b":0x83BFE5, "e":0x83BFEB, "l":6,  "en":"Blue",                        "ja":"ブルー"  },
  0x83BFED: { "b":0x83BFED, "e":0x83BFF5, "l":8,  "en":"Green",                       "ja":"グリーン"  },
  0x83BFF7: { "b":0x83BFF7, "e":0x83BFFF, "l":8,  "en":"Yellow",                      "ja":"イエロー"  },

  0x8EF12B: { "b":0x8EF12B, "e":0x8EF139, "l":14, "en":"Sound Test",                   "ja":"サウンドテスト"  },
  0x8EF13B: { "b":0x8EF13B, "e":0x8EF145, "l":10, "en":"Music_",                       "ja":"おんがく　"  },
  0x8EF147: { "b":0x8EF147, "e":0x8EF155, "l":14, "en":"SFX_⏺81_",                    "ja":"こうかおん１　"  },
  0x8EF157: { "b":0x8EF157, "e":0x8EF165, "l":14, "en":"SFX_⏺82_",                    "ja":"こうかおん２　"  },
  0x8EF167: { "b":0x8EF167, "e":0x8EF175, "l":14, "en":"SFX_⏺83_",                    "ja":"こうかおん３　"  },
  0x8EF1C7: { "b":0x8EF1C7, "e":0x8EF1CB, "l":4,  "en":"Train_",                       "ja":"嚶勧"  },
  0x8ACE5A: { "b":0x8ACE5A, "e":0x8ACE64, "l":10, "en":"Move Cost_",                   "ja":"移動コスト"  },

  #???
  #0x8AA859: { "b":0x8AA859, "e":0x8AA873, "l":26, "en":"Decide____Don't Record",                     "ja":"けってい　　　きろくしない"  },

  # No-name CO
  #0x8AB74B: { "b":0x8AB74B, "e":0x8AB75B, "l":16, "en":"_???___",               "ja":"なし　　　　　　"  },

  # Get off
  #0x87CE06: { "b":0x87CE06, "e":0x87CE14, "l":14, "ja":"　降車１　￣￣"  },
  #0x87CE1B: { "b":0x87CE1B, "e":0x87CE29, "l":14, "ja":"　降車２　￣￣"  },

  #0x8B9C08: { "b":0x8B9C08, "e":0x8B9C0C, "l":4,  "ja":"喝見"  },
  #0x8B9C0F: { "b":0x8B9C0F, "e":0x8B9C13, "l":4,  "ja":"糸姓"  },
  #0x8B9C16: { "b":0x8B9C16, "e":0x8B9C1A, "l":4,  "ja":"着畠"  },
  #0x8BA17C: { "b":0x8BA17C, "e":0x8BA182, "l":6,  "ja":"艤中立"  },

}
