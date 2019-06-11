###################

## stemming 

from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize
ps = PorterStemmer()

import random


from nltk import ngrams
sentence_1 = 'gst is there gst india greeting tax are happy with it'
sentence_2 = 'gst is from tax tax how about gst'
n = 2
bigrams = ngrams(sentence_1.split(), n)

ps = PorterStemmer()

a = []
b = []
class Gram:
	def gram(self,text,list_gram):
		oo = ngrams(text.split(),n)
		#gra = ngrams(text.split(), n)
		for i in oo:
			list_gram.append(' '.join(i)) 

Gram().gram(sentence_1,a)
Gram().gram(sentence_2,b)
print a
#print("............... 1 gram complete .........")

main = "gst is required there to get information greeting all the time gst "
main_2 = "gst hello all how are you india "
from nltk.corpus import stopwords

from nltk.tokenize import word_tokenize

z = []
y = []
x = []
w = []
class Stop_Word:
	def stop_word(self,list_name,text):
		stop_words = set(stopwords.words('english'))
		word_tokens = word_tokenize(text)
	
		for w in word_tokens:
			if w not in stop_words:
				list_name.append(w)

#Stop_Word().stop_word(z,main)
#Stop_Word().stop_word(w,main_2)
#Stop_Word().stop_word(y,sentence_1)
#Stop_Word().stop_word(x,sentence_2)

#print("........stop word complete .............")
p = []
q = []
r = []
s = []
al = [z,y,x,w]
new = [p,q,r,s]

class Stemm:
	def stemm(self,c,d):
		for i,j in zip(c,d):
			for k in range(0,len(j)):
				i.append(ps.stem(j[k]))
#Stemm().stemm(new,al)

#print("main p : %s " % p)
#print("main_2 s : %s " % s)
#print("sentense_1 q : %s " % q)
#print("sentense_2 r : %s " % r)
#print(".............. stemming complete ........")
m = []
n = []
mm = []
nn = []


class Main:
	def main(self,a,b,bb):
		for i in range(0,len(a)):
			if a[i] in p:
				b.append(a[i])
		for i in range(0,len(a)):
			if a[i] in s:
				bb.append(a[i])
	
#Main().main(q,m,mm)
#Main().main(r,n,nn)
#print("....")
#print(q,m,mm)
#print("sentense_1 m : %s " % set(m))
#print("sentense_2 n : %s" % set(n))
#print("sentense_1 mm : %s " % set(mm))
#print("sentense_2 nn : %s" % set(nn))

class Comparision:
	def comparision(self,e,f):
		if len(e) > len(f):
			print("%s is high" % e)
		elif len(f) > len(e):
			print("%s is high" % f)
		else:
			print("both are equal")

#Comparision().comparision(m,n)
#Comparision().comparision(mm,nn)
