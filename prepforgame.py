from tkinter import *
#need to install on all machines
from tkmacosx import Button
import os
import random
import time

#def rePlay():
	#root.mainloop()

press=0
vPressed=0
yPressed=0
rPressed=0
ePressed=0
jPressed=0
hPressed=0
done=0
click=0


def assign():
	spot1='00'
	spot2='01'
	spot3='02'
	spot4='10'
	spot5='11'
	spot6='12'
	spot7='20'
	spot8='21'
	spot9='22'
	spot10='30'
	spot11='31'
	spot12='32'
	cards=[spot1,spot2,spot3,spot4,spot5,spot6,spot7,spot8,spot9,spot10,spot11,spot12]
	vaders1 = random.choice(cards)
	cards.remove(vaders1)
	vaders2 = random.choice(cards)
	cards.remove(vaders2)
	yodas1 = random.choice(cards)
	cards.remove(yodas1)
	yodas2 = random.choice(cards)
	cards.remove(yodas2)
	rs1 = random.choice(cards)
	cards.remove(rs1)
	rs2 = random.choice(cards)
	cards.remove(rs2)
	ewoks1 = random.choice(cards)
	cards.remove(ewoks1)
	ewoks2 = random.choice(cards)
	cards.remove(ewoks2)
	jabbas1 = random.choice(cards)
	cards.remove(jabbas1)
	jabbas2 = random.choice(cards)
	cards.remove(jabbas2)
	hoths1 = random.choice(cards)
	cards.remove(hoths1)
	hoths2 = random.choice(cards)
	cards.remove(hoths2)
	vader1.grid(column=int(vaders1[0]),row=int(vaders1[1]),pady=10, padx=10)
	vader2.grid(column=int(vaders2[0]),row=int(vaders2[1]),pady=10, padx=10)
	yoda1.grid(column=int(yodas1[0]),row=int(yodas1[1]),pady=10, padx=10)
	yoda2.grid(column=int(yodas2[0]),row=int(yodas2[1]),pady=10, padx=10)
	r1.grid(column=int(rs1[0]),row=int(rs1[1]),pady=10, padx=10)
	r2.grid(column=int(rs2[0]),row=int(rs2[1]),pady=10, padx=10)
	ewok1.grid(column=int(ewoks1[0]),row=int(ewoks1[1]),pady=10, padx=10)
	ewok2.grid(column=int(ewoks2[0]),row=int(ewoks2[1]),pady=10, padx=10)
	jabba1.grid(column=int(jabbas1[0]),row=int(jabbas1[1]),pady=10, padx=10)
	jabba2.grid(column=int(jabbas2[0]),row=int(jabbas2[1]),pady=10, padx=10)
	hoth1.grid(column=int(hoths1[0]),row=int(hoths1[1]),pady=10, padx=10)
	hoth2.grid(column=int(hoths2[0]),row=int(hoths2[1]),pady=10, padx=10)


def checkCards():
	global press
	global vPressed
	global yPressed
	global rPressed
	global ePressed
	global jPressed
	global hPressed
	global done
	if press >= 2 and vPressed >= 2:
		press=0
		vPressed=0
		yPressed=0
		rPressed=0
		ePressed=0
		jPressed=0
		hPressed=0
		done+=1
		vader1.grid_remove()
		vader2.grid_remove()
	elif press >= 2 and yPressed >= 2:
		press=0
		vPressed=0
		yPressed=0
		rPressed=0
		ePressed=0
		jPressed=0
		hPressed=0
		done+=1
		yoda1.grid_remove()
		yoda2.grid_remove()
	elif press >= 2 and rPressed >= 2:
		press=0
		vPressed=0
		yPressed=0
		rPressed=0
		ePressed=0
		jPressed=0
		hPressed=0
		done+=1
		r1.grid_remove()
		r2.grid_remove()
	elif press >= 2 and ePressed >= 2:
		press=0
		vPressed=0
		yPressed=0
		rPressed=0
		ePressed=0
		jPressed=0
		hPressed=0
		done+=1
		ewok1.grid_remove()
		ewok2.grid_remove()
	elif press >= 2 and jPressed >= 2:
		press=0
		vPressed=0
		yPressed=0
		rPressed=0
		ePressed=0
		jPressed=0
		hPressed=0
		done+=1
		jabba1.grid_remove()
		jabba2.grid_remove()
	elif press >= 2 and hPressed >= 2:
		press=0
		vPressed=0
		yPressed=0
		rPressed=0
		ePressed=0
		jPressed=0
		hPressed=0
		done+=1
		hoth1.grid_remove()
		hoth2.grid_remove()
	elif press >= 2:
		press=0
		vPressed=0
		yPressed=0
		rPressed=0
		ePressed=0
		jPressed=0
		hPressed=0
		vader1.config(text='')
		vader2.config(text='')
		yoda1.config(text='')
		yoda2.config(text='')
		r1.config(text='')
		r2.config(text='')
		jabba1.config(text='')
		jabba2.config(text='')
		hoth1.config(text='')
		hoth2.config(text='')
		ewok1.config(text='')
		ewok2.config(text='')
		vader1.config(state="normal")
		vader2.config(state="normal")
		yoda1.config(state="normal")
		yoda2.config(state="normal")
		r1.config(state="normal")
		r2.config(state="normal")
		jabba1.config(state="normal")
		jabba2.config(state="normal")
		hoth1.config(state="normal")
		hoth2.config(state="normal")
		ewok1.config(state="normal")
		ewok2.config(state="normal")
	#elif done==2:
		#rame.grid_remove()
		#playAgain.pack()


