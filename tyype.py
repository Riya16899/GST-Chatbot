
from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize
import random
from nltk import ngrams
from nltk.corpus import stopwords
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
#from tki1 import *


#sentence_1 = 'registration here india so good power'
#main_3 = 'army is getting here get more power'
#main_1 = "we are registering here registration power india "
#main_2 = "you will get all information abour army of india great power"


sentence_1 = 'Soldier Technical'
sentence_2 = "Soldier Nursing Assistant"
main_3 = 'Soldier Technical which age tell'
main_1 = "Sepoy Pharma how which like chemical is  "
main_2 = "Soldier Nursing Assistant give who basic"

ni = 1
bigrams = ngrams(sentence_1.split(), ni)
ps = PorterStemmer()


class full_main:
	def gram(self,text,list_gram):
		grams = ngrams(text.split(), ni)
		for i in grams:
			list_gram.append(' '.join(i)) 

	def stop_word(self,list_name,text):
		stop_words = set(stopwords.words('english'))
		word_tokens = word_tokenize(text)
	
		for w in word_tokens:
			if w not in stop_words:
				list_name.append(w)

	def stemm(self,c,d):
		for i,j in zip(c,d):
			for k in range(0,len(j)):
				i.append(ps.stem(j[k]))

	def main(self,a,b):
		for i in range(0,len(a)):
			if a[i] in r:
				#print("r")
				b.append(a[i])
			elif a[i] in s1:
				#print("r")
				b.append(a[i])
		

	def comparision(self,e,f,g):
		if len(e) > len(f) and len(e) > len(g):
			return e
		elif len(f) > len(e) and len(f) > len(g):
			return f
		elif len(g) > len(e) and len(g) > len(f):
			return g
		
		else:
			print("equal")


	



a = []
b = []
c = []
aa = []
bb = []

z = []
y = []
x = []
w = []
v = []

p = []
q = []
r = []
s = []
s1 = []
al = [z,y,x,w,v]
new = [p,q,r,s,s1]

m = []
n = []
o = []
o1 = []
mm = []
nn = []

full_main().gram(sentence_1,aa)
#full_main().gram(sentence_2,bb)
full_main().gram(main_1,a)
full_main().gram(main_2,b)
full_main().gram(main_3,c)

full_main().stop_word(z,main_1)   # z main_1
full_main().stop_word(w,main_2) # w main_2
full_main().stop_word(y,main_3) # y main_3 
full_main().stop_word(x,sentence_1) # x sen_1
#full_main().stop_word(v,sentence_2)

full_main().stemm(new,al)

full_main().main(p,m)
full_main().main(s,n)
full_main().main(q,o)
#full_main().main(s1,o1)

#print full_main().comparision(m,n,o)



