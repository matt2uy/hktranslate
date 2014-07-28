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

"""

hk_audio_phoneme_combo_beginnings = {
        # consonant -> vowel
        "-B-AA-" : '-[static/speech/double_phoneme/baa.wav]-', # robot #######
        "-B-AE-" : '-[static/speech/double_phoneme/bae.wav]-', # bat
        "-B-AH-" : '-[static/speech/double_phoneme/ah.wav]-', # butter ###########    
        "-B-AO-" : '-[static/speech/double_phoneme/bao.wav]-', # aboard
        "-B-AW-" : '-[static/speech/double_phoneme/baw.wav]-', # bow (respect)
        "-B-AY-" : '-[static/speech/double_phoneme/bay.wav]-', # buy
        "-B-EH" : '-[static/speech/double_phoneme/beh.wav]-', # ben
        "-B-ER" : '-[static/speech/double_phoneme/ber.wav]-', # bait
        "-B-EY" : '-[static/speech/double_phoneme/bey.wav]-', # bait
        "-B-IH" : '-[static/speech/double_phoneme/bih.wav]-', # bit
        "-B-IY-" : '-[static/speech/double_phoneme/biy.wav]-', # be
        "-B-OW-" : '-[static/speech/double_phoneme/bow.wav]-', # boat
        "-B-OY-" : '-[static/speech/double_phoneme/boy.wav]-', # boat ###### no boi or oy speech/double_phonemes
        '-B-UH-' : '-[static/speech/double_phoneme/buh.wav]-',#'ou', #hood      HH UH D
        '-B-UW-' : '-[static/speech/double_phoneme/buw.wav]-',#boo
        
        # for c: edit out silence
        # and silence between words too!
        # time log: 25
        "-CH-AA-" : '-[static/speech/double_phoneme/chaa.wav]-', # chopper     
        "-CH-AE-" : '-[static/speech/double_phoneme/chae.wav]-', # chat     
        "-CH-AH-" : '-[static/speech/double_phoneme/chah.wav]-', # chutney    
        "-CH-AO-" : '-[static/speech/double_phoneme/chao.wav]-', # chop 
        "-CH-AW-" : '-[static/speech/double_phoneme/chaw.wav]-', # chow
        

        "-CH-AY-" : '-[static/speech/double_phoneme/chay.wav]-', # china
        "-CH-EH" : '-[static/speech/double_phoneme/cheh.wav]-', # checkers
        "-CH-ER" : '-[static/speech/double_phoneme/cher.wav]-', # churn
        "-CH-EY" : '-[static/speech/double_phoneme/chey.wav]-', # change
        "-CH-IH" : '-[static/speech/double_phoneme/chih.wav]-', # ching
        "-CH-IY-" : '-[static/speech/double_phoneme/chiy.wav]-', # cheese
        "-CH-OW-" : '-[static/speech/double_phoneme/chou.wav]-', # choke
        "-CH-OY-" : '-[static/speech/double_phoneme/choy.wav]-', # choice
        '-CH-UH-' : '-[static/speech/double_phoneme/chuh.wav]-', # chuck
        '-CH-UW-' : '-[static/speech/double_phoneme/chuw.wav]-', # chew

        # time log: 16
        "-D-AA-" : '-[static/speech/double_phoneme/daa.wav]-', # chopper     
        "-D-AE-" : '-[static/speech/double_phoneme/dae.wav]-', # chat     
        "-D-AH-" : '-[static/speech/double_phoneme/dah.wav]-', # chutney    
        "-D-AO-" : '-[static/speech/double_phoneme/dao.wav]-', # chop 
        "-D-AW-" : '-[static/speech/double_phoneme/daw.wav]-', # chow
        "-D-AY-" : '-[static/speech/double_phoneme/day.wav]-', # china
        "-D-EH" : '-[static/speech/double_phoneme/deh.wav]-', # checkers
        "-D-ER" : '-[static/speech/double_phoneme/der.wav]-', # churn
        "-D-EY" : '-[static/speech/double_phoneme/dey.wav]-', # change
        "-D-IH" : '-[static/speech/double_phoneme/dih.wav]-', # ching
        "-D-IY-" : '-[static/speech/double_phoneme/diy.wav]-', # cheese
        "-D-OW-" : '-[static/speech/double_phoneme/dow.wav]-', # choke
        "-D-OY-" : '-[static/speech/double_phoneme/doy.wav]-', # choice
        '-D-UH-' : '-[static/speech/double_phoneme/duh.wav]-', # chuck
        '-D-UW-' : '-[static/speech/double_phoneme/duw.wav]-', # chew

        # time log: 9
        "-F-AA-" : '-[static/speech/double_phoneme/faa.wav]-', # chopper     
        "-F-AE-" : '-[static/speech/double_phoneme/fae.wav]-', # chat     
        "-F-AH-" : '-[static/speech/double_phoneme/fah.wav]-' # chutney    
        
        "-F-AO-" : '-[static/speech/double_phoneme/fao.wav]-', # chop 
        "-F-AW-" : '-[static/speech/double_phoneme/faw.wav]-', # chow
        "-F-AY-" : '-[static/speech/double_phoneme/fay.wav]-', # china
        "-F-EH" : '-[static/speech/double_phoneme/feh.wav]-', # checkers
        "-F-ER" : '-[static/speech/double_phoneme/fer.wav]-', # churn
        "-F-EY" : '-[static/speech/double_phoneme/fey.wav]-', # change
        "-F-IH" : '-[static/speech/double_phoneme/fih.wav]-', # ching
        "-F-IY-" : '-[static/speech/double_phoneme/fiy.wav]-', # cheese
        "-F-OW-" : '-[static/speech/double_phoneme/fow.wav]-', # choke
        "-F-OY-" : '-[static/speech/double_phoneme/foy.wav]-', # choice
        '-F-UH-' : '-[static/speech/double_phoneme/fuh.wav]-', # chuck
        '-F-UW-' : '-[static/speech/double_phoneme/fuw.wav]-', # chew
       
        # time log: 12
        "-G-AA-" : '-[static/speech/double_phoneme/gaa.wav]-', # chopper     
        "-G-AE-" : '-[static/speech/double_phoneme/gae.wav]-', # chat     
        "-G-AH-" : '-[static/speech/double_phoneme/gah.wav]-', # chutney    
        "-G-AO-" : '-[static/speech/double_phoneme/gao.wav]-', # chop 
        "-G-AW-" : '-[static/speech/double_phoneme/gaw.wav]-', # chow
        "-G-AY-" : '-[static/speech/double_phoneme/gay.wav]-', # china
        "-G-EH" : '-[static/speech/double_phoneme/geh.wav]-', # checkers
        "-G-ER" : '-[static/speech/double_phoneme/ger.wav]-', # churn
        "-G-EY" : '-[static/speech/double_phoneme/gey.wav]-', # change
        "-G-IH" : '-[static/speech/double_phoneme/gih.wav]-', # ching
        "-G-IY-" : '-[static/speech/double_phoneme/giy.wav]-', # cheese
        "-G-OW-" : '-[static/speech/double_phoneme/gow.wav]-', # choke
        "-G-OY-" : '-[static/speech/double_phoneme/goy.wav]-', # choice
        '-G-UH-' : '-[static/speech/double_phoneme/guh.wav]-', # chuck
        '-G-UW-' : '-[static/speech/double_phoneme/guw.wav]-', # chew

        # time log: 9
        "-HH-AA-" : '-[static/speech/double_phoneme/haa.wav]-', # chopper     
        "-HH-AE-" : '-[static/speech/double_phoneme/hae.wav]-', # chat     
        "-HH-AH-" : '-[static/speech/double_phoneme/hah.wav]-', # chutney    
        "-HH-AO-" : '-[static/speech/double_phoneme/hao.wav]-', # chop 
        "-HH-AW-" : '-[static/speech/double_phoneme/haw.wav]-', # chow
        "-HH-AY-" : '-[static/speech/double_phoneme/hay.wav]-', # china
        "-HH-EH" : '-[static/speech/double_phoneme/heh.wav]-', # checkers
        "-HH-ER" : '-[static/speech/double_phoneme/her.wav]-', # churn
        "-HH-EY" : '-[static/speech/double_phoneme/hey.wav]-', # change
        "-HH-IH" : '-[static/speech/double_phoneme/hih.wav]-', # ching
        "-HH-IY-" : '-[static/speech/double_phoneme/hiy.wav]-', # cheese
        "-HH-OW-" : '-[static/speech/double_phoneme/how.wav]-', # choke
        "-HH-OY-" : '-[static/speech/double_phoneme/hoy.wav]-', # choice
        '-HH-UH-' : '-[static/speech/double_phoneme/huh.wav]-', # chuck
        '-HH-UW-' : '-[static/speech/double_phoneme/huw.wav]-', # chew

        # time log: 9
        "-JH-AA-" : '-[static/speech/double_phoneme/jaa.wav]-', # chopper     
        "-JH-AE-" : '-[static/speech/double_phoneme/jae.wav]-', # chat     
        "-JH-AH-" : '-[static/speech/double_phoneme/jah.wav]-', # chutney    
        "-JH-AO-" : '-[static/speech/double_phoneme/jao.wav]-', # chop 
        "-JH-AW-" : '-[static/speech/double_phoneme/jaw.wav]-', # chow
        "-JH-AY-" : '-[static/speech/double_phoneme/jay.wav]-', # china
        "-JH-EH" : '-[static/speech/double_phoneme/jeh.wav]-', # checkers
        "-JH-ER" : '-[static/speech/double_phoneme/jer.wav]-', # churn
        "-JH-EY" : '-[static/speech/double_phoneme/jey.wav]-', # change
        "-JH-IH" : '-[static/speech/double_phoneme/jih.wav]-', # ching
        "-JH-IY-" : '-[static/speech/double_phoneme/jiy.wav]-', # cheese
        "-JH-OW-" : '-[static/speech/double_phoneme/jow.wav]-', # choke
        "-JH-OY-" : '-[static/speech/double_phoneme/joy.wav]-', # choice
        '-JH-UH-' : '-[static/speech/double_phoneme/juh.wav]-', # chuck
        '-JH-UW-' : '-[static/speech/double_phoneme/juw.wav]-', # chew

        # time log: 9
        "-K-AA-" : '-[static/speech/double_phoneme/kaa.wav]-', # chopper     
        "-K-AE-" : '-[static/speech/double_phoneme/kae.wav]-', # chat     
        "-k-AH-" : '-[static/speech/double_phoneme/kah.wav]-', # chutney    
        "-K-AO-" : '-[static/speech/double_phoneme/kao.wav]-', # chop 
        "-K-AW-" : '-[static/speech/double_phoneme/kaw.wav]-', # chow
        "-K-AY-" : '-[static/speech/double_phoneme/kay.wav]-', # china
        "-K-EH" : '-[static/speech/double_phoneme/keh.wav]-', # checkers
        "-K-ER" : '-[static/speech/double_phoneme/ker.wav]-', # churn
        "-K-EY" : '-[static/speech/double_phoneme/key.wav]-', # change
        "-K-IH" : '-[static/speech/double_phoneme/kih.wav]-', # ching
        "-K-IY-" : '-[static/speech/double_phoneme/kiy.wav]-', # cheese
        "-K-OW-" : '-[static/speech/double_phoneme/kow.wav]-', # choke
        "-K-OY-" : '-[static/speech/double_phoneme/koy.wav]-', # choice
        '-K-UH-' : '-[static/speech/double_phoneme/kuh.wav]-', # chuck
        '-K-UW-' : '-[static/speech/double_phoneme/kuw.wav]-', # chew

        # time log: 9
        "-L-AA-" : '-[static/speech/double_phoneme/laa.wav]-', # chopper     
        "-L-AE-" : '-[static/speech/double_phoneme/lae.wav]-', # chat     
        "-L-AH-" : '-[static/speech/double_phoneme/lah.wav]-', # chutney    
        "-L-AO-" : '-[static/speech/double_phoneme/lao.wav]-', # chop 
        "-L-AW-" : '-[static/speech/double_phoneme/law.wav]-', # chow
        "-L-AY-" : '-[static/speech/double_phoneme/lay.wav]-', # china
        "-L-EH" : '-[static/speech/double_phoneme/leh.wav]-', # checkers
        "-L-ER" : '-[static/speech/double_phoneme/ler.wav]-', # churn
        "-L-EY" : '-[static/speech/double_phoneme/ley.wav]-', # change
        "-L-IH" : '-[static/speech/double_phoneme/lih.wav]-', # ching
        "-L-IY-" : '-[static/speech/double_phoneme/liy.wav]-', # cheese
        "-L-OW-" : '-[static/speech/double_phoneme/low.wav]-', # choke
        "-L-OY-" : '-[static/speech/double_phoneme/loy.wav]-', # choice
        '-L-UH-' : '-[static/speech/double_phoneme/luh.wav]-', # chuck
        '-L-UW-' : '-[static/speech/double_phoneme/luw.wav]-', # chew

        # time log: 9
        "-M-AA-" : '-[static/speech/double_phoneme/maa.wav]-', # chopper     
        "-M-AE-" : '-[static/speech/double_phoneme/mae.wav]-', # chat     
        "-M-AH-" : '-[static/speech/double_phoneme/mah.wav]-', # chutney    
        "-M-AO-" : '-[static/speech/double_phoneme/mao.wav]-', # chop 
        "-M-AW-" : '-[static/speech/double_phoneme/maw.wav]-', # chow
        "-M-AY-" : '-[static/speech/double_phoneme/may.wav]-', # china
        "-M-EH" : '-[static/speech/double_phoneme/meh.wav]-', # checkers
        "-M-ER" : '-[static/speech/double_phoneme/mer.wav]-', # churn
        "-M-EY" : '-[static/speech/double_phoneme/mey.wav]-', # change
        "-M-IH" : '-[static/speech/double_phoneme/mih.wav]-', # ching
        "-M-IY-" : '-[static/speech/double_phoneme/miy.wav]-', # cheese
        "-M-OW-" : '-[static/speech/double_phoneme/mow.wav]-', # choke
        "-M-OY-" : '-[static/speech/double_phoneme/moy.wav]-', # choice
        '-M-UH-' : '-[static/speech/double_phoneme/muh.wav]-', # chuck
        '-M-UW-' : '-[static/speech/double_phoneme/muw.wav]-', # chew
     
        # time log: 9
        "-N-AA-" : '-[static/speech/double_phoneme/naa.wav]-', # chopper     
        "-N-AE-" : '-[static/speech/double_phoneme/nae.wav]-', # chat     
        "-N-AH-" : '-[static/speech/double_phoneme/nah.wav]-', # chutney    
        "-N-AO-" : '-[static/speech/double_phoneme/nao.wav]-', # chop 
        "-N-AW-" : '-[static/speech/double_phoneme/naw.wav]-', # chow
        "-N-AY-" : '-[static/speech/double_phoneme/nay.wav]-', # china
        "-N-EH" : '-[static/speech/double_phoneme/neh.wav]-', # checkers
        "-N-ER" : '-[static/speech/double_phoneme/ner.wav]-', # churn
        "-N-EY" : '-[static/speech/double_phoneme/ney.wav]-', # change
        "-N-IH" : '-[static/speech/double_phoneme/nih.wav]-', # ching
        "-N-IY-" : '-[static/speech/double_phoneme/niy.wav]-', # cheese
        "-N-OW-" : '-[static/speech/double_phoneme/now.wav]-', # choke
        "-N-OY-" : '-[static/speech/double_phoneme/noy.wav]-', # choice
        '-N-UH-' : '-[static/speech/double_phoneme/nuh.wav]-', # chuck
        '-N-UW-' : '-[static/speech/double_phoneme/nuw.wav]-', # chew

        # time log: 9
        "-P-AA-" : '-[static/speech/double_phoneme/paa.wav]-', # chopper     
        "-P-AE-" : '-[static/speech/double_phoneme/pae.wav]-', # chat     
        "-P-AH-" : '-[static/speech/double_phoneme/pah.wav]-', # chutney    
        "-P-AO-" : '-[static/speech/double_phoneme/pao.wav]-', # chop 
        "-P-AW-" : '-[static/speech/double_phoneme/paw.wav]-', # chow
        "-P-AY-" : '-[static/speech/double_phoneme/pay.wav]-', # china
        "-P-EH" : '-[static/speech/double_phoneme/peh.wav]-', # checkers
        "-P-ER" : '-[static/speech/double_phoneme/per.wav]-', # churn
        "-P-EY" : '-[static/speech/double_phoneme/pey.wav]-', # change
        "-P-IH" : '-[static/speech/double_phoneme/pih.wav]-', # ching
        "-P-IY-" : '-[static/speech/double_phoneme/piy.wav]-', # cheese
        "-P-OW-" : '-[static/speech/double_phoneme/pow.wav]-', # choke
        "-P-OY-" : '-[static/speech/double_phoneme/poy.wav]-', # choice
        '-P-UH-' : '-[static/speech/double_phoneme/puh.wav]-', # chuck
        '-P-UW-' : '-[static/speech/double_phoneme/puw.wav]-', # chew

        # time log: 9
        "-R-AA-" : '-[static/speech/double_phoneme/raa.wav]-', # chopper     
        "-R-AE-" : '-[static/speech/double_phoneme/rae.wav]-', # chat     
        "-R-AH-" : '-[static/speech/double_phoneme/rah.wav]-', # chutney    
        "-R-AO-" : '-[static/speech/double_phoneme/rao.wav]-', # chop 
        "-R-AW-" : '-[static/speech/double_phoneme/raw.wav]-', # chow
        "-R-AY-" : '-[static/speech/double_phoneme/ray.wav]-', # china
        "-R-EH" : '-[static/speech/double_phoneme/reh.wav]-', # checkers
        "-R-ER" : '-[static/speech/double_phoneme/rer.wav]-', # churn
        "-R-EY" : '-[static/speech/double_phoneme/rey.wav]-', # change
        "-R-IH" : '-[static/speech/double_phoneme/rih.wav]-', # ching
        "-R-IY-" : '-[static/speech/double_phoneme/riy.wav]-', # cheese
        "-R-OW-" : '-[static/speech/double_phoneme/row.wav]-', # choke
        "-R-OY-" : '-[static/speech/double_phoneme/roy.wav]-', # choice
        '-R-UH-' : '-[static/speech/double_phoneme/ruh.wav]-', # chuck
        '-R-UW-' : '-[static/speech/double_phoneme/ruw.wav]-', # chew

        # time log: 9
        "-S-AA-" : '-[static/speech/double_phoneme/saa.wav]-', # chopper     
        "-S-AE-" : '-[static/speech/double_phoneme/sae.wav]-', # chat     
        "-S-AH-" : '-[static/speech/double_phoneme/sah.wav]-', # chutney    
        "-S-AO-" : '-[static/speech/double_phoneme/sao.wav]-', # chop 
        "-S-AW-" : '-[static/speech/double_phoneme/saw.wav]-', # chow
        "-S-AY-" : '-[static/speech/double_phoneme/say.wav]-', # china
        "-S-EH" : '-[static/speech/double_phoneme/seh.wav]-', # checkers
        "-S-ER" : '-[static/speech/double_phoneme/ser.wav]-', # churn
        "-S-EY" : '-[static/speech/double_phoneme/sey.wav]-', # change
        "-S-IH" : '-[static/speech/double_phoneme/sih.wav]-', # ching
        "-S-IY-" : '-[static/speech/double_phoneme/siy.wav]-', # cheese
        "-S-OW-" : '-[static/speech/double_phoneme/sow.wav]-', # choke
        "-S-OY-" : '-[static/speech/double_phoneme/soy.wav]-', # choice
        '-S-UH-' : '-[static/speech/double_phoneme/suh.wav]-', # chuck
        '-S-UW-' : '-[static/speech/double_phoneme/suw.wav]-', # chew
        
        # time log: 9
        "-SH-AA-" : '-[static/speech/double_phoneme/shaa.wav]-', # chopper     
        "-SH-AE-" : '-[static/speech/double_phoneme/shae.wav]-', # chat     
        "-SH-AH-" : '-[static/speech/double_phoneme/shah.wav]-', # chutney    
        "-SH-AO-" : '-[static/speech/double_phoneme/shao.wav]-', # chop 
        "-SH-AW-" : '-[static/speech/double_phoneme/shaw.wav]-', # chow
        "-SH-AY-" : '-[static/speech/double_phoneme/shay.wav]-', # china
        "-SH-EH" : '-[static/speech/double_phoneme/sheh.wav]-', # checkers
        "-SH-ER" : '-[static/speech/double_phoneme/sher.wav]-', # churn
        "-SH-EY" : '-[static/speech/double_phoneme/shey.wav]-', # change
        "-SH-IH" : '-[static/speech/double_phoneme/shih.wav]-', # ching
        "-SH-IY-" : '-[static/speech/double_phoneme/shiy.wav]-', # cheese
        "-SH-OW-" : '-[static/speech/double_phoneme/show.wav]-', # choke
        "-SH-OY-" : '-[static/speech/double_phoneme/shoy.wav]-', # choice
        '-SH-UH-' : '-[static/speech/double_phoneme/shuh.wav]-', # chuck
        '-SH-UW-' : '-[static/speech/double_phoneme/shuw.wav]-', # chew

        # time log: 9
        "-T-AA-" : '-[static/speech/double_phoneme/taa.wav]-', # chopper     
        "-T-AE-" : '-[static/speech/double_phoneme/tae.wav]-', # chat     
        "-T-AH-" : '-[static/speech/double_phoneme/tah.wav]-', # chutney    
        "-T-AO-" : '-[static/speech/double_phoneme/tao.wav]-', # chop 
        "-T-AW-" : '-[static/speech/double_phoneme/taw.wav]-', # chow
        "-T-AY-" : '-[static/speech/double_phoneme/tay.wav]-', # china
        "-T-EH" : '-[static/speech/double_phoneme/teh.wav]-', # checkers
        "-T-ER" : '-[static/speech/double_phoneme/ter.wav]-', # churn
        "-T-EY" : '-[static/speech/double_phoneme/tey.wav]-', # change
        "-T-IH" : '-[static/speech/double_phoneme/tih.wav]-', # ching
        "-T-IY-" : '-[static/speech/double_phoneme/tiy.wav]-', # cheese
        "-T-OW-" : '-[static/speech/double_phoneme/tow.wav]-', # choke
        "-T-OY-" : '-[static/speech/double_phoneme/toy.wav]-', # choice
        '-T-UH-' : '-[static/speech/double_phoneme/tuh.wav]-', # chuck
        '-T-UW-' : '-[static/speech/double_phoneme/tuw.wav]-', # chew
        
        # time log: 9
        "-TH-AA-" : '-[static/speech/double_phoneme/thaa.wav]-', # chopper     
        "-TH-AE-" : '-[static/speech/double_phoneme/thae.wav]-', # chat     
        "-TH-AH-" : '-[static/speech/double_phoneme/thah.wav]-', # chutney    
        "-TH-AO-" : '-[static/speech/double_phoneme/thao.wav]-', # chop 
        "-TH-AW-" : '-[static/speech/double_phoneme/thaw.wav]-', # chow
        "-TH-AY-" : '-[static/speech/double_phoneme/thay.wav]-', # china
        "-TH-EH" : '-[static/speech/double_phoneme/theh.wav]-', # checkers
        "-TH-ER" : '-[static/speech/double_phoneme/ther.wav]-', # churn
        "-TH-EY" : '-[static/speech/double_phoneme/they.wav]-', # change
        "-TH-IH" : '-[static/speech/double_phoneme/thih.wav]-', # ching
        "-TH-IY-" : '-[static/speech/double_phoneme/thiy.wav]-', # cheese
        "-TH-OW-" : '-[static/speech/double_phoneme/thow.wav]-', # choke
        "-TH-OY-" : '-[static/speech/double_phoneme/thoy.wav]-', # choice
        '-TH-UH-' : '-[static/speech/double_phoneme/thuh.wav]-', # chuck
        '-TH-UW-' : '-[static/speech/double_phoneme/thuw.wav]-', # chew


        # time log: 9
        "-V-AA-" : '-[static/speech/double_phoneme/vaa.wav]-', # chopper     
        "-V-AE-" : '-[static/speech/double_phoneme/vae.wav]-', # chat     
        "-V-AH-" : '-[static/speech/double_phoneme/vah.wav]-', # chutney    
        "-V-AO-" : '-[static/speech/double_phoneme/vao.wav]-', # chop 
        "-V-AW-" : '-[static/speech/double_phoneme/vaw.wav]-', # chow
        "-V-AY-" : '-[static/speech/double_phoneme/vay.wav]-', # china
        "-V-EH" : '-[static/speech/double_phoneme/veh.wav]-', # checkers
        "-V-ER" : '-[static/speech/double_phoneme/ver.wav]-', # churn
        "-V-EY" : '-[static/speech/double_phoneme/vey.wav]-', # change
        "-V-IH" : '-[static/speech/double_phoneme/vih.wav]-', # ching
        "-V-IY-" : '-[static/speech/double_phoneme/viy.wav]-', # cheese
        "-V-OW-" : '-[static/speech/double_phoneme/vow.wav]-', # choke
        "-V-OY-" : '-[static/speech/double_phoneme/voy.wav]-', # choice
        '-V-UH-' : '-[static/speech/double_phoneme/vuh.wav]-', # chuck
        '-V-UW-' : '-[static/speech/double_phoneme/vuw.wav]-', # chew

        # time log: 9
        "-W-AA-" : '-[static/speech/double_phoneme/waa.wav]-', # chopper     
        "-W-AE-" : '-[static/speech/double_phoneme/wae.wav]-', # chat     
        "-W-AH-" : '-[static/speech/double_phoneme/wah.wav]-', # chutney    
        "-W-AO-" : '-[static/speech/double_phoneme/wao.wav]-', # chop 
        "-W-AW-" : '-[static/speech/double_phoneme/waw.wav]-', # chow
        "-W-AY-" : '-[static/speech/double_phoneme/way.wav]-', # china
        "-W-EH" : '-[static/speech/double_phoneme/weh.wav]-', # checkers
        "-W-ER" : '-[static/speech/double_phoneme/wer.wav]-', # churn
        "-W-EY" : '-[static/speech/double_phoneme/wey.wav]-', # change
        "-W-IH" : '-[static/speech/double_phoneme/wih.wav]-', # ching
        "-W-IY-" : '-[static/speech/double_phoneme/wiy.wav]-', # cheese
        "-W-OW-" : '-[static/speech/double_phoneme/wow.wav]-', # choke
        "-W-OY-" : '-[static/speech/double_phoneme/woy.wav]-', # choice
        '-W-UH-' : '-[static/speech/double_phoneme/wuh.wav]-', # chuck
        '-W-UW-' : '-[static/speech/double_phoneme/wuw.wav]-', # chew



        # time log: 9
        "-Y-AA-" : '-[static/speech/double_phoneme/yaa.wav]-', # chopper     
        "-Y-AE-" : '-[static/speech/double_phoneme/yae.wav]-', # chat     
        "-Y-AH-" : '-[static/speech/double_phoneme/yah.wav]-', # chutney    
        "-Y-AO-" : '-[static/speech/double_phoneme/yao.wav]-', # chop 
        "-Y-AW-" : '-[static/speech/double_phoneme/yaw.wav]-', # chow
        "-Y-AY-" : '-[static/speech/double_phoneme/yay.wav]-', # china
        "-Y-EH" : '-[static/speech/double_phoneme/yeh.wav]-', # checkers
        "-Y-ER" : '-[static/speech/double_phoneme/yer.wav]-', # churn
        "-Y-EY" : '-[static/speech/double_phoneme/yey.wav]-', # change
        "-Y-IH" : '-[static/speech/double_phoneme/yih.wav]-', # ching
        "-Y-IY-" : '-[static/speech/double_phoneme/yiy.wav]-', # cheese
        "-Y-OW-" : '-[static/speech/double_phoneme/yow.wav]-', # choke
        "-Y-OY-" : '-[static/speech/double_phoneme/yoy.wav]-', # choice
        '-Y-UH-' : '-[static/speech/double_phoneme/yuh.wav]-', # chuck
        '-Y-UW-' : '-[static/speech/double_phoneme/yuw.wav]-', # chew



        # time log: 9
        "-Z-AA-" : '-[static/speech/double_phoneme/zaa.wav]-', # chopper     
        "-Z-AE-" : '-[static/speech/double_phoneme/zae.wav]-', # chat     
        "-Z-AH-" : '-[static/speech/double_phoneme/zah.wav]-', # chutney    
        "-Z-AO-" : '-[static/speech/double_phoneme/zao.wav]-', # chop 
        "-Z-AW-" : '-[static/speech/double_phoneme/zaw.wav]-', # chow
        "-Z-AY-" : '-[static/speech/double_phoneme/zay.wav]-', # china
        "-Z-EH" : '-[static/speech/double_phoneme/zeh.wav]-', # checkers
        "-Z-ER" : '-[static/speech/double_phoneme/zer.wav]-', # churn
        "-Z-EY" : '-[static/speech/double_phoneme/zey.wav]-', # change
        "-Z-IH" : '-[static/speech/double_phoneme/zih.wav]-', # ching
        "-Z-IY-" : '-[static/speech/double_phoneme/ziy.wav]-', # cheese
        "-Z-OW-" : '-[static/speech/double_phoneme/zow.wav]-', # choke
        "-Z-OY-" : '-[static/speech/double_phoneme/zoy.wav]-', # choice
        '-Z-UH-' : '-[static/speech/double_phoneme/zuh.wav]-', # chuck
        '-Z-UW-' : '-[static/speech/double_phoneme/zuw.wav]-', # chew


        # time log: 9
        "-ZH-AA-" : '-[static/speech/double_phoneme/zhaa.wav]-', # chopper     
        "-ZH-AE-" : '-[static/speech/double_phoneme/zhae.wav]-', # chat     
        "-ZH-AH-" : '-[static/speech/double_phoneme/zhah.wav]-', # chutney    
        "-ZH-AO-" : '-[static/speech/double_phoneme/zhao.wav]-', # chop 
        "-ZH-AW-" : '-[static/speech/double_phoneme/zhaw.wav]-', # chow
        "-ZH-AY-" : '-[static/speech/double_phoneme/zhay.wav]-', # china
        "-ZH-EH" : '-[static/speech/double_phoneme/zheh.wav]-', # checkers
        "-ZH-ER" : '-[static/speech/double_phoneme/zher.wav]-', # churn
        "-ZH-EY" : '-[static/speech/double_phoneme/zhey.wav]-', # change
        "-ZH-IH" : '-[static/speech/double_phoneme/zhih.wav]-', # ching
        "-ZH-IY-" : '-[static/speech/double_phoneme/zhiy.wav]-', # cheese
        "-ZH-OW-" : '-[static/speech/double_phoneme/zhow.wav]-', # choke
        "-ZH-OY-" : '-[static/speech/double_phoneme/zhoy.wav]-', # choice
        '-ZH-UH-' : '-[static/speech/double_phoneme/zhuh.wav]-', # chuck
        '-ZH-UW-' : '-[static/speech/double_phoneme/zhuw.wav]-', # chew     
        }

hk_audio_phoneme_combo_endings = {

        # vowel -> consonant
        "-AA-B-" : '-AA-[static/speech/double_phoneme/aab.wav]-', # odd
        "-AE-B-" : '-AE[static/speech/double_phoneme/aeb.wav]-', # at
        "-AH-B-" : '-AH-[static/speech/double_phoneme/ahb.wav]-', # hut     
        "-AO-B-" : '-AO-[static/speech/double_phoneme/aob.wav]-', # chop
        "-AW-B-" : '-AW-[static/speech/double_phoneme/awb.wav]-', # chow
        "-AY-B-" : '-AY-[static/speech/double_phoneme/ayb.wav]-', # hide
        "-EH-B-" : '-EH-[static/speech/double_phoneme/ehb.wav]-', # ed
        "-ER-B-" : '-EH-[static/speech/double_phoneme/erb.wav]-', # hurt 
        "-EY-B-" : '-EY-[static/speech/double_phoneme/eyb.wav]-', # made
        "-IH-B-" : '-IH-[static/speech/double_phoneme/ihb.wav]-', # ing
        "-IY-B-" : '-IY-[static/speech/double_phoneme/iyb.wav]-', # read
        "-OW-B-" : '-OW-[static/speech/double_phoneme/owb.wav]-', # oat
        "-OY-B-" : '-OY-[static/speech/double_phoneme/oyb.wav]-', # joy
        '-UH-B-' : '-UH-[static/speech/double_phoneme/uhb.wav]-',# bud   
        '-UW-B-' : '-UW-[static/speech/double_phoneme/uwb.wav]-',# tube


        "-AA-CH-" : '-AA-[static/speech/double_phoneme/aach.wav]-', # odd
        "-AE-CH-" : '-AE[static/speech/double_phoneme/aech.wav]-', # at
        "-AH-CH-" : '-AH-[static/speech/double_phoneme/ahch.wav]-', # hut     
        "-AO-CH-" : '-AO-[static/speech/double_phoneme/aoch.wav]-', # chop
        "-AW-CH-" : '-AW-[static/speech/double_phoneme/awch.wav]-', # chow
        "-AY-CH-" : '-AY-[static/speech/double_phoneme/aych.wav]-', # hide
        "-EH-CH-" : '-EH-[static/speech/double_phoneme/ehch.wav]-', # ed
        "-ER-CH-" : '-EH-[static/speech/double_phoneme/erch.wav]-', # hurt 
        "-EY-CH-" : '-EY-[static/speech/double_phoneme/eych.wav]-', # made
        "-IH-CH-" : '-IH-[static/speech/double_phoneme/ihch.wav]-', # ing
        "-IY-CH-" : '-IY-[static/speech/double_phoneme/iych.wav]-', # read
        "-OW-CH-" : '-OW-[static/speech/double_phoneme/owch.wav]-', # oat
        "-OY-CH-" : '-OY-[static/speech/double_phoneme/oych.wav]-', # joy
        '-UH-CH-' : '-UH-[static/speech/double_phoneme/uhch.wav]-',# bud   
        '-UW-CH-' : '-UW-[static/speech/double_phoneme/uwch.wav]-',# tube

        "-AA-D-" : '-AA-[static/speech/double_phoneme/aad.wav]-', # odd
        "-AE-D-" : '-AE[static/speech/double_phoneme/aed.wav]-', # at
        "-AH-D-" : '-AH-[static/speech/double_phoneme/ahd.wav]-', # hut     
        "-AO-D-" : '-AO-[static/speech/double_phoneme/aod.wav]-', # chop
        "-AW-D-" : '-AW-[static/speech/double_phoneme/awd.wav]-', # chow
        "-AY-D-" : '-AY-[static/speech/double_phoneme/ayd.wav]-', # hide
        "-EH-D-" : '-EH-[static/speech/double_phoneme/ehd.wav]-', # ed
        "-ER-D-" : '-EH-[static/speech/double_phoneme/erd.wav]-', # hurt 
        "-EY-D-" : '-EY-[static/speech/double_phoneme/eyd.wav]-', # made
        "-IH-D-" : '-IH-[static/speech/double_phoneme/ihd.wav]-', # ing
        "-IY-D-" : '-IY-[static/speech/double_phoneme/iyd.wav]-', # read
        "-OW-D-" : '-OW-[static/speech/double_phoneme/owd.wav]-', # oat
        "-OY-D-" : '-OY-[static/speech/double_phoneme/oyd.wav]-', # joy
        '-UH-D-' : '-UH-[static/speech/double_phoneme/uhd.wav]-',# bud   
        '-UW-D-' : '-UW-[static/speech/double_phoneme/uwd.wav]-',# tube

        "-AA-F-" : '-AA-[static/speech/double_phoneme/aaf.wav]-', # odd
        "-AE-F-" : '-AE[static/speech/double_phoneme/aef.wav]-', # at
        "-AH-F-" : '-AH-[static/speech/double_phoneme/ahf.wav]-', # hut     
        "-AO-F-" : '-AO-[static/speech/double_phoneme/aof.wav]-', # chop
        "-AW-F-" : '-AW-[static/speech/double_phoneme/awf.wav]-', # chow
        "-AY-F-" : '-AY-[static/speech/double_phoneme/ayf.wav]-', # hide
        "-EH-F-" : '-EH-[static/speech/double_phoneme/ehf.wav]-', # ed
        "-ER-F-" : '-EH-[static/speech/double_phoneme/erf.wav]-', # hurt 
        "-EY-F-" : '-EY-[static/speech/double_phoneme/eyf.wav]-', # made
        "-IH-F-" : '-IH-[static/speech/double_phoneme/ihf.wav]-', # ing
        "-IY-F-" : '-IY-[static/speech/double_phoneme/iyf.wav]-', # read
        "-OW-F-" : '-OW-[static/speech/double_phoneme/owf.wav]-', # oat
        "-OY-F-" : '-OY-[static/speech/double_phoneme/oyf.wav]-', # joy
        '-UH-F-' : '-UH-[static/speech/double_phoneme/uhf.wav]-',# bud   
        '-UW-F-' : '-UW-[static/speech/double_phoneme/uwf.wav]-',# tube

        "-AA-G-" : '-AA-[static/speech/double_phoneme/aag.wav]-', # odd
        "-AE-G-" : '-AE[static/speech/double_phoneme/aeg.wav]-', # at
        "-AH-G-" : '-AH-[static/speech/double_phoneme/ahg.wav]-', # hut     
        "-AO-G-" : '-AO-[static/speech/double_phoneme/aog.wav]-', # chop
        "-AW-G-" : '-AW-[static/speech/double_phoneme/awg.wav]-', # chow
        "-AY-G-" : '-AY-[static/speech/double_phoneme/ayg.wav]-', # hide
        "-EH-G-" : '-EH-[static/speech/double_phoneme/ehg.wav]-', # ed
        "-ER-G-" : '-EH-[static/speech/double_phoneme/erg.wav]-', # hurt 
        "-EY-G-" : '-EY-[static/speech/double_phoneme/eyg.wav]-', # made
        "-IH-G-" : '-IH-[static/speech/double_phoneme/ihg.wav]-', # ing
        "-IY-G-" : '-IY-[static/speech/double_phoneme/iyg.wav]-', # read
        "-OW-G-" : '-OW-[static/speech/double_phoneme/owg.wav]-', # oat
        "-OY-G-" : '-OY-[static/speech/double_phoneme/oyg.wav]-', # joy
        '-UH-G-' : '-UH-[static/speech/double_phoneme/uhg.wav]-',# bud   
        '-UW-G-' : '-UW-[static/speech/double_phoneme/uwg.wav]-',# tube


        "-AA-JH-" : '-AA-[static/speech/double_phoneme/aajh.wav]-', # odd
        "-AE-JH-" : '-AE[static/speech/double_phoneme/aejh.wav]-', # at
        "-AH-JH-" : '-AH-[static/speech/double_phoneme/ahjh.wav]-', # hut     
        "-AO-JH-" : '-AO-[static/speech/double_phoneme/aojh.wav]-', # chop
        "-AW-JH-" : '-AW-[static/speech/double_phoneme/awjh.wav]-', # chow
        "-AY-JH-" : '-AY-[static/speech/double_phoneme/ayjh.wav]-', # hide
        "-EH-JH-" : '-EH-[static/speech/double_phoneme/ehjh.wav]-', # ed
        "-ER-JH-" : '-EH-[static/speech/double_phoneme/erjh.wav]-', # hurt 
        "-EY-JH-" : '-EY-[static/speech/double_phoneme/eyjh.wav]-', # made
        "-IH-JH-" : '-IH-[static/speech/double_phoneme/ihjh.wav]-', # ing
        "-IY-JH-" : '-IY-[static/speech/double_phoneme/iyjh.wav]-', # read
        "-OW-JH-" : '-OW-[static/speech/double_phoneme/owjh.wav]-', # oat
        "-OY-JH-" : '-OY-[static/speech/double_phoneme/oyjh.wav]-', # joy
        '-UH-JH-' : '-UH-[static/speech/double_phoneme/uhjh.wav]-',# bud   
        '-UW-JH-' : '-UW-[static/speech/double_phoneme/uwjh.wav]-',# tube

        "-AA-K-" : '-AA-[static/speech/double_phoneme/aak.wav]-', # odd
        "-AE-K-" : '-AE[static/speech/double_phoneme/aek.wav]-', # at
        "-AH-K-" : '-AH-[static/speech/double_phoneme/ahk.wav]-', # hut     
        "-AO-K-" : '-AO-[static/speech/double_phoneme/aok.wav]-', # chop
        "-AW-K-" : '-AW-[static/speech/double_phoneme/awk.wav]-', # chow
        "-AY-K-" : '-AY-[static/speech/double_phoneme/ayk.wav]-', # hide
        "-EH-K-" : '-EH-[static/speech/double_phoneme/ehk.wav]-', # ed
        "-ER-K-" : '-EH-[static/speech/double_phoneme/erk.wav]-', # hurt 
        "-EY-K-" : '-EY-[static/speech/double_phoneme/eyk.wav]-', # made
        "-IH-K-" : '-IH-[static/speech/double_phoneme/ihk.wav]-', # ing
        "-IY-K-" : '-IY-[static/speech/double_phoneme/iyk.wav]-', # read
        "-OW-K-" : '-OW-[static/speech/double_phoneme/owk.wav]-', # oat
        "-OY-K-" : '-OY-[static/speech/double_phoneme/oyk.wav]-', # joy
        '-UH-K-' : '-UH-[static/speech/double_phoneme/uhk.wav]-',# bud   
        '-UW-K-' : '-UW-[static/speech/double_phoneme/uwk.wav]-',# tube

        "-AA-L-" : '-AA-[static/speech/double_phoneme/aal.wav]-', # odd
        "-AE-L-" : '-AE[static/speech/double_phoneme/ael.wav]-', # at
        "-AH-L-" : '-AH-[static/speech/double_phoneme/ahl.wav]-', # hut     
        "-AO-L-" : '-AO-[static/speech/double_phoneme/aol.wav]-', # chop
        "-AW-L-" : '-AW-[static/speech/double_phoneme/awl.wav]-', # chow
        "-AY-L-" : '-AY-[static/speech/double_phoneme/ayl.wav]-', # hide
        "-EH-L-" : '-EH-[static/speech/double_phoneme/ehl.wav]-', # ed
        "-ER-L-" : '-EH-[static/speech/double_phoneme/erl.wav]-', # hurt 
        "-EY-L-" : '-EY-[static/speech/double_phoneme/eyl.wav]-', # made
        "-IH-L-" : '-IH-[static/speech/double_phoneme/ihl.wav]-', # ing
        "-IY-L-" : '-IY-[static/speech/double_phoneme/iyl.wav]-', # read
        "-OW-L-" : '-OW-[static/speech/double_phoneme/owl.wav]-', # oat
        "-OY-L-" : '-OY-[static/speech/double_phoneme/oyl.wav]-', # joy
        '-UH-L-' : '-UH-[static/speech/double_phoneme/uhl.wav]-',# bud   
        '-UW-L-' : '-UW-[static/speech/double_phoneme/uwl.wav]-',# tube


        "-AA-M-" : '-AA-[static/speech/double_phoneme/aam.wav]-', # odd
        "-AE-M-" : '-AE[static/speech/double_phoneme/aem.wav]-', # at
        "-AH-M-" : '-AH-[static/speech/double_phoneme/ahm.wav]-', # hut     
        "-AO-M-" : '-AO-[static/speech/double_phoneme/aom.wav]-', # chop
        "-AW-M-" : '-AW-[static/speech/double_phoneme/awm.wav]-', # chow
        "-AY-M-" : '-AY-[static/speech/double_phoneme/aym.wav]-', # hide
        "-EH-M-" : '-EH-[static/speech/double_phoneme/ehm.wav]-', # ed
        "-ER-M-" : '-EH-[static/speech/double_phoneme/erm.wav]-', # hurt 
        "-EY-M-" : '-EY-[static/speech/double_phoneme/eym.wav]-', # made
        "-IH-M-" : '-IH-[static/speech/double_phoneme/ihm.wav]-', # ing
        "-IY-M-" : '-IY-[static/speech/double_phoneme/iym.wav]-', # read
        "-OW-M-" : '-OW-[static/speech/double_phoneme/owm.wav]-', # oat
        "-OY-M-" : '-OY-[static/speech/double_phoneme/oym.wav]-', # joy
        '-UH-M-' : '-UH-[static/speech/double_phoneme/uhm.wav]-',# bud   
        '-UW-M-' : '-UW-[static/speech/double_phoneme/uwm.wav]-',# tube


        "-AA-NG-" : '-AA-[static/speech/double_phoneme/aang.wav]-', # odd
        "-AE-NG-" : '-AE[static/speech/double_phoneme/aeng.wav]-', # at
        "-AH-NG-" : '-AH-[static/speech/double_phoneme/ahng.wav]-', # hut     
        "-AO-NG-" : '-AO-[static/speech/double_phoneme/aong.wav]-', # chop
        "-AW-NG-" : '-AW-[static/speech/double_phoneme/awng.wav]-', # chow
        "-AY-NG-" : '-AY-[static/speech/double_phoneme/ayng.wav]-', # hide
        "-EH-NG-" : '-EH-[static/speech/double_phoneme/ehng.wav]-', # ed
        "-ER-NG-" : '-EH-[static/speech/double_phoneme/erng.wav]-', # hurt 
        "-EY-NG-" : '-EY-[static/speech/double_phoneme/eyng.wav]-', # made
        "-IH-NG-" : '-IH-[static/speech/double_phoneme/ihng.wav]-', # ing
        "-IY-NG-" : '-IY-[static/speech/double_phoneme/iyng.wav]-', # read
        "-OW-NG-" : '-OW-[static/speech/double_phoneme/owng.wav]-', # oat
        "-OY-NG-" : '-OY-[static/speech/double_phoneme/oyng.wav]-', # joy
        '-UH-NG-' : '-UH-[static/speech/double_phoneme/uhng.wav]-',# bud   
        '-UW-NG-' : '-UW-[static/speech/double_phoneme/uwng.wav]-',# tube


        "-AA-N-" : '-AA-[static/speech/double_phoneme/aan.wav]-', # odd 
        "-AE-N-" : '-AE[static/speech/double_phoneme/aen.wav]-', # at
        "-AH-N-" : '-AH-[static/speech/double_phoneme/ahn.wav]-', # hut     
        "-AO-N-" : '-AO-[static/speech/double_phoneme/aon.wav]-', # ought
        "-AW-N-" : '-AW-[static/speech/double_phoneme/awn.wav]-', # cow
        "-AY-N-" : '-AY-[static/speech/double_phoneme/ayn.wav]-', # hide
        "-EH-N-" : '-EH-[static/speech/double_phoneme/ehn.wav]-', # ed
        "-ER-N-" : '-EH-[static/speech/double_phoneme/ern.wav]-', # hurt 
        "-EY-N-" : '-EY-[static/speech/double_phoneme/eyn.wav]-', # ate
        "-IH-N-" : '-IH-[static/speech/double_phoneme/ihn.wav]-', # it
        "-IY-N-" : '-IY-[static/speech/double_phoneme/iyn.wav]-', # eat
        "-OW-N-" : '-OW-[static/speech/double_phoneme/own.wav]-', # oat
        "-OY-N-" : '-OY-[static/speech/double_phoneme/oyn.wav]-', # toy
        '-UH-N-' : '-UH-[static/speech/double_phoneme/uhn.wav]-',# hood   
        '-UW-N-' : '-UW-[static/speech/double_phoneme/uwn.wav]-',# too


        "-AA-P-" : '-AA-[static/speech/double_phoneme/aap.wav]-', # odd 
        "-AE-P-" : '-AE[static/speech/double_phoneme/aep.wav]-', # at
        "-AH-P-" : '-AH-[static/speech/double_phoneme/ahp.wav]-', # hut     
        "-AO-P-" : '-AO-[static/speech/double_phoneme/aop.wav]-', # ought
        "-AW-P-" : '-AW-[static/speech/double_phoneme/awp.wav]-', # cow
        "-AY-P-" : '-AY-[static/speech/double_phoneme/ayp.wav]-', # hide
        "-EH-P-" : '-EH-[static/speech/double_phoneme/ehp.wav]-', # ed
        "-ER-P-" : '-EH-[static/speech/double_phoneme/erp.wav]-', # hurt 
        "-EY-P-" : '-EY-[static/speech/double_phoneme/eyp.wav]-', # ate
        "-IH-P-" : '-IH-[static/speech/double_phoneme/ihp.wav]-', # it
        "-IY-P-" : '-IY-[static/speech/double_phoneme/iyp.wav]-', # eat
        "-OW-P-" : '-OW-[static/speech/double_phoneme/owp.wav]-', # oat
        "-OY-P-" : '-OY-[static/speech/double_phoneme/oyp.wav]-', # toy
        '-UH-P-' : '-UH-[static/speech/double_phoneme/uhp.wav]-',# hood   
        '-UW-P-' : '-UW-[static/speech/double_phoneme/uwp.wav]-',# too


        "-AA-R-" : '-AA-[static/speech/double_phoneme/aar.wav]-', # odd 
        "-AE-R-" : '-AE[static/speech/double_phoneme/aer.wav]-', # at
        "-AH-R-" : '-AH-[static/speech/double_phoneme/ahr.wav]-', # hut     
        "-AO-R-" : '-AO-[static/speech/double_phoneme/aor.wav]-', # ought
        "-AW-R-" : '-AW-[static/speech/double_phoneme/awr.wav]-', # cow
        "-AY-R-" : '-AY-[static/speech/double_phoneme/ayr.wav]-', # hide
        "-EH-R-" : '-EH-[static/speech/double_phoneme/ehr.wav]-', # ed
        "-ER-R-" : '-EH-[static/speech/double_phoneme/eyr.wav]-', # hurt 
        "-EY-R-" : '-EY-[static/speech/double_phoneme/eyr.wav]-', # ate
        "-IH-R-" : '-IH-[static/speech/double_phoneme/ihr.wav]-', # it
        "-IY-R-" : '-IY-[static/speech/double_phoneme/iyr.wav]-', # eat
        "-OW-R-" : '-OW-[static/speech/double_phoneme/owr.wav]-', # oat
        "-OY-R-" : '-OY-[static/speech/double_phoneme/oyr.wav]-', # toy
        '-UH-R-' : '-UH-[static/speech/double_phoneme/uhr.wav]-',# hood   
        '-UW-R-' : '-UW-[static/speech/double_phoneme/uwr.wav]-',# too


        "-AA-S-" : '-AA-[static/speech/double_phoneme/aas.wav]-', # odd 
        "-AE-S-" : '-AE[static/speech/double_phoneme/aes.wav]-', # at
        "-AH-S-" : '-AH-[static/speech/double_phoneme/ahs.wav]-', # hut     
        "-AO-S-" : '-AO-[static/speech/double_phoneme/aos.wav]-', # ought
        "-AW-S-" : '-AW-[static/speech/double_phoneme/aws1.wav]-', # cow
        "-AY-S-" : '-AY-[static/speech/double_phoneme/ays.wav]-', # hide
        "-EH-S-" : '-EH-[static/speech/double_phoneme/ehs.wav]-', # ed
        "-ER-S-" : '-EH-[static/speech/double_phoneme/ers.wav]-', # hurt 
        "-EY-S-" : '-EY-[static/speech/double_phoneme/eys.wav]-', # ate
        "-IH-S-" : '-IH-[static/speech/double_phoneme/ihs.wav]-', # it
        "-IY-S-" : '-IY-[static/speech/double_phoneme/iys.wav]-', # eat
        "-OW-S-" : '-OW-[static/speech/double_phoneme/ows.wav]-', # oat
        "-OY-S-" : '-OY-[static/speech/double_phoneme/oys.wav]-', # toy
        '-UH-S-' : '-UH-[static/speech/double_phoneme/uhs.wav]-',# hood   
        '-UW-S-' : '-UW-[static/speech/double_phoneme/uws.wav]-',# too


        "-AA-SH-" : '-AA-[static/speech/double_phoneme/aash.wav]-', # odd 
        "-AE-SH-" : '-AE[static/speech/double_phoneme/aesh.wav]-', # at
        "-AH-SH-" : '-AH-[static/speech/double_phoneme/ahsh.wav]-', # hut     
        "-AO-SH-" : '-AO-[static/speech/double_phoneme/aosh.wav]-', # ought
        "-AW-SH-" : '-AW-[static/speech/double_phoneme/awsh.wav]-', # cow
        "-AY-SH-" : '-AY-[static/speech/double_phoneme/aysh.wav]-', # hide
        "-EH-SH-" : '-EH-[static/speech/double_phoneme/ehsh.wav]-', # ed
        "-ER-SH-" : '-EH-[static/speech/double_phoneme/ersh.wav]-', # hurt 
        "-EY-SH-" : '-EY-[static/speech/double_phoneme/eysh.wav]-', # ate
        "-IH-SH-" : '-IH-[static/speech/double_phoneme/ihsh.wav]-', # it
        "-IY-SH-" : '-IY-[static/speech/double_phoneme/iysh.wav]-', # eat
        "-OW-SH-" : '-OW-[static/speech/double_phoneme/owsh.wav]-', # oat
        "-OY-SH-" : '-OY-[static/speech/double_phoneme/oysh.wav]-', # toy
        '-UH-SH-' : '-UH-[static/speech/double_phoneme/uhsh.wav]-',# hood   
        '-UW-SH-' : '-UW-[static/speech/double_phoneme/uwsh.wav]-',# too


        "-AA-T-" : '-AA-[static/speech/double_phoneme/aat.wav]-', # odd 
        "-AE-T-" : '-AE[static/speech/double_phoneme/aet.wav]-', # at
        "-AH-T-" : '-AH-[static/speech/double_phoneme/aht.wav]-', # hut     
        "-AO-T-" : '-AO-[static/speech/double_phoneme/aot.wav]-', # ought
        "-AW-T-" : '-AW-[static/speech/double_phoneme/awt.wav]-', # cow
        "-AY-T-" : '-AY-[static/speech/double_phoneme/ayt.wav]-', # hide
        "-EH-T-" : '-EH-[static/speech/double_phoneme/eht.wav]-', # ed
        "-ER-T-" : '-EH-[static/speech/double_phoneme/ert.wav]-', # hurt 
        "-EY-T-" : '-EY-[static/speech/double_phoneme/eyt.wav]-', # ate
        "-IH-T-" : '-IH-[static/speech/double_phoneme/iht.wav]-', # it
        "-IY-T-" : '-IY-[static/speech/double_phoneme/iyt.wav]-', # eat
        "-OW-T-" : '-OW-[static/speech/double_phoneme/owt.wav]-', # oat
        "-OY-T-" : '-OY-[static/speech/double_phoneme/oyt.wav]-', # toy
        '-UH-T-' : '-UH-[static/speech/double_phoneme/uht.wav]-',# hood   
        '-UW-T-' : '-UW-[static/speech/double_phoneme/uwt.wav]-',# too


        "-AA-TH-" : '-AA-[static/speech/double_phoneme/aath.wav]-', # odd 
        "-AE-TH-" : '-AE[static/speech/double_phoneme/aeth.wav]-', # at
        "-AH-TH-" : '-AH-[static/speech/double_phoneme/ahth.wav]-', # hut     
        "-AO-TH-" : '-AO-[static/speech/double_phoneme/aoth.wav]-', # ought
        "-AW-TH-" : '-AW-[static/speech/double_phoneme/awth.wav]-', # cow
        "-AY-TH-" : '-AY-[static/speech/double_phoneme/ayth.wav]-', # hide
        "-EH-TH-" : '-EH-[static/speech/double_phoneme/ehth.wav]-', # ed
        "-ER-TH-" : '-EH-[static/speech/double_phoneme/erth.wav]-', # hurt 
        "-EY-TH-" : '-EY-[static/speech/double_phoneme/eyth.wav]-', # ate
        "-IH-TH-" : '-IH-[static/speech/double_phoneme/ihth.wav]-', # it
        "-IY-TH-" : '-IY-[static/speech/double_phoneme/iyth.wav]-', # eat
        "-OW-TH-" : '-OW-[static/speech/double_phoneme/owth.wav]-', # oat
        "-OY-TH-" : '-OY-[static/speech/double_phoneme/oyth.wav]-', # toy
        '-UH-TH-' : '-UH-[static/speech/double_phoneme/uhth.wav]-',# hood   
        '-UW-TH-' : '-UW-[static/speech/double_phoneme/uwth.wav]-',# too


        "-AA-V-" : '-AA-[static/speech/double_phoneme/aav.wav]-', # odd 
        "-AE-V-" : '-AE[static/speech/double_phoneme/aev.wav]-', # at
        "-AH-V-" : '-AH-[static/speech/double_phoneme/ahv.wav]-', # hut     
        "-AO-V-" : '-AO-[static/speech/double_phoneme/aov.wav]-', # ought
        "-AW-V-" : '-AW-[static/speech/double_phoneme/awv.wav]-', # cow
        "-AY-V-" : '-AY-[static/speech/double_phoneme/ayv.wav]-', # hide
        "-EH-V-" : '-EH-[static/speech/double_phoneme/ehv.wav]-', # ed
        "-ER-V-" : '-EH-[static/speech/double_phoneme/erv.wav]-', # hurt 
        "-EY-V-" : '-EY-[static/speech/double_phoneme/eyv.wav]-', # ate
        "-IH-V-" : '-IH-[static/speech/double_phoneme/ihv.wav]-', # it
        "-IY-V-" : '-IY-[static/speech/double_phoneme/iyv.wav]-', # eat
        "-OW-V-" : '-OW-[static/speech/double_phoneme/owv.wav]-', # oat
        "-OY-V-" : '-OY-[static/speech/double_phoneme/oyv.wav]-', # toy
        '-UH-V-' : '-UH-[static/speech/double_phoneme/uhv.wav]-',# hood   
        '-UW-V-' : '-UW-[static/speech/double_phoneme/uwv.wav]-',# too


        "-AA-WH-" : '-AA-[static/speech/double_phoneme/aawh.wav]-', # odd 
        "-AE-WH-" : '-AE[static/speech/double_phoneme/aewh.wav]-', # at
        "-AH-WH-" : '-AH-[static/speech/double_phoneme/ahwh.wav]-', # hut     
        "-AO-WH-" : '-AO-[static/speech/double_phoneme/aowh.wav]-', # ought
        "-AW-WH-" : '-AW-[static/speech/double_phoneme/awwh.wav]-', # cow
        "-AY-WH-" : '-AY-[static/speech/double_phoneme/aywh.wav]-', # hide
        "-EH-WH-" : '-EH-[static/speech/double_phoneme/ehwy.wav]-', # ed
        "-ER-WH-" : '-EH-[static/speech/double_phoneme/erwh.wav]-', # hurt 
        "-EY-WH-" : '-EY-[static/speech/double_phoneme/eywh.wav]-', # ate
        "-IH-WH-" : '-IH-[static/speech/double_phoneme/ihwh.wav]-', # it
        "-IY-WH-" : '-IY-[static/speech/double_phoneme/iywh.wav]-', # eat
        "-OW-WH-" : '-OW-[static/speech/double_phoneme/owwh.wav]-', # oat
        "-OY-WH-" : '-OY-[static/speech/double_phoneme/oywh.wav]-', # toy
        '-UH-WH-' : '-UH-[static/speech/double_phoneme/uhwh.wav]-',# hood   
        '-UW-WH-' : '-UW-[static/speech/double_phoneme/uwwh.wav]-',# too


        "-AA-Y-" : '-AA-[static/speech/double_phoneme/aay.wav]-', # odd 
        "-AE-Y-" : '-AE[static/speech/double_phoneme/aey.wav]-', # at
        "-AH-Y-" : '-AH-[static/speech/double_phoneme/ahy.wav]-', # hut     
        "-AO-Y-" : '-AO-[static/speech/double_phoneme/aoy.wav]-', # ought
        "-AW-Y-" : '-AW-[static/speech/double_phoneme/awy.wav]-', # cow
        "-AY-Y-" : '-AY-[static/speech/double_phoneme/ayy.wav]-', # hide
        "-EH-Y-" : '-EH-[static/speech/double_phoneme/ehy.wav]-', # ed
        "-ER-Y-" : '-EH-[static/speech/double_phoneme/ery.wav]-', # hurt 
        "-EY-Y-" : '-EY-[static/speech/double_phoneme/eyy.wav]-', # ate
        "-IH-Y-" : '-IH-[static/speech/double_phoneme/ihy.wav]-', # it
        "-IY-Y-" : '-IY-[static/speech/double_phoneme/iyy.wav]-', # eat
        "-OW-Y-" : '-OW-[static/speech/double_phoneme/owy.wav]-', # oat
        "-OY-Y-" : '-OY-[static/speech/double_phoneme/oyy.wav]-', # toy
        '-UH-Y-' : '-UH-[static/speech/double_phoneme/uhy.wav]-',# hood   
        '-UW-Y-' : '-UW-[static/speech/double_phoneme/uwy.wav]-',# too


        "-AA-Z-" : '-AA-[static/speech/double_phoneme/aaz.wav]-', # odd 
        "-AE-Z-" : '-AE[static/speech/double_phoneme/aez.wav]-', # at
        "-AH-Z-" : '-AH-[static/speech/double_phoneme/ahz.wav]-', # hut     
        "-AO-Z-" : '-AO-[static/speech/double_phoneme/aoz.wav]-', # ought
        "-AW-Z-" : '-AW-[static/speech/double_phoneme/awz.wav]-', # cow
        "-AY-Z-" : '-AY-[static/speech/double_phoneme/ayz.wav]-', # hide
        "-EH-Z-" : '-EH-[static/speech/double_phoneme/ehz.wav]-', # ed
        "-ER-Z-" : '-EH-[static/speech/double_phoneme/erz.wav]-', # hurt 
        "-EY-Z-" : '-EY-[static/speech/double_phoneme/eyz.wav]-', # ate
        "-IH-Z-" : '-IH-[static/speech/double_phoneme/ihz.wav]-', # it
        "-IY-Z-" : '-IY-[static/speech/double_phoneme/iyz.wav]-', # eat
        "-OW-Z-" : '-OW-[static/speech/double_phoneme/owz.wav]-', # oat
        "-OY-Z-" : '-OY-[static/speech/double_phoneme/oyz.wav]-', # toy
        '-UH-Z-' : '-UH-[static/speech/double_phoneme/uhz.wav]-',# hood   
        '-UW-Z-' : '-UW-[static/speech/double_phoneme/uwz.wav]-',# too


        "-AA-ZH-" : '-AA-[static/speech/double_phoneme/aazh.wav]-', # odd 
        "-AE-ZH-" : '-AE[static/speech/double_phoneme/aezh.wav]-', # at
        "-AH-ZH-" : '-AH-[static/speech/double_phoneme/ahzh.wav]-', # hut     
        "-AO-ZH-" : '-AO-[static/speech/double_phoneme/aozh.wav]-', # ought
        "-AW-ZH-" : '-AW-[static/speech/double_phoneme/awzh.wav]-', # cow
        "-AY-ZH-" : '-AY-[static/speech/double_phoneme/ayzh.wav]-', # hide
        "-EH-ZH-" : '-EH-[static/speech/double_phoneme/ehzh.wav]-', # ed
        "-ER-ZH-" : '-EH-[static/speech/double_phoneme/erzh.wav]-', # hurt 
        "-EY-ZH-" : '-EY-[static/speech/double_phoneme/eyzh.wav]-', # ate
        "-IH-ZH-" : '-IH-[static/speech/double_phoneme/ihzh.wav]-', # it
        "-IY-ZH-" : '-IY-[static/speech/double_phoneme/iyzh.wav]-', # eat
        "-OW-ZH-" : '-OW-[static/speech/double_phoneme/owzh.wav]-', # oat
        "-OY-ZH-" : '-OY-[static/speech/double_phoneme/oyzh.wav]-', # toy
        '-UH-ZH-' : '-UH-[static/speech/double_phoneme/uhzh.wav]-',# hood   
        '-UW-ZH-' : '-UW-[static/speech/double_phoneme/uwzh.wav]-',# too


        }



"""