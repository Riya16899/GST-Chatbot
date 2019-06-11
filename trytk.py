from Tkinter import *                       
from random import choice 
from tkinter import *
from tkinter import scrolledtext    
import Tkinter as tk  
from tkinter.scrolledtext import ScrolledText      
from see import *       
import time   
from see import * 
                                    
ask   = ["hi", "hello"]                         
hi    = ["hi", "hello", "Hello too"]                    
error = ["sorry, i don't know", "what u said?","i can not understand. sorry.","say again please..." ]            

root = tk.Tk()     
root.geometry("600x200") #geometry("window width x window height + pos right + pos down") pos of window           
#root = Tk()                             
user = StringVar()                          

                	     
def ff():
	
	time.sleep(2)
	Entry(root, textvariable=user).pack(side=LEFT,padx=10,pady=10)

	#time.sleep(2)
	#root.title(" Simple ChatBot ") 
             
	  


Button(root, text="say",command=ff).pack(side=LEFT,padx=10,pady=10)   

tk.Button(root, text='Exit', command=root.destroy).pack(side=LEFT,padx=10,pady=10)
mainloop()  

# print user.get()



from tkinter import *
from PIL import ImageTk, Image
roott = Tk()

canv = Canvas(roott, width=1000, height=600, bg='white')
canv.grid(row=2, column=3)

img = ImageTk.PhotoImage(Image.open("icon.png"))  # PIL solution
canv.create_image(20, 20, anchor=NW, image=img)

mainloop()
 


# http://effbot.org/tkinterbook/frame.htm
# https://stackoverflow.com/questions/14879916/python-tkinter-make-any-output-appear-in-a-text-box-on-gui-not-in-the-shell

