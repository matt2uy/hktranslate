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
    from phoneme_dict import hk_text_phonemes
    raw_english = request.form['text']
    
    raw_english = raw_english.split()

    def text_to_phoneme(text):
        phoneme_dict = cmudict.dict()
        text = ""
        for word in raw_english:
          syllable = phoneme_dict[word][0]
          # there should be a counter somewhere
          print syllable
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
        text = ' '.join(word[0].upper() + word[1:] for word in text.split())
        return text

    def add_accent(raw_english):
     
      accented_english = text_to_phoneme(raw_english)
      accented_english = phoneme_to_accent(accented_english)
      accented_english = format_text(accented_english)
      return accented_english
    accented_english = add_accent(raw_english)
    print accented_english
    def text_to_speech(input_text):
        from pydub import AudioSegment
        from phoneme_dict import hk_audio_phoneme_combos
        from phoneme_dict import hk_audio_solo_phonemes
        # turn plain text into parseable phonemes:
        input_text = " ".join(input_text)

        def text_to_phoneme_2(text): # different format for speech
          phoneme_dict = cmudict.dict()
          text = ""
          for word in raw_english:
            syllable = phoneme_dict[word][0]
            # there should be a counter somewhere
            print syllable
            syllable = '-'.join(syllable)
            text = text + syllable + "-"

          text = "-" + text
          print "text: ", text
          return text
        def format_text_2(text):
          # remove numbers (notation for pronounciation stress level)
          text = ''.join(i for i in text if not i.isdigit())
          # capitalize first letter of each word
          text = ' '.join(word[0].upper() + word[1:] for word in text.split())
          return text


        input_text = text_to_phoneme_2(input_text)
        print "phonemes:", input_text
        input_text = format_text_2(input_text)


        # convert text to .wav urls, in order, separated by spaces
        input_text = input_text + "-[static/sound/blank.wav]-"
        # sub in phoneme combninations first
        for phoneme in hk_audio_phoneme_combos.keys():
            input_text = re.sub(phoneme, "-["+hk_audio_phoneme_combos[phoneme]+"]-", input_text)

        # sub in individual phonemes after
        for phoneme in hk_audio_solo_phonemes.keys():
            input_text = re.sub(phoneme, "-["+hk_audio_solo_phonemes[phoneme]+"]-", input_text)

        print input_text
        # take away characters outside of brackets, then take away brackets, then add spaces in between urls
        def remove_words_without_audio(raw_english):
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

        input_text = remove_words_without_audio(input_text)

        wavlist = [] # list of filenames # not sure how to initalize, so I did this.

        # assign .wav urls to list
        for word in input_text.split():
            wavlist.append(word)

        # assign .wav urls in list to actual wav files
        #for pronounciation in wavlist:
        audiofile = [] # list of .wav files
        for idx, val in enumerate(wavlist):

            
            print idx, val
            audiofile.append(AudioSegment.from_wav(wavlist[idx]))
        # combine .wav files to make a 'sentence'
        for idx, val in enumerate(audiofile):
            if idx == 0:                    # because I can't do sentence = sentence + audiofile[idx] right away (sentence is undefined, and can't defien it with NULL either (supposedly different type than the .wav files))
                sentence = audiofile[0]
            else:
                sentence = sentence + audiofile[idx]






        #sentence = audiofile[0] + audiofile[1] + audiofile[2]
        print "wait..."
        # save the result
        sentence.export("static/sound/audio_processed.wav", format="wav")
        print "done"
    ''.join(raw_english)
    text_to_speech(raw_english) # updates audio_processed.wav
    print "hi"
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