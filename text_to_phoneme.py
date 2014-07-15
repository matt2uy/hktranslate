raw_english = "you are the best ming"

raw_english = raw_english.split()
def add_accent(raw_english):
	def text_to_phoneme(text):
		from nltk.corpus import cmudict
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
		from phoneme_dict import hk_text_phonemes
		import re
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
	accented_english = text_to_phoneme(raw_english)
	accented_english = phoneme_to_accent(accented_english)
	accented_english = format_text(accented_english)
	return accented_english
s = add_accent(raw_english)
print s