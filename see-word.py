from Tkinter import *                       
from random import choice 
from tkinter import *
from tkinter import scrolledtext    
import Tkinter as tk
from see import *  

root = tk.Tk()     
root.geometry("600x200") #geometry("window width x window height + pos right + pos down") pos of window           
#root = Tk()                             
user = StringVar()                          
bot  = StringVar()                          
                                    
root.title(" Simple ChatBot ")                  
Label(root, text=" user : ").pack(side=LEFT)    
Entry(root, textvariable=user).pack(side=LEFT,padx=10,pady=10)          
Label(root, text=" Bot  : ").pack(side=LEFT)                
Entry(root, textvariable=bot).pack(side=LEFT,padx=10,pady=10) 

def main():  
	r = match_with_str(aaa,see)                                                  
	bot.set('%s' % r)                    
 


Button(root, text="ok", command=main).pack(side=LEFT,padx=10,pady=10)  


                                    
mainloop()     





#match_with_str(aaa,see)




