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
# 18 tiles max (144 pixels) for terrain description lines.

strings = {

  "defaults": { "max_px": 144 },

  0x8ACE66: { "b":0x8ACE66, "e":0x8ACE6A, "l":4,  "en":"De⏮1f:",             "ja":"防御"  },
  0x8ACE6C: { "b":0x8ACE6C, "e":0x8ACE78, "l":12, "en":"_Incom⏮1e:___⏺8F_", "ja":"収入　　なし"  },
  0x8ACE7A: { "b":0x8ACE7A, "e":0x8ACE82, "l":8,  "en":"|1000",               "ja":"１０００"  },


# TERRAIN INFO
# Map overlay name (replaced with hand drawn glyphs)
# Long name
# Info text

  # None (not used in-game)
  0x8BC53D: { "b":0x8BC53D, "e":0x8BC541, "l":4,  "en":"No",      "ja":"なし"  },
  0x8BC5F0: { "b":0x8BC5F0, "e":0x8BC5F6, "l":6,  "en":"None",    "ja":"鞍なし"  },

  # Plain
  0x8BC543: { "b":0x8BC543, "e":0x8BC547, "l":4,  "en":"⏺58",      "ja":"平地"  },
  0x8BC5F8: { "b":0x8BC5F8, "e":0x8BC5FE, "l":6,  "en":"__Plain",   "ja":"平地　"  },
  0x8ADFFA: { "b":0x8ADFFA, "e":0x8AE020, "l":38, "en":"Plains are the most common type",      "ja":"　もっとも基本的な地形です。移動しや　"  },
  0x8AE024: { "b":0x8AE024, "e":0x8AE04A, "l":38, "en":"of terrain.  Offer minimal cover",     "ja":"すいですが、防御力が少ないため守りに　"  },
  0x8AE04E: { "b":0x8AE04E, "e":0x8AE05E, "l":16, "en":"and slow down tyre units.",            "ja":"はむきません。　"  },

  # River
  0x8BC549: { "b":0x8BC549, "e":0x8BC54D, "l":4,  "en":"⏺59",         "ja":"川　"  },
  0x8BC600: { "b":0x8BC600, "e":0x8BC606, "l":6,  "en":"_<  River",    "ja":"　川　"  },
  0x8AE060: { "b":0x8AE060, "e":0x8AE086, "l":38, "en":"A river deep enough for naval",        "ja":"浅瀬とにていますが、キャタピラタイプ　"  },
  0x8AE08A: { "b":0x8AE08A, "e":0x8AE0B0, "l":38, "en":"units to enter.  Foot soldiers can",   "ja":"は入れません。　　　　　　　　　　　　"  },
  0x8AE0B4: { "b":0x8AE0B4, "e":0x8AE0DA, "l":38, "en":"swim across, if need be.",             "ja":"　　　　　　　　　　　　　　　　　　　"  },

  # Mountain
  0x8BC54F: { "b":0x8BC54F, "e":0x8BC553, "l":4,  "en":"⏺5A",         "ja":"山　"  },
  0x8BC608: { "b":0x8BC608, "e":0x8BC60E, "l":6,  "en":"_Mountain",    "ja":"　山　"  },
  0x8AE0DC: { "b":0x8AE0DC, "e":0x8AE102, "l":38, "en":"Only infantry and air units can",      "ja":"　航空ユニットと歩兵、戦闘工兵のみは　"  },
  0x8AE106: { "b":0x8AE106, "e":0x8AE12C, "l":38, "en":"travel over mountains.  Vision",       "ja":"いることができます。山の上の歩兵、戦　"  },
  0x8AE130: { "b":0x8AE130, "e":0x8AE158, "l":40, "en":"is increased by 3 for troops.",        "ja":"闘工兵は索敵距離が３ふえます。　　　　　"  },

  # Wood
  0x8BC555: { "b":0x8BC555, "e":0x8BC559, "l":4,  "en":"⏺5B",         "ja":"森　"  },
  0x8BC610: { "b":0x8BC610, "e":0x8BC616, "l":6,  "en":"_<  Wood",     "ja":"　森　"  },
  0x8AE15A: { "b":0x8AE15A, "e":0x8AE180, "l":38, "en":"Woods provide good cover but",         "ja":"　タイヤ移動タイプのユニットは、はい　"  },
  0x8AE184: { "b":0x8AE184, "e":0x8AE1AA, "l":38, "en":"are difficult to traverse.  Tyre",     "ja":"ることができません。　あるていど防御　"  },
  0x8AE1AE: { "b":0x8AE1AE, "e":0x8AE1D2, "l":36, "en":"units cannot pass through at all.",    "ja":"力が高いので、守りにもつかえます。　"  },

  # Road
  0x8BC55B: { "b":0x8BC55B, "e":0x8BC55F, "l":4,  "en":"⏺5C",         "ja":"道路"  },
  0x8BC618: { "b":0x8BC618, "e":0x8BC61E, "l":6,  "en":"__Road",       "ja":"道路　"  },
  0x8AE1D4: { "b":0x8AE1D4, "e":0x8AE1FA, "l":38, "en":"Easy to traverse, but offer no",       "ja":"　もっとも移動しやすい地形ですが、防　"  },
  0x8AE1FE: { "b":0x8AE1FE, "e":0x8AE224, "l":38, "en":"protection.  Attacking from roads",    "ja":"御力がないので、守りにはむきません。　"  },
  0x8AE228: { "b":0x8AE228, "e":0x8AE24E, "l":38, "en":"is ill-advised and best avoided.",     "ja":"　　　　　　　　　　　　　　　　　　　"  },

  # City
  0x8BC561: { "b":0x8BC561, "e":0x8BC565, "l":4,  "en":"⏺5D",         "ja":"都市"  },
  0x8BC620: { "b":0x8BC620, "e":0x8BC626, "l":6,  "en":"__|City",      "ja":"都市　"  },
  0x8AE250: { "b":0x8AE250, "e":0x8AE276, "l":38, "en":"Cities provide income and facilities", "ja":"　ふつうの都市です。陸上ユニットの補　"  },
  0x8AE27A: { "b":0x8AE27A, "e":0x8AE2A0, "l":38, "en":"to repair and supply ground units.",   "ja":"充、補給ができます。　　　　　　　　　"  },
  0x8AE2A4: { "b":0x8AE2A4, "e":0x8AE2CA, "l":38, "en":"Also a good defensive position.",      "ja":"　　　　　　　　　　　　　　　　　　　"  },

  # Sea
  0x8BC567: { "b":0x8BC567, "e":0x8BC56B, "l":4,  "en":"⏺5E",         "ja":"海　"  },
  0x8BC628: { "b":0x8BC628, "e":0x8BC62E, "l":6,  "en":"__|Sea",       "ja":"　海　"  },
  0x8AE2CC: { "b":0x8AE2CC, "e":0x8AE2F2, "l":38, "en":"Seas are traversable by naval",        "ja":"　海上ユニットと航空ユニットだけが移　"  },
  0x8AE2F6: { "b":0x8AE2F6, "e":0x8AE31C, "l":38, "en":"and air units only.  Offer no",        "ja":"動できます。防御にはむきません。　　　"  },
  0x8AE320: { "b":0x8AE320, "e":0x8AE346, "l":38, "en":"defensive benefits.",                  "ja":"　　　　　　　　　　　　　　　　　　　"  },

  # HQ
  0x8BC56D: { "b":0x8BC56D, "e":0x8BC571, "l":4,  "en":"⏺5F",         "ja":"首都"  },
  0x8BC630: { "b":0x8BC630, "e":0x8BC636, "l":6,  "en":"__< HQ",       "ja":"首都　"  },
  0x8AE348: { "b":0x8AE348, "e":0x8AE36E, "l":38, "en":"The center of power for each",         "ja":"　各勢力のほんきょ地です。占領される　"  },
  0x8AE372: { "b":0x8AE372, "e":0x8AE398, "l":38, "en":"army.  Victory is yours if you",       "ja":"と敗北します。陸上ユニットの生産と補　"  },
  0x8AE39C: { "b":0x8AE39C, "e":0x8AE3C4, "l":40, "en":"capture the enemy's |HQ!",             "ja":"充、補給ができます。　　　　　　　　　　"  },

  # Lake
  0x8BC573: { "b":0x8BC573, "e":0x8BC577, "l":4,  "en":"⏺60",         "ja":"湖　"  },
  0x8BC638: { "b":0x8BC638, "e":0x8BC63E, "l":6,  "en":"__<Lake",      "ja":"　湖　"  },
  0x8AE3C6: { "b":0x8AE3C6, "e":0x8AE3EC, "l":38, "en":"A deep lake that can only be",         "ja":"　航空ユニットのみはいることができま　"  },
  0x8AE3F0: { "b":0x8AE3F0, "e":0x8AE416, "l":38, "en":"crossed by airborne units.",           "ja":"す。　　　　　　　　　　　　　　　　　"  },
  0x8AE41A: { "b":0x8AE41A, "e":0x8AE440, "l":38, "en":"_",                                    "ja":"　　　　　　　　　　　　　　　　　　　"  },

  # Airport
  0x8BC579: { "b":0x8BC579, "e":0x8BC57D, "l":4,  "en":"⏺61",         "ja":"空港"  },
  0x8BC640: { "b":0x8BC640, "e":0x8BC646, "l":6,  "en":"_ Airport",    "ja":"空港　"  },
  0x8AE442: { "b":0x8AE442, "e":0x8AE468, "l":38, "en":"Airports are the deployment points",   "ja":"　空港をもつ都市です。航空ユニットの　"  },
  0x8AE46C: { "b":0x8AE46C, "e":0x8AE492, "l":38, "en":"for all air units.  They provide",     "ja":"補充、補給ができます。自軍の首都周辺　"  },
  0x8AE496: { "b":0x8AE496, "e":0x8AE4C2, "l":44, "en":"repairs, supplies and defense.",       "ja":"の空港は航空ユニットの生産ができます。　　　"  },

  # Port
  0x8BC57F: { "b":0x8BC57F, "e":0x8BC583, "l":4,  "en":"⏺62",         "ja":"港　"  },
  0x8BC648: { "b":0x8BC648, "e":0x8BC64E, "l":6,  "en":"__<Port",      "ja":"　港　"  },
  0x8AE4C4: { "b":0x8AE4C4, "e":0x8AE4EA, "l":38, "en":"Ports are the deployment points",      "ja":"　港をもつ都市です。海上ユニットの補　"  },
  0x8AE4EE: { "b":0x8AE4EE, "e":0x8AE514, "l":38, "en":"for all naval units.  They provide",   "ja":"充、補給ができます。自軍の首都周辺の　"  },
  0x8AE518: { "b":0x8AE518, "e":0x8AE53A, "l":34, "en":"repairs, supplies and defense.",       "ja":"港は海上ユニットの生産ができます。"  },

  # Bridge
  0x8BC585: { "b":0x8BC585, "e":0x8BC589, "l":4,  "en":"⏺63",         "ja":"橋　"  },
  0x8BC650: { "b":0x8BC650, "e":0x8BC656, "l":6,  "en":"_< Bridge",    "ja":"　橋　"  },
  0x8AE53C: { "b":0x8AE53C, "e":0x8AE562, "l":38, "en":"Bridges are essentially roads",        "ja":"　道路と同じく移動しやすいですが、防　"  },
  0x8AE566: { "b":0x8AE566, "e":0x8AE58C, "l":38, "en":"with greater strategic value.",        "ja":"御力もない地形です。　　　　　　　　　"  },
  0x8AE590: { "b":0x8AE590, "e":0x8AE5B6, "l":38, "en":"No defense and hard to escape.",       "ja":"　　　　　　　　　　　　　　　　　　　"  },

  # Shoal
  0x8BC58B: { "b":0x8BC58B, "e":0x8BC58F, "l":4,  "en":"⏺64",         "ja":"浅瀬"  },
  0x8BC658: { "b":0x8BC658, "e":0x8BC65E, "l":6,  "en":"_  Shoal",  "ja":"浅瀬　"  },
  0x8AE5B8: { "b":0x8AE5B8, "e":0x8AE5DE, "l":38, "en":"Beaches & shoals provide loading",     "ja":"　輸送船への乗り降りができます。防御　"  },
  0x8AE5E2: { "b":0x8AE5E2, "e":0x8AE608, "l":38, "en":"and unloading points for landers,",    "ja":"力がないので守りにはむきません。　　　"  },
  0x8AE60C: { "b":0x8AE60C, "e":0x8AE632, "l":38, "en":"but offer no defensive cover.",        "ja":"　　　　　　　　　　　　　　　　　　　"  },

  # Base
  0x8BC591: { "b":0x8BC591, "e":0x8BC595, "l":4,  "en":"⏺65",             "ja":"工場"  },
  0x8BC660: { "b":0x8BC660, "e":0x8BC666, "l":6,  "en":"__Base",           "ja":"工場　"  },
  0x8AE634: { "b":0x8AE634, "e":0x8AE65A, "l":38, "en":"Bases are the deployment points",      "ja":"　工場をもつ都市です。自軍の首都周辺　"  },
  0x8AE65E: { "b":0x8AE65E, "e":0x8AE684, "l":38, "en":"for all ground units.  They offer",    "ja":"の工場は陸上ユニットの生産と補充、補　"  },
  0x8AE688: { "b":0x8AE688, "e":0x8AE6B0, "l":40, "en":"repairs, supplies and good cover.",    "ja":"給ができます。　　　　　　　　　　　　　"  },

  # Railroad
  0x8BC597: { "b":0x8BC597, "e":0x8BC59B, "l":4,  "en":"⏺66",             "ja":"鉄道"  },
  0x8BC668: { "b":0x8BC668, "e":0x8BC66E, "l":6,  "en":"_<Railroad",       "ja":"鉄道　"  },
  0x8AE6B2: { "b":0x8AE6B2, "e":0x8AE6CE, "l":28, "en":"Trains can travel quickly along",      "ja":"　列車砲の移動ができます。　"  },
  0x8AE6D2: { "b":0x8AE6D2, "e":0x8AE6F8, "l":38, "en":"railroads.  For most other units,",    "ja":"　　　　　　　　　　　　　　　　　　　"  },
  0x8AE6FC: { "b":0x8AE6FC, "e":0x8AE722, "l":38, "en":"they are difficult to cross.",         "ja":"　　　　　　　　　　　　　　　　　　　"  },

  # Fort
  0x8BC59D: { "b":0x8BC59D, "e":0x8BC5A1, "l":4,  "en":"⏺67",         "ja":"要塞"  },
  0x8BC670: { "b":0x8BC670, "e":0x8BC676, "l":6,  "en":"__|Fort",      "ja":"要塞　"  },
  0x8AE724: { "b":0x8AE724, "e":0x8AE74A, "l":38, "en":"Forts provide the best defense",       "ja":"さいだいの防御力をもつぼうえい用の　　"  },
  0x8AE74E: { "b":0x8AE74E, "e":0x8AE774, "l":38, "en":"available, halving damage taken.",     "ja":"地形です。　　　　　　　　　　　　　　"  },
  0x8AE778: { "b":0x8AE778, "e":0x8AE79E, "l":38, "en":"Cannot be occupied.",                  "ja":"　　　　　　　　　　　　　　　　　　　"  },

  # Lab
  0x8BC5A3: { "b":0x8BC5A3, "e":0x8BC5A7, "l":4,  "en":"⏺68",         "ja":"研究"  },
  0x8BC678: { "b":0x8BC678, "e":0x8BC67E, "l":6,  "en":"__ Lab",       "ja":"研究所"  },
  0x8AE7A0: { "b":0x8AE7A0, "e":0x8AE7C6, "l":38, "en":"The first unit to capture a Lab",      "ja":"　研究所をもつ都市です。機能は都市と　"  },
  0x8AE7CA: { "b":0x8AE7CA, "e":0x8AE7EE, "l":36, "en":"acquires the Proto Tank.  Also,",      "ja":"同じですが、中立のときに占領すると　"  },
  0x8AE7F2: { "b":0x8AE7F2, "e":0x8AE818, "l":38, "en":"it has the same benefits as cities.",  "ja":"「新型戦車」がてに入ります。　　　　　"  },

  # Depot
  0x8BC5A9: { "b":0x8BC5A9, "e":0x8BC5AD, "l":4,  "en":"⏺69",         "ja":"駅　"  },
  0x8BC680: { "b":0x8BC680, "e":0x8BC686, "l":6,  "en":"_| Depot",     "ja":"　駅　"  },
  0x8AE81A: { "b":0x8AE81A, "e":0x8AE840, "l":38, "en":"Train depots provide repairs and",     "ja":"　鉄道駅をもつ都市です。列車砲の補充、"  },
  0x8AE844: { "b":0x8AE844, "e":0x8AE86A, "l":38, "en":"supplies for trains, and serve as",    "ja":"補給ができます。首都周辺の駅は列車砲　"  },
  0x8AE86E: { "b":0x8AE86E, "e":0x8AE894, "l":38, "en":"a loading point for ground units.",    "ja":"の生産ができます。　　　　　　　　　　"  },

}
