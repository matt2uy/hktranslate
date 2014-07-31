from pydub import AudioSegment

address = "static/speech/misc/blank.wav"

sentence = AudioSegment.from_wav(address)

sentence = sentence + sentence

# shorten: 
# save first 0.5 secs
sentence = sentence[:100]

# save last 0.5 secs
#sentence = sentence[200:]

sentence.export(address, format="wav")
