### Eligiiity criteria of indian army

from tyype import *

from nltk.stem import PorterStemmer
ps = PorterStemmer()

from nltk.tokenize import word_tokenize
from nltk import ngrams
text1 = """ok: true that the chicken was the best bamboozler in the known multiverse. fgh fbwhdj fbweyu hjbfj bhjbf cjh fbehf  fbewu. few fewu .dqgyubjwqg bw

hjb bj j : vhj bj 
"""
text2 = """hello all is: hi \n hii all: gghddj hbdj """

criteria_read = open('/home/redcliff/Documents/de_project/defense.txt','r')
criteria = criteria_read.read()

army_read = open('/home/redcliff/Documents/de_project/army.txt','r')
army = army_read.read()
air_force_read = open('/home/redcliff/Documents/de_project/air_force.txt','r')
air_force = air_force_read.read()
navy_read = open('/home/redcliff/Documents/de_project/navy.txt','r')
navy = navy_read.read()

class Get_defination:

	main_word = ""
	filename = ""

	def get_defination(self,filename,word):
		with open("%s" % filename) as openfile:
			ww = word.lower()
			for line in openfile:
				ll = line.lower()
				main_word = ww.split(' ')
				#print(word_tokenize(ll))
			pps = ps.stem(' '.join(main_word))
			ppss = pps.split(' ')
			return ppss

printt = full_main().comparision(m,n,o)
printtt = ' '.join(printt)
see = Get_defination().get_defination('/home/redcliff/Documents/de_project/defense.txt',printtt) # printtt -> for matched word from sent.
#pps = ps.stem(' '.join(see))
#ppss = pps.split(' ')
#see = ['soldier', u'technic']
#print see

#wor = ['hello','all','is']
wor = ['category','is']
worr = []
iii= []
nn = []
def match_with_str(text,wor):
	p = text.split('\n')

	for j in wor:
		worr.append(ps.stem(j))

	for k in p:
		#print k
		ii1 = k.split(':')[0]
	
		ii2 = ii1.split(' ')
		ii3 = ps.stem(' '.join(ii2))
		ii4 = ii3.split(' ')
		
		if ii4 == wor:
			#print ii4, wor
			#for l,m in zip(i.split('age: '),i.split('education: ')): # whole line # 0 to 5 after word
				#print l
				#print m
			for l in k.split(':'):
				return k
		
	

		#else:
		#	print "sorry !"

print match_with_str("hello all you are good \n hh","all")

text = 'Soldier Clerk'
pp = text.split(' ')

ppp = (ps.stem(' '.join(text.split(' ')))).split(' ')


#match_with_str(criteria,(ps.stem(' '.join(text.split(' ')))).split(' ')) # see

word = ['true', 'that', 'the']

n = 3
bigrams = ngrams(text1.split(), n)
#for i in bigrams:
	#print(list(i),li)
	#if list(i) == word:
		#print()


def get_defination(filename,word):
	with open("%s" % filename) as openfile:
		ww = word.lower()
		for line in openfile:
			ll = line.lower()
			main_word = ww.split(' ')
			#print(word_tokenize(ll))
		print main_word


#get_defination('/home/redcliff/Documents/de_project/defense.txt','General Duty')



#http://joinindianarmy.nic.in/alpha/eligibility-criteria.htm
