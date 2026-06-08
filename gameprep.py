from tkinter import *
#need to install on all machines
from tkmacosx import Button
import os
import random


def assign():
	cards=['Rose','Daisy','Tulip','Violet','Lily','Orchids']
	global vaders
	global yodas
	vaders = random.choice(cards)
	cards.remove(vaders)
	yodas = random.choice(cards)
	cards.remove(yodas)
	print (vaders)
	

assign()


def checkV1():
	vader1.config(text=vaders)
	print (vaders)
def checkV2():
	vader2.config(text=vaders)
def checkY1():
	yoda1.config(text=yodas)
def checkY2():
	yoda2.config(text=yodas)
	

root = Tk()
root.title("Memory Game")

#Set size of window
root.geometry("2000x1000")

label = Label(root, text="Memory Game",font=("Arial", 20, "bold"))
frame = Frame(root,)

vader1 = Button(frame,height=175,width=175, command = checkV1,text='')
vader2 = Button(frame,height=175,width=175, command = checkV2,text='')
yoda1 = Button(frame,height=175,width=175, command = checkY1,text='')
yoda2 = Button(frame,height=175,width=175, command = checkY2,text='')

label.pack(pady=60)
frame.pack(pady=100)

vader1.grid(column=0,row=0,pady=10, padx=10)
vader2.grid(column=1,row=0,pady=10, padx=10)
yoda1.grid(column=1,row=1,pady=10, padx=10)
yoda2.grid(column=0,row=1,pady=10, padx=10)



root.mainloop()