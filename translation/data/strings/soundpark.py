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
# 16 tiles max (128 pixels) for main text area lines

# Staff
# Kenji Yamamoto (Metal KenKen)    メタル・ＫＥＮＫＥＮ
# Kenishi Nishimaki                コムラー・ニシマキ
# Hirokazu 'Hip' Tanaka            ヒップ・タナカ"
# Yuka Tsujiyoko                   リオ・ツジヨコ
# Atsuko Yamamoto                  びばのん・あつこ
# J.P. Sousa                       スーザ

strings = {

# Main header
  0x92E219: { "b":0x92E219, "e":0x92E235, "l":28, "en":"⏫e0< Welcome to Sound Park!",       "ja":"サウンドパークへようこそ！！"  },

# Unused?
  0x92E237: { "b":0x92E237, "e":0x92E241, "l":10, "en":"Music",                              "ja":"おんがく　"  },


# Welcome
  0x92E4D0: { "b":0x92E4D0, "e":0x92E4F0, "l":32, "en":"⏫00____|  Introduction___",            "ja":"　　　　　ようこそ！！　　　　　"  },
  0x92E980: { "en":[
    "⏫10"
    "{|Here you can listen to all",
    "_||the 29 songs included in",
    "_<{Super Famicom Wars!",
    "___  Please enjoy!!"
  ], "ja": [
    "スーファミウォーズの全２９曲を、",
    "　　　すべておひろめします。　　",
    "　　　　ぜひ、きいてね！　　　　",
    "一　サウンドスタッフいちどう　一"
  ]},
  0x92EA0E: { "b":0x92EA0E, "e":0x92EA2E, "l":32, "en":"_ Left:{Back___A: Play",               "ja":"左キー・もどる　／　Ａ・スタート"  },
  0x92EA32: { "b":0x92EA32, "e":0x92EA52, "l":32, "en":"_ Right:< Next___B: Stop",               "ja":"右キー・すすむ　／　Ｂ・ストップ"  },


# Track 1
# Title:
# HELTER SKELTER
# Note:
# Hurry hurry, your move!
# Eat this! (Big Cannon)
# What, no way!? (Kaboom!)
  0x92E4F2: { "b":0x92E4F2, "e":0x92E512, "l":32, "en":"⏫80____ Helter Skelter___",           "ja":"　　　へルター・スケルター　　　"  },
  0x92EA54: { "en":[
    "⏫90"
    "____ Hurry, hurry!",
    "____{Your move!",
    "_<  Eat this! (<Big Cannon<)",
    "< What, no way!<? (<Kaboom!<)"
  ], "ja": [
    "　　　あたふた、あたふた、",
    "　　　　　やったなー！",
    "これでどうだ！（ビッグたいほう）",
    "　え、うそ！？（ボッカーン！）"
  ]},
  0x92EAD0: { "b":0x92EAD0, "e":0x92EAEC, "l":28, "en":" Composition:__K.<Yamamoto",           "ja":"　作曲　メタル・ＫＥＮＫＥＮ"  },
  0x92EAF0: { "b":0x92EAF0, "e":0x92EB0A, "l":26, "en":" Arrangement:__K.|Nishimaki",          "ja":"　編曲　コムラー・ニシマキ"  },


# Track 2
# Title:
# Let's choose!
# Note:
# They are the armies
# Fresh and New❤
  0x92E514: { "b":0x92E514, "e":0x92E534, "l":32, "en":"⏫00____< Let's Choose!___",            "ja":"　　　　えらんじゃおう！　　　　"  },
  0x92EB0C: { "en":[
    "⏫10"
    "",
    "__| Here are the armies!",
    "___ $ New & Fresh $",
  ], "ja": [
    "　",
    "　　　とれとれ、ぴちぴちの",
    "　　　しょうぐんたちです▼",
    "　"
  ]},
  0x92EB52: { "b":0x92EB52, "e":0x92EB6E, "l":28, "en":" Composition:__K.<Yamamoto",           "ja":"　作曲　メタル・ＫＥＮＫＥＮ"  },
  0x92EB72: { "b":0x92EB72, "e":0x92EB8C, "l":26, "en":" Arrangement:__K.|Nishimaki",          "ja":"　編曲　コムラー・ニシマキ"  },


# Track 3
# Title:
# Watcha gonna do?
# Note:
# Today is this island, that island?
# So, what are you going to do?
  0x92E536: { "b":0x92E536, "e":0x92E556, "l":32, "en":"⏫80_|  Where Are You Going?_",        "ja":"　　　　　どうする？　　　　　　"  },
  0x92EB8E: { "en":[
    "⏫90"
    "",
    "_<This island?  That island?",
    "| Where are you going today?"
  ], "ja": [
    "　",
    "　きょうはこのしま、あのしま？",
    "　　さあ、きみならどうする？",
    "　"
  ]},
  0x92EBDA: { "b":0x92EBDA, "e":0x92EBF0, "l":22, "en":" Composition:__Hip|Tanaka",            "ja":"　作曲　ヒップ・タナカ"  },
  0x92EBF4: { "b":0x92EBF4, "e":0x92EC0E, "l":26, "en":" Arrangement:__K.|Nishimaki",          "ja":"　編曲　コムラー・ニシマキ"  },


# Track 4
# Title:
# I'll explain now
# Note:
# Blah Blah Blah
# And that is the explanation.
  0x92E558: { "b":0x92E558, "e":0x92E578, "l":32, "en":"⏫00____|Let Me Explain____",          "ja":"　　それでは、説明いたします　　"  },
  0x92EC10: { "en":[
    "⏫10"
    "",
    "_ ||Yada yada, and so on.",
    "_ And that's how it's done!"
  ], "ja": [
    "　",
    "　　　かくかく、しかじか、",
    "　　　というわけなんです。",
    "　"
  ]},
  0x92EC56: { "b":0x92EC56, "e":0x92EC70, "l":26, "en":" Composition:__K.|Nishimaki",          "ja":"　作曲　コムラー・ニシマキ"  },
  0x92EC74: { "b":0x92EC74, "e":0x92EC8E, "l":26, "en":" Arrangement:__K.|Nishimaki",          "ja":"　編曲　コムラー・ニシマキ"  },


# Track 5
# Title:
# Enemies comes in by a fighting gate.
# Note:
# Sneak around! Don't make a sound!
# Yes! They are not in here!
# (Encounter)
# Oh no!
  0x92E57A: { "b":0x92E57A, "e":0x92E59A, "l":32, "en":"⏫80_||Approaching The Enemy__",       "ja":"　　　戦うかどに、敵きたる　　　"  },
  0x92EC90: { "en":[
    "⏫90"
    "_ Sneak around!  Quietly!",
    "|||Yes... They are not here!",
    "____  (<Ambush!<)",
    "_____ Oh, no!!"
  ], "ja": [
    "ぬきあし、さしあし、しのびあし、",
    "　　よし、こっちはいないぞ！",
    "　　　　　　（遭遇）",
    "　　　　　　ギョッ！"
  ]},
  0x92ED02: { "b":0x92ED02, "e":0x92ED18, "l":22, "en":" Composition:__Hip|Tanaka",            "ja":"　作曲　ヒップ・タナカ"  },
  0x92ED1C: { "b":0x92ED1C, "e":0x92ED36, "l":26, "en":" Arrangement:__K.|Nishimaki",          "ja":"　編曲　コムラー・ニシマキ"  },


# Track 6
# Title:
# There's nothing I like more than fighting.
# Note:
# A How long does it continue?
# B That is until someone wins!
  0x92E59C: { "b":0x92E59C, "e":0x92E5BC, "l":32, "en":"⏫00_____| I| $ |War______",           "ja":"　　３どのめしより戦いがすき　　"  },
  0x92ED38: { "en":[
    "⏫10"
    "",
    " A)   How long will it last?",
    " B<)   Until someone wins!"
  ], "ja": [
    "　",
    "Ａ　いつまでつづく？",
    "Ｂ　それはけっちゃくが、",
    "　　　　　　　　　　つくまでさ！",
  ]},
  0x92ED94: { "b":0x92ED94, "e":0x92EDB0, "l":28, "en":" Composition:__K.<Yamamoto",           "ja":"　作曲　メタル・ＫＥＮＫＥＮ"  },
  0x92EDB4: { "b":0x92EDB4, "e":0x92EDCE, "l":26, "en":" Arrangement:__K.|Nishimaki",          "ja":"　編曲　コムラー・ニシマキ"  },


# Track 7
# Title:
# You step on a map
# Note:
# We will never betray you
# Is it fun? Wars are waiting for you.
  0x92E5BE: { "b":0x92E5BE, "e":0x92E5DE, "l":32, "en":"⏫80____< Raid The Map_____",          "ja":"　　一歩マップにふみこめば　　　"  },
  0x92EDD0: { "en":[
    "⏫90"
    "",
    "___  It's not too late!",
    "____|War is waiting."
  ], "ja": [
    "　　決してそんはさせません。",
    "　たのしい？ウォーズがあなたを",
    "　　　　おまちしています。",
    "　"
  ]},
  0x92EE34: { "b":0x92EE34, "e":0x92EE50, "l":28, "en":" Composition:__K.<Yamamoto",           "ja":"　作曲　メタル・ＫＥＮＫＥＮ"  },
  0x92EE54: { "b":0x92EE54, "e":0x92EE6E, "l":26, "en":" Arrangement:__K.|Nishimaki",          "ja":"　編曲　コムラー・ニシマキ"  },


# Track 8
# Title:
# Nonstop War Roleplaying
# Note:
# Even if you win or lose,
# it will never stop
# Dreaming about standing on the stage.
# (A's Wonder)
  0x92E5E0: { "b":0x92E5E0, "e":0x92E600, "l":32, "en":"⏫00__  Endless War Games___",         "ja":"　はてしない、せんそうごっこ　　"  },
  0x92EE70: { "en":[
    "⏫10"
    "____  Win or Lose,",
    "__< I will always dream of",
    "__<standing on the stage.",
    "____|(<A's fantasy<)"
  ], "ja": [
    "　　　かっても、まけても、",
    "　　　　ひたすらつづく、",
    "　ぶたいに立つ日を、ゆめにみて。",
    "　　　　　　　　　（Ａのおもい）"
  ]},
  0x92EEF0: { "b":0x92EEF0, "e":0x92EF0C, "l":28, "en":" Composition:__K.<Yamamoto",           "ja":"　作曲　メタル・ＫＥＮＫＥＮ"  },
  0x92EF10: { "b":0x92EF10, "e":0x92EF2A, "l":26, "en":" Arrangement:__K.|Nishimaki",          "ja":"　編曲　コムラー・ニシマキ"  },


# Track 9
# Title:
# Big fight in our Miniature garden!
# Note:
# Fun! Shy?
# SNES Wars!
# We are going to be strong
# Maybe!?
  0x92E602: { "b":0x92E602, "e":0x92E622, "l":32, "en":"⏫80  Big Fight in a Tiny Garden!_",   "ja":"ぼくらのはこにわ、だいせんそう！"  },
  0x92EF2C: { "en":[
    "⏫90"
    "_____ Happy!<?",
    "______ Shy?",
    "_   Super Famicom Wars!",
    "|  We're all mighty & strong!"
  ], "ja": [
    "　　　うれし！はずかし？",
    "　　　スーファミウォーズ！",
    "　　ぼくらはともにつよくなる",
    "　　　　　　はず！？"
  ]},
  0x92EF9C: { "b":0x92EF9C, "e":0x92EFB6, "l":26, "en":" Composition:__K.|Nishimaki",          "ja":"　作曲　コムラー・ニシマキ"  },
  0x92EFBA: { "b":0x92EFBA, "e":0x92EFD4, "l":26, "en":" Arrangement:__K.|Nishimaki",          "ja":"　編曲　コムラー・ニシマキ"  },


# Track 10
# Title:
# No problem in the front
# Note:
# Komura Nishimaki:
# I ripped the phrase
# Yep❤
  0x92E624: { "b":0x92E624, "e":0x92E644, "l":32, "en":"⏫00<All|Quiet|on<the|Western|Front",  "ja":"　　　ぜんせんいじょうなし　　　"  },
  0x92EFD6: { "en":[
    "⏫10"
    " ",
    "_<Thank you for the title|$",
    "_______|- K. Nishimaki"
  ], "ja": [
    "　　　コムラー・ニシマキの",
    "　　フレーズをいただきました",
    "　　　　　　　ごち▼"
  ]},
  0x92F030: { "b":0x92F030, "e":0x92F046, "l":22, "en":" Composition:__⏮2Y.|Tsujiyoko",       "ja":"　作曲　リオ・ツジヨコ"  },
  0x92F04A: { "b":0x92F04A, "e":0x92F064, "l":26, "en":" Arrangement:__K.|Nishimaki",          "ja":"　編曲　コムラー・ニシマキ"  },


# Track 11
# Title:
# The enemy yesterday is friend today.
# Note:
# Okay then, let me attack
  0x92E646: { "b":0x92E646, "e":0x92E666, "l":32, "en":"⏫80|Enemy|Yesterday,|Ally Today",      "ja":"　きのうの敵は、きょうのとも　　"  },
  0x92F066: { "en":[
    "⏫90"
    " ",
    "_____Okay then,",
    "____<let me attack!"
  ], "ja": [
    "　",
    "　　　それでは、攻撃させて",
    "　　　　　いただきます",
    "　"
  ]},
  0x92F0A8: { "b":0x92F0A8, "e":0x92F0BE, "l":22, "en":" Composition:__⏮2Y.|Tsujiyoko",       "ja":"　作曲　リオ・ツジヨコ"  },
  0x92F0C2: { "b":0x92F0C2, "e":0x92F0DC, "l":26, "en":" Arrangement:__K.|Nishimaki",          "ja":"　編曲　コムラー・ニシマキ"  },


# Track 12
# Title:
# Suddently, Gun Army
# Note:
# Bang! Bang!
# Ouch, How dare you!
  0x92E668: { "b":0x92E668, "e":0x92E688, "l":32, "en":"⏫00__<Big Guns Approaching___",        "ja":"　　てっぽう隊は、とつぜんに　　"  },
  0x92F0DE: { "en":[
    "⏫10"
    " ",
    "____<Bang! Bang!",
    "_| Ouch, how dare you!<?"
  ], "ja": [
    "　",
    "　バンッ、バンッ　",
    "　イテッ、やったなー！",
    "　"
  ]},
  0x92F16C: { "b":0x92F16C, "e":0x92F18C, "l":32, "en":" Composition:__Hip|Tanaka",            "ja":"　作曲　ヒップ・タナカ"  },
  0x92F190: { "b":0x92F190, "e":0x92F1B0, "l":32, "en":" Arrangement:__K.|Nishimaki",          "ja":"　編曲　コムラー・ニシマキ"  },


# Track 13
# Title:
# This is Tank Army
# Note:
# Kaboom Kaboom
# This is tank army number one
# We are attacking!
# Kaboom Kaboom
  0x92E68A: { "b":0x92E68A, "e":0x92E6AA, "l":32, "en":"⏫80< Here Comes The Tank Army_",      "ja":"　　こちらぜんせん、戦車部隊　　"  },
  0x92F1B2: { "en":[
    "⏫90"
    "___| Kaboom Kaboom",
    "_<This is Tank Army No.|1!",
    "___<We are attacking!",
    "___| Kaboom Kaboom"
  ], "ja": [
    "　",
    "　　　それでは、攻撃させて",
    "　　　　　いただきます",
    "　"
  ]},
  0x92F240: { "b":0x92F240, "e":0x92F260, "l":32, "en":" Composition:__Hip|Tanaka",            "ja":"　作曲　ヒップ・タナカ"  },
  0x92F264: { "b":0x92F264, "e":0x92F284, "l":32, "en":" Arrangement:__K.|Nishimaki",          "ja":"　編曲　コムラー・ニシマキ"  },


# Track 14
# Title:
# The title bout is on the air
# Note:
# We were waiting
# For this moment.
# Now, FIGHT!
# Kaboom (Whaaa)
  0x92E6AC: { "b":0x92E6AC, "e":0x92E6CC, "l":32, "en":"⏫00_   This Is The Title Fight__",    "ja":"　　　　　決戦は空中で！　　　　"  },
  0x92F286: { "en":[
    "⏫10"
    "___  We were waiting",
    "___  for this moment.",
    "____Now, F<I<G<HT!",
    "___|Kaboom! Whaaa!"
  ], "ja": [
    "　　　　　　ずっと、　　　　　　",
    "　　　このときを待っていた、　　",
    "　　　　　いざ、勝負！　　　　　",
    "　　　ボッカーン（あれーー）　　"
  ]},
  0x92F314: { "b":0x92F314, "e":0x92F334, "l":32, "en":" Composition:__Hip|Tanaka",            "ja":"　作曲　ヒップ・タナカ"  },
  0x92F338: { "b":0x92F338, "e":0x92F358, "l":32, "en":" Arrangement:__K.|Nishimaki",          "ja":"　編曲　コムラー・ニシマキ"  },


# Track 15
# Title:
# Hurry Hurry!
# Note:
# A Haa!
# B Hurry up, Get on!
  0x92E6CE: { "b":0x92E6CE, "e":0x92E6EE, "l":32, "en":"⏫80____ Hurry, Hurry!____",            "ja":"　　　いそいで、いそいで！　　　"  },
  0x92F35A: { "en":[
    "⏫90"
    "",
    " A)   Haa!",
    " B<)   Hurry up, come on!"
  ], "ja": [
    "　　　　　　　　　　　　　　　　",
    "Ａ　ソイヤー！　　　　　　　　　",
    "Ｂ　はよ、乗れ！　　　　　　　　",
    "　　　　　　　　　　　　　　　　"
  ]},
  0x92F3E8: { "b":0x92F3E8, "e":0x92F408, "l":32, "en":" Composition:__Hip|Tanaka",            "ja":"　作曲　ヒップ・タナカ"  },
  0x92F40C: { "b":0x92F40C, "e":0x92F42C, "l":32, "en":" Arrangement:__K.|Nishimaki",          "ja":"　編曲　コムラー・ニシマキ"  },


# Track 16
# Title:
# Fight! (Pull!)
# Note:
# Pull, Pull,
# Pull out some more!
  0x92E6F0: { "b":0x92E6F0, "e":0x92E710, "l":32, "en":"⏫00__<  Capture! (<Pull It!<)___",    "ja":"　勝負！（力づよくひっぱって）　"  },
  0x92F42E: { "en":[
    "⏫10"
    "",
    "_____ Pull, pull, ",
    "___<  pull some more!"
  ], "ja": [
    "　　　　　　　　　　　　　　　　",
    "　　ひっぱって、ひっぱって、　　",
    "　もっと、もっと、ひっぱって！　",
    "　　　　　　　　　　　　　　　　"
  ]},
  0x92F4BC: { "b":0x92F4BC, "e":0x92F4DC, "l":32, "en":" Composition:__Hip|Tanaka",            "ja":"　作曲　ヒップ・タナカ"  },
  0x92F4E0: { "b":0x92F4E0, "e":0x92F500, "l":32, "en":" Arrangement:__K.|Nishimaki",          "ja":"　編曲　コムラー・ニシマキ"  },


# Track 17
# Title:
# I got it!
# Note:
# Yeah!
# It's finally ours!
  0x92E712: { "b":0x92E712, "e":0x92E732, "l":32, "en":"⏫80______|Got It!______",             "ja":"　　　　　もらったぜ！　　　　　"  },
  0x92F502: { "en":[
    "⏫90"
    "",
    "______|Yeah!",
    "___  It's finally ours!"
  ], "ja": [
    "　　　　　　　　　　　　　　　　",
    "　　　　　　よっしゃ！　　　　　",
    "　　ついに、おれたちのものだ！　",
    "　　　　　　　　　　　　　　　　"
  ]},
  0x92F590: { "b":0x92F590, "e":0x92F5B0, "l":32, "en":" Composition:__Hip|Tanaka",            "ja":"　作曲　ヒップ・タナカ"  },
  0x92F5B4: { "b":0x92F5B4, "e":0x92F5D4, "l":32, "en":" Arrangement:__K.|Nishimaki",          "ja":"　編曲　コムラー・ニシマキ"  },


# Track 18
# Title:
# Chubby Cherub
# Note:
# Ohh I am so full
# I can't eat it anymore!
  0x92E734: { "b":0x92E734, "e":0x92E754, "l":32, "en":"⏫00___<  Chubby Cherub_____",         "ja":"　　　　まんぷくタロウ　　　　　"  },
  0x92F5D6: { "en":[
    "⏫10"
    "",
    "___Ohh, I am so full...",
    "__  I can't eat anymore!"
  ], "ja": [
    "　　　　　　　　　　　　　　　　",
    "　　　　　　よっしゃ！　　　　　",
    "　　ついに、おれたちのものだ！　",
    "　　　　　　　　　　　　　　　　"
  ]},
  0x92F664: { "b":0x92F664, "e":0x92F684, "l":32, "en":" Composition:__Hip|Tanaka",            "ja":"　作曲　ヒップ・タナカ"  },
  0x92F688: { "b":0x92F688, "e":0x92F6A8, "l":32, "en":" Arrangement:__K.|Nishimaki",          "ja":"　編曲　コムラー・ニシマキ"  },


# Track 19
# Title:
# Ha! Take that!
# Note:
# Tada!
# A Is this island ours?
# B That is why the color changed!
# Tada!
  0x92E756: { "b":0x92E756, "e":0x92E776, "l":32, "en":"⏫80____Ha!  It's Ours!____",          "ja":"　えっへん、どんなもんだい！　　"  },
  0x92F6AA: { "en":[
    "⏫90"
    "______< Tada!",
    " A)__ Is it our island now?",
    " B<)__ Yup, that's why the",
    "___ color changed!"
  ], "ja": [
    "　　　　パッパカパーン！　　　　",
    "Ａ　このしま、おれたちのものか？",
    "Ｂ　だから色がかわったのさ！　　",
    "　　パッパ、パンパカパーン！　　"
  ]},
  0x92F738: { "b":0x92F738, "e":0x92F758, "l":32, "en":" Composition:__Hip|Tanaka",            "ja":"　作曲　ヒップ・タナカ"  },
  0x92F75C: { "b":0x92F75C, "e":0x92F77C, "l":32, "en":" Arrangement:__K.|Nishimaki",          "ja":"　編曲　コムラー・ニシマキ"  },


# Track 20
# Title:
# Phew, that's enough
# Note:
# Nice work!
# Now do the rest!
  0x92E778: { "b":0x92E778, "e":0x92E798, "l":32, "en":"⏫00__|  Phew, We're Done!___",        "ja":"　やれやれ、こんなもんでしょ！　"  },
  0x92F77E: { "en":[
    "⏫10"
    "",
    "____<  Nice work!",
    "__| Now finish the rest!"
  ], "ja": [
    "　　　　　　　　　　　　　　　　",
    "　　　　　おつかれさん　　　　　",
    "　　んじゃ、あとはよろしく！　　",
    "　　　　　　　　　　　　　　　　"
  ]},
  0x92F80C: { "b":0x92F80C, "e":0x92F82C, "l":32, "en":" Composition:__Hip|Tanaka",            "ja":"　作曲　ヒップ・タナカ"  },
  0x92F830: { "b":0x92F830, "e":0x92F850, "l":32, "en":" Arrangement:__K.|Nishimaki",          "ja":"　編曲　コムラー・ニシマキ"  },


# Track 21
# Title:
# We got defeated
# Note:
# F.. Failed...
# Why in the world...
  0x92E79A: { "b":0x92E79A, "e":0x92E7BA, "l":32, "en":"⏫80___  We're Defeated____",          "ja":"　　　　やられちゃった　　　　　"  },
  0x92F852: { "en":[
    "⏫90"
    "",
    "____ F-F-Failed...",
    "__  Why in the world..."
  ], "ja": [
    "　　　　　　　　　　　　　　　　",
    "　　　　む、む、むねん、　　　　",
    "　　　わたしとしたことが。　　　",
    "　　　　　　　　　　　　　　　　"
  ]},
  0x92F8E0: { "b":0x92F8E0, "e":0x92F900, "l":32, "en":" Composition:__Hip|Tanaka",            "ja":"　作曲　ヒップ・タナカ"  },
  0x92F904: { "b":0x92F904, "e":0x92F924, "l":32, "en":" Arrangement:__K.|Nishimaki",          "ja":"　編曲　コムラー・ニシマキ"  },


# Track 22
# Title:
# I'm sorry
# Note:
# I will run now but
# I will never lose again!
  0x92E7BC: { "b":0x92E7BC, "e":0x92E7DC, "l":32, "en":"⏫00_____  I'm Sorry______",           "ja":"　　　　ごめんなちゃい　　　　　"  },
  0x92F926: { "en":[
    "⏫10"
    "",
    "__|I'm running away, but",
    "__<I will never lose again!"
  ], "ja": [
    "　　　　　　　　　　　　　　　　",
    "　　　ひとまずにげるけど　　　　",
    "　　このつぎは、負けないぞー！　",
    "　　　　　　　　　　　　　　　　"
  ]},
  0x92F9B4: { "b":0x92F9B4, "e":0x92F9D4, "l":32, "en":" Composition:__Hip|Tanaka",            "ja":"　作曲　ヒップ・タナカ"  },
  0x92F9D8: { "b":0x92F9D8, "e":0x92F9F8, "l":32, "en":" Arrangement:__K.|Nishimaki",          "ja":"　編曲　コムラー・ニシマキ"  },


# Track 23
# Title:
# For fight the bell tolls
# Note:
# Ding Dong
# A did we won?
# B That is why the bell tolls!
# Ding Dong
  0x92E7DE: { "b":0x92E7DE, "e":0x92E7FE, "l":32, "en":"⏫80_| For Whom The Bell Tolls__",     "ja":"　　勝利のために、カネはなる　　"  },
  0x92F9FA: { "en":[
    "⏫90"
    "____$ Ding Dong|$",
    " A) Did we win?",
    " B<) That's why the bell tolls!",
    "____$ Ding Dong|$"
  ], "ja": [
    "　　　　　　　　　　　　　　　　",
    "　　　ひとまずにげるけど　　　　",
    "　　このつぎは、負けないぞー！　",
    "　　　　　　　　　　　　　　　　"
  ]},
  0x92FA88: { "b":0x92FA88, "e":0x92FAA8, "l":32, "en":" Composition:__Hip|Tanaka",            "ja":"　作曲　ヒップ・タナカ"  },
  0x92FAAC: { "b":0x92FAAC, "e":0x92FACC, "l":32, "en":" Arrangement:__K.|Nishimaki",          "ja":"　編曲　コムラー・ニシマキ"  },


# Track 24
# Title:
# Thunder
# Note:
# One Two One Two
# Make the legs the same
# It's a march!
  0x92E800: { "b":0x92E800, "e":0x92E820, "l":32, "en":"⏫00___   The Thunderer____",          "ja":"　　　　　　　雷神　　　　　　　"  },
  0x92FACE: { "en":[
    "⏫10"
    "___ Sound off!  1|-<2",
    "___ Sound off!| 3<-<4",
    "___|I'll be marchin' the",
    "___  rest of my life!"
  ], "ja": [
    "　　　　　　　　　　　　　　　　",
    "　　　ひとまずにげるけど　　　　",
    "　　このつぎは、負けないぞー！　",
    "　　　　　　　　　　　　　　　　"
  ]},
  0x92FB5C: { "b":0x92FB5C, "e":0x92FB7C, "l":32, "en":" Composition:__J.⏮2P. Sousa",         "ja":"　作曲　スーザ　　　　　　　　　"  },
  0x92FB80: { "b":0x92FB80, "e":0x92FBA0, "l":32, "en":" Arrangement:__⏮2Y.|Tsujiyoko",       "ja":"　作曲　リオ・ツジヨコ"  },


# Track 25
# Title:
# Blue Plazma
# Note:
# The ending
# With everyone
# Heart is pounding❤
# La La La!
  0x92E822: { "b":0x92E822, "e":0x92E842, "l":32, "en":"⏫80____| Blue Plasma_____",           "ja":"　　　　あおいプラズマ　　　　　"  },
  0x92FBA2: { "en":[
    "⏫90"
    "_|  Everyone's hearts' are",
    "__< pounding in the end!",
    "_____| $  $  $",
    "_____<Oh<-<la<-<la!"
  ], "ja": [
    "　　　　みんなでたのしく　　　　",
    "　　　　　エンディング　　　　　",
    "　　　　こころウキウキ▼　　　　",
    "　　　　　るんるんるん！　　　　"
  ]},
  0x92FC30: { "b":0x92FC30, "e":0x92FC50, "l":32, "en":" Composition:__K.<Yamamoto",           "ja":"　作曲　メタル・ＫＥＮＫＥＮ"  },
  0x92FC54: { "b":0x92FC54, "e":0x92FC74, "l":32, "en":" Arrangement:__K.|Nishimaki",          "ja":"　編曲　コムラー・ニシマキ"  },


# Track 26
# Title:
# Samba De Thunder
# Note:
# Now everyone
# Together!
# Carnival in Wars!
  0x92E844: { "b":0x92E844, "e":0x92E864, "l":32, "en":"⏫00___< Samba Thunderer____",         "ja":"　　　サンバ・ＤＥ・雷神　　　　"  },
  0x92FC76: { "en":[
    "⏫10"
    "",
    "_< Everyone together now!",
    "___ Carnival of War!"
  ], "ja": [
    "　　　　さあさ、みなさん　　　　",
    "　　　　　ごいっしょに！　　　　",
    "　　　うおーずでカーニバル！　　",
    "　　　　　　　　　　　　　　　　"
  ]},
  0x92FD04: { "b":0x92FD04, "e":0x92FD24, "l":32, "en":" Composition:__J.⏮2P. Sousa",         "ja":"　作曲　スーザ　　　　　　　　　"  },
  0x92FD28: { "b":0x92FD28, "e":0x92FD48, "l":32, "en":" Arrangement:__⏮2Y.|Tsujiyoko",       "ja":"　作曲　リオ・ツジヨコ"  },


# Track 27
# Title:
# The Wars Stooges
# Note:
# So!
# Let's go!
  0x92E866: { "b":0x92E866, "e":0x92E886, "l":32, "en":"⏫80___|The War Stooges____",          "ja":"　　ウォーズのだい爆ショー　　　"  },
  0x92FD4A: { "en":[
    "⏫90"
    "",
    "_____Hey! Ho!",
    "_____<Let's Go!"
  ], "ja": [
    "　　　　　　　　　　　　　　　　",
    "　　　　　　さぁー！　　　　　　",
    "　　　　いってみようかー！　　　",
    "　　　　　　　　　　　　　　　　"
  ]},
  0x92FDD8: { "b":0x92FDD8, "e":0x92FDF8, "l":32, "en":" Composition:__K.<Yamamoto",           "ja":"　作曲　メタル・ＫＥＮＫＥＮ"  },
  0x92FDFC: { "b":0x92FDFC, "e":0x92FE1C, "l":32, "en":" Arrangement:__A.Yamamoto",            "ja":"　編曲　びばのん・あつこ　　　　"  },


# Track 28
# Title:
# Detana! SNES Wars!
# Note:
# It came out!
# Super Nintendo Wars!
# You will get sucked in!
# Super Nintendo Wars!
  0x92E888: { "b":0x92E888, "e":0x92E8A8, "l":32, "en":"⏫00_   Super Famicom Wars!___",       "ja":"　でたぞ！スーファミウォーズ　　"  },
  0x92FE1E: { "en":[
    "⏫10"
    "_____|It's here!",
    "_   Super Famicom Wars!",
    "__|You'll get sucked in!",
    "_   Super Famicom Wars!"
  ], "ja": [
    "　　　　でたぞ、でたぞ！　　　　",
    "　　　スーファミウォーズ！　　　",
    "　のめりこむぞ、のめりこむぞ！　",
    "　　　スーファミウォーズ！　　　"
  ]},
  0x92FEAC: { "b":0x92FEAC, "e":0x92FECC, "l":32, "en":" Composition:__?",                     "ja":"　作曲　？　　　　　　　　　　　"  },
  0x92FED0: { "b":0x92FED0, "e":0x92FEF0, "l":32, "en":" Arrangement:__K.|Nishimaki",          "ja":"　編曲　コムラー・ニシマキ"  },


# Track 29
# Title:
# Run for Tomorrow!
# Note:
# 1,2,1234!
# A How long are we going to run?
# B Until Tomorrow!
# 1,2,1234!
  0x92E8AA: { "b":0x92E8AA, "e":0x92E8CA, "l":32, "en":"⏫80__|  Run For Tomorrow!____",       "ja":"　　　明日にむかって走れ！　　　"  },
  0x92FEF2: { "en":[
    "⏫90"
    "___<  1, 2, 1-2-3-4!",
    " A) How far are we running?",
    " B<) Until tomorrow!",
    "___<  1, 2, 1-2-3-4!"
  ], "ja": [
    "　　１、２、１・２・３・４！　　",
    "Ａ　おれたち、いつまで走るんだ？",
    "Ｂ　きっと明日になるまでさ！　　",
    "　　１、２、１・２・３・４！　　"
  ]},
  0x92FF80: { "b":0x92FF80, "e":0x92FFA0, "l":32, "en":" Composition:__?",                     "ja":"　作曲　？　　　　　　　　　　　"  },
  0x92FFA4: { "b":0x92FFA4, "e":0x92FFC4, "l":32, "en":" Arrangement:__K.|Nishimaki",          "ja":"　編曲　コムラー・ニシマキ"  },
}
