import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer

a = open("gst.txt", "r")
for line in a: 
	train_text = line
	sample_text = line

	custom_sent_tokenizer = PunktSentenceTokenizer(train_text)

	tokenized = custom_sent_tokenizer.tokenize(sample_text)

	def process_content():
		try:
			for i in tokenized:
				words = nltk.word_tokenize(i)
				tagged = nltk.pos_tag(words)
				chunkGram = r"""Chunk: {<RB.?>*<VB.?>*<NNP>+<NN>?}"""
				chunkParser = nltk.RegexpParser(chunkGram)
				chunked = chunkParser.parse(tagged)
				chunked.draw()     
	
		except Exception as e:
			print(str(e))

	process_content()
