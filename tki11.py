#from googletrans import Translator
from tkinter import *                       
from random import choice 
from tkinter import *
from tkinter import scrolledtext    
import tkinter as tk  
from tkinter.scrolledtext import ScrolledText      
from see import *       
from PIL import ImageTk, Image   
import random
                       
hi    = ["hi", "hello", "Hello too","hey"] 
greeting = ["good day ahead","have a nice day","good day","good morning","morning","good evening","evening","good night","night"]          
ok = ["ok","okay"]
about = ["about you","what about you ?","say me about you","say about you"]
error = ["sorry, i don't know", "what u said?","i can not understand. sorry.","say again please..." ]            

root = tk.Tk()     
root.geometry("1000x800") #geometry("window width x window height + pos right + pos down") pos of window           
#root = Tk()   
i = Image.open("image.jpg")
background_image=ImageTk.PhotoImage(i)
background_label = tk.Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

                          
user = StringVar()                          
bot  = StringVar()
                       
root.title(" Simple ChatBot ")      
Label(root, text=" User:",font=("Courier", 12),padx=8,pady=8).place(x=30,y=100)            
#Label(root, text=" User : ").pack(side=LEFT,padx=10,pady=10)      
Entry(root, textvariable=user).place(x=150,y=110) 

tex = tk.Text(master=root,width=50,height=10,borderwidth=5,relief=RAISED,highlightthickness=6)
tex.place(x=500,y=45)
bop = tk.Frame()
bop.pack(side=tk.LEFT)  


#tex1 = tk.Text(master=root,width=50,height=10,borderwidth=5,relief=RAISED,highlightthickness=6)
#tex1.place(x=500,y=300)
#bop = tk.Frame()
#bop.pack(side=tk.LEFT)

variable = StringVar(root)
variable.set("army") # default value

w = OptionMenu(root, variable, "army", "air_force", "navy")
w.place(x=30,y=50)


	 
def cbc(tex,tex1):
	#print(namefile)
	return lambda : callback(tex,variable.get())
	#return lambda : callback(tex1,variable.get())
	#time.sleep(2)
	#root.title(" Simple ChatBot ") 
             
def userr():
	print(user.get())




def callback(tex,filename):
	text = user.get()
	if text in hi:
		s = '{}'.format('Hi !!')
		tex.insert(tk.END, s)
		tex.see(tk.END)

		#s = '{}'.format(translation.text)
		#tex1.insert(tk.END, s)
		#tex1.see(tk.END)

	elif text in greeting:
		s = '{}'.format('Good day !!')
		tex.insert(tk.END, s)
		tex.see(tk.END)

		#s = '{}'.format('Good day !!')
		#tex1.insert(tk.END, s)
		#tex1.see(tk.END)		

	elif text in about:
		s = '{}'.format('I am Chatbot for Defense Theme. i made from using NLP technique, which includes tokenization -> stemming -> stop_words -> String matching. ')
		tex.insert(tk.END,s)
		tex.see(tk.END)

		#s = '{}'.format('I am Chatbot for Defense Theme. i made from using NLP technique, which includes tokenization -> stemming -> stop_words -> String matching. ')
		#tex1.insert(tk.END,s)
		#tex1.see(tk.END)		

	else:
		if filename == 'army':
			s = '{}\n'.format(match_with_str(army,(ps.stem(' '.join(text.split(' ')))).split(' ')))
			tex.insert(tk.END, s)
			tex.see(tk.END) 
		elif filename == 'air_force':
			s = '{}\n'.format(match_with_str(air_force,(ps.stem(' '.join(text.split(' ')))).split(' ')))
			tex.insert(tk.END, s)
			tex.see(tk.END) 

			#s = '{}\n'.format(translation.origin, ' -> ', translation.text)
			#tex1.insert(tk.END, s)
			#tex1.see(tk.END) 

		elif filename == 'navy':
			s = '{}\n'.format(match_with_str(navy,(ps.stem(' '.join(text.split(' ')))).split(' ')))
			tex.insert(tk.END, s)
			tex.see(tk.END) 		

				



#root.configure(background='#111111')

#Button(root, text="send",command=userr).pack(side=LEFT,padx=10,pady=10)
Button(root, text="Bot",command=cbc(tex,variable.get())).place(x=380,y=110)
tk.Button(root, text='Exit', command=root.destroy).place(x=800,y=600)
mainloop()  

# print user.get()




 


# http://effbot.org/tkinterbook/frame.htm
# https://stackoverflow.com/questions/14879916/python-tkinter-make-any-output-appear-in-a-text-box-on-gui-not-in-the-shell

