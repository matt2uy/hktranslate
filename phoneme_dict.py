hk_text_phonemes = {
	'AA' : 'ao', #odd     AA D
        'AE' : 'a', #at	AE T
        'AH' : 'a', #hut	HH AH T
        'AO' : 'ou', #ought	AO T
        'AW' : 'ow', #cow	K AW
        'AY' : 'ai', #hide	HH AY D
        'B' : 'b', #be	B IY
        'CH' : 'ch', #cheese	CH IY Z
        'D' : 'd', #dee	D IY
        'DH' : 'd', #thee	DH IY
        'EH' : 'e', #Ed	EH D
        'ER' : 'ur', #hurt	HH ER T
        'EY' : 'ey', #ate	EY T
        'F' : 'eh', #fee	F IY
        'G' : 'g', #green	G R IY N
        'HH' : 'h', #he	HH IY
        'IH' : 'i', #it	IH T
        'IY' : 'eh', #eat	IY T
        'JH' : 'g', #gee	JH IY
        'K' : 'k', #key	K IY
        'L' : 'l', #lee	L IY
        'M' : 'm', #me	M IY
        'N' : 'n', #knee	N IY
        'NG' : 'ng', #ping	P IH NG
        'OW' : 'ow', #oat	OW T
        'OY' : 'oy', #toy	T OY
        'P' : 'p', #pee	P IY
        'R' : 'h', #read	R IY D
        'S' : 's', #sea	S IY
        'SH' : 'sh', #she	SH IY
        'T' : 't', #tea	T IY
        'TH' : 'th', #theta	TH EY T AH
        'UH' : 'oo', #hood	HH UH D
        'UW' : 'ooh', #two	T UW
        'V' : 'v', #vee	V IY
        'W' : 'w', #we	W IY
        'Y' : 'y', #yield	Y IY L D
        'Z' : 'zh', #zee	Z IY
        'ZH' : 'sh' #seizure	S IY ZH ER
        }

############ = needs better sound

## need to record:
"""
ow

"""
hk_audio_phoneme_combos1 = {
        # vowel -> consonant
        "-AE-NG-" : '-AE-[static/sound/ang1.wav]-',
        "-AH-L-" : '-AH-[static/sound/ou1.wav]-', # table - tabow
        "-AO-NG-" : '-AO-[static/sound/ong1.wav]-',
        "-IH-NG-" : '-IH-[static/sound/ing1.wav]-',
        "-AE-N-" : '-AE-[static/sound/an1.wav]-', # man
        "-AO-R-" : '-AO-[static/sound/er1.wav]-', ####### for 'buy more', does 'ru' at the end
        }


