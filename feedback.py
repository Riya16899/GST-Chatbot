import pygame
from tkinter import *
root = Tk()
root.geometry("800x250")
pygame.init()

 
user = StringVar()
Label(root, text="Your Feedback means a lot to us !!",font=("Courier", 25)).place(x=10,y=60)   
e = Entry(root, textvariable=user)
e.pack(side=LEFT,padx=10,pady=10,fill=X,expand=True)


def main():    
	print(user.get())   
	file_open = open('/home/redcliff/Documents/de_project/wordnet.txt','ab')
	file_open.write(" ")
	file_open.write(user.get())

Button(root, text="Submit", command=main).pack(side=RIGHT,padx=10,pady=5)  ## main in command

Button(root, text='Exit', command=root.destroy).place(x=680,y=190)
root.mainloop()
