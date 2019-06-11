from Tkinter import *                       
from random import choice 
from tkinter import *
from tkinter import scrolledtext    
import Tkinter as tk  
from see import *
from tkinter.scrolledtext import ScrolledText 
from PIL import ImageTk, Image 
from googletrans import Translator
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk import ngrams
from PIL import ImageTk, Image



sentence = 'this is a foo bar sentences and i want to ngramize it'

n = 2

from googletrans import Translator
translator = Translator(service_urls=[
		'translate.google.com',
		'translate.google.co.kr',
	])

root = tk.Tk()     
root.geometry("1000x800") 
user = StringVar()                          
bot  = StringVar()
root.title(" GST ChatBot ")



C = Canvas(root, bg="blue", height=250, width=300)
filename = PhotoImage(file = "/home/redcliff/Pictures/2.png")
background_label = Label(root, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

#tex = tk.Text(master=root,width=50,height=10,borderwidth=5,relief=RAISED,highlightthickness=6)
#tex.place(x=500,y=45)
#bop = tk.Frame()
#bop.pack(side=tk.LEFT)  

#tex1 = tk.Text(master=root,width=20,height=20,borderwidth=5,relief=RAISED,highlightthickness=6)
#tex1.place(x=500,y=400)
bop = tk.Frame()
bop.pack(side=tk.LEFT)
variable = StringVar(root)
variable1 = StringVar(root)
variable.set("Topic") # default value
variable1.set("Language")

w = OptionMenu(root, variable, "gst", "advantage", "affection","history","type")
w.place(x=30,y=50)

#w = OptionMenu(root, variable1, "urdu","english","hindi","spanish")
#w.place(x=140,y=50)
      
     
Entry(root, textvariable=user).place(x=50,y=100) 

tex = tk.Text(master=root,width=50,height=20,borderwidth=5,relief=RAISED,highlightthickness=6, font=("Helvetica", 15))
#tex.place(x=450,y=80)
tex.place(x=600,y=25)
bop = tk.Frame()
bop.pack(side=tk.LEFT)  


def cbc(tex):
	#return callback(tex,variable.get(),user.get())
	return lambda : callback(tex,variable.get(),user.get())
    
def language(languag):
	if languag == 'hindi':
		print 'hi'
	elif languag == 'urdu':
		return 'ur'
	elif languag == 'spanish':
		return 'es'


def userrr():
	print(user.get())


def callback(tex,filename,userr):
	
	if userr == 'hi':
		
		translations = translator.translate(["how are you ?"], dest='hi')
		
		for translation in translations:
			#print(translation.text)
			s1 = '%s ' % (translation.text)
			tex.insert(tk.END, s1)
			tex.see(tk.END)

	else:

		if filename == 'gst':
			aa = open('/home/redcliff/Documents/de_project/gst.txt','r')

			translations = translator.translate([match_with_str(aa.read(),(ps.stem(' '.join(userr.split(' ')))).split(' '))], dest='hi')
			for translation in translations:
				translation.text

				s1 = '%s ' % (translation.text)
				tex.insert(tk.END, s1)
				tex.see(tk.END) 

		elif filename == 'advantage':
			bb = open('/home/redcliff/Documents/de_project/advantage.txt','r')
			text = variable.get()
			

			translations = translator.translate([match_with_str(bb.read(),(ps.stem(' '.join(userr.split(' ')))).split(' '))], dest='hi')
			for translation in translations:
				translation.text

				s1 = '%s ' % (translation.text)
				tex.insert(tk.END, s1)
				tex.see(tk.END)

		elif filename == 'affection':
			bb = open('/home/redcliff/Documents/de_project/affection.txt','r')
			text = variable.get()
			

			translations = translator.translate([match_with_str(bb.read(),(ps.stem(' '.join(userr.split(' ')))).split(' '))], dest='hi')
			for translation in translations:
				translation.text

				s1 = '%s ' % (translation.text)
				tex.insert(tk.END, s1)
				tex.see(tk.END)

		elif filename == 'history':
			bb = open('/home/redcliff/Documents/de_project/history.txt','r')
			text = user.get()
			
		
			translations = translator.translate([match_with_str(bb.read(),(ps.stem(' '.join(userr.split(' ')))).split(' '))], dest='hi')
			for translation in translations:
				translation.text

				s1 = '%s ' % (translation.text)
				tex.insert(tk.END, s1)
				tex.see(tk.END)

		elif filename == 'type':
			bb = open('/home/redcliff/Documents/de_project/type.txt','r')
			
			translations = translator.translate([match_with_str(bb.read(),(ps.stem(' '.join(userr.split(' ')))).split(' '))], dest='hi')
		
	
			
			for translation in translations:
				translation.text
				s1 = '%s ' % (translation.text)
				tex.insert(tk.END, s1)
				tex.see(tk.END)
	

		
		
	
		
					
			
			
			#print(match_with_str(bb.read(),(ps.stem(' '.join(text.split(' ')))).split(' ')))
			

sixgrams = ngrams(str(user.get()).split(), n)
for grams in sixgrams:
  print list(grams)


Button(root, text="Bot",command=cbc(tex)).place(x=250,y=100)
tk.Button(root, text='Exit', command=root.destroy).place(x=850,y=680)
mainloop()  

