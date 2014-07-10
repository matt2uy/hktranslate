from nltk.corpus import cmudict
phoneme_dict = cmudict.dict()

def word_to_phoneme(word):
	for syllable in phoneme_dict[word]:
		print syllable
		print ''

raw_english = ['you', 'are', 'the', 'best', 'shanker']

for word in raw_english:
	word_to_phoneme(word)

