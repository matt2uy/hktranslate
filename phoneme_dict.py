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

# consonant -> vowel
hk_audio_phoneme_combo_beginnings = {
        "-B-AA-" : "-[static/speech/double_phoneme/baa.wav]-", # bow
        "-B-AE-" : "-[static/speech/double_phoneme/bae.wav]-", # bat
        "-B-AH-" : "-[static/speech/double_phoneme/baa.wav]-", # bow    
        "-B-AO-" : "-[static/speech/double_phoneme/baa.wav]-", # bow
        "-B-AW-" : "-[static/speech/double_phoneme/baa.wav]-", # bow
        "-B-AY-" : "-[static/speech/double_phoneme/bay.wav]-", # buy - baai
        "-B-EH-" : "-[static/speech/double_phoneme/beh.wav]-", # ben
        "-B-ER-" : "-[static/speech/double_phoneme/ber.wav]-", # bat - ba
        "-B-EY-" : "-[static/speech/double_phoneme/bey.wav]-", # bait
        "-B-IH-" : "-[static/speech/double_phoneme/bih.wav]-", # bit
        "-B-IY-" : "-[static/speech/double_phoneme/bey.wav]-", # bait
        "-B-OW-" : "-[static/speech/double_phoneme/bow.wav]-", # go
        "-B-OY-" : "-[static/speech/double_phoneme/boy.wav]-", # choice - choiee
        "-B-UH-" : "-[static/speech/double_phoneme/buh.wav]-", # chuck
        "-B-UW-" : "-[static/speech/double_phoneme/buw.wav]-", # few

        "-CH-AA-" : "-[static/speech/double_phoneme/chaa.wav]-",     
        "-CH-AE-" : "-[static/speech/double_phoneme/chae.wav]-",  
        "-CH-AH-" : "-[static/speech/double_phoneme/chaa.wav]-",   
        "-CH-AO-" : "-[static/speech/double_phoneme/chaa.wav]-",
        "-CH-AW-" : "-[static/speech/double_phoneme/chaa.wav]-",
        "-CH-AY-" : "-[static/speech/double_phoneme/chay.wav]-",
        "-CH-EH-" : "-[static/speech/double_phoneme/cheh.wav]-",
        "-CH-ER-" : "-[static/speech/double_phoneme/cher.wav]-",
        "-CH-EY-" : "-[static/speech/double_phoneme/chey.wav]-",
        "-CH-IH-" : "-[static/speech/double_phoneme/chih.wav]-",
        "-CH-IY-" : "-[static/speech/double_phoneme/chey.wav]-",
        "-CH-OW-" : "-[static/speech/double_phoneme/chou.wav]-",
        "-CH-OY-" : "-[static/speech/double_phoneme/choy.wav]-",
        "-CH-UH-" : "-[static/speech/double_phoneme/chuh.wav]-",
        "-CH-UW-" : "-[static/speech/double_phoneme/chuw.wav]-",
       
        "-DH-AA-" : "-[static/speech/double_phoneme/daa.wav]-",     
        "-DH-AE-" : "-[static/speech/double_phoneme/dae.wav]-",     
        "-DH-AH-" : "-[static/speech/double_phoneme/daa.wav]-",    
        "-DH-AO-" : "-[static/speech/double_phoneme/daa.wav]-",
        "-DH-AW-" : "-[static/speech/double_phoneme/daa.wav]-",
        "-DH-AY-" : "-[static/speech/double_phoneme/day.wav]-",
        "-DH-EH-" : "-[static/speech/double_phoneme/deh.wav]-",
        "-DH-ER-" : "-[static/speech/double_phoneme/der.wav]-",
        "-DH-EY-" : "-[static/speech/double_phoneme/dey.wav]-",
        "-DH-IH-" : "-[static/speech/double_phoneme/dih.wav]-",
        "-DH-IY-" : "-[static/speech/double_phoneme/dey.wav]-",
        "-DH-OW-" : "-[static/speech/double_phoneme/dow.wav]-",
        "-DH-OY-" : "-[static/speech/double_phoneme/doy.wav]-",
        "-DH-UH-" : "-[static/speech/double_phoneme/duh.wav]-",
        "-DH-UW-" : "-[static/speech/double_phoneme/duw.wav]-",

        "-D-AA-" : "-[static/speech/double_phoneme/daa.wav]-", 
        "-D-AE-" : "-[static/speech/double_phoneme/dae.wav]-",     
        "-D-AH-" : "-[static/speech/double_phoneme/daa.wav]-",   
        "-D-AO-" : "-[static/speech/double_phoneme/daa.wav]-", 
        "-D-AW-" : "-[static/speech/double_phoneme/daa.wav]-",
        "-D-AY-" : "-[static/speech/double_phoneme/day.wav]-",
        "-D-EH-" : "-[static/speech/double_phoneme/deh.wav]-",
        "-D-ER-" : "-[static/speech/double_phoneme/der.wav]-",
        "-D-EY-" : "-[static/speech/double_phoneme/dey.wav]-",
        "-D-IH-" : "-[static/speech/double_phoneme/dih.wav]-",
        "-D-IY-" : "-[static/speech/double_phoneme/dey.wav]-",
        "-D-OW-" : "-[static/speech/double_phoneme/dow.wav]-",
        "-D-OY-" : "-[static/speech/double_phoneme/doy.wav]-",
        "-D-UH-" : "-[static/speech/double_phoneme/duh.wav]-",
        "-D-UW-" : "-[static/speech/double_phoneme/duw.wav]-",

        "-F-AA-" : "-[static/speech/double_phoneme/faa.wav]-",
        "-F-AE-" : "-[static/speech/double_phoneme/fae.wav]-",  
        "-F-AH-" : "-[static/speech/double_phoneme/faa.wav]-",    
        "-F-AO-" : "-[static/speech/double_phoneme/faa.wav]-",
        "-F-AW-" : "-[static/speech/double_phoneme/faa.wav]-",
        "-F-AY-" : "-[static/speech/double_phoneme/fay.wav]-",
        "-F-EH-" : "-[static/speech/double_phoneme/feh.wav]-",
        "-F-ER-" : "-[static/speech/double_phoneme/fer.wav]-",
        "-F-EY-" : "-[static/speech/double_phoneme/fey.wav]-",
        "-F-IH-" : "-[static/speech/double_phoneme/fih.wav]-",
        "-F-IY-" : "-[static/speech/double_phoneme/fey.wav]-", 
        "-F-OW-" : "-[static/speech/double_phoneme/fow.wav]-",
        "-F-OY-" : "-[static/speech/double_phoneme/foy.wav]-",
        "-F-UH-" : "-[static/speech/double_phoneme/fuh.wav]-",
        "-F-UW-" : "-[static/speech/double_phoneme/fuw.wav]-",
       
        "-G-AA-" : "-[static/speech/double_phoneme/gaa.wav]-",     
        "-G-AE-" : "-[static/speech/double_phoneme/gae.wav]-", 
        "-G-AH-" : "-[static/speech/double_phoneme/gaa.wav]-",   
        "-G-AO-" : "-[static/speech/double_phoneme/gaa.wav]-",
        "-G-AW-" : "-[static/speech/double_phoneme/gaa.wav]-",
        "-G-AY-" : "-[static/speech/double_phoneme/gay.wav]-", 
        "-G-EH-" : "-[static/speech/double_phoneme/geh.wav]-",
        "-G-ER-" : "-[static/speech/double_phoneme/ger.wav]-",
        "-G-EY-" : "-[static/speech/double_phoneme/gey.wav]-",
        "-G-IH-" : "-[static/speech/double_phoneme/gih.wav]-",
        "-G-IY-" : "-[static/speech/double_phoneme/gey.wav]-",
        "-G-OW-" : "-[static/speech/double_phoneme/gow.wav]-", 
        "-G-OY-" : "-[static/speech/double_phoneme/goy.wav]-",
        "-G-UH-" : "-[static/speech/double_phoneme/guh.wav]-", 
        "-G-UW-" : "-[static/speech/double_phoneme/guw.wav]-",

        "-HH-AA-" : "-[static/speech/double_phoneme/hhaa.wav]-",      
        "-HH-AE-" : "-[static/speech/double_phoneme/hhae.wav]-",    
        "-HH-AH-" : "-[static/speech/double_phoneme/hhaa.wav]-",    
        "-HH-AO-" : "-[static/speech/double_phoneme/hhaa.wav]-",
        "-HH-AW-" : "-[static/speech/double_phoneme/hhaa.wav]-",
        "-HH-AY-" : "-[static/speech/double_phoneme/hhay.wav]-",
        "-HH-EH-" : "-[static/speech/double_phoneme/hheh.wav]-",
        "-HH-ER-" : "-[static/speech/double_phoneme/hher.wav]-", 
        "-HH-EY-" : "-[static/speech/double_phoneme/hhey.wav]-",
        "-HH-IH-" : "-[static/speech/double_phoneme/hhih.wav]-", 
        "-HH-IY-" : "-[static/speech/double_phoneme/hhey.wav]-",
        "-HH-OW-" : "-[static/speech/double_phoneme/hhow.wav]-",
        "-HH-OY-" : "-[static/speech/double_phoneme/hhoy.wav]-",
        "-HH-UH-" : "-[static/speech/double_phoneme/hhuh.wav]-",
        "-HH-UW-" : "-[static/speech/double_phoneme/hhuw.wav]-", 

        "-JH-AA-" : "-[static/speech/double_phoneme/jaa.wav]-",
        "-JH-AE-" : "-[static/speech/double_phoneme/jae.wav]-", 
        "-JH-AH-" : "-[static/speech/double_phoneme/jaa.wav]-",  
        "-JH-AO-" : "-[static/speech/double_phoneme/jaa.wav]-", 
        "-JH-AW-" : "-[static/speech/double_phoneme/jaa.wav]-", 
        "-JH-AY-" : "-[static/speech/double_phoneme/jay.wav]-", 
        "-JH-EH-" : "-[static/speech/double_phoneme/jeh.wav]-",
        "-JH-ER-" : "-[static/speech/double_phoneme/jer.wav]-", 
        "-JH-EY-" : "-[static/speech/double_phoneme/jey.wav]-",
        "-JH-IH-" : "-[static/speech/double_phoneme/jih.wav]-",
        "-JH-IY-" : "-[static/speech/double_phoneme/jey.wav]-",
        "-JH-OW-" : "-[static/speech/double_phoneme/jow.wav]-",
        "-JH-OY-" : "-[static/speech/double_phoneme/joy.wav]-",
        "-JH-UH-" : "-[static/speech/double_phoneme/juh.wav]-", 
        "-JH-UW-" : "-[static/speech/double_phoneme/juw.wav]-",

        "-K-AA-" : "-[static/speech/double_phoneme/kaa.wav]-",     
        "-K-AE-" : "-[static/speech/double_phoneme/kae.wav]-", 
        "-K-AH-" : "-[static/speech/double_phoneme/kaa.wav]-",  
        "-K-AO-" : "-[static/speech/double_phoneme/kaa.wav]-",
        "-K-AW-" : "-[static/speech/double_phoneme/kaa.wav]-",
        "-K-AY-" : "-[static/speech/double_phoneme/kay.wav]-",
        "-K-EH-" : "-[static/speech/double_phoneme/keh.wav]-", 
        "-K-ER-" : "-[static/speech/double_phoneme/ker.wav]-",
        "-K-EY-" : "-[static/speech/double_phoneme/key.wav]-",
        "-K-IH-" : "-[static/speech/double_phoneme/kih.wav]-",
        "-K-IY-" : "-[static/speech/double_phoneme/key.wav]-",
        "-K-OW-" : "-[static/speech/double_phoneme/kow.wav]-", 
        "-K-OY-" : "-[static/speech/double_phoneme/koy.wav]-",
        "-K-UH-" : "-[static/speech/double_phoneme/kuh.wav]-",
        "-K-UW-" : "-[static/speech/double_phoneme/kuw.wav]-", 

        "-L-AA-" : "-[static/speech/double_phoneme/laa.wav]-",     
        "-L-AE-" : "-[static/speech/double_phoneme/lae.wav]-",    
        "-L-AH-" : "-[static/speech/double_phoneme/laa.wav]-",   
        "-L-AO-" : "-[static/speech/double_phoneme/laa.wav]-", 
        "-L-AW-" : "-[static/speech/double_phoneme/laa.wav]-",
        "-L-AY-" : "-[static/speech/double_phoneme/lay.wav]-", 
        "-L-EH-" : "-[static/speech/double_phoneme/leh.wav]-", 
        "-L-ER-" : "-[static/speech/double_phoneme/ler.wav]-", 
        "-L-EY-" : "-[static/speech/double_phoneme/ley.wav]-", 
        "-L-IH-" : "-[static/speech/double_phoneme/lih.wav]-", 
        "-L-IY-" : "-[static/speech/double_phoneme/ley.wav]-", 
        "-L-OW-" : "-[static/speech/double_phoneme/low.wav]-", 
        "-L-OY-" : "-[static/speech/double_phoneme/loy.wav]-", 
        "-L-UH-" : "-[static/speech/double_phoneme/luh.wav]-", 
        "-L-UW-" : "-[static/speech/double_phoneme/luw.wav]-", 

        "-M-AA-" : "-[static/speech/double_phoneme/maa.wav]-",      
        "-M-AE-" : "-[static/speech/double_phoneme/mae.wav]-",      
        "-M-AH-" : "-[static/speech/double_phoneme/maa.wav]-",     
        "-M-AO-" : "-[static/speech/double_phoneme/maa.wav]-",  
        "-M-AW-" : "-[static/speech/double_phoneme/maa.wav]-", 
        "-M-AY-" : "-[static/speech/double_phoneme/may.wav]-", 
        "-M-EH-" : "-[static/speech/double_phoneme/meh.wav]-", 
        "-M-ER-" : "-[static/speech/double_phoneme/mer.wav]-", 
        "-M-EY-" : "-[static/speech/double_phoneme/mey.wav]-", 
        "-M-IH-" : "-[static/speech/double_phoneme/mih.wav]-", 
        "-M-IY-" : "-[static/speech/double_phoneme/mey.wav]-", 
        "-M-OW-" : "-[static/speech/double_phoneme/mow.wav]-", 
        "-M-OY-" : "-[static/speech/double_phoneme/moy.wav]-", 
        "-M-UH-" : "-[static/speech/double_phoneme/muh.wav]-", 
        "-M-UW-" : "-[static/speech/double_phoneme/muw.wav]-", 
     
        "-N-AA-" : "-[static/speech/double_phoneme/naa.wav]-",      
        "-N-AE-" : "-[static/speech/double_phoneme/nae.wav]-",      
        "-N-AH-" : "-[static/speech/double_phoneme/naa.wav]-",     
        "-N-AO-" : "-[static/speech/double_phoneme/naa.wav]-",  
        "-N-AW-" : "-[static/speech/double_phoneme/naa.wav]-", 
        "-N-AY-" : "-[static/speech/double_phoneme/nay.wav]-", 
        "-N-EH-" : "-[static/speech/double_phoneme/neh.wav]-", 
        "-N-ER-" : "-[static/speech/double_phoneme/ner.wav]-", 
        "-N-EY-" : "-[static/speech/double_phoneme/ney.wav]-", 
        "-N-IH-" : "-[static/speech/double_phoneme/nih.wav]-", 
        "-N-IY-" : "-[static/speech/double_phoneme/ney.wav]-", 
        "-N-OW-" : "-[static/speech/double_phoneme/now.wav]-", 
        "-N-OY-" : "-[static/speech/double_phoneme/noy.wav]-", 
        "-N-UH-" : "-[static/speech/double_phoneme/nuh.wav]-", 
        "-N-UW-" : "-[static/speech/double_phoneme/nuw.wav]-", 

        "-P-AA-" : "-[static/speech/double_phoneme/paa.wav]-",      
        "-P-AE-" : "-[static/speech/double_phoneme/pae.wav]-",      
        "-P-AH-" : "-[static/speech/double_phoneme/paa.wav]-",     
        "-P-AO-" : "-[static/speech/double_phoneme/paa.wav]-",  
        "-P-AW-" : "-[static/speech/double_phoneme/paa.wav]-", 
        "-P-AY-" : "-[static/speech/double_phoneme/pay.wav]-", 
        "-P-EH-" : "-[static/speech/double_phoneme/peh.wav]-", 
        "-P-ER-" : "-[static/speech/double_phoneme/.wav]-", 
        "-P-EY-" : "-[static/speech/double_phoneme/pey.wav]-", 
        "-P-IH-" : "-[static/speech/double_phoneme/pih.wav]-", 
        "-P-IY-" : "-[static/speech/double_phoneme/pey.wav]-", 
        "-P-OW-" : "-[static/speech/double_phoneme/pow.wav]-", 
        "-P-OY-" : "-[static/speech/double_phoneme/poy.wav]-", 
        "-P-UH-" : "-[static/speech/double_phoneme/puh.wav]-", 
        "-P-UW-" : "-[static/speech/double_phoneme/puw.wav]-", 

        "-R-AA-" : "-[static/speech/double_phoneme/raa.wav]-",      
        "-R-AE-" : "-[static/speech/double_phoneme/rae.wav]-",      
        "-R-AH-" : "-[static/speech/double_phoneme/raa.wav]-",     
        "-R-AO-" : "-[static/speech/double_phoneme/raa.wav]-",  
        "-R-AW-" : "-[static/speech/double_phoneme/raa.wav]-", 
        "-R-AY-" : "-[static/speech/double_phoneme/ray.wav]-", 
        "-R-EH-" : "-[static/speech/double_phoneme/reh.wav]-", 
        "-R-ER-" : "-[static/speech/double_phoneme/rer.wav]-", 
        "-R-EY-" : "-[static/speech/double_phoneme/rey.wav]-", 
        "-R-IH-" : "-[static/speech/double_phoneme/rih.wav]-", 
        "-R-IY-" : "-[static/speech/double_phoneme/rey.wav]-", 
        "-R-OW-" : "-[static/speech/double_phoneme/row.wav]-", 
        "-R-OY-" : "-[static/speech/double_phoneme/roy.wav]-", 
        "-R-UH-" : "-[static/speech/double_phoneme/ruh.wav]-", 
        "-R-UW-" : "-[static/speech/double_phoneme/ruw.wav]-", 

        "-S-AA-" : "-[static/speech/double_phoneme/saa.wav]-",      
        "-S-AE-" : "-[static/speech/double_phoneme/sae.wav]-",      
        "-S-AH-" : "-[static/speech/double_phoneme/saa.wav]-",     
        "-S-AO-" : "-[static/speech/double_phoneme/saa.wav]-",  
        "-S-AW-" : "-[static/speech/double_phoneme/saa.wav]-", 
        "-S-AY-" : "-[static/speech/double_phoneme/say.wav]-", 
        "-S-EH-" : "-[static/speech/double_phoneme/seh.wav]-", 
        "-S-ER-" : "-[static/speech/double_phoneme/ser.wav]-", 
        "-S-EY-" : "-[static/speech/double_phoneme/sey.wav]-", 
        "-S-IH-" : "-[static/speech/double_phoneme/sih.wav]-", 
        "-S-IY-" : "-[static/speech/double_phoneme/sey.wav]-", 
        "-S-OW-" : "-[static/speech/double_phoneme/sow.wav]-", 
        "-S-OY-" : "-[static/speech/double_phoneme/soy.wav]-", 
        "-S-UH-" : "-[static/speech/double_phoneme/suh.wav]-", 
        "-S-UW-" : "-[static/speech/double_phoneme/suw.wav]-", 
        
        "-SH-AA-" : "-[static/speech/double_phoneme/shaa.wav]-",      
        "-SH-AE-" : "-[static/speech/double_phoneme/shae.wav]-",      
        "-SH-AH-" : "-[static/speech/double_phoneme/shaa.wav]-",     
        "-SH-AO-" : "-[static/speech/double_phoneme/shaa.wav]-",  
        "-SH-AW-" : "-[static/speech/double_phoneme/shaa.wav]-", 
        "-SH-AY-" : "-[static/speech/double_phoneme/shay.wav]-", 
        "-SH-EH-" : "-[static/speech/double_phoneme/sheh.wav]-", 
        "-SH-ER-" : "-[static/speech/double_phoneme/sher.wav]-", 
        "-SH-EY-" : "-[static/speech/double_phoneme/shey.wav]-", 
        "-SH-IH-" : "-[static/speech/double_phoneme/shih.wav]-", 
        "-SH-IY-" : "-[static/speech/double_phoneme/shey.wav]-", 
        "-SH-OW-" : "-[static/speech/double_phoneme/show.wav]-", 
        "-SH-OY-" : "-[static/speech/double_phoneme/shoy.wav]-", 
        "-SH-UH-" : "-[static/speech/double_phoneme/shuh.wav]-", 
        "-SH-UW-" : "-[static/speech/double_phoneme/shuw.wav]-", 

        "-T-AA-" : "-[static/speech/double_phoneme/taa.wav]-",      
        "-T-AE-" : "-[static/speech/double_phoneme/tae.wav]-",      
        "-T-AH-" : "-[static/speech/double_phoneme/taa.wav]-",     
        "-T-AO-" : "-[static/speech/double_phoneme/taa.wav]-",  
        "-T-AW-" : "-[static/speech/double_phoneme/taa.wav]-", 
        "-T-AY-" : "-[static/speech/double_phoneme/tay.wav]-", 
        "-T-EH-" : "-[static/speech/double_phoneme/teh.wav]-", 
        "-T-ER-" : "-[static/speech/double_phoneme/ter.wav]-", 
        "-T-EY-" : "-[static/speech/double_phoneme/tey.wav]-", 
        "-T-IH-" : "-[static/speech/double_phoneme/tih.wav]-", 
        "-T-IY-" : "-[static/speech/double_phoneme/tey.wav]-", 
        "-T-OW-" : "-[static/speech/double_phoneme/tow.wav]-", 
        "-T-OY-" : "-[static/speech/double_phoneme/toy.wav]-", 
        "-T-UH-" : "-[static/speech/double_phoneme/tuh.wav]-", 
        "-T-UW-" : "-[static/speech/double_phoneme/tuw.wav]-", 
        
        "-TH-AA-" : "-[static/speech/double_phoneme/thaa.wav]-",      
        "-TH-AE-" : "-[static/speech/double_phoneme/thae.wav]-",      
        "-TH-AH-" : "-[static/speech/double_phoneme/thaa.wav]-",     
        "-TH-AO-" : "-[static/speech/double_phoneme/thaa.wav]-",  
        "-TH-AW-" : "-[static/speech/double_phoneme/thaa.wav]-", 
        "-TH-AY-" : "-[static/speech/double_phoneme/thay.wav]-", 
        "-TH-EH-" : "-[static/speech/double_phoneme/theh.wav]-", 
        "-TH-ER-" : "-[static/speech/double_phoneme/ther.wav]-", 
        "-TH-IH-" : "-[static/speech/double_phoneme/thih.wav]-", 
        "-TH-IY-" : "-[static/speech/double_phoneme/they.wav]-", 
        "-TH-OW-" : "-[static/speech/double_phoneme/thow.wav]-", 
        "-TH-OY-" : "-[static/speech/double_phoneme/thoy.wav]-", 
        "-TH-UH-" : "-[static/speech/double_phoneme/thuh.wav]-", 
        "-TH-UW-" : "-[static/speech/double_phoneme/thuw.wav]-", 

        "-V-AA-" : "-[static/speech/double_phoneme/vaa.wav]-",      
        "-V-AE-" : "-[static/speech/double_phoneme/vae.wav]-",      
        "-V-AH-" : "-[static/speech/double_phoneme/vaa.wav]-",     
        "-V-AO-" : "-[static/speech/double_phoneme/vaa.wav]-",  
        "-V-AW-" : "-[static/speech/double_phoneme/vaa.wav]-", 
        "-V-AY-" : "-[static/speech/double_phoneme/vay.wav]-", 
        "-V-EH-" : "-[static/speech/double_phoneme/veh.wav]-", 
        "-V-ER-" : "-[static/speech/double_phoneme/ver.wav]-", 
        "-V-EY-" : "-[static/speech/double_phoneme/vey.wav]-", 
        "-V-IH-" : "-[static/speech/double_phoneme/vih.wav]-", 
        "-V-IY-" : "-[static/speech/double_phoneme/vey.wav]-", 
        "-V-OW-" : "-[static/speech/double_phoneme/vow.wav]-", 
        "-V-OY-" : "-[static/speech/double_phoneme/voy.wav]-", 
        "-V-UH-" : "-[static/speech/double_phoneme/vuh.wav]-", 
        "-V-UW-" : "-[static/speech/double_phoneme/vuw.wav]-", 

        "-W-AA-" : "-[static/speech/double_phoneme/waa.wav]-",      
        "-W-AE-" : "-[static/speech/double_phoneme/wae.wav]-",      
        "-W-AH-" : "-[static/speech/double_phoneme/waa.wav]-",     
        "-W-AO-" : "-[static/speech/double_phoneme/waa.wav]-",  
        "-W-AW-" : "-[static/speech/double_phoneme/waa.wav]-", 
        "-W-AY-" : "-[static/speech/double_phoneme/way.wav]-", 
        "-W-EH-" : "-[static/speech/double_phoneme/weh.wav]-", 
        "-W-ER-" : "-[static/speech/double_phoneme/wer.wav]-", 
        "-W-EY-" : "-[static/speech/double_phoneme/wey.wav]-", 
        "-W-IH-" : "-[static/speech/double_phoneme/wih.wav]-", 
        "-W-IY-" : "-[static/speech/double_phoneme/wey.wav]-", 
        "-W-OW-" : "-[static/speech/double_phoneme/wow.wav]-", 
        "-W-OY-" : "-[static/speech/double_phoneme/woy.wav]-", 
        "-W-UH-" : "-[static/speech/double_phoneme/wuh.wav]-", 
        "-W-UW-" : "-[static/speech/double_phoneme/wuw.wav]-", 

        "-Y-AA-" : "-[static/speech/double_phoneme/yaa.wav]-",      
        "-Y-AE-" : "-[static/speech/double_phoneme/yae.wav]-",      
        "-Y-AH-" : "-[static/speech/double_phoneme/yaa.wav]-",     
        "-Y-AO-" : "-[static/speech/double_phoneme/yaa.wav]-",  
        "-Y-AW-" : "-[static/speech/double_phoneme/yaa.wav]-", 
        "-Y-AY-" : "-[static/speech/double_phoneme/yay.wav]-", 
        "-Y-EH-" : "-[static/speech/double_phoneme/yeh.wav]-", 
        "-Y-ER-" : "-[static/speech/double_phoneme/yer.wav]-", 
        "-Y-EY-" : "-[static/speech/double_phoneme/yey.wav]-", 
        "-Y-IH-" : "-[static/speech/double_phoneme/yih.wav]-", 
        "-Y-IY-" : "-[static/speech/double_phoneme/yey.wav]-", 
        "-Y-OW-" : "-[static/speech/double_phoneme/yow.wav]-", 
        "-Y-OY-" : "-[static/speech/double_phoneme/yoy.wav]-", 
        "-Y-UH-" : "-[static/speech/double_phoneme/yuh.wav]-", 
        "-Y-UW-" : "-[static/speech/double_phoneme/yuw.wav]-", 

        "-Z-AA-" : "-[static/speech/double_phoneme/zaa.wav]-",      
        "-Z-AE-" : "-[static/speech/double_phoneme/zae.wav]-",      
        "-Z-AH-" : "-[static/speech/double_phoneme/zaa.wav]-",     
        "-Z-AO-" : "-[static/speech/double_phoneme/zaa.wav]-",  
        "-Z-AW-" : "-[static/speech/double_phoneme/zaa.wav]-", 
        "-Z-AY-" : "-[static/speech/double_phoneme/zay.wav]-", 
        "-Z-EH-" : "-[static/speech/double_phoneme/zeh.wav]-", 
        "-Z-ER-" : "-[static/speech/double_phoneme/zer.wav]-", 
        "-Z-EY-" : "-[static/speech/double_phoneme/zey.wav]-", 
        "-Z-IH-" : "-[static/speech/double_phoneme/zih.wav]-", 
        "-Z-IY-" : "-[static/speech/double_phoneme/zey.wav]-", 
        "-Z-OW-" : "-[static/speech/double_phoneme/zow.wav]-", 
        "-Z-OY-" : "-[static/speech/double_phoneme/zoy.wav]-", 
        "-Z-UH-" : "-[static/speech/double_phoneme/zuh.wav]-", 
        "-Z-UW-" : "-[static/speech/double_phoneme/zuw.wav]-", 

        "-ZH-AA-" : "-[static/speech/double_phoneme/zhaa.wav]-",      
        "-ZH-AE-" : "-[static/speech/double_phoneme/zhae.wav]-",      
        "-ZH-AH-" : "-[static/speech/double_phoneme/zhaa.wav]-",     
        "-ZH-AO-" : "-[static/speech/double_phoneme/zhaa.wav]-",  
        "-ZH-AW-" : "-[static/speech/double_phoneme/zhaa.wav]-", 
        "-ZH-AY-" : "-[static/speech/double_phoneme/zhay.wav]-", 
        "-ZH-EH-" : "-[static/speech/double_phoneme/zheh.wav]-", 
        "-ZH-ER-" : "-[static/speech/double_phoneme/zher.wav]-", 
        "-ZH-EY-" : "-[static/speech/double_phoneme/zhey.wav]-", 
        "-ZH-IH-" : "-[static/speech/double_phoneme/zhih.wav]-", 
        "-ZH-IY-" : "-[static/speech/double_phoneme/zhey.wav]-", 
        "-ZH-OW-" : "-[static/speech/double_phoneme/zhow.wav]-", 
        "-ZH-OY-" : "-[static/speech/double_phoneme/zhoy.wav]-", 
        "-ZH-UH-" : "-[static/speech/double_phoneme/zhuh.wav]-", 
        "-ZH-UW-" : "-[static/speech/double_phoneme/zhuw.wav]-"      
        }