hk_audio_phoneme_combos2 = {
        # consonant -> vowel
        "-B-AA-" : '-[static/sound/bao1.wav]-', # robot #######
        "-B-AE-" : '-[static/sound/ba1.wav]-', # bat
        "-B-AH-" : '-[static/sound/ba1.wav]-', # butter ###########    
        "-B-AO-" : '-[static/sound/bo1.wav]-', # aboard
        "-B-AW-" : '-[static/sound/bao1.wav]-', # bow (respect)
        "-B-AY-" : '-[static/sound/bai1.wav]-', # buy
        "-B-EH" : '-[static/sound/bei1.wav]-', # ben
        #"-B-ER" : '-B and ER so far-', # burt ###########
        "-B-EY" : '-[static/sound/bei1.wav]-', # bait
        "-B-IH" : '-[static/sound/bin1.wav]-', # bit
        "-B-IY-" : '-[static/sound/bei1.wav]-', # be
        "-B-OW-" : '-[static/sound/bo1.wav]-', # boat
        #"-B-OY-" : '-[static/sound/bai1.wav]-', # boat ###### no boi or oy sounds
        #'-B-UH-' : '-[static/sound/bo1.wav]-',#'ou', #hood      HH UH D
        #'-B-UW-' : '-[static/sound/bou1.wav]-',#boo
        
        # for c: edit out silence
        # and silence between words too!
        # time log: 25
        "-CH-AA-" : '-[static/sound/cho1.wav]-', # chopper     
        "-CH-AE-" : '-[static/sound/cha1.wav]-', # chat     
        "-CH-AH-" : '-[static/sound/che1.wav]-', # chutney    
        "-CH-AO-" : '-[static/sound/chou1.wav]-', # chores 
        "-CH-AW-" : '-[static/sound/chao1.wav]-', # ciao
        "-CH-AY-" : '-[static/sound/chai1.wav]-', # china
        "-CH-EH" : '-[static/sound/che1.wav]-', # checkers ###########3
        #"-CH-ER" : '-B and ER so far-', # churn ###########
        #"-CH-EY" : '-[static/sound/bei1.wav]-', # change
        #"-CH-IH" : '-[static/sound/bin1.wav]-', # ching
        #"-CH-IY-" : '-[static/sound/che1.wav]-', # cheese
        "-CH-OW-" : '-[static/sound/chou1.wav]-', # choke
        #"-CH-OY-" : '-[static/sound/bai1.wav]-', # choice ###### no boi or oy sounds
        '-CH-UH-' : '-[static/sound/chu1.wav]-',# kravchuks  #####
        '-CH-UW-' : '-[static/sound/chu1.wav]-',# choo choo

        # time log: 16
        "-D-AA-" : '-[static/sound/dong1.wav]-', # dong  
        "-D-AE-" : '-[static/sound/da1.wav]-', # dab    
        "-D-AH-" : '-[static/sound/de1.wav]-', # dud   
        "-D-AO-" : '-[static/sound/dou1.wav]-', # door 
        "-D-AW-" : '-[static/sound/dao1.wav]-', # down
        "-D-AY-" : '-[static/sound/dai1.wav]-', # dine
        "-D-EH" : '-[static/sound/de1.wav]-', # deck  #######
        #"-D-ER" : '-B and ER so far-', # dirk 
        "-D-EY" : '-[static/sound/dei1.wav]-', # day
        #"-D-IH" : '-[static/sound/bin1.wav]-', # ding
        #"-D-IY-" : '-[static/sound/che1.wav]-', # deep
        "-D-OW-" : '-[static/sound/dou1.wav]-', # dope
        "-D-OY-" : '-[static/sound/dui1.wav]-', # doy ###### no boi or oy sounds
        '-D-UH-' : '-[static/sound/de1.wav]-',# duck  #####
        "-D-UW-" : '-[static/sound/dou1.wav]-', # do

        # time log: 9
        "-F-AA-" : '-[static/sound/fou1.wav]-', # fong  
        "-F-AE-" : '-[static/sound/fa1.wav]-', # fad    
        "-F-AH-" : '-[static/sound/fu1.wav]-', # fun #######3   
        "-F-AO-" : '-[static/sound/fo1.wav]-', # for 
        #"-F-AW-" : '-[static/sound/fa1.wav]-', # fountain ###########
        #"-F-AY-" : '-[static/sound/dai1.wav]-', # fine
        #"-F-EH" : '-[static/sound/de1.wav]-', # freckle  #######
        #"-F-ER" : '-B and ER so far-', # furnish  ##########
        "-F-EY" : '-[static/sound/fei1.wav]-', # fade
        #"-F-IH" : '-[static/sound/bin1.wav]-', # fickle
        #"-F-IY-" : '-[static/sound/che1.wav]-', # feel
        "-F-OW-" : '-[static/sound/fo1.wav]-', # foam
        #"-F-OY-" : '-[static/sound/dui1.wav]-', # foil ###### no boi or oy sounds
        '-F-UH-' : '-[static/sound/fa1.wav]-',# fuck  #####
        "-F-UW-" : '-[static/sound/fou1.wav]-', # foo
       
        # time log: 12
        "-G-AA-" : '-[static/sound/go1.wav]-', # gong  
        "-G-AE-" : '-[static/sound/ga1.wav]-', # gag  
        "-G-AH-" : '-[static/sound/ge1.wav]-', # gun 
        "-G-AO-" : '-[static/sound/go1.wav]-', # gore
        "-G-AW-" : '-[static/sound/gao1.wav]-', # gown
        "-G-AY-" : '-[static/sound/gai1.wav]-', # geiger
        "-G-EH" : '-[static/sound/gei1.wav]-', # gecko  #######
        #"-G-ER" : '-B and ER so far-', # digger  ##########
        "-G-EY" : '-[static/sound/gei1.wav]-', # gay
        #"-G-IH" : '-[static/sound/bin1.wav]-', # dragging
        "-G-IY-" : '-[static/sound/gei1.wav]-', # game
        "-G-OW-" : '-[static/sound/gou1.wav]-', # fargo
        "-G-OY-" : '-[static/sound/gou1.wav]-', # goin ###### no boi or oy sounds
        '-G-UH-' : '-[static/sound/ge1.wav]-',# good  #####
        "-G-UW-" : '-[static/sound/gu1.wav]-', # goo

        # time log: 9
        "-HH-AA-" : '-[static/sound/hu1.wav]-', # hong  33333333333
        "-HH-AE-" : '-[static/sound/ha1.wav]-', # haggle  
        "-HH-AH-" : '-[static/sound/he1.wav]-', # hug 
        "-HH-AO-" : '-[static/sound/hou1.wav]-', # hope
        "-HH-AW-" : '-[static/sound/hou1.wav]-', # hone
        "-HH-AY-" : '-[static/sound/hai1.wav]-', # hi
        "-HH-EH" : '-[static/sound/hei1.wav]-', # heck  ######
        #"-HH-ER" : '-B and ER so far-', # her
        "-HH-EY" : '-[static/sound/hei1.wav]-', # hey
        #"-HH-IH" : '-[static/sound/bin1.wav]-', # him
        "-HH-IY-" : '-[static/sound/hei1.wav]-', # hate
        "-HH-OW-" : '-[static/sound/hou1.wav]-', # hobo
        "-HH-OY-" : '-[static/sound/hui1.wav]-', # hoylake ###### no boi or oy sounds
        '-HH-UH-' : '-[static/sound/he1.wav]-',# hood  #####
        "-HH-UW-" : '-[static/sound/hu1.wav]-', # who

        # time log: 
        #"-JH-AA-" : '-[static/sound/ju1.wav]-', # hong  33333333333
        #"-JH-AE-" : '-[static/sound/ha1.wav]-', # haggle  
        #"-JH-AH-" : '-[static/sound/he1.wav]-', # hug 
        #"-JH-AO-" : '-[static/sound/hou1.wav]-', # hope
        #"-JH-AW-" : '-[static/sound/hou1.wav]-', # hone
        #"-JH-AY-" : '-[static/sound/hai1.wav]-', # hi
        #"-JH-EH" : '-[static/sound/hei1.wav]-', # heck  ######
        #"-JH-ER" : '-B and ER so far-', # her
        #"-JH-EY" : '-[static/sound/hei1.wav]-', # hey
        #"-JH-IH" : '-[static/sound/bin1.wav]-', # him
        #"-JH-IY-" : '-[static/sound/hei1.wav]-', # hate
        #"-JH-OW-" : '-[static/sound/hou1.wav]-', # hobo
        #"-JH-OY-" : '-[static/sound/hui1.wav]-', # hoylake ###### no boi or oy sounds
        #'-JH-UH-' : '-[static/sound/he1.wav]-',# hood  #####
        #"-JH-UW-" : '-[static/sound/hu1.wav]-', # who

        # time log: 9
        "-K-AA-" : '-[static/sound/ku1.wav]-', # kong
        "-K-AE-" : '-[static/sound/ka1.wav]-', # cap 
        "-K-AH-" : '-[static/sound/ke1.wav]-', # cup 
        "-K-AO-" : '-[static/sound/kou1.wav]-', # cope
        "-K-AW-" : '-[static/sound/kou1.wav]-', # cone
        "-K-AY-" : '-[static/sound/kai1.wav]-', # kind
        #"-K-EH" : '-[static/sound/ke1.wav]-', # heck  ##########
        #"-K-ER" : '-B and ER so far-', # her
        #"-K-EY" : '-[static/sound/hei1.wav]-', # hey
        #"-K-IH" : '-[static/sound/bin1.wav]-', # him
        "-K-IY-" : '-[static/sound/kai1.wav]-', # kite #######
        "-K-OW-" : '-[static/sound/kao1.wav]-', # cow
        "-K-OY-" : '-[static/sound/kui1.wav]-', # coy ###### no boi or oy sounds
        '-K-UH-' : '-[static/sound/ke1.wav]-',# could  #####
        "-K-UW-" : '-[static/sound/ku1.wav]-', # coo

        # time log: 16
        "-L-AA-" : '-[static/sound/lou1.wav]-', # long ######
        "-L-AE-" : '-[static/sound/la1.wav]-', # lap 
        "-L-AH-" : '-[static/sound/le1.wav]-', # lump 
        "-L-AO-" : '-[static/sound/lo1.wav]-', # logo
        "-L-AW-" : '-[static/sound/1ao1.wav]-', # allow
        "-L-AY-" : '-[static/sound/lai1.wav]-', # lion
        #"-L-EH" : '-[static/sound/ke1.wav]-', # lept  ##########
        #"-L-ER" : '-B and ER so far-', # learn
        "-L-EY" : '-[static/sound/lei1.wav]-', # lay
        "-L-IH" : '-[static/sound/li1.wav]-', # lip #####
        "-L-IY-" : '-[static/sound/li1.wav]-', # lean #######
        "-L-OW-" : '-[static/sound/lou1.wav]-', # allow
        #"-L-OY-" : '-[static/sound/kui1.wav]-', # loyd ###### no boi or oy sounds
        '-L-UH-' : '-[static/sound/le1.wav]-',# loot 
        "-L-UW-" : '-[static/sound/lu1.wav]-', # loo

        # time log: 27
        "-M-AA-" : '-[static/sound/ma1.wav]-', # mod ######
        "-M-AE-" : '-[static/sound/ma1.wav]-', # map
        #"-M-AH-" : '-[static/sound/1.wav]-', # month
        "-M-AO-" : '-[static/sound/mo1.wav]-', # mope
        "-M-AW-" : '-[static/sound/mao1.wav]-', # mouse
        "-M-AY-" : '-[static/sound/mai1.wav]-', # my
        "-M-EH" : '-[static/sound/me1.wav]-', # met  ##########
        #"-M-ER" : '-B and ER so far-', # mercenary
        "-M-EY" : '-[static/sound/mei1.wav]-', # may
        "-M-IH" : '-[static/sound/mi1.wav]-', # miss #####
        "-M-IY-" : '-[static/sound/mi1.wav]-', # mean #######
        "-M-OW-" : '-[static/sound/mou1.wav]-', # mow
        #"-M-OY-" : '-[static/sound/kui1.wav]-', # loyd ###### no boi or oy sounds
        '-M-UH-' : '-[static/sound/mu1.wav]-',# moot
        "-M-UW-" : '-[static/sound/mu1.wav]-', # moo
     
        # time log: 8
        "-N-AA-" : '-[static/sound/na1.wav]-', # nod ######
        "-N-AE-" : '-[static/sound/na1.wav]-', # nap
        #"-N-AH-" : '-[static/sound/ne1.wav]-', # nub
        "-N-AO-" : '-[static/sound/nou1.wav]-', # nope
        "-N-AW-" : '-[static/sound/nao1.wav]-', # mouse
        "-N-AY-" : '-[static/sound/nai1.wav]-', # nye
        "-N-EH" : '-[static/sound/ne1.wav]-', # net  ##########
        #"-N-ER" : '-B and ER so far-', # nerd
        "-N-EY" : '-[static/sound/nei1.wav]-', # neighbor
        "-N-IH" : '-[static/sound/ni1.wav]-', # nip #####
        "-N-IY-" : '-[static/sound/ni1.wav]-', # neal #######
        "-N-OW-" : '-[static/sound/nou1.wav]-', # no
        #"-N-OY-" : '-[static/sound/kui1.wav]-', # annoyed ###### no boi or oy sounds
        '-N-UH-' : '-[static/sound/nu1.wav]-',# nu
        "-N-UW-" : '-[static/sound/nu1.wav]-', # nu

        # time log: 11
        "-P-AA-" : '-[static/sound/pou1.wav]-', # pod ######
        "-P-AE-" : '-[static/sound/pa1.wav]-', # pad
        #"-P-AH-" : '-[static/sound/ne1.wav]-', # pub
        "-P-AO-" : '-[static/sound/po1.wav]-', # pope
        "-P-AW-" : '-[static/sound/pao1.wav]-', # power
        "-P-AY-" : '-[static/sound/pai1.wav]-', # pie
        "-P-EH" : '-[static/sound/pen1.wav]-', # pet  ##########33333333 crop #########3
        #"-P-ER" : '-B and ER so far-', # per
        "-P-EY" : '-[static/sound/pei1.wav]-', # pay
        "-P-IH" : '-[static/sound/pi1.wav]-', # pill #####
        "-P-IY-" : '-[static/sound/pi1.wav]-', # peel #######
        "-P-OW-" : '-[static/sound/pou1.wav]-', # poker
        #"-P-OY-" : '-[static/sound/kui1.wav]-', # point ###### no boi or oy sounds
        '-P-UH-' : '-[static/sound/pu1.wav]-',# poo
        "-P-UW-" : '-[static/sound/pu1.wav]-', # poo

        # time log: 15
        "-R-AA-" : '-[static/sound/rou1.wav]-', # rod ######
        "-R-AE-" : '-[static/sound/ra1.wav]-', # rad
        #"-R-AH-" : '-[static/sound/ne1.wav]-', # rub
        "-R-AO-" : '-[static/sound/rou1.wav]-', # rope
        "-R-AW-" : '-[static/sound/rao1.wav]-', # row
        "-R-AY-" : '-[static/sound/wai1.wav]-', # rye
        "-R-EH" : '-[static/sound/re1.wav]-', # rep  ##########33333333 crop #########3
        #"-R-ER" : '-B and ER so far-', # rer
        "-R-EY" : '-[static/sound/wei1.wav]-', # ray
        "-R-IH" : '-[static/sound/wai1.wav]-', # rice #####
        #"-R-IY-" : '-[static/sound/ri1.wav]-', # reel #######
        "-R-OW-" : '-[static/sound/rou1.wav]-', # roker
        "-R-OY-" : '-[static/sound/rui1.wav]-', # roint ###### no boi or oy sounds
        '-R-UH-' : '-[static/sound/ruo1.wav]-',# roo
        "-R-UW-" : '-[static/sound/ruo1.wav]-', # roo

        # time log: 5
        "-S-AA-" : '-[static/sound/sou1.wav]-', # rod ######
        "-S-AE-" : '-[static/sound/sa1.wav]-', # rad
        "-S-AH-" : '-[static/sound/se1.wav]-', # rub
        "-S-AO-" : '-[static/sound/sou1.wav]-', # rope
        "-S-AW-" : '-[static/sound/sao1.wav]-', # cow
        "-S-AY-" : '-[static/sound/sai1.wav]-', # rye
        "-S-EH" : '-[static/sound/sen1.wav]-', # rep  ##########33333333 crop #########3
        #"-S-ER" : '-B and ER so far-', # rer
        "-S-EY" : '-[static/sound/sai1.wav]-', # ray  ########3 sei
        #"-S-IH" : '-[static/sound/wai1.wav]-', # rice #####
        #"-S-IY-" : '-[static/sound/ri1.wav]-', # reel #######
        "-S-OW-" : '-[static/sound/sou1.wav]-', # roker
        #"-S-OY-" : '-[static/sound/rui1.wav]-', # roint ###### no boi or oy sounds
        '-S-UH-' : '-[static/sound/sou1.wav]-',# roo
        "-S-UW-" : '-[static/sound/sou1.wav]-', # roo

        # time log: 3
        "-SH-AA-" : '-[static/sound/shou1.wav]-', # rod ######
        "-SH-AE-" : '-[static/sound/sha1.wav]-', # rad
        "-SH-AH-" : '-[static/sound/she1.wav]-', # rub
        "-SH-AO-" : '-[static/sound/shou1.wav]-', # rope
        "-SH-AW-" : '-[static/sound/shao1.wav]-', # cow
        "-SH-AY-" : '-[static/sound/shai1.wav]-', # rye
        "-SH-EH" : '-[static/sound/shen1.wav]-', # rep  ##########33333333 crop #########3
        #"-SH-ER" : '-B and ER so far-', # rer
        "-SH-EY" : '-[static/sound/shai1.wav]-', # ray  ########3 sei
        #"-SH-IH" : '-[static/sound/wai1.wav]-', # rice #####
        #"-SH-IY-" : '-[static/sound/ri1.wav]-', # reel #######
        "-SH-OW-" : '-[static/sound/shou1.wav]-', # roker
        #"-SH-OY-" : '-[static/sound/rui1.wav]-', # roint ###### no boi or oy sounds
        '-SH-UH-' : '-[static/sound/shou1.wav]-',# roo
        "-SH-UW-" : '-[static/sound/shou1.wav]-', # roo

        # time log: 3
        "-T-AA-" : '-[static/sound/tou1.wav]-', # rod ######
        "-T-AE-" : '-[static/sound/ta1.wav]-', # rad
        "-T-AH-" : '-[static/sound/te1.wav]-', # rub
        "-T-AO-" : '-[static/sound/tou1.wav]-', # rope
        "-T-AW-" : '-[static/sound/tao1.wav]-', # cow
        "-T-AY-" : '-[static/sound/tai1.wav]-', # rye
        #"-T-EH" : '-[static/sound/ten1.wav]-', # rep  ##########33333333 crop #########3
        #"-T-ER" : '-B and ER so far-', # rer
        "-T-EY" : '-[static/sound/tai1.wav]-', # ray  ########3 sei
        #"-T-IH" : '-[static/sound/wai1.wav]-', # rice #####
        #"-T-IY-" : '-[static/sound/ri1.wav]-', # reel #######
        "-T-OW-" : '-[static/sound/tou1.wav]-', # roker
        #"-T-OY-" : '-[static/sound/rui1.wav]-', # roint ###### no boi or oy sounds
        '-T-UH-' : '-[static/sound/tou1.wav]-',# roo
        "-T-UW-" : '-[static/sound/tou1.wav]-', # roo
        
        # time log: 3
        "-TH-AA-" : '-[static/sound/dong1.wav]-', # dong  
        "-TH-AE-" : '-[static/sound/da1.wav]-', # dab    
        "-TH-AH-" : '-[static/sound/de1.wav]-', # dud   
        "-TH-AO-" : '-[static/sound/dou1.wav]-', # door 
        "-TH-AW-" : '-[static/sound/dao1.wav]-', # down
        "-TH-AY-" : '-[static/sound/dai1.wav]-', # dine
        "-TH-EH" : '-[static/sound/de1.wav]-', # deck  #######
        #"-TH-ER" : '-B and ER so far-', # dirk 
        "-TH-EY" : '-[static/sound/dei1.wav]-', # day
        #"-TH-IH" : '-[static/sound/bin1.wav]-', # ding
        #"-TH-IY-" : '-[static/sound/che1.wav]-', # deep
        "-TH-OW-" : '-[static/sound/dou1.wav]-', # dope
        "-TH-OY-" : '-[static/sound/dui1.wav]-', # doy ###### no boi or oy sounds
        '-TH-UH-' : '-[static/sound/de1.wav]-',# duck  #####
        "-TH-UW-" : '-[static/sound/dou1.wav]-', # do


        "-V-AA-" : '-[static/sound/wo1.wav]-', # dong  
        "-V-AE-" : '-[static/sound/wa1.wav]-', # dab    
        "-V-AH-" : '-[static/sound/wen1.wav]-', # dud   
        "-V-AO-" : '-[static/sound/wo1.wav]-', # door 
        #"-V-AW-" : '-[static/sound/1.wav]-', # down
        "-V-AY-" : '-[static/sound/wai1.wav]-', # dine
        "-V-EH" : '-[static/sound/wei1.wav]-', # deck  #######
        #"-V-ER" : '-B and ER so far-', # dirk 
        "-V-EY" : '-[static/sound/wei1.wav]-', # day
        #"-V-IH" : '-[static/sound/bin1.wav]-', # ding
        #"-V-IY-" : '-[static/sound/che1.wav]-', # deep
        "-V-OW-" : '-[static/sound/wo1.wav]-', # dope
        #"-V-OY-" : '-[static/sound/dui1.wav]-', # doy ###### no boi or oy sounds
        #'-V-UH-' : '-[static/sound/1.wav]-',# duck  #####
        #"-V-UW-" : '-[static/sound/wu1.wav]-', # do

        # time log: 
        "-W-AA-" : '-[static/sound/wo1.wav]-', # dong  
        "-W-AE-" : '-[static/sound/wa1.wav]-', # dab    
        "-W-AH-" : '-[static/sound/wen1.wav]-', # dud   
        "-W-AO-" : '-[static/sound/wo1.wav]-', # door 
        #"-W-AW-" : '-[static/sound/1.wav]-', # down
        "-W-AY-" : '-[static/sound/wai1.wav]-', # dine
        "-W-EH" : '-[static/sound/wei1.wav]-', # deck  #######
        #"-W-ER" : '-B and ER so far-', # dirk 
        "-W-EY" : '-[static/sound/wei1.wav]-', # day
        #"-W-IH" : '-[static/sound/bin1.wav]-', # ding
        #"-W-IY-" : '-[static/sound/che1.wav]-', # deep
        "-W-OW-" : '-[static/sound/wo1.wav]-', # dope
        #"-W-OY-" : '-[static/sound/dui1.wav]-', # doy ###### no boi or oy sounds
        #'-W-UH-' : '-[static/sound/1.wav]-',# duck  #####
        #"-W-UW-" : '-[static/sound/wu1.wav]-', # do



        "-Y-AA-" : '-[static/sound/yong1.wav]-', # dong  
        "-Y-AE-" : '-[static/sound/ya1.wav]-', # dab    
        "-Y-AH-" : '-[static/sound/ye1.wav]-', # dud   
        "-Y-AO-" : '-[static/sound/you1.wav]-', # door 
        #"-Y-AW-" : '-[static/sound/1.wav]-', # down
        #"-Y-AY-" : '-[static/sound/yai1.wav]-', # dine
        "-Y-EH" : '-[static/sound/ye1.wav]-', # deck  #######
        #"-Y-ER" : '-B and ER so far-', # dirk 
        "-Y-EY" : '-[static/sound/ye1.wav]-', # day
        "-Y-IH" : '-[static/sound/yi1.wav]-', # ding
        "-Y-IY-" : '-[static/sound/yi1.wav]-', # deep
        "-Y-OW-" : '-[static/sound/yao1.wav]-', # dope
        #"-Y-OY-" : '-[static/sound/yui1.wav]-', # doy ###### no boi or oy sounds
        #'-Y-UH-' : '-[static/sound/1.wav]-',# duck  #####
        "-Y-UW-" : '-[static/sound/yu1.wav]-', # do



        "-Z-AA-" : '-[static/sound/zong1.wav]-', # dong  
        "-Z-AE-" : '-[static/sound/za1.wav]-', # dab    
        "-Z-AH-" : '-[static/sound/ze1.wav]-', # dud   
        "-Z-AO-" : '-[static/sound/zou1.wav]-', # door 
        #"-Z-AW-" : '-[static/sound/1.wav]-', # down
        "-Z-AY-" : '-[static/sound/zai1.wav]-', # dine
        "-Z-EH" : '-[static/sound/ze1.wav]-', # deck  #######
        #"-Z-ER" : '-B and ER so far-', # dirk 
        "-Z-EY" : '-[static/sound/zei1.wav]-', # day
        "-Z-IH" : '-[static/sound/zi1.wav]-', # ding
        "-Z-IY-" : '-[static/sound/zi1.wav]-', # deep
        "-Z-OW-" : '-[static/sound/zao1.wav]-', # dope
        #"-Z-OY-" : '-[static/sound/yui1.wav]-', # doy ###### no boi or oy sounds
        '-Z-UH-' : '-[static/sound/ze1.wav]-',# duck  #####
        "-Z-UW-" : '-[static/sound/zu1.wav]-', # do


        "-ZH-AA-" : '-[static/sound/zhong1.wav]-', # dong  
        "-ZH-AE-" : '-[static/sound/zha1.wav]-', # dab    
        "-ZH-AH-" : '-[static/sound/zhe1.wav]-', # dud   
        "-ZH-AO-" : '-[static/sound/zhou1.wav]-', # door 
        #"-ZH-AW-" : '-[static/sound/1.wav]-', # down
        "-ZH-AY-" : '-[static/sound/zhai1.wav]-', # dine
        "-ZH-EH" : '-[static/sound/zhe1.wav]-', # deck  #######
        #"-ZH-ER" : '-B and ER so far-', # dirk 
        "-ZH-EY" : '-[static/sound/zhei1.wav]-', # day
        "-ZH-IH" : '-[static/sound/zhi1.wav]-', # ding
        "-ZH-IY-" : '-[static/sound/zhi1.wav]-', # deep
        "-ZH-OW-" : '-[static/sound/zhao1.wav]-', # dope
        #"-ZH-OY-" : '-[static/sound/yui1.wav]-', # doy ###### no boi or oy sounds
        '-ZH-UH-' : '-[static/sound/zhe1.wav]-',# duck  #####
        "-ZH-UW-" : '-[static/sound/zhu1.wav]-', # do        
        }

