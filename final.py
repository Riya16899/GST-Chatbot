import random
import requests
from bs4 import BeautifulSoup
from PIL import Image
import time
import re
import pyttsx
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from best_match import *

engine = pyttsx.init()
engine.setProperty('rate', 115)
engine.setProperty('volume', 2)


import pymongo
from pymongo import MongoClient
from flask import Flask, request, jsonify, abort

######## one to many with referanced documents 

Client = MongoClient()
client = MongoClient('localhost', 27017)
client = MongoClient('mongodb://localhost:27017')
db = client.gst_db
posts = db.posts

def all_data():
	for i in posts.find():
		print("\n")
		#print(i)
all_data()
def insert(payload):
	#payload = request.get_json()
	user = posts.insert_one(payload)
	print("\n*********")
	print(" inserted in database")
	print("**********\n")

def data():
	print("what you want to know about? \n\nType any of the below section.")
	print("\n gst \n history \n advantages \n affections \n types \n registration details")

a = ['hii','hy','hi','hey','hello','heelo','helloo','hio']
b = "Hello There! I am GST Chatbot. I can help you to know details about GST Tax."
c = ['good morning','morning']
gst = ['what is GST in India?','GST Tax','GST Tax in india','gst','gst tax']
history = ['history of GST Tax','history','GST history']
advantage = ['advatages of GST Tax','GST Tax Advantage','Tax advantage','advantages']
affection = ['what are the effects of GST Tax','affection of GST Tax','affections']
three = ['types of GST Tax','GST Tax type','types','GST types']
sector = ['which sector is under GST','GST sector','GST affected sector']
register = ['how can i register?','registration details','how should i register','register','registration details']


def web_scraping(url):
	r = requests.get(url)
	data = r.text
	soup = BeautifulSoup(data)
	for paragraph in soup.find_all('p'):
		print(str(paragraph.text))
		print("\n")

def web_scraping1(url):
	read = open(url,'r')
	print(read.read())

web_scraping1("/home/redcliff/Documents/de_project/gst.txt")
   



while True:
	x = raw_input(">>>")  
	userinput = x.lower()


	if userinput in a:
		engine.say('hello good morning')
		print(b)
		engine.say(b)
		engine.runAndWait()
		
		data()
	       	
	elif userinput in c:
		print("good morning!  Have a nice day ahead!")
		data()
	elif userinput in gst:
		print("****************************************************************")
		print("\n\n")
		website = "https://rr.smitpatadiya.me/1.html"
		test = web_scraping(website)

		payload = {
		"userinput" : userinput,
		"website" : website
		}
		insert(payload)
		data()

		

		
	elif userinput in history:
		print("****************************************************************")
		print("\n\n")
		website = "https://rr.smitpatadiya.me/2a.html"
		test = web_scraping(website)
		
	       
		payload = {
		"userinput" : userinput,
		"website" : website
		}
		insert(payload)
		data()


		
	elif userinput in advantage:
		print("****************************************************************")
		print("\n\n")
		website = "https://rr.smitpatadiya.me/4.html"
		test = web_scraping(website)
	   

		payload = {
		"userinput" : userinput,
		"website" : website
		}
		insert(payload)		
		data()

	elif userinput in affection:
		print("****************************************************************")
		print("\n\n")
		website = "https://rr.smitpatadiya.me/5.html"
		test = web_scraping(website)
		  

		payload = {
		"userinput" : userinput,
		"website" : website
		}
		insert(payload)
		
		data()

	elif userinput in three:
		print("****************************************************************")
		print("\n\n")
		website = "https://rr.smitpatadiya.me/3a.html"
		test = web_scraping(website)
		
		payload = {
		"userinput" : userinput,
		"website" : website
		}
		insert(payload)
		data()

	elif userinput in register:
		print("****************************************************************")
		print("\n\n")
		website = "https://rr.smitpatadiya.me/6.html"
		test = web_scraping(website)
	       
		payload = {
		"userinput" : userinput,
		"website" : website
		}
		insert(payload)

		time.sleep(5)
		data()
		time.sleep(10)
		engine.say('now what you want to know about? \n type any of the below section.')
		engine.runAndWait()
		time.sleep(3)


	else:
		print("try again please...")




