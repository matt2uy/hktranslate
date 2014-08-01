hk_list = {
            'the ' : 'dah ',
            'that ' : 'dat ', 
            'ere' : 'ah ',
            'er' : 'ah',
            'v' : 'f', 
            'at' : 'ah', 
            'tr' : 'ch', 
            'ch' : 'tr', 
            'al' : 'ow', 
            'or' : 'oe', 
            'llo ' : 'woh ',
            'ars' : 'as',
            'ar' : 'ah',
            'dol' : 'dow',
            'ty' : 'tay',
            'xclu' : 'xcawu',
            'ble' : 'bow',
            'ro' : 'wo',
            'state' : 'stayte',
            'ay' : 'ai'
            }
# not used in search and replace

hk_text_phonemes = {
        'AA' : 'ao', #odd     AA D
        'AE' : 'ah', #at AE T
        'AH' : 'ah', #hut        HH AH T
        'AO' : 'ou', #ought     AO T
        'AW' : 'ow', #cow       K AW
        'AY' : 'ai', #hide      HH AY D
        'B' : 'b', #be  B IY
        'CH' : 'ch', #cheese    CH IY Z
        'D' : 'd', #dee D IY
        'DH' : 'd', #thee       DH IY
        'EH' : 'e', #Ed EH D
        'ER' : 'ur', #hurt      HH ER T
        'EY' : 'ey', #ate       EY T
        'F' : 'eh', #fee        F IY
        'G' : 'g', #green       G R IY N
        'HH' : 'h', #he HH IY
        'IH' : 'i', #it IH T
        'IY' : 'ee', #eat       IY T
        'JH' : 'g', #gee        JH IY
        'K' : 'k', #key K IY
        'L' : 'l', #lee L IY
        'M' : 'm', #me  M IY
        'N' : 'n', #knee        N IY
        'NG' : 'ng', #ping      P IH NG
        'OW' : 'ow', #oat       OW T
        'OY' : 'oy', #toy       T OY
        'P' : 'p', #pee P IY
        'R' : 'h', #read        R IY D
        'S' : 's', #sea S IY
        'SH' : 'sh', #she       SH IY
        'T' : 't', #tea T IY
        'TH' : 'd', #theta     TH EY T AH
        'UH' : 'oo', #hood      HH UH D
        'UW' : 'ooh', #two      T UW
        'V' : 'w', #vee V IY
        'W' : 'v', #we  W IY
        'Y' : 'y', #yield       Y IY L D
        'Z' : 'zh', #zee        Z IY
        'ZH' : 'sh' #seizure    S IY ZH ER
        }


hk_audio_solo_phonemes = {
        "-AA-" : "-[static/speech/single_phoneme/aa.wav]-", # aww in odd
        "-AE-" : "-[static/speech/single_phoneme/ae.wav]-", # a in bass
        "-AH-" : "-[static/speech/single_phoneme/ah.wav]-", # uh in hut        HH AH T
        "-AO-" : "-[static/speech/single_phoneme/ao.wav]-", # aww in ought     AO T
        "-AW-" : "-[static/speech/single_phoneme/aw.wav]-", #  ow, in cow       K AW
        "-AY-" : "-[static/speech/single_phoneme/ay.wav]-", #  i in hide      HH AY D
        "-EH-" : "-[static/speech/single_phoneme/eh.wav]-", # eh in Ed 
        "-ER-" : "-[static/speech/single_phoneme/er.wav]-", # ur #hurt      HH ER T
        "-EY-" : "-[static/speech/single_phoneme/ey.wav]-", # ey  #ate       EY T
        "-IH-" : "-[static/speech/single_phoneme/ih.wav]-", # ih #it IH T
        "-IY-" : "-[static/speech/single_phoneme/iy.wav]-", # iy #eat       IY T
        "-OW-" : "-[static/speech/single_phoneme/ow.wav]-", #'ow', #oat       OW T
        "-OY-" : "-[static/speech/single_phoneme/oy.wav]-", #'oy', #toy       T OY
        "-UH-" : "-[static/speech/single_phoneme/uh.wav]-", #'ou', #hood      HH UH D
        "-UW-" : "-[static/speech/single_phoneme/uw.wav]-", #'ooh', #two      T UW
        


        "-B-" : "-[static/speech/single_phoneme/b.wav]-", #   b  in bee
        "-CH-" : "-[static/speech/single_phoneme/ch.wav]-", # ch in cheese    CH IY Z
        "-D-" : "-[static/speech/single_phoneme/d.wav]-", # d in dee
        "-F-" : "-[static/speech/single_phoneme/f.wav]-", # f #fee        F IY
        "-G-" : "-[static/speech/single_phoneme/g.wav]-", # g #green       G R IY N
        "-HH-" : "-[static/speech/single_phoneme/hh.wav]-", # h #he HH IY
        "-JH-" : "-[static/speech/single_phoneme/jh.wav]-", # j  #gee        JH IY
        "-K-" : "-[static/speech/single_phoneme/k.wav]-", # k #key K IY
        "-L-" : "-[static/speech/single_phoneme/l.wav]-", # l #lee L IY
        "-M-" : "-[static/speech/single_phoneme/m.wav]-", # m, #me  M IY
        "-NG-" : "-[static/speech/single_phoneme/ng.wav]-", # ng #ping      P IH NG
        "-N-" : "-[static/speech/single_phoneme/n.wav]-", # n in #knee        N IY
        "-P-" : "-[static/speech/single_phoneme/p.wav]-", #'p', #pee P IY
        "-R-" : "-[static/speech/single_phoneme/r.wav]-", #'h', #read        R IY D
        "-S-" : "-[static/speech/single_phoneme/s.wav]-", #'s', #sea S IY
        "-SH-" : "-[static/speech/single_phoneme/sh.wav]-", #'sh', #she       SH IY
        "-T-" : "-[static/speech/single_phoneme/t.wav]-", #'t', #tea T IY
        "-TH-" : "-[static/speech/single_phoneme/th.wav]-", #'th', #theta     TH EY T AH
        "-V-" : "-[static/speech/single_phoneme/v.wav]-", #'we', #vee V IY
        "-W-" : "-[static/speech/single_phoneme/w.wav]-", #'w', #we  W IY
        "-Y-" : "-[static/speech/single_phoneme/y.wav]-", #'y', #yield       Y IY L D
        "-Z-" : "-[static/speech/single_phoneme/z.wav]-", #'zh', #zee        Z IY
        "-ZH-" : "-[static/speech/single_phoneme/zh.wav]-"# #seizure    S IY ZH ER
        }

