import re
from pydub import AudioSegment


def hi():
    # convert text to .mp3 urls, in order, separated by spaces
    from letter_combinations import audio_list
    all_audio = "you are the"
    for letter_comb in audio_list.keys():
        all_audio = re.sub(letter_comb, audio_list[letter_comb], all_audio)


    mp3list = [] # list of filenames # not sure how to initalize, so I did this.

    # assign .mp3 urls to list
    for word in all_audio.split():
        mp3list.append(word)

    # assign .mp3 urls in list to actual mp3 files
    #for pronounciation in mp3list:
    audiofile = [] # list of .mp3 files
    for idx, val in enumerate(mp3list):
        audiofile.append(AudioSegment.from_mp3(mp3list[idx]))

    # combine .mp3 files to make a 'sentence'
    for idx, val in enumerate(audiofile):
        print idx, val
        if idx == 0:                    # because I can't do sentence = sentence + audiofile[idx] right away (sentence is undefined, and can't defien it with NULL either (supposedly different type than the .mp3 files))
            sentence = audiofile[0]
        else:
            sentence = sentence + audiofile[idx]

    #sentence = audiofile[0] + audiofile[1] + audiofile[2]
    print "wait..."
    # save the result
    sentence.export("static/sound/audio_processed.mp3", format="mp3")
    print "done"


    
hi()