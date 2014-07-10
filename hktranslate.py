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
    from letter_combinations import hk_list

    translation_list = hk_list
    raw_english = request.form['text']
    
    # add the accent to the text
    accented_english = raw_english
    for letter_comb in translation_list.keys():
      accented_english = re.sub(letter_comb, translation_list[letter_comb], accented_english)
    
    def text_to_speech(input_text):
        from pydub import AudioSegment
        from letter_combinations import audio_list 

        # convert text to .mp3 urls, in order, separated by spaces
        for letter_comb in audio_list.keys():
            input_text = "[static/sound/blank.mp3]"+ re.sub(letter_comb, "["+audio_list[letter_comb]+"]", input_text)

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

        mp3list = [] # list of filenames # not sure how to initalize, so I did this.

        # assign .mp3 urls to list
        for word in input_text.split():
            mp3list.append(word)

        # assign .mp3 urls in list to actual mp3 files
        #for pronounciation in mp3list:
        audiofile = [] # list of .mp3 files
        for idx, val in enumerate(mp3list):
            print idx,val
            audiofile.append(AudioSegment.from_mp3(mp3list[idx]))

        
        # combine .mp3 files to make a 'sentence'
        for idx, val in enumerate(audiofile):
            if idx == 0:                    # because I can't do sentence = sentence + audiofile[idx] right away (sentence is undefined, and can't defien it with NULL either (supposedly different type than the .mp3 files))
                sentence = audiofile[0]
            else:
                sentence = sentence + audiofile[idx]

        #sentence = audiofile[0] + audiofile[1] + audiofile[2]
        print "wait..."
        # save the result
        sentence.export("static/sound/audio_processed.mp3", format="mp3")
        print "done"
    text_to_speech(raw_english) # updates audio_processed.mp3

    return render_template('translate.html', word=accented_english, audio_file='audio_processed.mp3')

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