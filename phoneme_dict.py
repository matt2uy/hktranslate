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
        "-P-AE-" : '-[static/sound/pa1.wav]-',
        "-P-AO-" : '-[static/sound/po1.wav]-',
        "-B-AE-" : '-[static/sound/ba1.wav]-',
        "-P-IH-" : '-[static/sound/pi1.wav]-',
        "-G-AE-" : '-[static/sound/ga1.wav]-', #

        "-B-AA-" : '-[static/sound/bao1.wav]-', # robot #######
        "-B-AE-" : '-[static/sound/ba1.wav]-', # bat
        "-B-AH-" : '-[static/sound/ba1.wav]-', # butter ###########    
        "-B-AO-" : '-[static/sound/bo1.wav]-', # aboard
        "-B-AW-" : '-[static/sound/bao1.wav]-', # bow
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
        

        "-D-UW-" : '-[static/sound/dou1.wav]-', # do
        "-DH-AH-" : '-[static/sound/da1.wav]-', # dah, or the

        "-M-AO" : '-[static/sound/mo1.wav]-', # bow
        "-M-AE-" : '-[static/sound/ma1.wav]-', # bow
        "-N-AE" : '-[static/sound/na4.wav]-', # banana
        "-N-AH" : '-[static/sound/na4.wav]-', # banana
        "-R-AY" : '-[static/sound/wai4.wav]-', # right
        "-T-IH" : '-[static/sound/ti1.wav]-', # tickle
        "-TH-IH" : '-[static/sound/ti1.wav]-' # thing

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
        '-HH-' : '-[static/sound/ha1.wav]-',#'h', #he HH IY
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