
#user : raw_input("User : ")
def get_defination(filename,word):
	with open("%s" % filename) as openfile:
		ww = word.lower()
		for line in openfile:
			ll = line.lower()
			#print(ll)
			for part in ll.split():
				if ww in part:
					print line

#get_defination('air_force.txt','an-32')





###################

## stemming 

from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize
ps = PorterStemmer()

import random


from nltk import ngrams
sentence_1 = 'registration here india so good power'
sentence_2 = 'army is getting here get more power'
main = "we are registering here registration power "
main_2 = "you will get all information abour army of india great "

n = 1
bigrams = ngrams(sentence_1.split(), n)

ps = PorterStemmer()

a = []
b = []
aa = []
bb = []
class Gram:
	def gram(self,text,list_gram):
		grams = ngrams(text.split(), n)
		for i in grams:
			list_gram.append(' '.join(i)) 

#Gram().gram(sentence_1,a)
#Gram().gram(sentence_2,b)

#print("............... 1 gram complete .........")

from nltk.corpus import stopwords
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

Gram().gram(sentence_1,a)
Gram().gram(sentence_2,b)
Gram().gram(main,aa)
Gram().gram(main_2,bb)
#print(a,b)
#print(aa,bb)


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

Stop_Word().stop_word(z,main)
Stop_Word().stop_word(w,main_2)
Stop_Word().stop_word(y,sentence_1)
Stop_Word().stop_word(x,sentence_2)

#print("........stop word complete .............")
p = []
q = []
r = []
s = []
al = [z,y,x,w]
new = [p,q,r,s]
#al = [z,w,y,x]
#new = [p,q,r,s]

class Stemm:
	def stemm(self,c,d):
		for i,j in zip(c,d):
			for k in range(0,len(j)):
				i.append(ps.stem(j[k]))
Stemm().stemm(new,al)
#print(al)
#print(new)
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
		print("p match %s" %p)
		print(a,b)
		for i in range(0,len(a)):
			if a[i] in s:
				bb.append(a[i])
		print(a,bb)
		print("s match %s" %s)
class Mainn:   # another version of Main
	def main(self,a,b,bb):
		for i in range(0,len(a)):
			if a[i] in p:
				b.append(a[i])
			elif a[i] in s:
				bb.append(a[i])
		#print("p match %s" %p)
		#print(a,b)
		#print(a,bb)
		#print("s match %s" %s)
print("....")	
Mainn().main(q,m,mm)
Mainn().main(r,n,nn)
print("....")
print(q,m,mm)
print(r,n,nn)
print("match with p sentense_1 m : %s " % (m))
print("match with s sentense_1 mm : %s" % (mm))
print("match with p sentense_2 n : %s " % (n))
print("match with s sentense_2 nn : %s" % (nn))

class Comparision:
	def comparision(self,e,f):
		if len(e) > len(f):
			print("%s is high" % e)
		elif len(f) > len(e):
			print("%s is high" % f)
		else:
			print("both are equal")


print("comparision for 1 & 2 with p(main)")
print(m,n,p)
Comparision().comparision(m,n)

print("comparision for 1 & 2 with s(main_2)")
print(mm,nn,s)
Comparision().comparision(mm,nn)




