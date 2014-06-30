# translate user input and put a hong kong accent on it

# all the imports
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
    word = request.form['text'] # get text from form
    # replace letter combs with ones from hk_list
    for letter_comb in translation_list.keys():
        word = re.sub(letter_comb, translation_list[letter_comb], word)


    # convert text to .mp3 urls, in order, separated by spaces
    from letter_combinations import audio_list
    all_audio = "you are the"
    for letter_comb in audio_list.keys():
        all_audio = re.sub(letter_comb, audio_list[letter_comb], all_audio)
        
    print all_audio

    # assign .mp3 urls to
    print all_audio.split()

    # combine sound files
    from pydub import AudioSegment

    you = AudioSegment.from_mp3("static/sound/you.mp3")
    are = AudioSegment.from_mp3("static/sound/are.mp3")
    the = AudioSegment.from_mp3("static/sound/the.mp3")
    audio = you+are+the
    print "wait..."
    # save the result
    audio.export("static/sound/audio_processed.mp3", format="mp3")
    print "done"




    return render_template('translate.html', word=word, audio_file='audio_processed.mp3')

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