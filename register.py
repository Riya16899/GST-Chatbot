from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import re

read = open("register.txt", "r")

for line in read:
	new_filtered_sentence = re.sub('[^ a-zA-Z0-9]','',line)
	#print(new_filtered_sentence)


	stop_words = set(stopwords.words('english'))

	word_tokens = word_tokenize(new_filtered_sentence)

	filtered_sentence = [w for w in word_tokens if not w in stop_words]

	filtered_sentence = []

	for w in word_tokens:
	    if w not in stop_words:
			filtered_sentence.append(w)
	       
	        #re.sub('[^ a-zA-Z0-9]','',w)

	print(filtered_sentence)
	
	


