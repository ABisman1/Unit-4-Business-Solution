from tkinter import *
#need to install on all machines
from tkmacosx import Button
import os

def (assign):
	cards=[]

root = Tk()
root.title("Memory Game")

#Set size of window
root.geometry("2000x1000")

label = Label(root, text="Memory Game",font=("Arial", 20, "bold"))
frame = Frame(root,)

vader1 = Button(frame, text="vader",height=175,width=175)
vader2 = Button(frame, text="vader",height=175,width=175)
yoda1 = Button(frame, text="yoda",height=175,width=175)
yoda2 = Button(frame, text="yoda",height=175,width=175)
r1 = Button(frame, text="R2-D2",height=175,width=175)
r2 = Button(frame, text="R2-D2",height=175,width=175)
ewok1 = Button(frame, text="Ewok",height=175,width=175)
ewok2 = Button(frame, text="Ewok",height=175,width=175)
jabba1 = Button(frame, text="Jabba",height=175,width=175)
jabba2 = Button(frame, text="Jabba",height=175,width=175)
hoth1 = Button(frame, text="Hoth",height=175,width=175)
hoth2 = Button(frame, text="Hoth",height=175,width=175)

label.pack(pady=25)
frame.pack(pady=40)

vader1.grid(column=0,row=0,pady=10, padx=10)
vader2.grid(column=1,row=0,pady=10, padx=10)
yoda1.grid(column=2,row=0,pady=10, padx=10)
yoda2.grid(column=0,row=1,pady=10, padx=10)
r1.grid(column=1,row=1,pady=10, padx=10)
r2.grid(column=2,row=1,pady=10, padx=10)
ewok1.grid(column=3,row=0,pady=10, padx=10)
ewok2.grid(column=0,row=2,pady=10, padx=10)
jabba1.grid(column=3,row=1,pady=10, padx=10)
jabba2.grid(column=1,row=2,pady=10, padx=10)
hoth1.grid(column=3,row=2,pady=10, padx=10)
hoth2.grid(column=2,row=2,pady=10, padx=10)



root.mainloop()