# translate user input and put a hong kong accent on it

# all the imports
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template

from contextlib import closing

from pydub import AudioSegment

song1 = AudioSegment.from_mp3("static/sound/one.mp3")
song2 = AudioSegment.from_mp3("static/sound/two.mp3")
audio = song1+song2
print "wait..."
# save the result
audio.export("static/sound/audio_processed.mp3", format="mp3")
print "done"


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
    word = request.form['text']
    for letter_comb in translation_list.keys():
        word = re.sub(letter_comb, translation_list[letter_comb], word)
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