# vowel -> consonant
hk_audio_phoneme_combo_endings = {
        "-AA-B-" : '-AA-[static/speech/double_phoneme/aab.wav]-', # ode
        "-AE-B-" : '-AE-[static/speech/double_phoneme/aeb.wav]-', # ab
        "-AH-B-" : '-AH-[static/speech/double_phoneme/aab.wav]-', # ode     
        "-AO-B-" : '-AO-[static/speech/double_phoneme/aab.wav]-', # ode
        "-AW-B-" : '-AW-[static/speech/double_phoneme/aab.wav]-', # ode
        "-AY-B-" : '-AY-[static/speech/double_phoneme/ayb.wav]-', # hide - haaide
        "-EH-B-" : '-EH-[static/speech/double_phoneme/ehb.wav]-', # ebb
        "-ER-B-" : '-EH-[static/speech/double_phoneme/erb.wav]-', # ebb - sharp
        "-EY-B-" : '-EY-[static/speech/double_phoneme/eyb.wav]-', # aid
        "-IH-B-" : '-IH-[static/speech/double_phoneme/ihb.wav]-', # ing - sharp
        "-IY-B-" : '-IY-[static/speech/double_phoneme/eyb.wav]-', # aid
        "-OW-B-" : '-OW-[static/speech/double_phoneme/owb.wav]-', # oat
        "-OY-B-" : '-OY-[static/speech/double_phoneme/oyb.wav]-', # joy - joiee
        "-UH-B-" : '-UH-[static/speech/double_phoneme/uhb.wav]-', # bud  
        "-UW-B-" : '-UW-[static/speech/double_phoneme/uwb.wav]-', # oob

        "-AA-CH-" : '-AA-[static/speech/double_phoneme/aach.wav]-', 
        "-AE-CH-" : '-AE-[static/speech/double_phoneme/aech.wav]-', 
        "-AH-CH-" : '-AH-[static/speech/double_phoneme/aach.wav]-',      
        "-AO-CH-" : '-AO-[static/speech/double_phoneme/aach.wav]-', 
        "-AW-CH-" : '-AW-[static/speech/double_phoneme/aach.wav]-', 
        "-AY-CH-" : '-AY-[static/speech/double_phoneme/aych.wav]-', 
        "-EH-CH-" : '-EH-[static/speech/double_phoneme/ehch.wav]-', 
        "-ER-CH-" : '-EH-[static/speech/double_phoneme/erch.wav]-',  
        "-EY-CH-" : '-EY-[static/speech/double_phoneme/eych.wav]-', 
        "-IH-CH-" : '-IH-[static/speech/double_phoneme/ihch.wav]-', 
        "-IY-CH-" : '-IY-[static/speech/double_phoneme/eych.wav]-', 
        "-OW-CH-" : '-OW-[static/speech/double_phoneme/owch.wav]-', 
        "-OY-CH-" : '-OY-[static/speech/double_phoneme/oych.wav]-', 
        "-UH-CH-" : '-UH-[static/speech/double_phoneme/uhch.wav]-',   
        "-UW-CH-" : '-UW-[static/speech/double_phoneme/uwch.wav]-',

        "-AA-D-" : '-AA-[static/speech/double_phoneme/aad.wav]-', 
        "-AE-D-" : '-AE-[static/speech/double_phoneme/aed.wav]-', 
        "-AH-D-" : '-AH-[static/speech/double_phoneme/aad.wav]-',      
        "-AO-D-" : '-AO-[static/speech/double_phoneme/aad.wav]-', 
        "-AW-D-" : '-AW-[static/speech/double_phoneme/aad.wav]-', 
        "-AY-D-" : '-AY-[static/speech/double_phoneme/ayd.wav]-', 
        "-EH-D-" : '-EH-[static/speech/double_phoneme/ehd.wav]-', 
        "-ER-D-" : '-EH-[static/speech/double_phoneme/erd.wav]-',  
        "-EY-D-" : '-EY-[static/speech/double_phoneme/eyd.wav]-', 
        "-IH-D-" : '-IH-[static/speech/double_phoneme/ihd.wav]-', 
        "-IY-D-" : '-IY-[static/speech/double_phoneme/eyd.wav]-', 
        "-OW-D-" : '-OW-[static/speech/double_phoneme/owd.wav]-', 
        "-OY-D-" : '-OY-[static/speech/double_phoneme/oyd.wav]-', 
        "-UH-D-" : '-UH-[static/speech/double_phoneme/uhd.wav]-',   
        "-UW-D-" : '-UW-[static/speech/double_phoneme/uwd.wav]-',

        "-AA-F-" : '-AA-[static/speech/double_phoneme/aaf.wav]-', 
        "-AE-F-" : '-AE-[static/speech/double_phoneme/aef.wav]-', 
        "-AH-F-" : '-AH-[static/speech/double_phoneme/aaf.wav]-',      
        "-AO-F-" : '-AO-[static/speech/double_phoneme/aaf.wav]-', 
        "-AW-F-" : '-AW-[static/speech/double_phoneme/aaf.wav]-', 
        "-AY-F-" : '-AY-[static/speech/double_phoneme/ayf.wav]-', 
        "-EH-F-" : '-EH-[static/speech/double_phoneme/ehf.wav]-', 
        "-ER-F-" : '-EH-[static/speech/double_phoneme/erf.wav]-',  
        "-EY-F-" : '-EY-[static/speech/double_phoneme/eyf.wav]-', 
        "-IH-F-" : '-IH-[static/speech/double_phoneme/ihf.wav]-', 
        "-IY-F-" : '-IY-[static/speech/double_phoneme/eyf.wav]-', 
        "-OW-F-" : '-OW-[static/speech/double_phoneme/owf.wav]-', 
        "-OY-F-" : '-OY-[static/speech/double_phoneme/oyf.wav]-', 
        "-UH-F-" : '-UH-[static/speech/double_phoneme/uhf.wav]-',   
        "-UW-F-" : '-UW-[static/speech/double_phoneme/uwf.wav]-',

        "-AA-G-" : '-AA-[static/speech/double_phoneme/aag.wav]-', 
        "-AE-G-" : '-AE-[static/speech/double_phoneme/aeg.wav]-', 
        "-AH-G-" : '-AH-[static/speech/double_phoneme/aag.wav]-',      
        "-AO-G-" : '-AO-[static/speech/double_phoneme/aag.wav]-', 
        "-AW-G-" : '-AW-[static/speech/double_phoneme/aag.wav]-', 
        "-AY-G-" : '-AY-[static/speech/double_phoneme/ayg.wav]-', 
        "-EH-G-" : '-EH-[static/speech/double_phoneme/ehg.wav]-', 
        "-ER-G-" : '-EH-[static/speech/double_phoneme/erg.wav]-',  
        "-EY-G-" : '-EY-[static/speech/double_phoneme/eyg.wav]-', 
        "-IH-G-" : '-IH-[static/speech/double_phoneme/ihg.wav]-', 
        "-IY-G-" : '-IY-[static/speech/double_phoneme/eyg.wav]-', 
        "-OW-G-" : '-OW-[static/speech/double_phoneme/owg.wav]-', 
        "-OY-G-" : '-OY-[static/speech/double_phoneme/oyg.wav]-', 
        "-UH-G-" : '-UH-[static/speech/double_phoneme/uhg.wav]-',   
        "-UW-G-" : '-UW-[static/speech/double_phoneme/uwg.wav]-',

        "-AA-K-" : '-AA-[static/speech/double_phoneme/aak.wav]-', 
        "-AE-K-" : '-AE-[static/speech/double_phoneme/aek.wav]-', 
        "-AH-K-" : '-AH-[static/speech/double_phoneme/aak.wav]-',      
        "-AO-K-" : '-AO-[static/speech/double_phoneme/aak.wav]-', 
        "-AW-K-" : '-AW-[static/speech/double_phoneme/aak.wav]-', 
        "-AY-K-" : '-AY-[static/speech/double_phoneme/ayk.wav]-', 
        "-EH-K-" : '-EH-[static/speech/double_phoneme/ehk.wav]-', 
        "-ER-K-" : '-EH-[static/speech/double_phoneme/erk.wav]-',  
        "-EY-K-" : '-EY-[static/speech/double_phoneme/eyk.wav]-', 
        "-IH-K-" : '-IH-[static/speech/double_phoneme/ihk.wav]-', 
        "-IY-K-" : '-IY-[static/speech/double_phoneme/eyk.wav]-', 
        "-OW-K-" : '-OW-[static/speech/double_phoneme/owk.wav]-', 
        "-OY-K-" : '-OY-[static/speech/double_phoneme/oyk.wav]-', 
        "-UH-K-" : '-UH-[static/speech/double_phoneme/uhk.wav]-',   
        "-UW-K-" : '-UW-[static/speech/double_phoneme/uwk.wav]-',

        "-AA-L-" : '-AA-[static/speech/double_phoneme/aal.wav]-', 
        "-AE-L-" : '-AE-[static/speech/double_phoneme/ael.wav]-', 
        "-AH-L-" : '-AH-[static/speech/double_phoneme/aal.wav]-',      
        "-AO-L-" : '-AO-[static/speech/double_phoneme/aal.wav]-', 
        "-AW-L-" : '-AW-[static/speech/double_phoneme/aal.wav]-', 
        "-AY-L-" : '-AY-[static/speech/double_phoneme/ayl.wav]-', 
        "-EH-L-" : '-EH-[static/speech/double_phoneme/ehl.wav]-', 
        "-ER-L-" : '-EH-[static/speech/double_phoneme/erl.wav]-',  
        "-EY-L-" : '-EY-[static/speech/double_phoneme/eyl.wav]-', 
        "-IH-L-" : '-IH-[static/speech/double_phoneme/ihl.wav]-', 
        "-IY-L-" : '-IY-[static/speech/double_phoneme/eyl.wav]-', 
        "-OW-L-" : '-OW-[static/speech/double_phoneme/owl.wav]-', 
        "-OY-L-" : '-OY-[static/speech/double_phoneme/oyl.wav]-', 
        "-UH-L-" : '-UH-[static/speech/double_phoneme/uhl.wav]-',   
        "-UW-L-" : '-UW-[static/speech/double_phoneme/uwl.wav]-',

        "-AA-M-" : '-AA-[static/speech/double_phoneme/owm.wav]-', 
        "-AE-M-" : '-AE-[static/speech/double_phoneme/aem.wav]-', 
        "-AH-M-" : '-AH-[static/speech/double_phoneme/owm.wav]-',      
        "-AO-M-" : '-AO-[static/speech/double_phoneme/owm.wav]-', 
        "-AW-M-" : '-AW-[static/speech/double_phoneme/owm.wav]-', 
        "-AY-M-" : '-AY-[static/speech/double_phoneme/aym.wav]-', 
        "-EH-M-" : '-EH-[static/speech/double_phoneme/ehm.wav]-', 
        "-ER-M-" : '-EH-[static/speech/double_phoneme/erm.wav]-',  
        "-EY-M-" : '-EY-[static/speech/double_phoneme/eym.wav]-', 
        "-IH-M-" : '-IH-[static/speech/double_phoneme/ihm.wav]-', 
        "-IY-M-" : '-IY-[static/speech/double_phoneme/eym.wav]-', 
        "-OW-M-" : '-OW-[static/speech/double_phoneme/owm.wav]-', 
        "-OY-M-" : '-OY-[static/speech/double_phoneme/oym.wav]-', 
        "-UH-M-" : '-UH-[static/speech/double_phoneme/uhm.wav]-',   
        "-UW-M-" : '-UW-[static/speech/double_phoneme/uwm.wav]-',

        "-AA-NG-" : '-AA-[static/speech/double_phoneme/aang.wav]-', 
        "-AE-NG-" : '-AE-[static/speech/double_phoneme/aeng.wav]-', 
        "-AH-NG-" : '-AH-[static/speech/double_phoneme/aang.wav]-',      
        "-AO-NG-" : '-AO-[static/speech/double_phoneme/aang.wav]-', 
        "-AW-NG-" : '-AW-[static/speech/double_phoneme/aang.wav]-', 
        "-AY-NG-" : '-AY-[static/speech/double_phoneme/ayng.wav]-', 
        "-EH-NG-" : '-EH-[static/speech/double_phoneme/ehng.wav]-', 
        "-ER-NG-" : '-EH-[static/speech/double_phoneme/erng.wav]-',  
        "-EY-NG-" : '-EY-[static/speech/double_phoneme/eyng.wav]-', 
        "-IH-NG-" : '-IH-[static/speech/double_phoneme/ihng.wav]-', 
        "-IY-NG-" : '-IY-[static/speech/double_phoneme/eyng.wav]-', 
        "-OW-NG-" : '-OW-[static/speech/double_phoneme/owng.wav]-', 
        "-OY-NG-" : '-OY-[static/speech/double_phoneme/oyng.wav]-', 
        "-UH-NG-" : '-UH-[static/speech/double_phoneme/uhng.wav]-',   
        "-UW-NG-" : '-UW-[static/speech/double_phoneme/uwng.wav]-',

        "-AA-N-" : '-AA-[static/speech/double_phoneme/aan.wav]-',  
        "-AE-N-" : '-AE-[static/speech/double_phoneme/aen.wav]-', 
        "-AH-N-" : '-AH-[static/speech/double_phoneme/aan.wav]-',      
        "-AO-N-" : '-AO-[static/speech/double_phoneme/aan.wav]-', 
        "-AW-N-" : '-AW-[static/speech/double_phoneme/aan.wav]-', 
        "-AY-N-" : '-AY-[static/speech/double_phoneme/ayn.wav]-', 
        "-EH-N-" : '-EH-[static/speech/double_phoneme/ehn.wav]-', 
        "-ER-N-" : '-EH-[static/speech/double_phoneme/ern.wav]-',  
        "-EY-N-" : '-EY-[static/speech/double_phoneme/eyn.wav]-', 
        "-IH-N-" : '-IH-[static/speech/double_phoneme/ihn.wav]-', 
        "-IY-N-" : '-IY-[static/speech/double_phoneme/eyn.wav]-', 
        "-OW-N-" : '-OW-[static/speech/double_phoneme/own.wav]-', 
        "-OY-N-" : '-OY-[static/speech/double_phoneme/oyn.wav]-', 
        "-UH-N-" : '-UH-[static/speech/double_phoneme/uhn.wav]-',   
        "-UW-N-" : '-UW-[static/speech/double_phoneme/uwn.wav]-',

        "-AA-P-" : '-AA-[static/speech/double_phoneme/aap.wav]-',  
        "-AE-P-" : '-AE-[static/speech/double_phoneme/aep.wav]-', 
        "-AH-P-" : '-AH-[static/speech/double_phoneme/aap.wav]-',      
        "-AO-P-" : '-AO-[static/speech/double_phoneme/aap.wav]-', 
        "-AW-P-" : '-AW-[static/speech/double_phoneme/aap.wav]-', 
        "-AY-P-" : '-AY-[static/speech/double_phoneme/ayp.wav]-', 
        "-EH-P-" : '-EH-[static/speech/double_phoneme/ehp.wav]-', 
        "-ER-P-" : '-EH-[static/speech/double_phoneme/erp.wav]-',  
        "-EY-P-" : '-EY-[static/speech/double_phoneme/eyp.wav]-', 
        "-IH-P-" : '-IH-[static/speech/double_phoneme/ihp.wav]-', 
        "-IY-P-" : '-IY-[static/speech/double_phoneme/eyp.wav]-', 
        "-OW-P-" : '-OW-[static/speech/double_phoneme/owp.wav]-', 
        "-OY-P-" : '-OY-[static/speech/double_phoneme/oyp.wav]-', 
        "-UH-P-" : '-UH-[static/speech/double_phoneme/uhp.wav]-',   
        "-UW-P-" : '-UW-[static/speech/double_phoneme/uwp.wav]-',

        "-AA-R-" : '-AA-[static/speech/double_phoneme/aar.wav]-',  
        "-AE-R-" : '-AE-[static/speech/double_phoneme/aer.wav]-', 
        "-AH-R-" : '-AH-[static/speech/double_phoneme/aar.wav]-',      
        "-AO-R-" : '-AO-[static/speech/double_phoneme/aar.wav]-', 
        "-AW-R-" : '-AW-[static/speech/double_phoneme/aar.wav]-', 
        "-AY-R-" : '-AY-[static/speech/double_phoneme/ayr.wav]-', 
        "-EH-R-" : '-EH-[static/speech/double_phoneme/ehr.wav]-', 
        "-ER-R-" : '-EH-[static/speech/double_phoneme/eyr.wav]-',  
        "-EY-R-" : '-EY-[static/speech/double_phoneme/eyr.wav]-', 
        "-IH-R-" : '-IH-[static/speech/double_phoneme/ihr.wav]-', 
        "-IY-R-" : '-IY-[static/speech/double_phoneme/eyr.wav]-', 
        "-OW-R-" : '-OW-[static/speech/double_phoneme/owr.wav]-', 
        "-OY-R-" : '-OY-[static/speech/double_phoneme/oyr.wav]-', 
        "-UH-R-" : '-UH-[static/speech/double_phoneme/uhr.wav]-',   
        "-UW-R-" : '-UW-[static/speech/double_phoneme/uwr.wav]-',

        "-AA-S-" : '-AA-[static/speech/double_phoneme/aas.wav]-',  
        "-AE-S-" : '-AE-[static/speech/double_phoneme/aes.wav]-', 
        "-AH-S-" : '-AH-[static/speech/double_phoneme/aas.wav]-',      
        "-AO-S-" : '-AO-[static/speech/double_phoneme/aas.wav]-', 
        "-AW-S-" : '-AW-[static/speech/double_phoneme/aas1.wav]-', 
        "-AY-S-" : '-AY-[static/speech/double_phoneme/ays.wav]-', 
        "-EH-S-" : '-EH-[static/speech/double_phoneme/ehs.wav]-', 
        "-ER-S-" : '-EH-[static/speech/double_phoneme/ers.wav]-',  
        "-EY-S-" : '-EY-[static/speech/double_phoneme/eys.wav]-', 
        "-IH-S-" : '-IH-[static/speech/double_phoneme/ihs.wav]-', 
        "-IY-S-" : '-IY-[static/speech/double_phoneme/eys.wav]-', 
        "-OW-S-" : '-OW-[static/speech/double_phoneme/ows.wav]-', 
        "-OY-S-" : '-OY-[static/speech/double_phoneme/oys.wav]-', 
        "-UH-S-" : '-UH-[static/speech/double_phoneme/uhs.wav]-',   
        "-UW-S-" : '-UW-[static/speech/double_phoneme/uws.wav]-',

        "-AA-SH-" : '-AA-[static/speech/double_phoneme/aash.wav]-',  
        "-AE-SH-" : '-AE-[static/speech/double_phoneme/aesh.wav]-', 
        "-AH-SH-" : '-AH-[static/speech/double_phoneme/aash.wav]-',      
        "-AO-SH-" : '-AO-[static/speech/double_phoneme/aash.wav]-', 
        "-AW-SH-" : '-AW-[static/speech/double_phoneme/aash.wav]-', 
        "-AY-SH-" : '-AY-[static/speech/double_phoneme/aysh.wav]-', 
        "-EH-SH-" : '-EH-[static/speech/double_phoneme/ehsh.wav]-', 
        "-ER-SH-" : '-EH-[static/speech/double_phoneme/ersh.wav]-',  
        "-EY-SH-" : '-EY-[static/speech/double_phoneme/eysh.wav]-', 
        "-IH-SH-" : '-IH-[static/speech/double_phoneme/ihsh.wav]-', 
        "-IY-SH-" : '-IY-[static/speech/double_phoneme/eysh.wav]-', 
        "-OW-SH-" : '-OW-[static/speech/double_phoneme/owsh.wav]-', 
        "-OY-SH-" : '-OY-[static/speech/double_phoneme/oysh.wav]-', 
        "-UH-SH-" : '-UH-[static/speech/double_phoneme/uhsh.wav]-',   
        "-UW-SH-" : '-UW-[static/speech/double_phoneme/uwsh.wav]-',

        "-AA-T-" : '-AA-[static/speech/double_phoneme/aat.wav]-',  
        "-AE-T-" : '-AE-[static/speech/double_phoneme/aet.wav]-', 
        "-AH-T-" : '-AH-[static/speech/double_phoneme/aat.wav]-',      
        "-AO-T-" : '-AO-[static/speech/double_phoneme/aat.wav]-', 
        "-AW-T-" : '-AW-[static/speech/double_phoneme/aat.wav]-', 
        "-AY-T-" : '-AY-[static/speech/double_phoneme/ayt.wav]-', 
        "-EH-T-" : '-EH-[static/speech/double_phoneme/eht.wav]-', 
        "-ER-T-" : '-EH-[static/speech/double_phoneme/ert.wav]-',  
        "-EY-T-" : '-EY-[static/speech/double_phoneme/eyt.wav]-', 
        "-IH-T-" : '-IH-[static/speech/double_phoneme/iht.wav]-', 
        "-IY-T-" : '-IY-[static/speech/double_phoneme/eyt.wav]-', 
        "-OW-T-" : '-OW-[static/speech/double_phoneme/owt.wav]-', 
        "-OY-T-" : '-OY-[static/speech/double_phoneme/oyt.wav]-', 
        "-UH-T-" : '-UH-[static/speech/double_phoneme/uht.wav]-',   
        "-UW-T-" : '-UW-[static/speech/double_phoneme/uwt.wav]-',

        "-AA-TH-" : '-AA-[static/speech/double_phoneme/aath.wav]-',  
        "-AE-TH-" : '-AE-[static/speech/double_phoneme/aeth.wav]-', 
        "-AH-TH-" : '-AH-[static/speech/double_phoneme/aath.wav]-',      
        "-AO-TH-" : '-AO-[static/speech/double_phoneme/aath.wav]-', 
        "-AW-TH-" : '-AW-[static/speech/double_phoneme/aath.wav]-', 
        "-AY-TH-" : '-AY-[static/speech/double_phoneme/ayth.wav]-', 
        "-EH-TH-" : '-EH-[static/speech/double_phoneme/ehth.wav]-', 
        "-ER-TH-" : '-EH-[static/speech/double_phoneme/erth.wav]-',  
        "-EY-TH-" : '-EY-[static/speech/double_phoneme/eyth.wav]-', 
        "-IH-TH-" : '-IH-[static/speech/double_phoneme/ihth.wav]-', 
        "-IY-TH-" : '-IY-[static/speech/double_phoneme/eyth.wav]-', 
        "-OW-TH-" : '-OW-[static/speech/double_phoneme/owth.wav]-', 
        "-OY-TH-" : '-OY-[static/speech/double_phoneme/oyth.wav]-', 
        "-UH-TH-" : '-UH-[static/speech/double_phoneme/uhth.wav]-',   
        "-UW-TH-" : '-UW-[static/speech/double_phoneme/uwth.wav]-',

        "-AA-V-" : '-AA-[static/speech/double_phoneme/aav.wav]-',  
        "-AE-V-" : '-AE-[static/speech/double_phoneme/aev.wav]-', 
        "-AH-V-" : '-AH-[static/speech/double_phoneme/aav.wav]-',      
        "-AO-V-" : '-AO-[static/speech/double_phoneme/aav.wav]-', 
        "-AW-V-" : '-AW-[static/speech/double_phoneme/aav.wav]-', 
        "-AY-V-" : '-AY-[static/speech/double_phoneme/ayv.wav]-', 
        "-EH-V-" : '-EH-[static/speech/double_phoneme/ehv.wav]-', 
        "-ER-V-" : '-EH-[static/speech/double_phoneme/erv.wav]-',  
        "-EY-V-" : '-EY-[static/speech/double_phoneme/eyv.wav]-', 
        "-IH-V-" : '-IH-[static/speech/double_phoneme/ihv.wav]-', 
        "-IY-V-" : '-IY-[static/speech/double_phoneme/eyv.wav]-', 
        "-OW-V-" : '-OW-[static/speech/double_phoneme/owv.wav]-', 
        "-OY-V-" : '-OY-[static/speech/double_phoneme/oyv.wav]-', 
        "-UH-V-" : '-UH-[static/speech/double_phoneme/uhv.wav]-',   
        "-UW-V-" : '-UW-[static/speech/double_phoneme/uwv.wav]-',

        "-AA-Z-" : '-AA-[static/speech/double_phoneme/aaz.wav]-',  
        "-AE-Z-" : '-AE-[static/speech/double_phoneme/aez.wav]-', 
        "-AH-Z-" : '-AH-[static/speech/double_phoneme/aaz.wav]-',      
        "-AO-Z-" : '-AO-[static/speech/double_phoneme/aaz.wav]-', 
        "-AW-Z-" : '-AW-[static/speech/double_phoneme/aaz.wav]-', 
        "-AY-Z-" : '-AY-[static/speech/double_phoneme/ayz.wav]-', 
        "-EH-Z-" : '-EH-[static/speech/double_phoneme/ehz.wav]-', 
        "-ER-Z-" : '-EH-[static/speech/double_phoneme/erz.wav]-',  
        "-EY-Z-" : '-EY-[static/speech/double_phoneme/eyz.wav]-', 
        "-IH-Z-" : '-IH-[static/speech/double_phoneme/ihz.wav]-', 
        "-IY-Z-" : '-IY-[static/speech/double_phoneme/eyz.wav]-', 
        "-OW-Z-" : '-OW-[static/speech/double_phoneme/owz.wav]-', 
        "-OY-Z-" : '-OY-[static/speech/double_phoneme/oyz.wav]-', 
        "-UH-Z-" : '-UH-[static/speech/double_phoneme/uhz.wav]-',   
        "-UW-Z-" : '-UW-[static/speech/double_phoneme/uwz.wav]-',

        "-AA-ZH-" : '-AA-[static/speech/double_phoneme/aazh.wav]-',  
        "-AE-ZH-" : '-AE-[static/speech/double_phoneme/aezh.wav]-', 
        "-AH-ZH-" : '-AH-[static/speech/double_phoneme/aazh.wav]-',      
        "-AO-ZH-" : '-AO-[static/speech/double_phoneme/aazh.wav]-', 
        "-AW-ZH-" : '-AW-[static/speech/double_phoneme/aazh.wav]-', 
        "-AY-ZH-" : '-AY-[static/speech/double_phoneme/ayzh.wav]-', 
        "-EH-ZH-" : '-EH-[static/speech/double_phoneme/ehzh.wav]-', 
        "-ER-ZH-" : '-EH-[static/speech/double_phoneme/erzh.wav]-',  
        "-EY-ZH-" : '-EY-[static/speech/double_phoneme/eyzh.wav]-', 
        "-IH-ZH-" : '-IH-[static/speech/double_phoneme/ihzh.wav]-', 
        "-IY-ZH-" : '-IY-[static/speech/double_phoneme/eyzh.wav]-', 
        "-OW-ZH-" : '-OW-[static/speech/double_phoneme/owzh.wav]-', 
        "-OY-ZH-" : '-OY-[static/speech/double_phoneme/oyzh.wav]-', 
        "-UH-ZH-" : '-UH-[static/speech/double_phoneme/uhzh.wav]-',   
        "-UW-ZH-" : '-UW-[static/speech/double_phoneme/uwzh.wav]-'
        }
