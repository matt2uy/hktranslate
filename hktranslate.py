# translate user input and put a hong kong accent on it
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template

from contextlib import closing

# configuration

# application:
app = Flask(__name__)
app.config.from_envvar('FLASKR_SETTINGS', silent = True) # if there is no FLASKR_SETTINGS, then run the one below
app.config.from_object(__name__)
        
@app.route('/')
def translate():
    return render_template('translate.html')
    
@app.route('/translate', methods=['POST'])
def add_entry():   
    import re
    from nltk.corpus import cmudict

    def get_text():
        # get text from web page
        raw_english = request.form['text']
        raw_english = raw_english.split()
        return raw_english
    '''
    def add_accent(raw_english):
        from phoneme_dict import hk_text_phonemes

        def opening_message():
            print ''
            print '-- Begin translation --'
            print ''
            print "Raw English: ", raw_english
        def text_to_phoneme(text):
            phoneme_dict = cmudict.dict()
            text = ""
            for word in raw_english:
              syllable = phoneme_dict[word][0] # (selects first instance of phonemic conversion only) there should be a counter somewhere
              syllable = ''.join(syllable)
              text = text + syllable + " "
            return text
        def phoneme_to_accent(text):
            for phoneme in text:
              for phoneme in hk_text_phonemes.keys():
                text = re.sub(phoneme, hk_text_phonemes[phoneme], text)
            return text 
        def format_text(text):
            # remove numbers (notation for pronounciation stress level)
            text = ''.join(i for i in text if not i.isdigit())
            # convert all to lowercase
            text = text.lower()
            # capitalize first letter of each word
            text = ''.join(text[0].upper() + text[1:])
            return text

        opening_message()
        accented_english = text_to_phoneme(raw_english)
        accented_english = phoneme_to_accent(accented_english)
        accented_english = format_text(accented_english)
        print "Accented Text: ", accented_english
        return accented_english   
    '''
    def add_accent(raw_english):
        accented_english = raw_english
        accented_english = ' '.join(accented_english)
        from phoneme_dict import hk_list
        for phoneme in hk_list.keys():
            accented_english = re.sub(phoneme, hk_list[phoneme], accented_english)
        return accented_english    
    def text_to_speech(input_text):
        from pydub import AudioSegment
        
        # turn plain text into parseable phonemes:
        input_text = " ".join(input_text)

        def text_to_phoneme_2(text): # different format for speech
          phoneme_dict = cmudict.dict()
          text = ""
          for word in raw_english:
            syllable = phoneme_dict[word][0] # there should be a counter somewhere for each phonemic version
            syllable = '-'.join(syllable)
            text = text + syllable + "- -"

          text = "-" + text
          return text
        def format_text_2(text):
          # remove numbers (notation for pronounciation stress level)
          text = ''.join(i for i in text if not i.isdigit())
          print "Phonemized version:", text
          return text
        def text_to_phoneme_filename(input_text):
            from phoneme_dict import separate_words
            from phoneme_dict import hk_audio_phoneme_combo_endings
            from phoneme_dict import hk_audio_phoneme_combo_beginnings
            from phoneme_dict import hk_audio_solo_phonemes
            # convert text to .wav urls, in order, separated by spaces
            input_text = input_text + "-[static/speech/misc/blank.wav]-"
           
            # add spaces between words:
            for phoneme in separate_words.keys():
                input_text = re.sub(phoneme, separate_words[phoneme], input_text)
            print "STAGE ZERO (separate words):"
            print input_text
            
            # sub in phoneme combo endings first
            for phoneme in hk_audio_phoneme_combo_endings.keys():
                input_text = re.sub(phoneme, hk_audio_phoneme_combo_endings[phoneme], input_text)
            print "STAGE ONE (suffixes):"
            print input_text   
            
            # sub in phoneme combo beginnings second
            for phoneme in hk_audio_phoneme_combo_beginnings.keys():
                input_text = re.sub(phoneme, hk_audio_phoneme_combo_beginnings[phoneme], input_text)
            print "STAGE TWO (prefixes):"
            print input_text
            
            # sub in individual phonemes last
            for phoneme in hk_audio_solo_phonemes.keys():
                input_text = re.sub(phoneme, hk_audio_solo_phonemes[phoneme], input_text)
            
            print "STAGE THREE (indiv.):"
            print "audio file formatted: ", input_text
            return input_text
        def remove_words_without_audio(raw_english):
            # take away characters outside of brackets, 
            # then take away brackets
            # add spaces between urls
            output = []
            record = False
            for char in raw_english:
                if char == "]":
                    output.append(" ")
                    record = False
                if record == True:
                    output.append(char)
                if char == "[":
                    record = True
            return ''.join(output)
        def filenames_to_list(input_text):
            wavlist = [] # list of filenames
            # assign .wav urls to list
            for word in input_text.split():
                wavlist.append(word)
            print "wav  list", wavlist
            return wavlist
        def filename_list_to_audio_file_list(wavlist):
            ###### Actual audio processsing #######
            print "Processing audio file..."
            # assign .wav urls in list to actual wav files
            audiofile = [] # list of .wav files
            print "Sound files:"
            shorten_next_audio = False
            for idx, val in enumerate(wavlist):
                print "|", idx, "|", val

                current_phoneme = AudioSegment.from_wav(wavlist[idx]) 

                #audio blending
                '''
                audio_file = []
                word_done = False
                for idx, wav in wavlist:
                    if wav not 'static/misc/blank.mp3':
                        word_done = False
                        audio_file[idx] = wav
                        cut_end_of_audio()
                    else:
                        cut start of previous audio
                        word_done = True
                '''

                '''digraph_prefix = ['static/sound/pa1.wav',
                                  'static/sound/ba1.wav',
                                  'static/sound/ga1.wav',
                                  'static/sound/pi1.wav']

                digraph_dict = {'static/sound/pa1.wav':'static/sound/ang1.wav',
                                'static/sound/ba1.wav':'static/sound/ang1.wav',
                                'static/sound/ga1.wav':'static/sound/ang1.wav',
                                'static/sound/pi1.wav':'static/sound/ing1.wav'}

                digraph_suffix = ['static/sound/ang1.wav',
                                  'static/sound/ing1.wav']

                for suffix in digraph_suffix:
                    for prefix in digraph_prefix:
                        # check is prefix matches suffix and match them correspondingly

                        #  current phoneme |  next phoneme      |
                        if val == prefix and wavlist[idx+1] == suffix:
             
                            print 'shortened end of audio'
                            # save first 0.5 secs
                            print "length before", current_phoneme.duration_seconds*1000
                            audio_length = current_phoneme.duration_seconds*1000*0.6
                            current_phoneme = current_phoneme[:audio_length]
                            print "length after", current_phoneme.duration_seconds*1000
                            shorten_next_audio = True
                        if shorten_next_audio == True:
                            print "length before", current_phoneme.duration_seconds*1000
                            audio_length = current_phoneme.duration_seconds*1000*0.3
                            current_phoneme = current_phoneme[audio_length:]
                            print "length after", current_phoneme.duration_seconds*1000
                            
                            print "Shortened start of audio"
                            shorten_next_audio = False'''
                                            
                audiofile.append(current_phoneme)
            return audiofile
        def combine_audio_file_list(audiofile):
            # combine .wav files to make a 'sentence'
            for idx, val in enumerate(audiofile):
                if idx == 0:                    # because I can't do sentence = sentence + audiofile[idx] right away (sentence is undefined, and can't defien it with NULL either (supposedly different type than the .wav files))
                    sentence = audiofile[0]
                else:
                    sentence = sentence + audiofile[idx]
            return sentence
        def save_audio_file():
            # save the result
            sentence.export("static/speech/misc/audio_processed.wav", format="wav")
            print "Done!"
            print ''
            print '-- Done translation --'
            print ''

        input_text = text_to_phoneme_2(input_text)
        input_text = format_text_2(input_text)
        input_text = text_to_phoneme_filename(input_text)
        input_text = remove_words_without_audio(input_text)
        wavlist = filenames_to_list(input_text)
        audiofile = filename_list_to_audio_file_list(wavlist)
        sentence = combine_audio_file_list(audiofile)
        save_audio_file()      
    
    raw_english = get_text()
    accented_english = add_accent(raw_english)
    text_to_speech(raw_english) # updates audio_processed.wav

    return render_template('translate.html', word=accented_english, audio_file='audio_processed.wav')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/more')
def more():
    return render_template('more.html')
    
if __name__ == '__main__':
    app.run()
