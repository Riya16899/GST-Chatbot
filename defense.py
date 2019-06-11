import nltk

# tokenize -> stop words -> spell check -> 

from autocorrect import spell
from whoosh.spelling import *
#from best_match import *
from nltk.corpus import stopwords

from nltk.tokenize import word_tokenize

#print spell('heloo')
#print spell(u'mussage')

from whoosh.lang.porter import stem

import random
from nltk import NaiveBayesClassifier
from nltk.classify import accuracy as nltk_accuracy
from nltk.corpus import names

army_read = open('/home/redcliff/Documents/de_project/army.txt','r')
army_readd = nltk.word_tokenize(army_read.read().lower())
navy_read = open('/home/redcliff/Documents/de_project/navy.txt','r')
navy_readd = nltk.word_tokenize(navy_read.read().lower())
air_force_read = open('/home/redcliff/Documents/de_project/air_force.txt','r')
air_force_readd = nltk.word_tokenize(air_force_read.read().lower())





#print(stem("rendering"))


def Spell(x,x1):
	for i in x:
		x1.append(i)
		#print(x1)
	for i in x1:
		if i in data:
			x1.remove(i)
		else:
			x1.append(spell(i))
	print(x1)

w = ['hiii','helloo','riya']
w1 = []
#Spell(w,w1)


z = []
z1 = []
a = ['ok','okay','ohk','oky']
b = ['hello','thank']

print("we are categorize it by 3 category. army, navy, air force \n so which one would you like to know about ?  ")
first_ask = raw_input(" > ")
army = ['army','indian army','army force','man force']
navy = ['navy of india','navy force','navy','indian navy']
air_force = ['air force','indian air force','air force of india']


class Stop_Word:
	def stop_word(self,list_name,text):
		stop_words = set(stopwords.words('english'))
		word_tokens = word_tokenize(text)
	
		for w in word_tokens:
			if w not in stop_words:
				list_name.append(w)


male_list = [(name, 'male') for name in names.words('male.txt')]
female_list = [(name, 'female') for name in names.words('female.txt')]
data = (male_list + female_list)

x = raw_input(">>>")  
userinput = x.lower()
Stop_Word().stop_word(z,x)
#print(z)
Spell(z,z1)



def stop():
	if first_ask in army:
		x = raw_input(">>>")  
		userinput = x.lower()
		print("................")
		Stop_Word().stop_word(z,x)
		#print(z)
		Spell(z,z1)
		print(z1)
		for j in z1:
			if j in army_readd:
				print("army")
			elif j not in army_readd:
				print("another")



# https://whoosh.readthedocs.io/en/latest/stemming.html
# https://mod.gov.in/dod/



# https://www.globalfirepower.com/country-military-strength-detail.asp?country_id=india

# https://www.rediff.com/news/report/pix-by-2050-india-will-have-a-world-class-navy-naval-chief/20181203.htm
# https://defenceupdate.in/tag/indian-navy/




# its really satisfactory feeling experoence to serve your more than half life to protect your country. 
# its filled up by arrogance in yourself to be with it. 




