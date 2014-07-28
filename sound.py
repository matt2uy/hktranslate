from pydub import AudioSegment

address = "static/speech/aat.wav"

sentence = AudioSegment.from_wav(address)

sentence = sentence + sentence

# shorten: 
# save first 0.5 secs
#sentence = sentence[:500]

# save last 0.5 secs
#sentence = sentence[200:]

sentence.export('aat_test.wav', format="wav")
