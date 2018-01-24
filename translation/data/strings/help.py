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
# 22 tiles max (176 pixels) for main text area lines (incl. one initial space, needed for nice layout).

strings = {

# HELP BAR
  0x918422: { "b":0x918422, "e":0x918436, "l":20, "en":"⏫00|Browse____<Done",    "ja":"せんたく　　　ぬける"  },

# SECTIONS (Upper left box)
  0x9184F3: { "b":0x9184F3, "e":0x918503, "l":16, "en":"⏫08_Section A", "ja":"あそびかたの説明"  },
  0x918505: { "b":0x918505, "e":0x918515, "l":16, "en":"⏫10_Section B", "ja":"マップコマンド　"  },
  0x918517: { "b":0x918517, "e":0x918527, "l":16, "en":"⏫08_Section C", "ja":"部隊コマンド　　"  },

# PAGE NAVIGATION BAR

  # Guide A: General / Overview / How To Play
  0x9195C2: { "b":0x9195C2, "e":0x9195C8, "l":6,  "en":"_⏺81_",      "ja":"Ｐ１　"  },
  0x9195CA: { "b":0x9195CA, "e":0x9195D0, "l":6,  "en":"_⏺82_",      "ja":"Ｐ２　"  },
  0x9195D2: { "b":0x9195D2, "e":0x9195D8, "l":6,  "en":"_⏺83_",      "ja":"Ｐ３　"  },
  0x9195DA: { "b":0x9195DA, "e":0x9195E0, "l":6,  "en":"_⏺84_",      "ja":"Ｐ４　"  },
  0x9195E2: { "b":0x9195E2, "e":0x9195E8, "l":6,  "en":"_⏺85_",      "ja":"Ｐ５　"  },
  0x9195EA: { "b":0x9195EA, "e":0x9195F0, "l":6,  "en":"_⏺86_",      "ja":"Ｐ６　"  },
  0x9195F2: { "b":0x9195F2, "e":0x9195F8, "l":6,  "en":"_⏺87_",      "ja":"Ｐ７　"  },
  0x9195FA: { "b":0x9195FA, "e":0x919600, "l":6,  "en":"_⏺88_",      "ja":"Ｐ８　"  },
  0x919602: { "b":0x919602, "e":0x919608, "l":6,  "en":"_⏺89_",      "ja":"Ｐ９　"  },
  0x91960A: { "b":0x91960A, "e":0x919610, "l":6,  "en":"⏺81⏺80_",   "ja":"Ｐ１０"  },
  0x919612: { "b":0x919612, "e":0x919618, "l":6,  "en":"⏺81⏺81_",   "ja":"Ｐ１１"  },
  0x91961A: { "b":0x91961A, "e":0x919620, "l":6,  "en":"⏺81⏺82_",   "ja":"Ｐ１２"  },
  0x919622: { "b":0x919622, "e":0x919628, "l":6,  "en":"⏺81⏺83_",   "ja":"Ｐ１３"  },
  0x91962A: { "b":0x91962A, "e":0x919630, "l":6,  "en":"⏺81⏺84_",   "ja":"Ｐ１４"  },
  0x919632: { "b":0x919632, "e":0x919638, "l":6,  "en":"⏺81⏺85_",   "ja":"Ｐ１５"  },

  # Guide B: Main Commands
  0x91963A: { "b":0x91963A, "e":0x919640, "l":6,  "en":"_⏺81_",      "ja":"生産　"  }, # Deploying Units (1)
  0x919642: { "b":0x919642, "e":0x919648, "l":6,  "en":"_⏺82_",      "ja":"生産２"  }, # Deploying Units (2)
  0x91964A: { "b":0x91964A, "e":0x919650, "l":6,  "en":"_⏺83_",      "ja":"説明　"  }, # Help
  0x919652: { "b":0x919652, "e":0x919658, "l":6,  "en":"_⏺84_",      "ja":"部隊　"  }, # Units
  0x91965A: { "b":0x91965A, "e":0x919660, "l":6,  "en":"_⏺85_",      "ja":"全補　"  }, # Supply (1)
  0x919662: { "b":0x919662, "e":0x919668, "l":6,  "en":"_⏺86_",      "ja":"全補２"  }, # Supply (2)
  0x91966A: { "b":0x91966A, "e":0x919670, "l":6,  "en":"_⏺87_",      "ja":"全補３"  }, # Supply (3)
  0x919672: { "b":0x919672, "e":0x919678, "l":6,  "en":"_⏺88_",      "ja":"状況　"  }, # Intel
  0x91967A: { "b":0x91967A, "e":0x919680, "l":6,  "en":"_⏺89_",      "ja":"設定　"  }, # Options
  0x919682: { "b":0x919682, "e":0x919688, "l":6,  "en":"⏺81⏺80_",   "ja":"処分　"  }, # Dismiss
  0x91968A: { "b":0x91968A, "e":0x919690, "l":6,  "en":"⏺81⏺81_",   "ja":"降伏　"  }, # Retreat
  0x919692: { "b":0x919692, "e":0x919698, "l":6,  "en":"⏺81⏺82_",   "ja":"再戦　"  }, # Load
  0x91969A: { "b":0x91969A, "e":0x9196A0, "l":6,  "en":"⏺81⏺83_",   "ja":"休戦　"  }, # Save
  0x9196A2: { "b":0x9196A2, "e":0x9196A8, "l":6,  "en":"⏺81⏺84_",   "ja":"終了　"  }, # End Day
  0x9196AA: { "b":0x9196AA, "e":0x9196B0, "l":6,  "en":"___",          "ja":"　　　"  },

  # Guide C: Unit Commands
  0x9196B2: { "b":0x9196B2, "e":0x9196B8, "l":6,  "en":"_⏺81_",      "ja":"攻撃　"  }, # Attack (1)
  0x9196BA: { "b":0x9196BA, "e":0x9196C0, "l":6,  "en":"_⏺82_",      "ja":"攻撃２"  }, # Attack (2)
  0x9196C2: { "b":0x9196C2, "e":0x9196C8, "l":6,  "en":"_⏺83_",      "ja":"待機　"  }, # End Day
  0x9196CA: { "b":0x9196CA, "e":0x9196D0, "l":6,  "en":"_⏺84_",      "ja":"占領　"  }, # Capture (1)
  0x9196D2: { "b":0x9196D2, "e":0x9196D8, "l":6,  "en":"_⏺85_",      "ja":"占領２"  }, # Capture (2)
  0x9196DA: { "b":0x9196DA, "e":0x9196E0, "l":6,  "en":"_⏺86_",      "ja":"合流　"  }, # Join
  0x9196E2: { "b":0x9196E2, "e":0x9196E8, "l":6,  "en":"_⏺87_",      "ja":"補給　"  }, # Supply (1)
  0x9196EA: { "b":0x9196EA, "e":0x9196F0, "l":6,  "en":"_⏺88_",      "ja":"補給２"  }, # Supply (2)
  0x9196F2: { "b":0x9196F2, "e":0x9196F8, "l":6,  "en":"_⏺89_",      "ja":"搭載　"  }, # Load (1)
  0x9196FA: { "b":0x9196FA, "e":0x919700, "l":6,  "en":"⏺81⏺80_",   "ja":"搭載２"  }, # Load (2)
  0x919702: { "b":0x919702, "e":0x919708, "l":6,  "en":"⏺81⏺81_",   "ja":"搭載３"  }, # Load (3)
  0x91970A: { "b":0x91970A, "e":0x919710, "l":6,  "en":"⏺81⏺82_",   "ja":"降車　"  }, # Drop
  0x919712: { "b":0x919712, "e":0x919718, "l":6,  "en":"___",         "ja":"　　　"  },
  0x91971A: { "b":0x91971A, "e":0x919720, "l":6,  "en":"___",         "ja":"　　　"  },
  0x919722: { "b":0x919722, "e":0x919728, "l":6,  "en":"___",         "ja":"　　　"  },



# SECTION A: "How To Play"

  # A0: Table of Contents
  0x91979E: { "b":0x91979E, "e":0x9197BA, "l":28, "en":"⏫20 Field Manual________", "ja":"　　　　ページの説明　　　　"  },
  0x919DFE: { "en":[
    " Welcome to training, CO!  Section A",
    " is your basic Field Manual, which",
    " contains an overview of how to play..",
    "__   SUPER FAMICOM WARS!",
    "",
    " Discover useful info for both novice",
    " and seasoned COs.  ATTEN-TION!",
    " Use up/down on{|} to flip pages, and",
    " and left/right to change sections."
  ], "ja": [
    "　この「あそびかたの説明」は、下のようなペー",
    "ジでなりたっています。目をとおしてみてくださ",
    "い。",
    "　Ｐ１　〜Ｐ９　　　あそびかたの説明　　　　"
    "　Ｐ１０〜Ｐ１１　　さくてきモードの説明",
    "　Ｐ１２　　　　　　同盟の説明",
    "　Ｐ１３〜Ｐ１５　　わんぽいんとあどばいす",
    "",
    "　また　　の左右で説明をきりかえられます。"
  ]},

  # A1: Field Manual
  0x9197BC: { "b":0x9197BC, "e":0x9197D8, "l":28, "en":"⏫20 A1: Introduction_______", "ja":"　　　あそびかたの説明　　　"  },
  0x91BC8E: { "en":[
    " Let's begin with basic training.",
    "",
    " This will cover the mission objectives,",
    " how to build and move your forces",
    " around and engaging with the enemy.",
    "",
    " We'll finish this section with button",
    " shortcuts, Fog of War mode, Diplomatic",
    " Relations and some additional advice."
  ], "ja": [
    "　あそびかたの説明は、",
    "Ｐ２　　　　　何をすればいいの？",
    "Ｐ３〜Ｐ４　　何を生産する？",
    "Ｐ５〜Ｐ６　　どう行動する？",
    "Ｐ７　　　　　占領しよう！　",
    "Ｐ８　　　　　さあ攻撃だ！　",
    "Ｐ９　　　　　おわりに　　　",
    "　となっています。基本をひととおりかいてます"
    "ので、はじめてのかたはよんでください。"
  ]},

  # A2: Mission Objective
  0x9197DA: { "b":0x9197DA, "e":0x9197F6, "l":28, "en":"⏫20 A2: Mission Objective____", "ja":"　　　何をすればいいの？　　"  },
  0x91BDC4: { "en":[
    " The objective of the game is to either",
    " destroy all enemy forces, or capture",
    " the enemy's HQ{} .  Meet these",
    " objectives by building an army and",
    " engaging the enemy across the map.",
    "",
    " Equally, you will be defeated if all of",
    " your units are destroyed or if your",
    " HQ{{}is captured by the enemy."
  ], "ja": [
    "　ゲームの目的は、敵を全滅、もしくは敵の首都",
    "を占領することです。全滅させられたり、こちら",
    "の首都を占領されたりすると負けです。　",
    "　目的をたっせいするには、ユニットを生産し、",
    "占領ポイントを占領して収入をふやし、敵を攻撃",
    "して勝たねばなりません。　　　　　　　　　　"
  ]},

  # A3: Building An Army 1/2
  0x9197F8: { "b":0x9197F8, "e":0x919814, "l":28, "en":"⏫20 A3: Building An Army_|1⏮1|/|2_", "ja":"　　何を生産する？　その１　"  },
  0x91BF0E: { "en":[
    " Every CO needs an army.  To deploy",
    " your first unit, move the cursor to",
    " your HQ{{}and press{|<}when the",
    " cursor changes to {{}.  Your funds",
    " to build with are shown next to the",
    " icon.  If a unit exceeds your funds, it",
    " is grayed out and cannot be deployed.",
    " Start by deploying a basic unit such as",
    " an Infantry {} or Mech{} ."
  ], "ja": [
    "　はじめにすることは生産です。カーソル　　が",
    "　　　にかわるところで　　をおしてください。",
    "　自軍の色の首都　　と、そこにちかい工場　　",
    "空港　　港　　駅　　でかわるはずです。",
    "　生産するにはお金がいります。　　のとなりの",
    "数が今の自分のお金です。これより高いユニット",
    "はグレーで表示され、生産できません。　　　　",
    "　まず、歩兵　　か戦闘工兵　　を生産してくだ",
    "さい。"
  ]},

  # A4: Building An Army 2/2
  0x919816: { "b":0x919816, "e":0x919832, "l":28, "en":"⏫20 A4: Building An Army_2⏮1|/|2_", "ja":"　　何を生産する？　その２　"  },
  0x91C090: { "en":[
    " Infantry {} are cheap, but weak.",
    " Mechs {} are more expensive and less",
    " mobile, but more powerful.  Only these",
    " two unit types can capture buildings,",
    " so they can be essential to victory.",
    " Hit{|<}over any unit to view its combat",
    " stats.  When finished building, select",
    " [End Day] from the menu to continue.",
    " You can move new units the next day."
  ], "ja": [
    "　歩兵　　は安いがよわい、戦闘工兵　　は高く",
    "移動力も少ないがそこそこつよい、という個性が",
    "あります。占領できるのはこの２ユニットだけな",
    "ので、多めに生産しておいてください。",
    "　何が何につよい、どこを移動できるという個性",
    "は、ユニットごとにありますので、生産するとき",
    "に　　をおして、かくにんしてみてださい。　　",
    "　１日目は生産だけになります。終了をえらんで",
    "ください。"
  ]},

  # A5: Moving Out! 1/2
  0x919834: { "b":0x919834, "e":0x919850, "l":28, "en":"⏫20 A5: Moving Out!____|1⏮1|/|2_", "ja":"　　どう行動する？　その１　"  },
  0x91C214: { "en":[
    " Pressing{|<}over a unit will highlight",
    " the areas of the map it can move to.",
    "",
    " For instance, move Infantry {} and",
    " Mechs {} towards buildings before",
    " capturing them. |Then deploy more",
    " powerful units, such as tanks, and",
    " move them nearby as protection.  Or,",
    " to launch attacks on the enemy."
  ], "ja": [
    "　さきほど生産したユニットの上で　　をおして",
    "ください。ユニットを中心にマップの色がかわり",
    "ます。色がかわったはんい内が、ユニットの移動",
    "はんいです。",
    "　歩兵　　や戦闘工兵　　なら、占領ポイントの",
    "上もしくはちかくに、戦車など攻撃がつよいユニ",
    "ットは歩兵　　や戦闘工兵　　を守るように動く",
    "か、敵ユニットと闘いに行くのがよいでしょう。"
  ]},

  # A6: Moving Out! 2/2
  0x919852: { "b":0x919852, "e":0x91986E, "l":28, "en":"⏫20 A6: Moving Out!____2⏮1|/|2_", "ja":"　　どう行動する？　その２　"  },
  0x91C376: { "en":[
    " When faced with difficult terrain, or",
    " to cover long distances at speed,",
    " use APCs { }, Landers {} and",
    " T-Copters { }.  For example, load an",
    " Infantry {} onto a T-Copter {}.",
    " Loading will consume one turn. |The",
    " following day, move the helicopter",
    " over land or sea and drop the foot",
    " soldier onto solid ground."
  ], "ja": [
    "　海などにはばまれて、そのユニットでは移動で",
    "きないとき、きょりがとおくて、移動するのに何",
    "日もかかるときには、輸送ヘリ　　や輸送船　　",
    "などに載っていくといいでしょう。",
    "　たとえば、空港　　で輸送ヘリ　　をつくり、",
    "歩兵　　を輸送ヘリ　　の上に移動させてみてく",
    "ださい。つぎの日から輸送ヘリ　　の移動力で動",
    "けるので、とおくまではこべます。"
  ]},

  # A7: Capturing Buildings
  0x919870: { "b":0x919870, "e":0x91988C, "l":28, "en":"⏫20 A7: Capturing Buildings___", "ja":"　　　　占領しよう！　　　　"  },
  0x91C4E0: { "en":[
    " When moving your Infantry {} or",
    " Mech {} to a building not currently",
    " controlled by your army, you'll be given",
    " the option to Capture it.",
    "",
    " Buildings have 20 capture points, so",
    " an Infantry {} or Mech {} unit with",
    " its full 10{}|can capture it in two",
    " consecutive days."
  ], "ja": [
    "　歩兵　　や戦闘工兵　　を自分の色以外の占領",
    "ポイントに移動させてください。「占領」という",
    "コマンドがでますので決定してください。　　　",
    "　占領ポイントにはたいきゅう力があります。ふ",
    "だんは２０あり、歩兵　　や戦闘工兵　　が　　",
    "１０のときに、２日で占領できます。　　　　　"
  ]},

  # A8: Engage The Enemy!
  0x91988E: { "b":0x91988E, "e":0x9198AA, "l":28, "en":"⏫20 A8: Engage The Enemy!___", "ja":"　　　　さあ攻撃だ！　　　　"  },
  0x91C60A: { "en":[
    " When attacking, it's advised to use",
    " stronger units and the terrain to your",
    " advantage.  Intel on terrain can too be",
    " seen by pressing{|<}above it.  Most",
    " units must be next|to|enemies to attack,",
    " but others such as Artillery {|} can",
    " attack indirectly.  Indirect attacks are",
    " powerful, but can't be performed after",
    " moving <-< so move these units wisely."
  ], "ja": [
    "　敵がじゃまな所にいたり、こちらのじゃまをし",
    "てきたら戦闘をしましょう。戦闘をしかけるとき",
    "は、敵よりゆうりな地形で、つよいユニットでが",
    "基本です。それぞれ地形やユニットの上で　　を",
    "おして、かくにんしてください。",
    "　基本的にとなりにいる敵ユニットに行える「攻",
    "撃」ですが、　　　が２以上のユニットはかんせ",
    "つ攻撃できます。移動したあとすぐには攻撃でき",
    "ませんが、つよいのでうまくつかいましょう。"
  ]},

  # A9: Button Shortcuts
  0x9198AC: { "b":0x9198AC, "e":0x9198C8, "l":28, "en":"⏫20 A9: Button Shortcuts____", "ja":"　　　　　おわりに　　　　　"  },
  0x91C7A8: { "en":[
    " There are shortcuts for efficient COs:",
    "____Displays{} for all units and",
    "____whether they are loaded.",
    "____Quickly moves the cursor",
    "____between each army's HQ {}.",
    "____Quickly moves the cursor",
    "____between units yet to move.",
    "",  # Leave blank (row of icons)
    "____Restarts the game."
  ], "ja": [
    "　さいごに、べんりなキーの説明をします。",
    "　　　　がめん中の全ユニットの　　と、搭載状",
    "　　　　況をみることができます。",
    "　　　　赤軍、青軍、　軍、　軍のじゅんばんで",
    "　　　　首都　　にカーソル　　がいきます。",
    "　　　　まだ行動していないユニットにカーソル",
    "　　　　　　がいきます。",
    "",
    "　　　　リセットできます。"
  ]},

  # A10: Fog of War 1/2
  0x9198CA: { "b":0x9198CA, "e":0x9198E6, "l":28, "en":"⏫20 A10: Fog of War____|1⏮1|/|2_", "ja":"　　さくてきモード　その１　"  },
  0x91C8F2: { "en":[
    " During Fog of War, your view of the",
    " map will be limited.  Only your army's",
    " and allies' buildings, and areas within",
    " { | } range of your units, will be fully",
    " visible.  Outside of this, any enemy",
    " movement will be undetectable.",
    " Infantry {} and Mech {} have a",
    " useful skill <-< when climbing mountains",
    " __<|, their vision increases by 3."
  ], "ja": [
    "　索敵はんい外はみえなくなるモードです。",
    "　索敵はんいは、自軍と同盟軍の占領ポイントの",
    "上、自軍と同盟軍ユニットの　　　内となってい",
    "ます。　　　　　　　　　　　　　　　　　　",
    "　歩兵　　と戦闘工兵　　は山　　の上にいると",
    "索敵はんいにプラス３されます。　　　　　　　"
  ]},

  # A11: Fog of War 2/2
  0x9198E8: { "b":0x9198E8, "e":0x919904, "l":28, "en":"⏫20 A11: Fog of War____2⏮1|/|2_", "ja":"　　さくてきモード　その２　"  },
  0x91CA18: { "en":[
    " If a unit is moved into the path of an",
    " enemy concealed by the Fog of War,",
    " that unit's turn will end.",
    "",
    " In this mode, Subs{{<}cannot be",
    " detected, even if they are within your",
    " range of vision, unless they are",
    " directly adjacent to one of your units",
    " or instead docked within a port{} ."
  ], "ja": [
    "　索敵はんい外、つまりマップがグレーになって",
    "いる場所に行動したとき、もしその目的地、もし",
    "くは移動とちゅうに敵がいたら「そうぐう」とな",
    "りきょうせい的に行動が終了させられます。",
    "　なお、潜水艦　　は索敵はんい内にいても、と",
    "なりあう、もしくはこちらの港　　にいないかぎ",
    "りみえません。"
  ]},

  # A12: Diplomatic Relations
  0x919906: { "b":0x919906, "e":0x919922, "l":28, "en":"⏫20 A12: Diplomatic Relations___", "ja":"　　　　　　同盟　　　　　　"  },
  0x91CB4C: { "en":[
    " In 4P games, up to two COs may be",
    " allied with your side against the enemy.",
    " Allies can help destroy the enemy's",
    " units, or capture their HQ {}.",
    "",
    " However, allied buildings cannot be",
    " captured, and they will not supply or",
    " repair your units.  After all, this is",
    " war <-< not a tea party!"
  ], "ja": [
    "　同盟をむすぶことができるモードです。　　　",
    "　同盟したあいてとともに同盟軍と自軍以外の敵",
    "を全滅、もしくは首都占領してください。ただ、",
    "同盟軍の都市は占領することはできませんし、そ",
    "の都市の上で補充、補給することもできません。"
  ]},

  # A13: Advice 1/3
  0x919924: { "b":0x919924, "e":0x919940, "l":28, "en":"⏫20 A13: Advice______|1⏮1|/|3_", "ja":"　わんぽいんとあどばいす１　"  },
  0x91CC64: { "en":[
    " Capturing <-< Call For Reinforcements!",
    "",
    " Units can be attacked while capturing a",
    " building.  If the unit is wiped out, all",
    " capturing progress will also be lost.",
    "",
    " This can be avoided by joining another",
    " unit with the injured one.< Capturing can",
    " then continue until the building is taken."
  ], "ja": [
    "　　　　　占領中に合流できること　　　　　",
    "",
    "・占領とちゅうに敵に攻撃されて、全滅したこ",
    "　とがあるとおもいます。そうしたらまたさい",
    "　しょからやりなおしになり、たいへんです。",
    "　そういうときには、占領しているユニットに",
    "　合流しましょう。占領ポイントからでたわけ",
    "　ではありませんから、そのままつづけて占領",
    "　できます。"
  ]},

  # A14: Advice 2/3
  0x919942: { "b":0x919942, "e":0x91995E, "l":28, "en":"⏫20 A14: Advice______2⏮1|/|3_", "ja":"　わんぽいんとあどばいす２　"  },
  0x91CDB8: { "en":[
    " Remembering Your Rank",
    "",
    " Enabling [Level Up] allows units to",
    " increase their level after a skirmish.",
    "",
    " Note that if the unit has sustained",
    " damage, and is joined with another to",
    " increase  }, the higher of the two",
    " units' levels will be retained."
  ], "ja": [
    "　　　　　　　レベルと合流",
    "",
    "・さいしょの設定で、レベルアップを○●にす",
    "　ると戦闘でレベルが上がるようになりますが、",
    "　レベルが上がるころにはこちらのＨＰ　　も",
    "　少なくなっていることでしょう。そういうと",
    "　きにはレベルのひくいユニットを合流させて",
    "　みてください。レベルは高いほうがひきつが",
    "　れます。"
  ]},

  # A15: Advice 3/3
  0x919960: { "b":0x919960, "e":0x91997C, "l":28, "en":"⏫20 A15: Advice______3⏮1|/|3_", "ja":"　わんぽいんとあどばいす３　"  },
  0x91CEFC: { "en":[
    " Expose & Destroy",
    "",
    " During Fog of War, indirect units are",
    " unable to fire on concealed areas -",
    " even when you know an enemy is there.",
    "",
    " Wide {|| } range units, such as Recons",
    " {}and Cruisers{} , can be sent in",
    " first to expose a target for attack."
  ], "ja": [
    "　　　　　　偵察車　　と護衛艦",
    "",
    "・索敵モードのときの索敵はんい外には、たと",
    "　えそこに敵がいるとしっていても、かんせつ",
    "　攻撃などをしかけることはできません。そう",
    "　いうときには　　　のひろい偵察車　　や護",
    "　衛艦　　などをすてるつもりで行かせましょ",
    "　う。少なくともその日は攻撃できるようにな",
    "　ります。"
  ]},



# SECTION B: "Main Commands"

  # B0
  0x91997E: { "b":0x91997E, "e":0x91999A, "l":28, "en":"⏫20 Main Commands________", "ja":"　マップコマンドの説明　　　"  },
  0x919D3A: { "en":[
    " In Section B, we'll walk through the",
    " commands available from the high level",
    " and system menus. (Menus are good for",
    " more than your rations in the mess hall.)",
    "",
    " Discover useful info for both novice",
    " and seasoned COs.  ATTEN-TION!",
    " Use up/down on{|} to flip pages, and",
    " and left/right to change sections."
  ], "ja": [
    "ぜんたいをかんりするためのコマンドです。　　",
    "　　　　　　　　　　　　　　　　　　　　　　"
  ]},

  # B1: Deploy 1/3
  0x91999C: { "b":0x91999C, "e":0x9199B8, "l":28, "en":"⏫20 B1: Deploy_______|1⏮1|/|3_", "ja":"　　生産コマンドの説明その１"  },
  0x919F42: { "en":[
    " If owned from the start of a battle,",
    " press{|<}over these buildings to",
    " deploy the following unit types:",
    "",
    "___HQ______Ground Units",
    "___Bases____Ground Units",
    "___Airports___Air Units",
    "___Ports____Naval Units",
    "___Depots____Train"
  ], "ja": [
    "　ユニットの生産を行うコマンドです。　　　　",
    "　生産ができる場所とは、　　　が　　　のよう",
    "に表示される場所、つまり自軍の首都　　をふく",
    "め２マス周辺の工場　　空港　　港　　駅　　で",
    "す。",
    "　生産は６０部隊までです。なお、列車砲　　を",
    "生産すると、こわされるまでは、あらたな列車砲",
    "を生産することはできません。"
  ]},

  # B2: Deploy 2/3
  0x9199BA: { "b":0x9199BA, "e":0x9199D6, "l":28, "en":"⏫20 B2: Deploy_______2⏮1|/|3_", "ja":"　　生産コマンドの説明その２"  },
  0x91A08C: { "en":[
    " Every good CO has, at some point,",
    " imagined themselves with an unlimited",
    " number of troops at their disposal.",
    "",
    " The realities of war, however, limit you",
    " to a maximum of 60 units under your",
    " command at any one time.  This includes",
    " no more than one train at once per CO.",
    " Do not get ideas above your station."
  ], "ja": [
    "　どこで何が生産できるか説明します。　　　　",
    "　　　　　　　・・・地上ユニット　　　　　　",
    "　　　　　　　・・・航空ユニット　　　　　　",
    "　　　　　　　・・・海上ユニット　　　　　　",
    "　　　　　　　・・・列車砲　　　　　　　　　"
  ]},

  # B3: Deploy 3/3
  0x9199D8: { "b":0x9199D8, "e":0x9199F4, "l":28, "en":"⏫20 B3: Deploy_______3⏮1|/|3_", "ja":"　　説明コマンドの説明　　　"  },
  0x91A182: { "en":[
    " Successful COs will often capture",
    " unoccupied and enemy Bases{|},",
    " Airports{|},|Ports{|} & Depots{|}.",
    "",
    " Due to staff shortages, captured",
    " buildings cannot be used to deploy new",
    " units.  However, they can repair and",
    " supply their correlating units.| For more",
    " information on this, study B5."
  ], "ja": [
    "　このがめんをみることができるコマンドです。",
    "　各コマンドのかいせつやあそびかたを説明して",
    "いるので、こまったらみてください。　　　　　",
    "　　　　　　　　　　　　　　　　　　　　　　　"
  ]},

  # B4: Units
  0x9199F6: { "b":0x9199F6, "e":0x919A12, "l":28, "en":"⏫20 B4: Units___________", "ja":"　　部隊コマンドの説明　　　"  },
  0x91A242: { "en":[
    " The Units option in the main menu allows",
    " you to view all of your own forces",
    " currently deployed on the battlefield.",
    "",
    " Use{{   }}to sort units based on",
    " their Type, Level, HP{  , Fuel|{} or",
    " Ammo{}.  Scroll through the list with",
    " up or down{|} and hit{|<}on a unit to",
    " jump directly to it on the map."
  ], "ja": [
    "　部隊いちらんを表示するコマンドです。　　　",
    "　　の左右でへいしゅ、レベル、ＨＰ　　、ねん",
    "りょう　　、弾　　のそれぞれについてならべか",
    "えることができます。",
    "　また、　　の上下で目的のユニットをえらび決",
    "定すると、マップ中のユニットへカーソル　　を",
    "移動させることができます。"
  ]},

  # B5: Supply 1/3
  0x919A14: { "b":0x919A14, "e":0x919A30, "l":28, "en":"⏫20 B5: Supply_______|1⏮1|/|3_", "ja":"　　全補コマンドの説明その１"  },
  0x91A36E: { "en":[
    " With Auto Supply on, units at buildings",
    " under your control on the start of a",
    " new day will gain 2{|}and have their",
    " <{}&<{} resupplied at these sites:",
    "",
    "__________Ground units",
    "__________Air units",
    "__________Naval units",
    "__________Train"
  ], "ja": [
    "　全ユニットに補給、補充を行うコマンドです。",
    "　それぞれのユニットにたいおうした自軍占領ポ",
    "イントで、１日につき２だいの補充、　　　　の",
    "補給が行われます。どこで何が補充、補給をうけ",
    "られるかは下をみてください。　　　　　　　　",
    "　　　　　　　　　・・・地上ユニット　　　　",
    "　　　　　　　　　・・・航空ユニット　　　　",
    "　　　　　　　　　・・・海上ユニット　　　　",
    "　　　　　　　　　・・・列車砲　　　　　　　　"
  ]},

  # B6: Supply 2/3
  0x919A32: { "b":0x919A32, "e":0x919A4E, "l":28, "en":"⏫20 B6: Supply_______2⏮1|/|3_", "ja":"　　全補コマンドの説明その２"  },
  0x91A51E: { "en":[
    " Of course, the bean counters at HQ",
    " (grumbles under breath..<) do not allow",
    " us to supply and repair our forces for",
    " free.  The costs in{|<}are below:",
    "",
    "____1/<10 of the unit's price to repair",
    "____1{|}per fuel point refilled",
    "____Depends on weapon type. Hit",
    "____{<  while over a unit to see it."
  ], "ja": [
    "　なお、つぎのじょうけんのユニットは　　　　",
    "の補給はされますが、補充はされません。　　　",
    "",
    "　補給車にりんせつした地上ユニットと　　　　",
    "　護衛艦に搭載された　　　　　　　　　　　　",
    "",
    "　全補は、すでに待機じょうたいになった（その",
    "日の行動がおわった）ユニットにたいしては、行",
    "われません。"
  ]},

  # B7: Supply 3/3
  0x919A50: { "b":0x919A50, "e":0x919A6C, "l":28, "en":"⏫20 B7: Supply_______3⏮1|/|3_", "ja":"　　全補コマンドの説明その３"  },
  0x91A654: { "en":[
    " While repair can only occur in buildings,",
    " some units can be resupplied with",
    " &{<} on the battlefield.  These are:",
    " Ground units &{{}{}|adjacent to",
    " a Supply Truck, and{{}{} loaded",
    " onto a Cruiser{|}.  Additionally, if",
    " Auto Supply is not enabled, the Supply",
    " menu option can be used to resupply",
    " any unit yet to move."
  ], "ja": [
    "　補充、補給にはお金がかかります。",
    "　補充には１だいにつきそのユニットの１／１０",
    "のねだんのお金がひつようです。",
    "　ねんりょう　　の補給は、１　ユニットの数",
    "つかったねんりょう、でもとめられます。",
    "　弾　　の補給は、ユニットごとにきめられた弾",
    "のねだんに、ユニットの数とつかった弾の数をか",
    "けたものです。弾のねだんはそれぞれのユニット",
    "の上で　　をおして、かくにんしてください。"
  ]},

  # B8: Intel
  0x919A6E: { "b":0x919A6E, "e":0x919A8A, "l":28, "en":"⏫20 B8: Intel____________", "ja":"　　状況コマンドの説明　　　"  },
  0x91A7E0: { "en":[
    " Intel offers data on the current battle.",
    " The first page displays the buildings,",
    " funds, income and units for each army.",
    " ",
    "____Available Funds",
    "____Income Per Day",
    "",
    " The second shows deployment info.",
    " Use{|} to change the army displayed."
  ], "ja": [
    "　ぜんたいの状況をはあくするコマンドです。　",
    "　それぞれの軍の占領状況や今もっているお金、",
    "収入や全ユニット数をみることができます。　",
    "　生産部隊数と全滅部隊数もここでみることがで",
    "きます。",
    "　　　　・・・今もっているお金",
    "　　　　・・・収入",
    "　です。"
  ]},

  # B9: Options
  0x919A8C: { "b":0x919A8C, "e":0x919AA8, "l":28, "en":"⏫20 B9: Options___________", "ja":"　　設定コマンドの説明　　　"  },
  0x91A8F0: { "en":[
    " The following Options can still be",
    " adjusted with a battle in progress:",
    "",
    " Auto Supply_____⏺C0/⏺C1",
    " Quick Battle</|Map__⏺C0/⏺C1",
    " Sound_________ Mono</|Stereo",
    "",
    " In 4P mode, you can also view the",
    " Diplomatic Relations between COs."
  ], "ja": [
    "　ゲームの設定をみるコマンドです。",
    "　以下の設定をへんこうできます。",
    "　プレイヤーのオート全補　ＯＮ／ＯＦＦ　　　",
    "　かんい戦闘モード　　　　ＯＮ／ＯＦＦ　　　",
    "　こうそくモード　　　　　ＯＮ／ＯＦＦ　　　",
    "　サウンドの設定　　　　　　",
    "　また、４Ｐモードでは　　　　　もみることが",
    "できます。"
  ]},

  # B10: Disband
  0x919AAA: { "b":0x919AAA, "e":0x919AC6, "l":28, "en":"⏫20 B10: Disband__________", "ja":"　　処分コマンドの説明　　　"  },
  0x91AA2A: { "en":[
    " There may be times when, for strategic",
    " reasons, it becomes necessary to",
    " remove a unit from the battlefield.",
    "",
    " The Disband command will change",
    " the< cursor< from{{<}  to< this{{|} ,",
    " allowing you to permanently remove the",
    " selected unit by pressing{|<}above it."
    ""
  ], "ja": [
    "　自軍のユニットを処分できるコマンドです。　",
    "　処分コマンドをえらぶと、カーソルの形が、",
    "",
    "　　　から、　　　にかわるので、処分したいユ",
    "ニットへあわせ決定してください。　"
  ]},

  # B11: Retreat
  0x919AC8: { "b":0x919AC8, "e":0x919AE4, "l":28, "en":"⏫20 B11: Retreat__________", "ja":"　　降伏コマンドの説明　　　"  },
  0x91AAE0: { "en":[
    " Q<) Which is the better outcome:| Losing",
    " a battle or to retreat first instead<?",
    "",
    " A) W<I<N<N<I<N<G.",
    "",
    " However, if you MUST leave the",
    " current battlefield, selecting Retreat",
    " will disband all of your units and allow",
    " any remaining COs to fight for victory."
  ], "ja": [
    "　戦いに降伏するコマンドです。　　　　　　　",
    "　降伏すると負けになってしまうので注意してく",
    "ださい。　　　　　　　　　　　　　　　　　　　"
  ]},

  # B12: Load
  0x919AE6: { "b":0x919AE6, "e":0x919B02, "l":28, "en":"⏫20 B12: Load___________", "ja":"　　再戦コマンドの説明　　　"  },
  0x91AB70: { "en":[
    " Load will quickly load from your most",
    " recent save point within the current",
    " game.  This will, of course, lose any",
    " progress beyond when the loaded save",
    " was made.",
    "",
    " (<If you have started a new game, but",
    " not yet made any saves, this option",
    " will not yet be available.<)"
  ], "ja": [
    "　休戦データを再開するコマンドです。　　　　",
    "　セーブしたところからやりなおしたいときにえ",
    "らんでください。　　　　　　　　　　　　　　　"
  ]},

  # B13: Save
  0x919B04: { "b":0x919B04, "e":0x919B20, "l":28, "en":"⏫20 B13: Save___________", "ja":"　　休戦コマンドの説明　　　"  },
  0x91AC00: { "en":[
    " Even the most dedicated CO may need",
    " to temporarily leave the battlefield <-",
    " to consider new strategies or perhaps",
    " to make a delicious sandwich.",
    "",
    " Choosing Save from the menu will save",
    " the current state of battle for you to",
    " return to later.  Please note that this",
    " will overwrite the previous save state."
  ], "ja": [
    "　今のじょうたいをほぞんするコマンドです。",
    "　休戦すると、まえのデータがきえてしまうので",
    "注意してください。　　　　　　　　　　　　　　"
  ]},

  # B14: End Day
  0x919B22: { "b":0x919B22, "e":0x919B3E, "l":28, "en":"⏫20 B14: End Day__________", "ja":"　　終了コマンドの説明　　　"  },
  0x91AC50: { "en":[
    " If you have finished deploying, moving,",
    " capturing, loading, unloading and",
    " attacking, select the [End Day] option",
    " from the menu.",
    "",
    " This will allow all other COs to command",
    " their armies.  You will regain command",
    " of your own once all other COs have",
    " finished and a new day has begun."
  ], "ja": [
    "　その日の行動を終了するコマンドです。　　　",
    "　　　　　　"
  ]},



# SECTION C: "Unit Commands"

  # C0
  0x919B40: { "b":0x919B40, "e":0x919B5C, "l":28, "en":"⏫20 Unit Commands________", "ja":"　　部隊コマンドの説明　　　"  },
  0x919DA0: { "en":[
    " Finally, Section C will cover perhaps",
    " the most important commands:  Those",
    " which allow you to give direct orders to",
    " your units.",
    "",
    " Discover useful info for both novice",
    " and seasoned COs.  ATTEN-TION!",
    " Use up/down on{|} to flip pages, and",
    " and left/right to change sections."
  ], "ja": [
    "ユニットごとにしれいをあたえるコマンドです。",
    "　　　　　　　　　　　　　　　　　　　　　　"
  ]},

  # C1: Attack 1/2
  0x919B5E: { "b":0x919B5E, "e":0x919B7A, "l":28, "en":"⏫20 C1: Attack_______|1⏮1|/|2_", "ja":"　　攻撃コマンドの説明その１"  },
  0x91ACCC: { "en":[
    " Some COs have been heard to say that",
    " ⏮1[Attack] is their most favorite word.",
    "",
    " Attacks are either Direct or Indirect.",
    " Unit weapons with a{{} of 1 must be",
    " used when adjacent to an enemy unit to",
    " inflict damage.  A{{} of 2 or more",
    " means an Indirect attack over distance.",
    " Press{|<}on a unit to view its{{}|."
  ], "ja": [
    "　敵に攻撃をしかけるコマンドです。　　　　　",
    "　攻撃はおおきくわけて、ちょくせつ攻撃とかん",
    "せつ攻撃の２つがあります。",
    "　　ちょくせつ攻撃は、　　　が１のユニットが",
    "敵ユニットととなりあったときにできます。攻撃",
    "コマンドをえらぶと、攻撃カーソル　　　がでる",
    "ので、敵をえらんでください。"
  ]},

  # C2: Attack 2/2
  0x919B7C: { "b":0x919B7C, "e":0x919B98, "l":28, "en":"⏫20 C2: Attack_______2⏮1|/|2_", "ja":"　　攻撃コマンドの説明その２"  },
  0x91AE00: { "en":[
    " Indirect weapons can inflict heavy",
    " damage, but have another advantage:",
    " Indirect attacks do not allow the",
    " enemy to counterattack in that move.",
    "",
    " However, remember that a unit cannot",
    " move and fire an Indirect weapon on",
    " the same day.  Furthermore, Indirect",
    " weapons have a minimum firing range."
  ], "ja": [
    "　かんせつ攻撃は　　　が２以上のユニットが行",
    "うことができます。さらに、はんげきをうけない",
    "ので、いっぽうてきにダメージをあたえることが",
    "できます。ただし、移動と攻撃を１日で行うこと",
    "はできません。",
    "　ちょくせつ攻撃ユニット、かんせつ攻撃ユニッ",
    "トともに攻撃できる敵がきまっているので、くわ",
    "しくしりたいかたはユニットの上で　　をおして",
    "かくにんしてください。"
  ]},

  # C3: Capture 1/2
  0x919B9A: { "b":0x919B9A, "e":0x919BB6, "l":28, "en":"⏫20 C3: Capture______|1⏮1|/|2_", "ja":"　　待機コマンドの説明　　　"  },
  0x91AF7A: { "en":[
    " Have you been paying attention, CO?",
    " If so, you will already understand the",
    " importance of capturing.  If not, revise",
    " sections A7, A13 and B5 immediately!",
    "",
    " Those who have studied will be suitably",
    " rewarded:  Except for the HQ {}, all",
    " captured buildings generate an income",
    " {}of 1|000{|}per day."
  ], "ja": [
    "　ユニットの行動を終わらせるコマンドです。　",
    "　　　　　　　　　　　　　　　　　　　　　　"
  ]},

  # C4: Capture 2/2
  0x919BB8: { "b":0x919BB8, "e":0x919BD4, "l":28, "en":"⏫20 C4: Capture______2⏮1|/|2_", "ja":"　　占領コマンドの説明その１"  },
  0x91AFD8: { "en":[
    " Science has taught us many wonderful",
    " things <-< but with military research,",
    " we are able to make even bigger bangs.",
    "",
    " Once a lab{<  }has been captured, you",
    " can deploy the Proto<Tank{ }.  As",
    " also generates 1|000{|}per day, and",
    " the{{}is extremely powerful, you are",
    " advised to capture these when able."
  ], "ja": [
    "　占領ポイントを占領するコマンドです。　　　",
    "　自軍の色以外の首都　　工場　　都市　　研究",
    "所　　空港　　港　　駅　　に、歩兵　　か戦闘",
    "工兵　　を移動させると行えます。",
    "　これらの占領ポイントはたいきゅう力が２０あ",
    "り、　　１０のユニットが２日で占領できます。",
    "占領しかけのユニットがとちゅうでどこかへ移動",
    "したり、敵に全滅させられると、たいきゅう力が",
    "もどってしまうので注意してください。"
  ]},

  # C5: Join
  0x919BD6: { "b":0x919BD6, "e":0x919BF2, "l":28, "en":"⏫20 C5: Join____________", "ja":"　　占領コマンドの説明その２"  },
  0x91B172: { "en":[
    " One last briefing on the Join command:",
    "",
    " Two units of the same type can join",
    " when moved into the same square,",
    " unless both already have 10{}.  The",
    " joined unit takes the higher {|}&",
    " of the two, and combines their{||}up",
    " to a total of 10.  Finally, units loaded",
    " on transports cannot be joined."
  ], "ja": [
    "　首都　　以外は、占領すると収入　　が、つぎ",
    "の日から１０００ふえます。　　　　　　　　",
    "　研究所　　を中立のとき占領すると、新型戦車",
    "　　がてにはいります。研究所　　のそのあとの",
    "やくわりは都市　　とかわりませんが、新型戦車",
    "　　はおおきな戦力となりますのでがんばって占",
    "領してください。",
    "　れいがいとして、４Ｐマップのときの同盟して",
    "いる軍の占領ポイントは、占領できません。　"
  ]},

  # C6: Supply 1/2
  0x919BF4: { "b":0x919BF4, "e":0x919C10, "l":28, "en":"⏫20 C6: Supply_______|1⏮1|/|2_", "ja":"　　合流コマンドの説明　　　"  },
  0x91B300: { "en":[
    " The [Supply] command is exclusive to",
    " Supply Trucks {}.  This will replenish",
    " adjacent ground units and helicopters",
    " {}{}< with {}|&<{}.  All four of the",
    " surrounding units would be assisted in",
    " the move shown below:",
    # Note: The last 3 lines are dedicated to a figure showing a cross formation with Supply Truck in the center
  ], "ja": [
    "　おなじしゅるいのユニットを合流させるコマン",
    "ドです。　　　　　　　　　　　　　　　　　　",
    "　同じユニットの上に移動することで合流できま",
    "すが、りょうほう　　１０のときはできません。",
    "　合流すると、　　　　は多いほうがひきつがれ",
    "ます。　　は、たした数になりますが、１０をこ",
    "えるときりすてられます。　　　　　　　　　　",
    "　何かを搭載中のユニットは合流できませんので",
    "注意してください。　　　　　　　　　　　　　　"
  ]},

  # C7: Supply 2/2
  0x919C12: { "b":0x919C12, "e":0x919C2E, "l":28, "en":"⏫20 C7: Supply_______2⏮1|/|2_", "ja":"　　補給コマンドの説明その１"  },
  0x91B4B0: { "en":[
    " Your units will consume {} during",
    " movement around the battlefield.",
    "",
    " However, Air and Naval units consume",
    " {|}per day, even if they do not move.",
    " If these units run out of {}, the unit",
    " will be lost.  Press{||}over a unit to",
    " review its daily {} consumption (and",
    " revisit your training on how to refuel)."
  ], "ja": [
    "　補給車が補給を行うコマンドです。　　　　　",
    "　補給車　　ととなりあうマスにいるすべての地",
    "上ユニットと戦闘ヘリ　　、輸送ヘリ　　に、ね",
    "んりょう　　と弾　　の補給ができます。　　　",
    "　ただし、補充はできません。"
  ]},

  # C8: Load 1/3
  0x919C30: { "b":0x919C30, "e":0x919C4C, "l":28, "en":"⏫20 C8: Load________|1⏮1|/|3_", "ja":"　　補給コマンドの説明その２"  },
  0x91B59E: { "en":[
    " Each type of transport has a different",
    " load capacity.  Study what each one is",
    " able to carry below:",
    "_",
    "__  APC_____⏮1|1_*___| or",
    "__ |T-Copter___⏮1|1_*___| or",
    "__  Lander____2_*_ Ground Units",
    "__  Cruiser____2_*___| or",
    "__ |Train_____2_*_ Ground Units"
  ], "ja": [
    "　補給にはお金がかかります。くわしいことは、",
    "「全補３」のページをみてください。",
    "",
    "　航空ユニットと海上ユニットは、１日ごとに、",
    "たとえ場所を移動しなくとも、ねんりょう　　が",
    "へっていきます。ねんりょう　　が０になると、",
    "ついらく（ちんぼつ）してしまうので注意してく",
    "ださい。ユニットの上で　　をおし、　　のマイ",
    "ナス表示が１日のへるりょうです。"
  ]},

  # C9: Load 2/2
  0x919C4E: { "b":0x919C4E, "e":0x919C6A, "l":28, "en":"⏫20 C9: Load________2⏮1|/|3__", "ja":"　　搭載コマンドの説明その１"  },
  0x91B70A: { "en":[
    " Accordingly, each transport can be",
    " ordered to load and drop its cargo",
    " when over specific types of terrain:",
    "",
    "____ Anywhere { } can traverse",  # APC
    "____ Not on__________ or",        # T-Copter
    "____ Shoals & Ports",             # Lander
    "____ Anywhere|{|}|can traverse",  # Cruiser
    "____ Depots"                      # Train
  ], "ja": [
    "どのユニットに、どのユニットが搭載されるかは",
    "下のひょうをみてください。",
    "",
    "搭載ユニット　　搭載数　　搭載されるユニット",
    "　　列車砲　　　　２　　　地上ユニット　　",
    "　　輸送船　　　　２　　　地上ユニット　　",
    "　　輸送ヘリ　　　１　　　　　　",
    "　　兵員輸送車　　１　　　　　　",
    "　　護衛艦　　　　２　　　　"
  ]},

  # C10: Load 3/3
  0x919C6C: { "b":0x919C6C, "e":0x919C88, "l":28, "en":"⏫20 C10: Load________3⏮1|/|3__", "ja":"　　搭載コマンドの説明その２"  },
  0x91B84E: { "en":[
    " The{||}of any loaded unit will drop",
    " to match the{||}of its transport if",
    " attacked.  This occurs even if no",
    " actual damage was sustained during the",
    " attack.",
    #
    # Come back to this one.  There's space for a joke or extra detail.
    #
  ], "ja": [
    "　どのユニットにどこで載れるかは下をみてくだ",
    "さい。",
    "　　　　・・・　　　　　　",
    "　　　　・・・　　　　　　",
    "　　　　・・・　　が移動できる地形　　　",
    "　　　　・・・　　　　　　　　　　　　以外　",
    "　　　　・・・　　が移動できる地形　　　"
  ]},

  # C11: Drop
  0x919C8A: { "b":0x919C8A, "e":0x919CA6, "l":28, "en":"⏫20 C11: Drop____________", "ja":"　　搭載コマンドの説明その３"  },
  0x91B952: { "en":[
    " Using the Drop command, your unit<(s)",
    " can be unloaded onto any available",
    " area immediately next to the transport.",
    "",
    " Yet while transports can move your",
    " forces across great distances, a unit",
    " may still only be dropped on the same",
    " terrain types it can move into when",
    " traversing the battlefield by itself."
  ], "ja": [
    "　搭載するがわのユニットの　　がいくつでも搭",
    "載されるがわにえいきょうはありませんが、戦闘",
    "にはいったときに、たとえダメージをうけなくて",
    "も搭載するがわのユニットの　　になります。",
    "　れいをあげると、　　６の輸送ヘリ　　に　　",
    "１０の歩兵　　が載っていたとします。そのまま",
    "戦闘にはいらずに降車できたら　　は１０のまま",
    "ですが、戦闘にはいってしまうとダメージがなく",
    "とも　　６になってしまう、ということです。"
  ]},

  # C12: Wait
  0x919CA8: { "b":0x919CA8, "e":0x919CC4, "l":28, "en":"⏫20 C12: Wait____________", "ja":"　　降車コマンドの説明　　　"  },
  0x91BAFC: { "en":[
    " While every unit hopes their next move",
    " will strike the winning blow, this dream",
    " cannot come true every day.  Choosing",
    " [Wait] will, quite simply, end that unit's",
    " turn until the next day arrives.",
    "",
    " Perhaps tomorrow.  This concludes your",
    " training, but revisit any page or section",
    " at any time.  Good luck and enjoy, CO!"
  ], "ja": [
    "　搭載されたユニットが降りるコマンドです。　",
    "　降ろされる場所については、降りるユニットが",
    "移動できる場所ならどこでもいいですが、降ろす",
    "ユニットには、以下のじょうけんがあります。",
    "　　　　・・・　　のみ降車できる",
    "　　　　・・・　　　　のみ降車できる",
    "　　　　・・・　　が移動できる地形　　　",
    "　　　　・・・　　　　　　　　　　　　以外　",
    "　　　　・・・　　が移動できる地形　　　　"
  ]},



# CLEARING STRINGS

  0x91856B: { "b":0x91856B, "e":0x918599, "l":46, "en":"_______________________", "ja":"　　　　　　　　　　　　　　　　　　　　　　　"  },
  0x91859D: { "b":0x91859D, "e":0x9185CB, "l":46, "en":"_______________________", "ja":"　　　　　　　　　　　　　　　　　　　　　　　"  },
  0x9185CF: { "b":0x9185CF, "e":0x9185FD, "l":46, "en":"_______________________", "ja":"　　　　　　　　　　　　　　　　　　　　　　　"  },
  0x918601: { "b":0x918601, "e":0x91862F, "l":46, "en":"_______________________", "ja":"　　　　　　　　　　　　　　　　　　　　　　　"  },
  0x918633: { "b":0x918633, "e":0x918661, "l":46, "en":"_______________________", "ja":"　　　　　　　　　　　　　　　　　　　　　　　"  },
  0x918665: { "b":0x918665, "e":0x918693, "l":46, "en":"_______________________", "ja":"　　　　　　　　　　　　　　　　　　　　　　　"  },
  0x918697: { "b":0x918697, "e":0x9186C5, "l":46, "en":"_______________________", "ja":"　　　　　　　　　　　　　　　　　　　　　　　"  },
  0x9186C9: { "b":0x9186C9, "e":0x9186F7, "l":46, "en":"_______________________", "ja":"　　　　　　　　　　　　　　　　　　　　　　　"  },
  0x9186FB: { "b":0x9186FB, "e":0x918729, "l":46, "en":"_______________________", "ja":"　　　　　　　　　　　　　　　　　　　　　　　"  },

}