hk_audio_solo_phonemes = {
        '-AA-' : '-[static/sound/ao1.wav]-', #odd     AA D
        '-AE-' : '-[static/sound/a1.wav]-', #at AE T
        '-AH-' : '-[static/sound/a1.wav]-',#'a', #hut        HH AH T
        '-AO-' : '-[static/sound/e1.wav]-',#'ou', #ought     AO T
        '-AW-' : '-[static/sound/ao1.wav]-',#'ow', #cow       K AW
        '-AY-' : '-[static/sound/ai1.wav]-',#'ee', #hide      HH AY D
        '-B-' : '-[static/sound/b1.wav]-',#'b', #be  B IY
        '-CH-' : '-[static/sound/cha1.wav]-',#'ch', #cheese    CH IY Z
        '-D-' : '-[static/sound/de1.wav]-',#'d', #dee D IY
        '-EH-' : '-[static/sound/ei1.wav]-',#'e', #Ed EH D
        '-ER-' : '-[static/sound/er1.wav]-',#'ur', #hurt      HH ER T
        '-EY-' : '-[static/sound/ei1.wav]-',#'ey', #ate       EY T
        '-F-' : '-[static/sound/fa1.wav]-',#'eh', #fee        F IY
        '-G-' : '-[static/sound/g1.wav]-',#'g', #green       G R IY N
        '-HH-' : '-[static/sound/h1.wav]-',#'h', #he HH IY
        '-IH-' : '-[static/sound/ei1.wav]-',#'i', #it IH T
        '-IY-' : '-[static/sound/ei1.wav]-',#'eh', #eat       IY T
        '-JH-' : '-[static/sound/ji1.wav]-',#'g', #gee        JH IY
        '-K-' : '-[static/sound/ke1.wav]-',#'k', #key K IY
        '-L-' : '-[static/sound/le1.wav]-',#'l', #lee L IY
        '-M-' : '-[static/sound/ma1.wav]-',#'m', #me  M IY
        '-NG-' : '-[static/sound/ang1.wav]-',#'ng', #ping      P IH NG
        '-N-' : '-[static/sound/ne1.wav]-',#'n', #knee        N IY

        '-OW-' : '-[static/sound/ou1.wav]-',#'ow', #oat       OW T
        '-OY-' : '-[static/sound/ai1.wav]-',#'oy', #toy       T OY
        '-P-' : '-[static/sound/pa1.wav]-',#'p', #pee P IY
        '-R-' : '-[static/sound/ru1.wav]-',#'h', #read        R IY D
        '-S-' : '-[static/sound/se1.wav]-',#'s', #sea S IY
        '-SH-' : '-[static/sound/she1.wav]-',#'sh', #she       SH IY
        '-T-' : '-[static/sound/t1.wav]-',#'t', #tea T IY
        '-TH-' : '-[static/sound/de1.wav]-',#'th', #theta     TH EY T AH
        '-UH-' : '-[static/sound/bo1.wav]-',#'ou', #hood      HH UH D
        '-UW-' : '-[static/sound/ou1.wav]-',#'ooh', #two      T UW
        '-V-' : '-[static/sound/wo1.wav]-',#'we', #vee V IY
        '-W-' : '-[static/sound/wo1.wav]-',#'w', #we  W IY
        '-Y-' : '-[static/sound/yu1.wav]-',#'y', #yield       Y IY L D
        '-Z-' : '-[static/sound/zhe1.wav]-',#'zh', #zee        Z IY
        '-ZH-' : '-[static/sound/zhe1.wav]-'#'' #seizure    S IY ZH ER
        }