def checkV1():
	global press
	global vPressed
	global yPressed
	global rPressed
	global ePressed
	global jPressed
	global hPressed
	global click
	vader1.config(text='Daisy',font='bold')
	vader1.config(state="disabled")
	press+=1
	vPressed+=1
	click+=1
	clicks.config(text="Clicks: " + str(click))
	root.after(1000, checkCards)
def checkV2():
	global press
	global vPressed
	global yPressed
	global rPressed
	global ePressed
	global jPressed
	global hPressed
	global click
	vader2.config(text='Daisy',font='bold')
	vader2.config(state="disabled")
	press+=1
	vPressed+=1
	click+=1
	clicks.config(text="Clicks: " + str(click))
	root.after(1000, checkCards)
def checkY1():
	global press
	global vPressed
	global yPressed
	global rPressed
	global ePressed
	global jPressed
	global hPressed
	global click
	yoda1.config(text='Rose',font='bold')
	yoda1.config(state="disabled")
	press+=1
	yPressed+=1
	click+=1
	clicks.config(text="Clicks: " + str(click))
	root.after(1000, checkCards)
def checkY2():
	global press
	global vPressed
	global yPressed
	global rPressed
	global ePressed
	global jPressed
	global hPressed
	global click
	yoda2.config(text='Rose',font='bold')
	yoda2.config(state="disabled")
	press+=1
	yPressed+=1
	click+=1
	clicks.config(text="Clicks: " + str(click))
	root.after(1000, checkCards)
def checkR1():
	global press
	global vPressed
	global yPressed
	global rPressed
	global ePressed
	global jPressed
	global hPressed
	global click
	r1.config(text='Tulip',font='bold')
	r1.config(state="disabled")
	press+=1
	rPressed+=1
	click+=1
	clicks.config(text="Clicks: " + str(click))
	root.after(1000, checkCards)
def checkR2():
	global press
	global vPressed
	global yPressed
	global rPressed
	global ePressed
	global jPressed
	global hPressed
	global click
	r2.config(text='Tulip',font='bold')
	r2.config(state="disabled")
	press+=1
	rPressed+=1
	click+=1
	clicks.config(text="Clicks: " + str(click))
	root.after(1000, checkCards)
def checkE1():
	global press
	global vPressed
	global yPressed
	global rPressed
	global ePressed
	global jPressed
	global hPressed
	global click
	ewok1.config(text='Violet',font='bold')
	ewok1.config(state="disabled")
	press+=1
	ePressed+=1
	click+=1
	clicks.config(text="Clicks: " + str(click))
	root.after(1000, checkCards)
def checkE2():
	global press
	global vPressed
	global yPressed
	global rPressed
	global ePressed
	global jPressed
	global hPressed
	global click
	ewok2.config(text='Violet',font='bold')
	ewok2.config(state="disabled")
	press+=1
	ePressed+=1
	click+=1
	clicks.config(text="Clicks: " + str(click))
	root.after(1000, checkCards)
def checkJ1():
	global press
	global vPressed
	global yPressed
	global rPressed
	global ePressed
	global jPressed
	global hPressed
	global click
	jabba1.config(text='Lily',font='bold')
	jabba1.config(state="disabled")
	press+=1
	jPressed+=1
	click+=1
	clicks.config(text="Clicks: " + str(click))
	root.after(1000, checkCards)
def checkJ2():
	global press
	global vPressed
	global yPressed
	global rPressed
	global ePressed
	global jPressed
	global hPressed
	global click
	jabba2.config(text='Lily',font='bold')
	jabba2.config(state="disabled")
	press+=1
	jPressed+=1
	click+=1
	clicks.config(text="Clicks: " + str(click))
	root.after(1000, checkCards)
def checkH1():
	global press
	global vPressed
	global yPressed
	global rPressed
	global ePressed
	global jPressed
	global hPressed
	global click
	hoth1.config(text='Orchids',font='bold')
	hoth1.config(state="disabled")
	press+=1
	hPressed+=1
	click+=1
	clicks.config(text="Clicks: " + str(click))
	root.after(1000, checkCards)
def checkH2():
	global press
	global vPressed
	global yPressed
	global rPressed
	global ePressed
	global jPressed
	global hPressed
	global click
	hoth2.config(text='Orchids',font='bold')
	hoth2.config(state="disabled")
	press+=1
	hPressed+=1
	click+=1
	clicks.config(text="Clicks: " + str(click))
	root.after(1000, checkCards)



root = Tk()
root.title("Memory Game")

#Set size of window
root.geometry("2000x1000")
label = Label(root, text="Memory Game",font=("Arial", 20, "bold"))
frame = Frame(root,)

clicks = Label(root, text="Clicks: " + str(click), font=("Arial", 20, "bold"))

vader1 = Button(frame,height=175,width=175, command = checkV1,text='')
vader2 = Button(frame,height=175,width=175, command = checkV2,text='')
yoda1 = Button(frame,height=175,width=175, command = checkY1,text='')
yoda2 = Button(frame,height=175,width=175, command = checkY2,text='')
r1 = Button(frame, text="",height=175,width=175,command = checkR1)
r2 = Button(frame, text="",height=175,width=175,command = checkR2)
ewok1 = Button(frame,height=175,width=175, command = checkE1,text='')
ewok2 = Button(frame,height=175,width=175, command = checkE2,text='')
jabba1 = Button(frame,height=175,width=175, command = checkJ1,text='')
jabba2 = Button(frame,height=175,width=175, command = checkJ2,text='')
hoth1 = Button(frame,height=175,width=175, command = checkH1,text='')
hoth2 = Button(frame,height=175,width=175, command = checkH2,text='')

#playAgain = Button(root, text='Press to Play Again',command = rePlay,font=("Arial", 20, "bold"))
#playAgain.pack_forget()
label.pack(pady=25)
clicks.pack(pady=20)
frame.pack(pady=20)

assign()


root.mainloop()