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

# Space restrictions:
# 24 tiles max (192 pixels) for unit description lines. Possibly a few pixels more in a pinch.
# Max 4 lines for all descriptions.

strings = {

  # Clear first column in deploy menu
  0x87D619: { "b":0x87D619, "e":0x87D61D, "l":4,  "en":"___", "ja":"￣￣"  },

  # Deploy unit alert messages
  0x8A818F: { "b":0x8A818F, "e":0x8A81A7, "l":24, "en":"⏫80|| Insufficient funds!",   "ja":"　おかねがたりません！　"  },
  0x8A81C5: { "b":0x8A81C5, "e":0x8A81DD, "l":24, "en":"⏫80_Unit not available!",     "ja":"　ひつようありません！　"  },
  0x8A8171: { "b":0x8A8171, "e":0x8A818D, "l":28, "en":"⏫80_Unit limit reached!",     "ja":"　ユニット数６０オーバー！　"  },
  0x8A81A9: { "b":0x8A81A9, "e":0x8A81C3, "l":26, "en":"⏫80Train already deployed!",  "ja":"　列車砲はせいさんずみ！　"  },

  # Unit info
  0x8AC52A: { "b":0x8AC52A, "e":0x8AC53A, "l":16, "en":"Build Cost:",              "ja":"ユニットのねだん"  },
  0x8AC53C: { "b":0x8AC53C, "e":0x8AC548, "l":12, "en":"Ammo Cost:",               "ja":"たまのねだん"  },
  0x8AC54A: { "b":0x8AC54A, "e":0x8AC54E, "l":4,  "en":"_⏺8F",                    "ja":"なし"  },

  0x8AC796: { "b":0x8AC796, "e":0x8AC79C, "l":6,  "en":"_⏺8B_",                   "ja":"　−　"  },
  0x8AC782: { "b":0x8AC782, "e":0x8AC784, "l":2,  "en":"⏺8B",                     "ja":"−"  },
  0x8AC786: { "b":0x8AC786, "e":0x8AC78A, "l":4,  "en":"_⏺8B",                    "ja":"　−"  },
  0x8AC78C: { "b":0x8AC78C, "e":0x8AC78E, "l":2,  "en":"⏺8C",                     "ja":"×"  },
  0x8AC790: { "b":0x8AC790, "e":0x8AC794, "l":4,  "en":"⏺C2_",                    "ja":"　∞"  },
  0x8AC79E: { "b":0x8AC79E, "e":0x8AC7A4, "l":6,  "en":"___",                      "ja":"　　　"  },

  # Units screen
  0x8B889C: { "b":0x8B889C, "e":0x8B889F, "l":2,  "en":"⏺8E",              "ja":"／"  },
  0x8B8A98: { "b":0x8B8A98, "e":0x8B8A9B, "l":2,  "en":"⏺8E",              "ja":"／"  },
  0x8B88A0: { "b":0x8B88A0, "e":0x8B88A8, "l":8,  "en":"⏫80Unit|Type",     "ja":"へいしゅ"  },
  0x8B8A7C: { "b":0x8B8A7C, "e":0x8B8A86, "l":10, "en":"__⏺8F⏺8F_",       "ja":"−−−−−"  },
  0x8B8A88: { "b":0x8B8A88, "e":0x8B8A92, "l":10, "en":"__⏺C3_",           "ja":"　無限　　"  }, # infinite

  0x8B8864: { "b":0x8B8864, "e":0x8B889A, "l":54, "en":"⏫90 Navigate_____ Sort_____<Select____|Done",    "ja":"せんたく　　　　　ならべかえ　　　けってい　　　ぬける"  },



# UNIT INFO
# Map overlay name (replaced with special glyphs)
# Short name (build/intel menu)
# Long name (unit info window)
# Long name (???)
# Weapon 1
# Weapon 2
# Info text

# Short names need explicit tile ranges to prevent the unit intel screen from
# overwriting tiles when traversing the list

  # Infantry
  0x8A865E: { "b":0x8A865E, "e":0x8A8662, "l":4,  "en":"⏺40",               "ja":"歩兵"  },
  0x8BC6FB: { "b":0x8BC6FB, "e":0x8BC70B, "l":16, "en":"⏫00_Infantry____",  "ja":"　歩兵　　　　　"  },
  0x8BC904: { "b":0x8BC904, "e":0x8BC912, "l":14, "en":"_|Infantry",         "ja":"　　歩兵　　　"  },
  0x83C039: { "b":0x83C039, "e":0x83C03D, "l":4,  "en":"$Infantry",          "ja":"歩兵"  },
  0x8BCAD5: { "b":0x8BCAD5, "e":0x8BCAE1, "l":12, "en":" ~",                 "ja":"　――――　"  },
  0x8BCC76: { "b":0x8BCC76, "e":0x8BCC82, "l":12, "en":" M Gun",             "ja":"マシンガン　"  },
  0x8AD047: { "en":[
    "The cheapest unit to deploy.  Can capture",
    "bases, but has weak firepower.  Vision",
    "range increases by 3 on top of mountains."
  ], "ja": [
    "　いちばん安く、よわいユニットです。しかし占領で",
    "きるのは歩兵と戦闘工兵だけなので、さいごまでおせ",
    "わになるでしょう。山の上では索敵距離が３上がりま",
    "す。"
  ]},

  # Mech Infantry
  0x8A8664: { "b":0x8A8664, "e":0x8A8668, "l":4,  "en":"⏺41",               "ja":"戦工"  },
  0x8BC70D: { "b":0x8BC70D, "e":0x8BC71D, "l":16, "en":"⏫06_Mech______",    "ja":"　戦闘工兵　　　"  },
  0x8BC914: { "b":0x8BC914, "e":0x8BC922, "l":14, "en":"__Mech",             "ja":"　　戦闘工兵　"  },
  0x83C03F: { "b":0x83C03F, "e":0x83C047, "l":8,  "en":"$Mech",              "ja":"戦闘工兵"  },
  0x8BCAE3: { "b":0x8BCAE3, "e":0x8BCAEF, "l":12, "en":" Bazooka",           "ja":"ロケット砲　"  },
  0x8BCC84: { "b":0x8BCC84, "e":0x8BCC90, "l":12, "en":" M Gun",             "ja":"マシンガン　"  },
  0x8AD0E9: { "en":[
    "Infantry unit with increased firepower.  Due",
    "to its heavy bazooka, mobility is reduced",
    "compared to standard infantry."
  ], "ja": [
    "　ロケット砲をもち、攻撃力の上がった歩兵です。し",
    "かし、ロケット砲が重いせいか、歩兵よりさらに移動",
    "力が少ないです。また、山の上では索敵距離が３上が",
    "ります。占領できます。"
  ]},

  # Heavy Tank
  0x8A866A: { "b":0x8A866A, "e":0x8A866E, "l":4,  "en":"⏺42",               "ja":"重戦"  },
  0x8BC71F: { "b":0x8BC71F, "e":0x8BC72F, "l":16, "en":"⏫0A_Heavy<Tank__",  "ja":"　重戦車　　　　"  },
  0x8BC924: { "b":0x8BC924, "e":0x8BC932, "l":14, "en":"|Heavy<Tank",        "ja":"　　重戦車　　"  },
  0x83C049: { "b":0x83C049, "e":0x83C04F, "l":6,  "en":"$Heavy Tank",        "ja":"重戦車"  },
  0x8BCAF1: { "b":0x8BCAF1, "e":0x8BCAFD, "l":12, "en":" Tank Gun",          "ja":"　戦車砲　　"  },
  0x8BCC92: { "b":0x8BCC92, "e":0x8BCC9E, "l":12, "en":" M Gun",             "ja":"マシンガン　"  },
  0x8AD19D: { "en":[
    "Possesses the strongest offensive and",
    "defensive capabilities among ground forces.",
    "But it is expensive, slow and low on ammo."
  ], "ja": [
    "　買えるユニットの中では、地上さいきょうです。ほ",
    "とんどの攻撃をよせつけず、高い攻撃力をほこります。",
    "しかし重いので、移動力が少ないです。"
  ]},

  # Medium Tank
  0x8A8670: { "b":0x8A8670, "e":0x8A8674, "l":4,  "en":"⏺43",               "ja":"中戦"  },
  0x8BC731: { "b":0x8BC731, "e":0x8BC741, "l":16, "en":"⏫12_Medium<Tank__", "ja":"　中戦車　　　　"  },
  0x8BC934: { "b":0x8BC934, "e":0x8BC942, "l":14, "en":"<Medium<Tank",       "ja":"　　中戦車　　"  },
  0x83C051: { "b":0x83C051, "e":0x83C057, "l":6,  "en":"$Medium Tank",       "ja":"中戦車"  },
  0x8BCAFF: { "b":0x8BCAFF, "e":0x8BCB0B, "l":12, "en":" Tank Gun",          "ja":"　戦車砲　　"  },
  0x8BCCA0: { "b":0x8BCCA0, "e":0x8BCCAC, "l":12, "en":" M Gun",             "ja":"マシンガン　"  },
  0x8AD231: { "en":[
    "A versatile unit which strikes a good",
    "balance between firepower and mobility.",
    "The perfect infantry and vehicle stopper."
  ], "ja": [
    "　軽戦車と重戦車のあいだの力をもつユニットです。",
    "そこそこかたく、移動力もあるのでつかいやすいでし",
    "ょう。"
  ]},

  # Light Tank
  0x8A8676: { "b":0x8A8676, "e":0x8A867A, "l":4,  "en":"⏺44",               "ja":"軽戦"  },
  0x8BC743: { "b":0x8BC743, "e":0x8BC753, "l":16, "en":"⏫19_Light<Tank___", "ja":"　軽戦車　　　　"  },
  0x8BC944: { "b":0x8BC944, "e":0x8BC952, "l":14, "en":"| Light<Tank",       "ja":"　　軽戦車　　"  },
  0x83C059: { "b":0x83C059, "e":0x83C05F, "l":6,  "en":"$Light Tank",        "ja":"軽戦車"  },
  0x8BCB0D: { "b":0x8BCB0D, "e":0x8BCB19, "l":12, "en":" Tank Gun",          "ja":"　戦車砲　　"  },
  0x8BCCAE: { "b":0x8BCCAE, "e":0x8BCCBA, "l":12, "en":" M Gun",             "ja":"マシンガン　"  },
  0x8AD2A5: { "en":[
    "A workhorse tank with great mobility, but",
    "mediocre stopping power.  The low cost and",
    "high ammo capacity make it a dependable unit",
    "in early stages of battle."
  ], "ja": [
    "　ねだんも安く、移動力が高いので地上ではメインの",
    "戦力になるでしょう。しかし装甲はそれほどかたくな",
    "いので、とびだしすぎないよう注意がひつようです。"
  ]},

  # Recon
  0x8A867C: { "b":0x8A867C, "e":0x8A8680, "l":4,  "en":"⏺45",               "ja":"偵察"  },
  0x8BC755: { "b":0x8BC755, "e":0x8BC765, "l":16, "en":"⏫1F_Recon_____",    "ja":"　偵察車　　　　"  },
  0x8BC954: { "b":0x8BC954, "e":0x8BC962, "l":14, "en":"_| Recon",           "ja":"　　偵察車　　"  },
  0x83C061: { "b":0x83C061, "e":0x83C067, "l":6,  "en":"$Recon",             "ja":"偵察車"  },
  0x8BCB1B: { "b":0x8BCB1B, "e":0x8BCB27, "l":12, "en":" ~",                 "ja":"　――――　"  },
  0x8BCCBC: { "b":0x8BCCBC, "e":0x8BCCC8, "l":12, "en":" M Gun",             "ja":"マシンガン　"  },
  0x8AD343: { "en":[
    "Excellent mobility and vision range.  A solid",
    "unit against foot soldiers and indispensible",
    "during Fog of War battles."
  ], "ja": [
    "　移動力が高く歩兵につよいので、敵の歩兵たいじに",
    "はもってこいです。また索敵モードでは、偵察車のひ",
    "ろい索敵はんいにおせわになるでしょう。"
  ]},

  # APC
  0x8A8682: { "b":0x8A8682, "e":0x8A8686, "l":4,  "en":"⏺46",               "ja":"兵輸"  },
  0x8BC767: { "b":0x8BC767, "e":0x8BC777, "l":16, "en":"⏫23_APC______",     "ja":"　兵員輸送車　　"  },
  0x8BC964: { "b":0x8BC964, "e":0x8BC972, "l":14, "en":"__APC",              "ja":"　兵員輸送車　"  },
  0x83C069: { "b":0x83C069, "e":0x83C06F, "l":6,  "en":"$APC",               "ja":"輸送車"  },
  0x8BCB29: { "b":0x8BCB29, "e":0x8BCB35, "l":12, "en":" ~",                 "ja":"　――――　"  },
  0x8BCCCA: { "b":0x8BCCCA, "e":0x8BCCD6, "l":12, "en":" M Gun",             "ja":"マシンガン　"  },
  0x8AD3D7: { "en":[
    "Provides the fastest way to move a single",
    "infantry unit by land.  Predominantly a",
    "transport vehicle, the APC has limited",
    "attack and poor defense abilities."
  ], "ja": [
    "　歩兵、戦闘工兵を搭載してはこぶことができます。",
    "また、輸送ヘリとはちがい攻撃力があるので、あるて",
    "いど闘うこともできます。"
  ]},

  # Prototype Tank
  0x8A8688: { "b":0x8A8688, "e":0x8A868C, "l":4,  "en":"⏺47",               "ja":"新型"  },
  0x8BC779: { "b":0x8BC779, "e":0x8BC789, "l":16, "en":"⏫74_Proto<Tank__",  "ja":"　新型戦車　　　"  },
  0x8BC974: { "b":0x8BC974, "e":0x8BC982, "l":14, "en":"< Proto<Tank",       "ja":"　　新型戦車　"  },
  0x83C071: { "b":0x83C071, "e":0x83C079, "l":8,  "en":"$Proto Tank",        "ja":"新型戦車"  },
  0x8BCB37: { "b":0x8BCB37, "e":0x8BCB43, "l":12, "en":" Tank Gun",          "ja":"　戦車砲　　"  },
  0x8BCCD8: { "b":0x8BCCD8, "e":0x8BCCE4, "l":12, "en":" M Gun",             "ja":"マシンガン　"  },
  0x8AD45D: { "en":[
    "Developed in secrecy, the Prototype Tank",
    "can only be acquired by capturing a neutral",
    "research lab.  It has firepower superior",
    "to Heavy Tank but none of the drawbacks."
  ], "ja": [
    "　地上さいきょうのユニットです。軽戦車なみの移動",
    "力と重戦車以上の攻撃力、かたさをほこります。中立",
    "の研究所を占領したときのみてにはいりますので、が",
    "んばって占領してください。"
  ]},

  # Supply Truck
  0x8A868E: { "b":0x8A868E, "e":0x8A8692, "l":4,  "en":"⏺48",               "ja":"補給"  },
  0x8BC78B: { "b":0x8BC78B, "e":0x8BC79B, "l":16, "en":"⏫26_Supply_____",   "ja":"　補給車　　　　"  },
  0x8BC984: { "b":0x8BC984, "e":0x8BC992, "l":14, "en":"<SupplyTruck","ja":"　　補給車　　"  },
  0x83C07B: { "b":0x83C07B, "e":0x83C081, "l":6,  "en":"$Supply Truck",      "ja":"補給車"  },
  0x8BCB45: { "b":0x8BCB45, "e":0x8BCB51, "l":12, "en":" ~",                 "ja":"　――――　"  },
  0x8BCCE6: { "b":0x8BCCE6, "e":0x8BCCF2, "l":12, "en":" ~",                 "ja":"　――――　"  },
  0x8AD515: { "en":[
    "A vehicle capable of supplying all ground and",
    "helicopter units with fuel and ammo.  Yet with",
    "no offensive or defensive capabilities, it is",
    "powerless against enemy attacks."
  ], "ja": [
    "　地上ユニット、ヘリにたいして補給できるユニット",
    "です。戦闘かいしのとき、となりあうユニットにたい",
    "してねんりょう、弾の補給ができるほか、みずから動",
    "いてほかのユニットに補給しにも行けます。"
  ]},

  # Artillery
  0x8A8694: { "b":0x8A8694, "e":0x8A8698, "l":4,  "en":"⏺49",               "ja":"自走"  },
  0x8BC79D: { "b":0x8BC79D, "e":0x8BC7AD, "l":16, "en":"⏫2A_Artillery____", "ja":"　自走砲　　　　"  },
  0x8BC994: { "b":0x8BC994, "e":0x8BC9A2, "l":14, "en":"⏮1|  Artillery",    "ja":"　　自走砲　　"  },
  0x83C083: { "b":0x83C083, "e":0x83C089, "l":6,  "en":"$Artillery",         "ja":"自走砲"  },
  0x8BCB53: { "b":0x8BCB53, "e":0x8BCB5F, "l":12, "en":" Field Gun",         "ja":"　カノン砲　"  },
  0x8BCCF4: { "b":0x8BCCF4, "e":0x8BCD00, "l":12, "en":" ~",                 "ja":"　――――　"  },
  0x8AD5DB: { "en":[
    "Basic indirect combat unit.  Although slower",
    "than the rocket launcher, its treads can",
    "move through harsh terrain.  Defenseless",
    "against direct attacks."
  ], "ja": [
    "　かんせつ攻撃ユニットです。ロケット砲よりしゃて",
    "いはみじかいものの、キャタピラなのでいろいろな所",
    "に移動できます。ちょくせつ攻撃にはよわいので注意",
    "してください。対地上です。"
  ]},

  # Rockets
  0x8A869A: { "b":0x8A869A, "e":0x8A869E, "l":4,  "en":"⏺4a",               "ja":"ロケ"  },
  0x8BC7AF: { "b":0x8BC7AF, "e":0x8BC7BF, "l":16, "en":"⏫2F_Rockets____",   "ja":"　ロケット砲　　"  },
  0x8BC9A4: { "b":0x8BC9A4, "e":0x8BC9B2, "l":14, "en":"_<Rockets",          "ja":"　ロケット砲　"  },
  0x83C08B: { "b":0x83C08B, "e":0x83C095, "l":10, "en":"$Rockets",           "ja":"ロケット砲"  },
  0x8BCB61: { "b":0x8BCB61, "e":0x8BCB6D, "l":12, "en":" Rockets",           "ja":"ロケット砲　"  },
  0x8BCD02: { "b":0x8BCD02, "e":0x8BCD0E, "l":12, "en":" ~",                 "ja":"　――――　"  },
  0x8AD693: { "en":[
    "Inflicts devastating damage to land and sea",
    "units from a distance, at the price of being",
    "slow moving and exposed at close range."
  ], "ja": [
    "　かんせつ攻撃ユニットです。ひろいしゃていはんい",
    "で敵をよせつけません。ただし、ちょくせつ攻撃には",
    "自走砲以上によわいので注意してください。"
  ]},

  # Train
  0x8A86A0: { "b":0x8A86A0, "e":0x8A86A4, "l":4,  "en":"⏺4b",               "ja":"列車"  },
  0x8BC7C1: { "b":0x8BC7C1, "e":0x8BC7D1, "l":16, "en":"⏫7B_Train______",   "ja":"　列車砲　　　　"  },
  0x8BC9B4: { "b":0x8BC9B4, "e":0x8BC9C2, "l":14, "en":"__Train",            "ja":"　　列車砲　　"  },
  0x83C097: { "b":0x83C097, "e":0x83C09D, "l":6,  "en":"$Train",             "ja":"列車砲"  },
  0x8BCB6F: { "b":0x8BCB6F, "e":0x8BCB7B, "l":12, "en":" Train Gun",         "ja":"　カノン砲　"  },
  0x8BCD10: { "b":0x8BCD10, "e":0x8BCD1C, "l":12, "en":" M Gun",             "ja":"マシンガン　"  },
  0x8AD729: { "en":[
    "A veritable fortress on rails that can load",
    "two ground units.  The train gun deals",
    "devastating indirect damage against all",
    "ground and naval units."
  ], "ja": [
    "　地上ユニットを２ユニット搭載でき、かんせつ攻撃",
    "の攻撃力も高く、高い移動力をもつばんのうユニット",
    "です。しかし、レールと駅しか移動できない上、１だ",
    "いしか生産できません。"
  ]},

  # Flak Gun
  0x8A86A6: { "b":0x8A86A6, "e":0x8A86AA, "l":4,  "en":"⏺4c",               "ja":"空自"  },
  0x8BC7D3: { "b":0x8BC7D3, "e":0x8BC7E3, "l":16, "en":"⏫34_Flak|Gun____",  "ja":"　対空自走砲　　"  },
  0x8BC9C4: { "b":0x8BC9C4, "e":0x8BC9D2, "l":14, "en":"_Flak Gun",          "ja":"　対空自走砲　"  },
  0x83C09F: { "b":0x83C09F, "e":0x83C0A9, "l":10, "en":"$Flak Gun",          "ja":"対空自走砲"  },
  0x8BCB7D: { "b":0x8BCB7D, "e":0x8BCB89, "l":12, "en":" Flak Gun",          "ja":"　高射砲　　"  },
  0x8BCD1E: { "b":0x8BCD1E, "e":0x8BCD2A, "l":12, "en":" ~",                 "ja":"　――――　"  },
  0x8AD7DD: { "en":[
    "Flak is the anti-air equivalent to the standard",
    "Artillery unit.  It's a low-cost, indirect combat",
    "unit that can strike against any airborne",
    "enemy targets."
  ], "ja": [
    "　かんせつ攻撃ユニットです。対空ミサイルよりしゃ",
    "ていはみじかいですが、あまり場所をえらばず移動で",
    "きます。れいによって、ちょくせつ攻撃によわいです。",
    "対空です。"
  ]},

  # AA Tank
  0x8A86AC: { "b":0x8A86AC, "e":0x8A86B0, "l":4,  "en":"⏺4d",               "ja":"空戦"  },
  0x8BC7E5: { "b":0x8BC7E5, "e":0x8BC7F5, "l":16, "en":"⏫39_AA<Tank____",   "ja":"　対空戦車　　　"  },
  0x8BC9D4: { "b":0x8BC9D4, "e":0x8BC9E2, "l":14, "en":"_AA<Tank",           "ja":"　　対空戦車　"  },
  0x83C0AB: { "b":0x83C0AB, "e":0x83C0B3, "l":8,  "en":"$AA Tank",           "ja":"対空戦車"  },
  0x8BCB8B: { "b":0x8BCB8B, "e":0x8BCB97, "l":12, "en":" Vulcan",            "ja":"バルカン砲　"  },
  0x8BCD2C: { "b":0x8BCD2C, "e":0x8BCD38, "l":12, "en":" ~",                 "ja":"　――――　"  },
  0x8AD887: { "en":[
    "The anti-air tank is equipped with the unique",
    "Vulcan cannon, which can inflict damage",
    "against most ground and air units."
  ], "ja": [
    "　「対空」となまえがついているだけあって、航空ユ",
    "ニットにつよいですが、戦車ユニットをのぞく地上ユ",
    "ニットにもつよいのがポイントです。"
  ]},

  # Missiles
  0x8A86B2: { "b":0x8A86B2, "e":0x8A86B6, "l":4,  "en":"⏺4e",               "ja":"空ミ"  },
  0x8BC7F7: { "b":0x8BC7F7, "e":0x8BC807, "l":16, "en":"⏫3F_Missiles____",  "ja":"　対空ミサイル　"  },
  0x8BC9E4: { "b":0x8BC9E4, "e":0x8BC9F2, "l":14, "en":"_|Missiles",         "ja":"　対空ミサイル"  },
  0x83C0B5: { "b":0x83C0B5, "e":0x83C0C1, "l":12, "en":"$Missiles",          "ja":"対空ミサイル"  },
  0x8BCB99: { "b":0x8BCB99, "e":0x8BCBA5, "l":12, "en":" Missiles",          "ja":"対空ミサイル"  },
  0x8BCD3A: { "b":0x8BCD3A, "e":0x8BCD46, "l":12, "en":" ~",                 "ja":"　――――　"  },
  0x8AD917: { "en":[
    "An excellent weapon against airborne enemy",
    "units.  Poor mobility is offset by its great",
    "striking distance."
  ], "ja": [
    "　かんせつ攻撃ユニットです。航空ユニットにはめっ",
    "ぽうつよいですが、移動力が少ないので占領ポイント",
    "防御用でしょう。ちょくせつ攻撃によわいです。"
  ]},



  # Fighter
  0x8A86B8: { "b":0x8A86B8, "e":0x8A86BC, "l":4,  "en":"⏺4f",               "ja":"戦闘"  },
  0x8BC809: { "b":0x8BC809, "e":0x8BC819, "l":16, "en":"⏫44_Fighter_____",  "ja":"　戦闘機　　　　"  },
  0x8BC9F4: { "b":0x8BC9F4, "e":0x8BCA02, "l":14, "en":"_ Fighter",          "ja":"　　戦闘機　　"  },
  0x83C0C3: { "b":0x83C0C3, "e":0x83C0C9, "l":6,  "en":"$Fighter",           "ja":"戦闘機"  },
  0x8BCBA7: { "b":0x8BCBA7, "e":0x8BCBB3, "l":12, "en":" ⏮2AA|Missiles",    "ja":"対空ミサイル"  },
  0x8BCD48: { "b":0x8BCD48, "e":0x8BCD54, "l":12, "en":" M Gun",             "ja":"マシンガン　"  },
  0x8AD9B1: { "en":[
    "Provides superior firepower and mobility",
    "for air-to-air engagements.  Can't attack",
    "ground units and consumes fuel at an",
    "alarming rate."
  ], "ja": [
    "　航空ユニットで、戦闘機にかなうユニットはいませ",
    "ん。ただし、地上に対して攻撃ができないので、対空",
    "ユニットには注意してください。ねんりょうぎれのつ",
    "いらくにも注意してください。"
  ]},

  # Bomber
  0x8A86BE: { "b":0x8A86BE, "e":0x8A86C2, "l":4,  "en":"⏺50",               "ja":"爆撃"  },
  0x8BC81B: { "b":0x8BC81B, "e":0x8BC82B, "l":16, "en":"⏫49_Bomber____",    "ja":"　爆撃機　　　　"  },
  0x8BCA04: { "b":0x8BCA04, "e":0x8BCA12, "l":14, "en":"_ Bomber",           "ja":"　　爆撃機　　"  },
  0x83C0CB: { "b":0x83C0CB, "e":0x83C0D1, "l":6,  "en":"$Bomber",            "ja":"爆撃機"  },
  0x8BCBB5: { "b":0x8BCBB5, "e":0x8BCBC1, "l":12, "en":" Bombs",             "ja":"　　爆弾　　"  },
  0x8BCD56: { "b":0x8BCD56, "e":0x8BCD62, "l":12, "en":" ~",                 "ja":"　――――　"  },
  0x8ADA6B: { "en":[
    "The menace of the skies.  Inflicts stupendous",
    "damage to all ground units.  However, they",
    "are defenseless against attacks so supporting",
    "units are recommended for engagement."
  ], "ja": [
    "　航空ユニットです。対地上攻撃にはつよいですが、",
    "対空ユニット、戦闘機、攻撃機には注意してください。",
    "　まいにち５ずつねんりょうがつかわれますので、",
    "ついらくにも注意してください。"
  ]},

  # Striker
  0x8A86C4: { "b":0x8A86C4, "e":0x8A86C8, "l":4,  "en":"⏺51",               "ja":"攻撃"  },
  0x8BC82D: { "b":0x8BC82D, "e":0x8BC83D, "l":16, "en":"⏫4E_Striker____",   "ja":"　攻撃機　　　　"  },
  0x8BCA14: { "b":0x8BCA14, "e":0x8BCA22, "l":14, "en":"_|Striker",          "ja":"　　攻撃機　　"  },
  0x83C0D3: { "b":0x83C0D3, "e":0x83C0D9, "l":6,  "en":"$Striker",           "ja":"攻撃機"  },
  0x8BCBC3: { "b":0x8BCBC3, "e":0x8BCBCF, "l":12, "en":" Missiles",          "ja":"汎用ミサイル"  },
  0x8BCD64: { "b":0x8BCD64, "e":0x8BCD70, "l":12, "en":" M Gun",             "ja":"マシンガン　"  },
  0x8ADB27: { "en":[
    "This multirole combat aircraft can engage all",
    "enemy units except Subs.  While versatile,",
    "it comes at a high price and does not excel",
    "against any unit."
  ], "ja": [
    "　対空ユニットと戦闘機以外、どのユニットともごか",
    "く以上に闘えますが、とくに海上ユニットに対しては",
    "ばつぐんの攻撃力があります。ねんりょうぎれには注",
    "意してください。"
  ]},

  # Battle Copter
  0x8A86CA: { "b":0x8A86CA, "e":0x8A86CE, "l":4,  "en":"⏺52",               "ja":"戦ヘ"  },
  0x8BC83F: { "b":0x8BC83F, "e":0x8BC84F, "l":16, "en":"⏫53_B-Copter___",   "ja":"　戦闘ヘリ　　　"  },
  0x8BCA24: { "b":0x8BCA24, "e":0x8BCA32, "l":14, "en":"  B-Copter",         "ja":"　　戦闘ヘリ　"  },
  0x83C0DB: { "b":0x83C0DB, "e":0x83C0E3, "l":8,  "en":"$B-Copter",          "ja":"戦闘ヘリ"  },
  0x8BCBD1: { "b":0x8BCBD1, "e":0x8BCBDD, "l":12, "en":" Missiles",          "ja":"対地ミサイル"  },
  0x8BCD72: { "b":0x8BCD72, "e":0x8BCD7E, "l":12, "en":" M Gun",             "ja":"マシンガン　"  },
  0x8ADBD5: { "en":[
    "Cheap, versatile and ultimately expendable",
    "airborne unit that can engage ground and",
    "naval enemies.  Vulnerable to counter",
    "attacks, but a great support unit."
  ], "ja": [
    "　対地上ユニットにつよく、航空ユニットであるため",
    "場所をえらばず行動できる、とてもつかいやすいユニ",
    "ットです。補給車で補給もできるため、ねんりょうや",
    "弾もあまりきにせず闘えます。"
  ]},

  # Transport Copter
  0x8A86D0: { "b":0x8A86D0, "e":0x8A86D4, "l":4,  "en":"⏺53",               "ja":"輸ヘ"  },
  0x8BC851: { "b":0x8BC851, "e":0x8BC861, "l":16, "en":"⏫59_T-Copter___",   "ja":"　輸送ヘリ　　　"  },
  0x8BCA34: { "b":0x8BCA34, "e":0x8BCA42, "l":14, "en":"  T-Copter",         "ja":"　　輸送ヘリ　"  },
  0x83C0E5: { "b":0x83C0E5, "e":0x83C0ED, "l":8,  "en":"$T-Copter",          "ja":"輸送ヘリ"  },
  0x8BCBDF: { "b":0x8BCBDF, "e":0x8BCBEB, "l":12, "en":" ~",                 "ja":"　――――　"  },
  0x8BCD80: { "b":0x8BCD80, "e":0x8BCD8C, "l":12, "en":" ~",                 "ja":"　――――　"  },
  0x8ADC8F: { "en":[
    "Airborne transport capable of loading one",
    "infantry unit.  Essential for quickly moving",
    "foot soldiers into hard to reach areas.",
    "No offensive or defensive capabilities."
  ], "ja": [
    "　歩兵、戦闘工兵をはこべます。どこでも移動できる",
    "ためとてもべんりですが、攻撃力がないため、つかう",
    "ときには注意がひつようです。補給車でのねんりょう",
    "の補給ができます。"
  ]},



  # Battleship
  0x8A86D6: { "b":0x8A86D6, "e":0x8A86DA, "l":4,  "en":"⏺54",               "ja":"戦艦"  },
  0x8BC863: { "b":0x8BC863, "e":0x8BC873, "l":16, "en":"⏫60_Battleship___", "ja":"　戦艦　　　　　"  },
  0x8BCA44: { "b":0x8BCA44, "e":0x8BCA52, "l":14, "en":"  Battleship",       "ja":"　　戦艦　　　"  },
  0x83C0EF: { "b":0x83C0EF, "e":0x83C0F3, "l":4,  "en":"$Battleship",        "ja":"戦艦"  },
  0x8BCBED: { "b":0x8BCBED, "e":0x8BCBF9, "l":12, "en":" Naval Gun",         "ja":"　カノン砲　"  },
  0x8BCD8E: { "b":0x8BCD8E, "e":0x8BCD9A, "l":12, "en":" M Gun",             "ja":"マシンガン　"  },
  0x8ADD3F: { "en":[
    "A floating fortress, at a high price.  Its large",
    "caliber naval guns inflict massive damage over",
    "long distances on everything but submarines."
  ], "ja": [
    "　ひろいしゃていはんいをもつ海上ユニットです。航",
    "空ユニットにも攻撃できます。潜水艦には攻撃できな",
    "いので注意してください。"
  ]},

  # Cruiser
  0x8A86DC: { "b":0x8A86DC, "e":0x8A86E0, "l":4,  "en":"⏺55",               "ja":"護衛"  },
  0x8BC875: { "b":0x8BC875, "e":0x8BC885, "l":16, "en":"⏫66_Cruiser____",   "ja":"　護衛艦　　　　"  },
  0x8BCA54: { "b":0x8BCA54, "e":0x8BCA62, "l":14, "en":"_|Cruiser",          "ja":"　　護衛艦　　"  },
  0x83C0F5: { "b":0x83C0F5, "e":0x83C0FB, "l":6,  "en":"$Cruiser",           "ja":"護衛艦"  },
  0x8BCBFB: { "b":0x8BCBFB, "e":0x8BCC07, "l":12, "en":" Torpedoes",         "ja":"対潜ミサイル"  },
  0x8BCD9C: { "b":0x8BCD9C, "e":0x8BCDA8, "l":12, "en":" M Gun",             "ja":"マシンガン　"  },
  0x8ADDC5: { "en":[
    "A specialized naval unit that can carry two",
    "helicopters.  High mobility and vision range",
    "make it an ideal scout ship in Fog of War.",
    "Its torpedoes can only target submarines."
  ], "ja": [
    "　ヘリを２機まで搭載し、補給することができます。",
    "また、潜水艦に攻撃できるのは護衛艦と潜水艦だけで",
    "す。索敵はんいがひろいので、索敵モードのときには",
    "やくにたつでしょう。"
  ]},

  # Lander
  0x8A86E2: { "b":0x8A86E2, "e":0x8A86E6, "l":4,  "en":"⏺56",               "ja":"輸送"  },
  0x8BC887: { "b":0x8BC887, "e":0x8BC897, "l":16, "en":"⏫6B_Lander_____",   "ja":"　輸送船　　　　"  },
  0x8BCA64: { "b":0x8BCA64, "e":0x8BCA72, "l":14, "en":"_| Lander",          "ja":"　　輸送船　　"  },
  0x83C0FD: { "b":0x83C0FD, "e":0x83C103, "l":6,  "en":"$Lander",            "ja":"輸送艦"  },
  0x8BCC09: { "b":0x8BCC09, "e":0x8BCC15, "l":12, "en":" ~",                 "ja":"　――――　"  },
  0x8BCDAA: { "b":0x8BCDAA, "e":0x8BCDB6, "l":12, "en":" ~",                 "ja":"　――――　"  },
  0x8ADE77: { "en":[
    "Naval transport capable of loading two",
    "ground units.  Poor armor and no weapons",
    "can make it vulnerable without an escort."
  ], "ja": [
    "　地上ユニットを２だいまで搭載することができます。",
    "輸送ヘリとおなじく、まったく攻撃力をもたないので",
    "注意がひつようです。"
  ]},

  # Submarine
  0x8A86E8: { "b":0x8A86E8, "e":0x8A86EC, "l":4,  "en":"⏺57",               "ja":"潜水"  },
  0x8BC899: { "b":0x8BC899, "e":0x8BC8A9, "l":16, "en":"⏫70_Sub______",     "ja":"　潜水艦　　　　"  },
  0x8BCA74: { "b":0x8BCA74, "e":0x8BCA82, "l":14, "en":"  Submarine",        "ja":"　　潜水艦　　"  },
  0x83C105: { "b":0x83C105, "e":0x83C10B, "l":6,  "en":"$Submarine",         "ja":"潜水艦"  },
  0x8BCC17: { "b":0x8BCC17, "e":0x8BCC23, "l":12, "en":" Torpedoes",         "ja":"　　魚雷　　"  },
  0x8BCDB8: { "b":0x8BCDB8, "e":0x8BCDC4, "l":12, "en":" ~",                 "ja":"　――――　"  },
  0x8ADEFB: { "en":[
    "Silent but deadly unit against naval enemies.",
    "Can only be attacked by cruisers and other",
    "submarines.  In Fog of War, an enemy must",
    "be directly adjacent in order to spot it."
  ], "ja": [
    "　護衛艦と潜水艦以外のユニットにはいっさいダメー",
    "ジをうけません。また索敵モードでは、たとえ敵の索",
    "敵はんいにはいっていたとしても、となりあわないか",
    "ぎりはっけんされることはありません。"
  ]},



  # Dummy unit definition
  #0x8A8654: { "b":0x8A8654, "e":0x8A865C, "l":8,  "en":"⏺8b⏺8b",            "ja":"竊閹　　"  },
  #0x8BC6EF: { "b":0x8BC6EF, "e":0x8BC6F9, "l":10, "en":"⏺8b⏺8b⏺8b",        "ja":"（なまえ）"  },
  #0x83C033: { "b":0x83C033, "e":0x83C037, "l":4,  "en":"⏺8b",                "ja":"なし"  },
  #0x8BCACD: { "b":0x8BCACD, "e":0x8BCAD3, "l":6,  "en":"⏺8b",                "ja":"ダミー"  },
  #0x8BCC6E: { "b":0x8BCC6E, "e":0x8BCC74, "l":6,  "en":"⏺8b",                "ja":"ダミー"  },

}