separate_words = {
        " " : "-[static/speech/misc/blank.wav]-"
        }

hk_audio_phoneme_combo_beginnings = {
        # consonant -> vowel
        "-B-AA-" : "-[static/speech/double_phoneme/baa.wav]-", # robot #######
        "-B-AE-" : "-[static/speech/double_phoneme/bae.wav]-", # bat
        "-B-AH-" : "-[static/speech/double_phoneme/bah.wav]-", # butter ###########    
        "-B-AO-" : "-[static/speech/double_phoneme/bao.wav]-", # aboard
        "-B-AW-" : "-[static/speech/double_phoneme/baw.wav]-", # bow (respect)
        "-B-AY-" : "-[static/speech/double_phoneme/bay.wav]-", # buy
        "-B-EH-" : "-[static/speech/double_phoneme/beh.wav]-", # ben
        "-B-ER-" : "-[static/speech/double_phoneme/ber.wav]-", # bait
        "-B-EY-" : "-[static/speech/double_phoneme/bey.wav]-", # bait
        "-B-IH-" : "-[static/speech/double_phoneme/bih.wav]-", # bit
        "-B-IY-" : "-[static/speech/double_phoneme/biy.wav]-", # be
        "-B-OW-" : "-[static/speech/double_phoneme/bow.wav]-", # boat
        "-B-OY-" : "-[static/speech/double_phoneme/boy.wav]-", # boat ###### no boi or oy speech/double_phonemes
        "-B-UH-" : "-[static/speech/double_phoneme/buh.wav]-", #'ou', #hood      HH UH D
        "-B-UW-" : "-[static/speech/double_phoneme/buw.wav]-", #boo
        
        # for c: edit out silence
        # and silence between words too!
        # time log: 25
        "-CH-AA-" : "-[static/speech/double_phoneme/chaa.wav]-", # chopper     
        "-CH-AE-" : "-[static/speech/double_phoneme/chae.wav]-", # chat     
        "-CH-AH-" : "-[static/speech/double_phoneme/chah.wav]-", # chutney    
        "-CH-AO-" : "-[static/speech/double_phoneme/chao.wav]-", # chop 
        "-CH-AW-" : "-[static/speech/double_phoneme/chaw.wav]-", # chow
        "-CH-AY-" : "-[static/speech/double_phoneme/chay.wav]-", # china
        "-CH-EH-" : "-[static/speech/double_phoneme/cheh.wav]-", # checkers
        "-CH-ER-" : "-[static/speech/double_phoneme/cher.wav]-", # churn
        "-CH-EY-" : "-[static/speech/double_phoneme/chey.wav]-", # change
        "-CH-IH-" : "-[static/speech/double_phoneme/chih.wav]-", # ching
        "-CH-IY-" : "-[static/speech/double_phoneme/chiy.wav]-", # cheese
        "-CH-OW-" : "-[static/speech/double_phoneme/chou.wav]-", # choke
        "-CH-OY-" : "-[static/speech/double_phoneme/choy.wav]-", # choice
        "-CH-UH-" : "-[static/speech/double_phoneme/chuh.wav]-", # chuck
        "-CH-UW-" : "-[static/speech/double_phoneme/chuw.wav]-", # chew

        # time log: 16
        "-D-AA-" : "-[static/speech/double_phoneme/daa.wav]-", # chopper     
        "-D-AE-" : "-[static/speech/double_phoneme/dae.wav]-", # chat     
        "-D-AH-" : "-[static/speech/double_phoneme/dah.wav]-", # chutney    
        "-D-AO-" : "-[static/speech/double_phoneme/dao.wav]-", # chop 
        "-D-AW-" : "-[static/speech/double_phoneme/daw.wav]-", # chow
        "-D-AY-" : "-[static/speech/double_phoneme/day.wav]-", # china
        "-D-EH-" : "-[static/speech/double_phoneme/deh.wav]-", # checkers
        "-D-ER-" : "-[static/speech/double_phoneme/der.wav]-", # churn
        "-D-EY-" : "-[static/speech/double_phoneme/dey.wav]-", # change
        "-D-IH-" : "-[static/speech/double_phoneme/dih.wav]-", # ching
        "-D-IY-" : "-[static/speech/double_phoneme/diy.wav]-", # cheese
        "-D-OW-" : "-[static/speech/double_phoneme/dow.wav]-", # choke
        "-D-OY-" : "-[static/speech/double_phoneme/doy.wav]-", # choice
        "-D-UH-" : "-[static/speech/double_phoneme/duh.wav]-", # chuck
        "-D-UW-" : "-[static/speech/double_phoneme/duw.wav]-", # chew

        # time log: 9
        "-F-AA-" : "-[static/speech/double_phoneme/faa.wav]-", # chopper     
        "-F-AE-" : "-[static/speech/double_phoneme/fae.wav]-", # chat     
        "-F-AH-" : "-[static/speech/double_phoneme/fah.wav]-", # chutney      
        "-F-AO-" : "-[static/speech/double_phoneme/fao.wav]-", # chop 
        "-F-AW-" : "-[static/speech/double_phoneme/faw.wav]-", # chow
        "-F-AY-" : "-[static/speech/double_phoneme/fay.wav]-", # china
        "-F-EH-" : "-[static/speech/double_phoneme/feh.wav]-", # checkers
        "-F-ER-" : "-[static/speech/double_phoneme/fer.wav]-", # churn
        "-F-EY-" : "-[static/speech/double_phoneme/fey.wav]-", # change
        "-F-IH-" : "-[static/speech/double_phoneme/fih.wav]-", # ching
        "-F-IY-" : "-[static/speech/double_phoneme/fiy.wav]-", # cheese
        "-F-OW-" : "-[static/speech/double_phoneme/fow.wav]-", # choke
        "-F-OY-" : "-[static/speech/double_phoneme/foy.wav]-", # choice
        "-F-UH-" : "-[static/speech/double_phoneme/fuh.wav]-", # chuck
        "-F-UW-" : "-[static/speech/double_phoneme/fuw.wav]-", # chew
       
        # time log: 12
        "-G-AA-" : "-[static/speech/double_phoneme/gaa.wav]-", # chopper     
        "-G-AE-" : "-[static/speech/double_phoneme/gae.wav]-", # chat     
        "-G-AH-" : "-[static/speech/double_phoneme/gah.wav]-", # chutney    
        "-G-AO-" : "-[static/speech/double_phoneme/gao.wav]-", # chop 
        "-G-AW-" : "-[static/speech/double_phoneme/gaw.wav]-", # chow
        "-G-AY-" : "-[static/speech/double_phoneme/gay.wav]-", # china
        "-G-EH-" : "-[static/speech/double_phoneme/geh.wav]-", # checkers
        "-G-ER-" : "-[static/speech/double_phoneme/ger.wav]-", # churn
        "-G-EY-" : "-[static/speech/double_phoneme/gey.wav]-", # change
        "-G-IH-" : "-[static/speech/double_phoneme/gih.wav]-", # ching
        "-G-IY-" : "-[static/speech/double_phoneme/giy.wav]-", # cheese
        "-G-OW-" : "-[static/speech/double_phoneme/gow.wav]-", # choke
        "-G-OY-" : "-[static/speech/double_phoneme/goy.wav]-", # choice
        "-G-UH-" : "-[static/speech/double_phoneme/guh.wav]-", # chuck
        "-G-UW-" : "-[static/speech/double_phoneme/guw.wav]-", # chew

        # time log: 9
        "-HH-AA-" : "-[static/speech/double_phoneme/haa.wav]-", # chopper     
        "-HH-AE-" : "-[static/speech/double_phoneme/hae.wav]-", # chat     
        "-HH-AH-" : "-[static/speech/double_phoneme/hah.wav]-", # chutney    
        "-HH-AO-" : "-[static/speech/double_phoneme/hao.wav]-", # chop 
        "-HH-AW-" : "-[static/speech/double_phoneme/haw.wav]-", # chow
        "-HH-AY-" : "-[static/speech/double_phoneme/hay.wav]-", # china
        "-HH-EH-" : "-[static/speech/double_phoneme/heh.wav]-", # checkers
        "-HH-ER-" : "-[static/speech/double_phoneme/her.wav]-", # churn
        "-HH-EY-" : "-[static/speech/double_phoneme/hey.wav]-", # change
        "-HH-IH-" : "-[static/speech/double_phoneme/hih.wav]-", # ching
        "-HH-IY-" : "-[static/speech/double_phoneme/hiy.wav]-", # cheese
        "-HH-OW-" : "-[static/speech/double_phoneme/how.wav]-", # choke
        "-HH-OY-" : "-[static/speech/double_phoneme/hoy.wav]-", # choice
        "-HH-UH-" : "-[static/speech/double_phoneme/huh.wav]-", # chuck
        "-HH-UW-" : "-[static/speech/double_phoneme/huw.wav]-", # chew

        # time log: 9
        "-JH-AA-" : "-[static/speech/double_phoneme/jaa.wav]-", # chopper     
        "-JH-AE-" : "-[static/speech/double_phoneme/jae.wav]-", # chat     
        "-JH-AH-" : "-[static/speech/double_phoneme/jah.wav]-", # chutney    
        "-JH-AO-" : "-[static/speech/double_phoneme/jao.wav]-", # chop 
        "-JH-AW-" : "-[static/speech/double_phoneme/jaw.wav]-", # chow
        "-JH-AY-" : "-[static/speech/double_phoneme/jay.wav]-", # china
        "-JH-EH-" : "-[static/speech/double_phoneme/jeh.wav]-", # checkers
        "-JH-ER-" : "-[static/speech/double_phoneme/jer.wav]-", # churn
        "-JH-EY-" : "-[static/speech/double_phoneme/jey.wav]-", # change
        "-JH-IH-" : "-[static/speech/double_phoneme/jih.wav]-", # ching
        "-JH-IY-" : "-[static/speech/double_phoneme/jiy.wav]-", # cheese
        "-JH-OW-" : "-[static/speech/double_phoneme/jow.wav]-", # choke
        "-JH-OY-" : "-[static/speech/double_phoneme/joy.wav]-", # choice
        "-JH-UH-" : "-[static/speech/double_phoneme/juh.wav]-", # chuck
        "-JH-UW-" : "-[static/speech/double_phoneme/juw.wav]-", # chew

        # time log: 9
        "-K-AA-" : "-[static/speech/double_phoneme/kaa.wav]-", # chopper     
        "-K-AE-" : "-[static/speech/double_phoneme/kae.wav]-", # chat     
        "-K-AH-" : "-[static/speech/double_phoneme/kah.wav]-", # chutney    
        "-K-AO-" : "-[static/speech/double_phoneme/kao.wav]-", # chop 
        "-K-AW-" : "-[static/speech/double_phoneme/kaw.wav]-", # chow
        "-K-AY-" : "-[static/speech/double_phoneme/kay.wav]-", # china
        "-K-EH-" : "-[static/speech/double_phoneme/keh.wav]-", # checkers
        "-K-ER-" : "-[static/speech/double_phoneme/ker.wav]-", # churn
        "-K-EY-" : "-[static/speech/double_phoneme/key.wav]-", # change
        "-K-IH-" : "-[static/speech/double_phoneme/kih.wav]-", # ching
        "-K-IY-" : "-[static/speech/double_phoneme/kiy.wav]-", # cheese
        "-K-OW-" : "-[static/speech/double_phoneme/kow.wav]-", # choke
        "-K-OY-" : "-[static/speech/double_phoneme/koy.wav]-", # choice
        "-K-UH-" : "-[static/speech/double_phoneme/kuh.wav]-", # chuck
        "-K-UW-" : "-[static/speech/double_phoneme/kuw.wav]-", # chew

        # time log: 9
        "-L-AA-" : "-[static/speech/double_phoneme/laa.wav]-", # chopper     
        "-L-AE-" : "-[static/speech/double_phoneme/lae.wav]-", # chat     
        "-L-AH-" : "-[static/speech/double_phoneme/lah.wav]-", # chutney    
        "-L-AO-" : "-[static/speech/double_phoneme/lao.wav]-", # chop 
        "-L-AW-" : "-[static/speech/double_phoneme/law.wav]-", # chow
        "-L-AY-" : "-[static/speech/double_phoneme/lay.wav]-", # china
        "-L-EH-" : "-[static/speech/double_phoneme/leh.wav]-", # checkers
        "-L-ER-" : "-[static/speech/double_phoneme/ler.wav]-", # churn
        "-L-EY-" : "-[static/speech/double_phoneme/ley.wav]-", # change
        "-L-IH-" : "-[static/speech/double_phoneme/lih.wav]-", # ching
        "-L-IY-" : "-[static/speech/double_phoneme/liy.wav]-", # cheese
        "-L-OW-" : "-[static/speech/double_phoneme/low.wav]-", # choke
        "-L-OY-" : "-[static/speech/double_phoneme/loy.wav]-", # choice
        "-L-UH-" : "-[static/speech/double_phoneme/luh.wav]-", # chuck
        "-L-UW-" : "-[static/speech/double_phoneme/luw.wav]-", # chew

        # time log: 9
        "-M-AA-" : "-[static/speech/double_phoneme/maa.wav]-", # chopper     
        "-M-AE-" : "-[static/speech/double_phoneme/mae.wav]-", # chat     
        "-M-AH-" : "-[static/speech/double_phoneme/mah.wav]-", # chutney    
        "-M-AO-" : "-[static/speech/double_phoneme/mao.wav]-", # chop 
        "-M-AW-" : "-[static/speech/double_phoneme/maw.wav]-", # chow
        "-M-AY-" : "-[static/speech/double_phoneme/may.wav]-", # china
        "-M-EH-" : "-[static/speech/double_phoneme/meh.wav]-", # checkers
        "-M-ER-" : "-[static/speech/double_phoneme/mer.wav]-", # churn
        "-M-EY-" : "-[static/speech/double_phoneme/mey.wav]-", # change
        "-M-IH-" : "-[static/speech/double_phoneme/mih.wav]-", # ching
        "-M-IY-" : "-[static/speech/double_phoneme/miy.wav]-", # cheese
        "-M-OW-" : "-[static/speech/double_phoneme/mow.wav]-", # choke
        "-M-OY-" : "-[static/speech/double_phoneme/moy.wav]-", # choice
        "-M-UH-" : "-[static/speech/double_phoneme/muh.wav]-", # chuck
        "-M-UW-" : "-[static/speech/double_phoneme/muw.wav]-", # chew
     
        # time log: 9
        "-N-AA-" : "-[static/speech/double_phoneme/naa.wav]-", # chopper     
        "-N-AE-" : "-[static/speech/double_phoneme/nae.wav]-", # chat     
        "-N-AH-" : "-[static/speech/double_phoneme/nah.wav]-", # chutney    
        "-N-AO-" : "-[static/speech/double_phoneme/nao.wav]-", # chop 
        "-N-AW-" : "-[static/speech/double_phoneme/naw.wav]-", # chow
        "-N-AY-" : "-[static/speech/double_phoneme/nay.wav]-", # china
        "-N-EH-" : "-[static/speech/double_phoneme/neh.wav]-", # checkers
        "-N-ER-" : "-[static/speech/double_phoneme/ner.wav]-", # churn
        "-N-EY-" : "-[static/speech/double_phoneme/ney.wav]-", # change
        "-N-IH-" : "-[static/speech/double_phoneme/nih.wav]-", # ching
        "-N-IY-" : "-[static/speech/double_phoneme/niy.wav]-", # cheese
        "-N-OW-" : "-[static/speech/double_phoneme/now.wav]-", # choke
        "-N-OY-" : "-[static/speech/double_phoneme/noy.wav]-", # choice
        "-N-UH-" : "-[static/speech/double_phoneme/nuh.wav]-", # chuck
        "-N-UW-" : "-[static/speech/double_phoneme/nuw.wav]-", # chew

        # time log: 9
        "-P-AA-" : "-[static/speech/double_phoneme/paa.wav]-", # chopper     
        "-P-AE-" : "-[static/speech/double_phoneme/pae.wav]-", # chat     
        "-P-AH-" : "-[static/speech/double_phoneme/pah.wav]-", # chutney    
        "-P-AO-" : "-[static/speech/double_phoneme/pao.wav]-", # chop 
        "-P-AW-" : "-[static/speech/double_phoneme/paw.wav]-", # chow
        "-P-AY-" : "-[static/speech/double_phoneme/pay.wav]-", # china
        "-P-EH-" : "-[static/speech/double_phoneme/peh.wav]-", # checkers
        "-P-ER-" : "-[static/speech/double_phoneme/per.wav]-", # churn
        "-P-EY-" : "-[static/speech/double_phoneme/pey.wav]-", # change
        "-P-IH-" : "-[static/speech/double_phoneme/pih.wav]-", # ching
        "-P-IY-" : "-[static/speech/double_phoneme/piy.wav]-", # cheese
        "-P-OW-" : "-[static/speech/double_phoneme/pow.wav]-", # choke
        "-P-OY-" : "-[static/speech/double_phoneme/poy.wav]-", # choice
        "-P-UH-" : "-[static/speech/double_phoneme/puh.wav]-", # chuck
        "-P-UW-" : "-[static/speech/double_phoneme/puw.wav]-", # chew

        # time log: 9
        "-R-AA-" : "-[static/speech/double_phoneme/raa.wav]-", # chopper     
        "-R-AE-" : "-[static/speech/double_phoneme/rae.wav]-", # chat     
        "-R-AH-" : "-[static/speech/double_phoneme/rah.wav]-", # chutney    
        "-R-AO-" : "-[static/speech/double_phoneme/rao.wav]-", # chop 
        "-R-AW-" : "-[static/speech/double_phoneme/raw.wav]-", # chow
        "-R-AY-" : "-[static/speech/double_phoneme/ray.wav]-", # china
        "-R-EH-" : "-[static/speech/double_phoneme/reh.wav]-", # checkers
        "-R-ER-" : "-[static/speech/double_phoneme/rer.wav]-", # churn
        "-R-EY-" : "-[static/speech/double_phoneme/rey.wav]-", # change
        "-R-IH-" : "-[static/speech/double_phoneme/rih.wav]-", # ching
        "-R-IY-" : "-[static/speech/double_phoneme/riy.wav]-", # cheese
        "-R-OW-" : "-[static/speech/double_phoneme/row.wav]-", # choke
        "-R-OY-" : "-[static/speech/double_phoneme/roy.wav]-", # choice
        "-R-UH-" : "-[static/speech/double_phoneme/ruh.wav]-", # chuck
        "-R-UW-" : "-[static/speech/double_phoneme/ruw.wav]-", # chew

        # time log: 9
        "-S-AA-" : "-[static/speech/double_phoneme/saa.wav]-", # chopper     
        "-S-AE-" : "-[static/speech/double_phoneme/sae.wav]-", # chat     
        "-S-AH-" : "-[static/speech/double_phoneme/sah.wav]-", # chutney    
        "-S-AO-" : "-[static/speech/double_phoneme/sao.wav]-", # chop 
        "-S-AW-" : "-[static/speech/double_phoneme/saw.wav]-", # chow
        "-S-AY-" : "-[static/speech/double_phoneme/say.wav]-", # china
        "-S-EH-" : "-[static/speech/double_phoneme/seh.wav]-", # checkers
        "-S-ER-" : "-[static/speech/double_phoneme/ser.wav]-", # churn
        "-S-EY-" : "-[static/speech/double_phoneme/sey.wav]-", # change
        "-S-IH-" : "-[static/speech/double_phoneme/sih.wav]-", # ching
        "-S-IY-" : "-[static/speech/double_phoneme/siy.wav]-", # cheese
        "-S-OW-" : "-[static/speech/double_phoneme/sow.wav]-", # choke
        "-S-OY-" : "-[static/speech/double_phoneme/soy.wav]-", # choice
        "-S-UH-" : "-[static/speech/double_phoneme/suh.wav]-", # chuck
        "-S-UW-" : "-[static/speech/double_phoneme/suw.wav]-", # chew
        
        # time log: 9
        "-SH-AA-" : "-[static/speech/double_phoneme/shaa.wav]-", # chopper     
        "-SH-AE-" : "-[static/speech/double_phoneme/shae.wav]-", # chat     
        "-SH-AH-" : "-[static/speech/double_phoneme/shah.wav]-", # chutney    
        "-SH-AO-" : "-[static/speech/double_phoneme/shao.wav]-", # chop 
        "-SH-AW-" : "-[static/speech/double_phoneme/shaw.wav]-", # chow
        "-SH-AY-" : "-[static/speech/double_phoneme/shay.wav]-", # china
        "-SH-EH-" : "-[static/speech/double_phoneme/sheh.wav]-", # checkers
        "-SH-ER-" : "-[static/speech/double_phoneme/sher.wav]-", # churn
        "-SH-EY-" : "-[static/speech/double_phoneme/shey.wav]-", # change
        "-SH-IH-" : "-[static/speech/double_phoneme/shih.wav]-", # ching
        "-SH-IY-" : "-[static/speech/double_phoneme/shiy.wav]-", # cheese
        "-SH-OW-" : "-[static/speech/double_phoneme/show.wav]-", # choke
        "-SH-OY-" : "-[static/speech/double_phoneme/shoy.wav]-", # choice
        "-SH-UH-" : "-[static/speech/double_phoneme/shuh.wav]-", # chuck
        "-SH-UW-" : "-[static/speech/double_phoneme/shuw.wav]-", # chew

        # time log: 9
        "-T-AA-" : "-[static/speech/double_phoneme/taa.wav]-", # chopper     
        "-T-AE-" : "-[static/speech/double_phoneme/tae.wav]-", # chat     
        "-T-AH-" : "-[static/speech/double_phoneme/tah.wav]-", # chutney    
        "-T-AO-" : "-[static/speech/double_phoneme/tao.wav]-", # chop 
        "-T-AW-" : "-[static/speech/double_phoneme/taw.wav]-", # chow
        "-T-AY-" : "-[static/speech/double_phoneme/tay.wav]-", # china
        "-T-EH-" : "-[static/speech/double_phoneme/teh.wav]-", # checkers
        "-T-ER-" : "-[static/speech/double_phoneme/ter.wav]-", # churn
        "-T-EY-" : "-[static/speech/double_phoneme/tey.wav]-", # change
        "-T-IH-" : "-[static/speech/double_phoneme/tih.wav]-", # ching
        "-T-IY-" : "-[static/speech/double_phoneme/tiy.wav]-", # cheese
        "-T-OW-" : "-[static/speech/double_phoneme/tow.wav]-", # choke
        "-T-OY-" : "-[static/speech/double_phoneme/toy.wav]-", # choice
        "-T-UH-" : "-[static/speech/double_phoneme/tuh.wav]-", # chuck
        "-T-UW-" : "-[static/speech/double_phoneme/tuw.wav]-", # chew
        
        # time log: 9
        "-TH-AA-" : "-[static/speech/double_phoneme/thaa.wav]-", # chopper     
        "-TH-AE-" : "-[static/speech/double_phoneme/thae.wav]-", # chat     
        "-TH-AH-" : "-[static/speech/double_phoneme/thah.wav]-", # chutney    
        "-TH-AO-" : "-[static/speech/double_phoneme/thao.wav]-", # chop 
        "-TH-AW-" : "-[static/speech/double_phoneme/thaw.wav]-", # chow
        "-TH-AY-" : "-[static/speech/double_phoneme/thay.wav]-", # china
        "-TH-EH-" : "-[static/speech/double_phoneme/theh.wav]-", # checkers
        "-TH-ER-" : "-[static/speech/double_phoneme/ther.wav]-", # churn
        "-TH-EY-" : "-[static/speech/double_phoneme/they.wav]-", # change
        "-TH-IH-" : "-[static/speech/double_phoneme/thih.wav]-", # ching
        "-TH-IY-" : "-[static/speech/double_phoneme/thiy.wav]-", # cheese
        "-TH-OW-" : "-[static/speech/double_phoneme/thow.wav]-", # choke
        "-TH-OY-" : "-[static/speech/double_phoneme/thoy.wav]-", # choice
        "-TH-UH-" : "-[static/speech/double_phoneme/thuh.wav]-", # chuck
        "-TH-UW-" : "-[static/speech/double_phoneme/thuw.wav]-", # chew


        # time log: 9
        "-V-AA-" : "-[static/speech/double_phoneme/vaa.wav]-", # chopper     
        "-V-AE-" : "-[static/speech/double_phoneme/vae.wav]-", # chat     
        "-V-AH-" : "-[static/speech/double_phoneme/vah.wav]-", # chutney    
        "-V-AO-" : "-[static/speech/double_phoneme/vao.wav]-", # chop 
        "-V-AW-" : "-[static/speech/double_phoneme/vaw.wav]-", # chow
        "-V-AY-" : "-[static/speech/double_phoneme/vay.wav]-", # china
        "-V-EH-" : "-[static/speech/double_phoneme/veh.wav]-", # checkers
        "-V-ER-" : "-[static/speech/double_phoneme/ver.wav]-", # churn
        "-V-EY-" : "-[static/speech/double_phoneme/vey.wav]-", # change
        "-V-IH-" : "-[static/speech/double_phoneme/vih.wav]-", # ching
        "-V-IY-" : "-[static/speech/double_phoneme/viy.wav]-", # cheese
        "-V-OW-" : "-[static/speech/double_phoneme/vow.wav]-", # choke
        "-V-OY-" : "-[static/speech/double_phoneme/voy.wav]-", # choice
        "-V-UH-" : "-[static/speech/double_phoneme/vuh.wav]-", # chuck
        "-V-UW-" : "-[static/speech/double_phoneme/vuw.wav]-", # chew

        # time log: 9
        "-W-AA-" : "-[static/speech/double_phoneme/waa.wav]-", # chopper     
        "-W-AE-" : "-[static/speech/double_phoneme/wae.wav]-", # chat     
        "-W-AH-" : "-[static/speech/double_phoneme/wah.wav]-", # chutney    
        "-W-AO-" : "-[static/speech/double_phoneme/wao.wav]-", # chop 
        "-W-AW-" : "-[static/speech/double_phoneme/waw.wav]-", # chow
        "-W-AY-" : "-[static/speech/double_phoneme/way.wav]-", # china
        "-W-EH-" : "-[static/speech/double_phoneme/weh.wav]-", # checkers
        "-W-ER-" : "-[static/speech/double_phoneme/wer.wav]-", # churn
        "-W-EY-" : "-[static/speech/double_phoneme/wey.wav]-", # change
        "-W-IH-" : "-[static/speech/double_phoneme/wih.wav]-", # ching
        "-W-IY-" : "-[static/speech/double_phoneme/wiy.wav]-", # cheese
        "-W-OW-" : "-[static/speech/double_phoneme/wow.wav]-", # choke
        "-W-OY-" : "-[static/speech/double_phoneme/woy.wav]-", # choice
        "-W-UH-" : "-[static/speech/double_phoneme/wuh.wav]-", # chuck
        "-W-UW-" : "-[static/speech/double_phoneme/wuw.wav]-", # chew



        # time log: 9
        "-Y-AA-" : "-[static/speech/double_phoneme/yaa.wav]-", # chopper     
        "-Y-AE-" : "-[static/speech/double_phoneme/yae.wav]-", # chat     
        "-Y-AH-" : "-[static/speech/double_phoneme/yah.wav]-", # chutney    
        "-Y-AO-" : "-[static/speech/double_phoneme/yao.wav]-", # chop 
        "-Y-AW-" : "-[static/speech/double_phoneme/yaw.wav]-", # chow
        "-Y-AY-" : "-[static/speech/double_phoneme/yay.wav]-", # china
        "-Y-EH-" : "-[static/speech/double_phoneme/yeh.wav]-", # checkers
        "-Y-ER-" : "-[static/speech/double_phoneme/yer.wav]-", # churn
        "-Y-EY-" : "-[static/speech/double_phoneme/yey.wav]-", # change
        "-Y-IH-" : "-[static/speech/double_phoneme/yih.wav]-", # ching
        "-Y-IY-" : "-[static/speech/double_phoneme/yiy.wav]-", # cheese
        "-Y-OW-" : "-[static/speech/double_phoneme/yow.wav]-", # choke
        "-Y-OY-" : "-[static/speech/double_phoneme/yoy.wav]-", # choice
        "-Y-UH-" : "-[static/speech/double_phoneme/yuh.wav]-", # chuck
        "-Y-UW-" : "-[static/speech/double_phoneme/yuw.wav]-", # chew



        # time log: 9
        "-Z-AA-" : "-[static/speech/double_phoneme/zaa.wav]-", # chopper     
        "-Z-AE-" : "-[static/speech/double_phoneme/zae.wav]-", # chat     
        "-Z-AH-" : "-[static/speech/double_phoneme/zah.wav]-", # chutney    
        "-Z-AO-" : "-[static/speech/double_phoneme/zao.wav]-", # chop 
        "-Z-AW-" : "-[static/speech/double_phoneme/zaw.wav]-", # chow
        "-Z-AY-" : "-[static/speech/double_phoneme/zay.wav]-", # china
        "-Z-EH-" : "-[static/speech/double_phoneme/zeh.wav]-", # checkers
        "-Z-ER-" : "-[static/speech/double_phoneme/zer.wav]-", # churn
        "-Z-EY-" : "-[static/speech/double_phoneme/zey.wav]-", # change
        "-Z-IH-" : "-[static/speech/double_phoneme/zih.wav]-", # ching
        "-Z-IY-" : "-[static/speech/double_phoneme/ziy.wav]-", # cheese
        "-Z-OW-" : "-[static/speech/double_phoneme/zow.wav]-", # choke
        "-Z-OY-" : "-[static/speech/double_phoneme/zoy.wav]-", # choice
        "-Z-UH-" : "-[static/speech/double_phoneme/zuh.wav]-", # chuck
        "-Z-UW-" : "-[static/speech/double_phoneme/zuw.wav]-", # chew


        # time log: 9
        "-ZH-AA-" : "-[static/speech/double_phoneme/zhaa.wav]-", # chopper     
        "-ZH-AE-" : "-[static/speech/double_phoneme/zhae.wav]-", # chat     
        "-ZH-AH-" : "-[static/speech/double_phoneme/zhah.wav]-", # chutney    
        "-ZH-AO-" : "-[static/speech/double_phoneme/zhao.wav]-", # chop 
        "-ZH-AW-" : "-[static/speech/double_phoneme/zhaw.wav]-", # chow
        "-ZH-AY-" : "-[static/speech/double_phoneme/zhay.wav]-", # china
        "-ZH-EH-" : "-[static/speech/double_phoneme/zheh.wav]-", # checkers
        "-ZH-ER-" : "-[static/speech/double_phoneme/zher.wav]-", # churn
        "-ZH-EY-" : "-[static/speech/double_phoneme/zhey.wav]-", # change
        "-ZH-IH-" : "-[static/speech/double_phoneme/zhih.wav]-", # ching
        "-ZH-IY-" : "-[static/speech/double_phoneme/zhiy.wav]-", # cheese
        "-ZH-OW-" : "-[static/speech/double_phoneme/zhow.wav]-", # choke
        "-ZH-OY-" : "-[static/speech/double_phoneme/zhoy.wav]-", # choice
        "-ZH-UH-" : "-[static/speech/double_phoneme/zhuh.wav]-", # chuck
        "-ZH-UW-" : "-[static/speech/double_phoneme/zhuw.wav]-" # chew     
        }
