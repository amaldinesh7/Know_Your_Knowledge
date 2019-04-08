#************************************************************* Micro Project 2016*****************************************************************
#************************************************************* This is a quiz game **************************************************************
#**********************************************************!!! KNOW YOUR KNOWLEDGE !!!************************************************************

'''
*******************************************************************Created By********************************************************************
******************************************************************AMAL DINESH********************************************************************
******************************************************************AROMAL BENNY*******************************************************************
'''

import Tkinter
from Tkinter import *
import db
import threading
from threading import Thread
import random
import time

questionif = 0       # Controls the question ans options
flag = 0
flag2 = 0
flag3 = 0

main = Tkinter.Tk()
main.title("KNOW YOUR KNOWLEDGE!")
main.configure(background="white")
#main.attributes('-alpha', 0.3)
def gamefn():				#main game function

	gamefn.flag4 = 0

	start_frame.destroy()

	def destroy():
		main_frame.destroy()

	def wrong_ans():					#if the answer is wrong
		global flag,flag3,questionif
		flag = 1
		flag3 = 1
		points = [1000, 2000, 5000, 10000, 25000, 50000, 100000, 200000, 500000]
		gamefn.flag4=1
		msg_but = Button(msg_frame, text="OK", width=4, command=ok_2, bg="#EC7063")
		msg_but.pack(side="bottom", pady=5)
		if questionif > 0:
			msg_var.set("OOPS..ITS WRONG \n YOU LOSE\nYou earned %d pts\n CLICK OK TO EXIT"%points[questionif-1])
		else:
			msg_var.set("OOPS..ITS WRONG \n YOU LOSE\nYou got 0 pts\n CLICK OK TO EXIT")
		quesnans.B1['state'] = DISABLED
		quesnans.B2['state'] = DISABLED
		quesnans.B3['state'] = DISABLED
		quesnans.B4['state'] = DISABLED
		return flag,flag3
		
	def right_ans():					#if the answer is right
		global flag3,questionif
		points=[1000,2000,5000,10000,25000,50000,100000,200000,500000]    # list for points
		if questionif < 9 :
			msg_var.set("CONGRATULATIONS.... \n\nYou Got %d pts\n\nPress OK to continue\n"%points[questionif])
		if questionif == 9 :
			msg_var.set("CONGRATULATIONS....\nIts end of the game\n\nPress OK to continue\n")
		flag3 = 1
		gamefn.flag4=1
		msg_but = Button(msg_frame, text="OK", width=4, command=ok, bg="#EC7063")
		msg_but.pack(side="bottom", pady=5)
		quesnans.B1['state'] = DISABLED
		quesnans.B2['state'] = DISABLED
		quesnans.B3['state'] = DISABLED
		quesnans.B4['state'] = DISABLED
		return flag3

	def time_out():						# if the timer ends
		msg_but = Button(msg_frame, text="OK", width=4, command=exit, bg="#EC7063")
		msg_but.pack(side="bottom", pady=5)

	def ok():							#for the ok button that appears on right answer
		global questionif
		questionif = questionif + 1

		def secondary():
			destroy()
			gamefn()
		secondary()
		return questionif

	def ok_2():							#for the ok button that appears on wrong answer
		if flag3 == 1:
			exit()
		global flag2
		flag2=1
		return flag2

	main_frame = Frame(main)                 #main frame in which all the content displays except starting frame
	main_frame.configure(background='white')
	main_frame.pack(fill=X)

	msg_frame = Frame(main_frame, height=4, bg="lightblue", bd=2, relief=RIDGE)
	msg_frame.pack()

	msg_var = StringVar()
	msg = Label(msg_frame, textvariable=msg_var, bg="lightblue", height=9, width=45, font=('ALGERIAN',16))
	msg.pack(pady=6)

	if questionif == 0:
		msg_var.set("1")

	if questionif >= 1:
		time.sleep(0.1)
		msg_var.set(questionif+1)

	if questionif == 10:
		msg_frame.destroy()
		final_frame = Frame(main, height=14, width=100, bg="lightgreen",bd=5, relief=SUNKEN,)
		final_frame.pack()
		won = StringVar()
		final_label = Label( final_frame, textvariable=won, height=14, width=100, font=("ALGERIAN",22),bg="lightgreen")
		final_label.pack()
		won.set("CONGRATULATIONS\n\nYOU WON THE GAME\n\nYOU GOT : 1000000")
		fin_but = Button( final_frame, text="EXIT", bg="ORANGE", width=15, height=6, command=exit, font=("comic sans ms",18))
		fin_but.pack(side="bottom",pady=70, padx=8)	
	
	def timer():								# function for timer
		timer_frame = Frame(main_frame, height=150)
		timer_frame.pack(fill=X, pady=12)
		canvas = Canvas(timer_frame, height=150, bg= "lightyellow")
		canvas.pack(fill=X)
		bar = canvas.create_rectangle(20,5, 30, 150, fill="#191163")
		for x in range(0,249):
			canvas.move(bar,5, 0)
			timer_frame.update()
			main_frame.update()
			time.sleep(0.10)
			if gamefn.flag4 == 1:
				T2.paused()
		msg_var.set("TIME OUT \n\n YOU LOSE \n\n CLICK OK TO EXIT")
		time_out()
		T2.paused()

	def quesnans():								# function for both question and answer

		tot_frame = Frame(main_frame, width=500)
		aa=bb=cc=dd=questionif
		for i in range(aa,10):
			if questionif == i :
				temp = random.choice(db.ques[questionif])
				ques_frame = Frame(tot_frame,width=500)
				ques_var = StringVar()
				ques = Label( ques_frame, textvariable=ques_var, relief=SUNKEN, justify=LEFT, height=4, font=('Helvitica',16),bg="yellow")
				ques_var.set(temp)
				ques.pack(side="bottom", fill=X)
				ques_frame.pack(side="top",pady=3, padx=5, fill=X)

		but_frame = Frame(tot_frame, bg="#CD5C5C")

		but_frame1 = Frame(but_frame, bg="#CD5C5C")
		but_frame2 = Frame(but_frame, bg="#CD5C5C")

		B1_var = StringVar()
		B2_var = StringVar()
		B3_var = StringVar()
		B4_var = StringVar()

		for j in range(bb,10):						# for setting the answer buttons
			if temp == db.ques[j][0]:
				quesnans.B1 = Tkinter.Button(but_frame1, textvariable=B1_var, padx=2, pady=2, width=30, command=right_ans, bg="#ADFF2F")
				quesnans.B2 = Tkinter.Button(but_frame1, textvariable=B2_var, padx=2, pady=2, width=30, command=wrong_ans, bg="#ADFF2F")
				quesnans.B3 = Tkinter.Button(but_frame2, textvariable=B3_var, padx=2, pady=2, width=30, command=wrong_ans, bg="#ADFF2F")
				quesnans.B4 = Tkinter.Button(but_frame2, textvariable=B4_var, padx=2, pady=2, width=30, command=wrong_ans, bg="#ADFF2F")
			elif temp == db.ques[j][1]:
				quesnans.B1 = Tkinter.Button(but_frame1, textvariable=B1_var, padx=2, pady=2, width=30, command=wrong_ans, bg="#ADFF2F")
				quesnans.B2 = Tkinter.Button(but_frame1, textvariable=B2_var, padx=2, pady=2, width=30, command=wrong_ans, bg="#ADFF2F")
				quesnans.B3 = Tkinter.Button(but_frame2, textvariable=B3_var, padx=2, pady=2, width=30, command=wrong_ans, bg="#ADFF2F")
				quesnans.B4 = Tkinter.Button(but_frame2, textvariable=B4_var, padx=2, pady=2, width=30, command=right_ans, bg="#ADFF2F")
			elif temp == db.ques[j][2]:
				quesnans.B1 = Tkinter.Button(but_frame1, textvariable=B1_var, padx=2, pady=2, width=30, command=wrong_ans, bg="#ADFF2F")
				quesnans.B2 = Tkinter.Button(but_frame1, textvariable=B2_var, padx=2, pady=2, width=30, command=wrong_ans, bg="#ADFF2F")
				quesnans.B3 = Tkinter.Button(but_frame2, textvariable=B3_var, padx=2, pady=2, width=30, command=right_ans, bg="#ADFF2F")
				quesnans.B4 = Tkinter.Button(but_frame2, textvariable=B4_var, padx=2, pady=2, width=30, command=wrong_ans, bg="#ADFF2F")
			elif temp == db.ques[j][3]:
				quesnans.B1 = Tkinter.Button(but_frame1, textvariable=B1_var, padx=2, pady=2, width=30, command=wrong_ans, bg="#ADFF2F")
				quesnans.B2 = Tkinter.Button(but_frame1, textvariable=B2_var, padx=2, pady=2, width=30, command=right_ans, bg="#ADFF2F")
				quesnans.B3 = Tkinter.Button(but_frame2, textvariable=B3_var, padx=2, pady=2, width=30, command=wrong_ans, bg="#ADFF2F")
				quesnans.B4 = Tkinter.Button(but_frame2, textvariable=B4_var, padx=2, pady=2, width=30, command=wrong_ans, bg="#ADFF2F")
			elif temp == db.ques[j][4]:
				quesnans.B1 = Tkinter.Button(but_frame1, textvariable=B1_var, padx=2, pady=2, width=30, command=right_ans, bg="#ADFF2F")
				quesnans.B2 = Tkinter.Button(but_frame1, textvariable=B2_var, padx=2, pady=2, width=30, command=wrong_ans, bg="#ADFF2F")
				quesnans.B3 = Tkinter.Button(but_frame2, textvariable=B3_var, padx=2, pady=2, width=30, command=wrong_ans, bg="#ADFF2F")
				quesnans.B4 = Tkinter.Button(but_frame2, textvariable=B4_var, padx=2, pady=2, width=30, command=wrong_ans, bg="#ADFF2F")
			else:
				pass

		for question in range(dd,10):						# for setting answers to the buttons
			if temp == db.ques[question][0]:
				B1_var.set(db.ans[question][0][1])
				B2_var.set(db.ans[question][0][2])
				B3_var.set(db.ans[question][0][3])
				B4_var.set(db.ans[question][0][4])
			if temp == db.ques[question][1]:
				B1_var.set(db.ans[question][1][1])
				B2_var.set(db.ans[question][1][2])
				B3_var.set(db.ans[question][1][3])
				B4_var.set(db.ans[question][1][4])
			if temp == db.ques[question][2]:
				B1_var.set(db.ans[question][2][1])
				B2_var.set(db.ans[question][2][2])
				B3_var.set(db.ans[question][2][3])
				B4_var.set(db.ans[question][2][4])
			if temp == db.ques[question][3]:
				B1_var.set(db.ans[question][3][1])
				B2_var.set(db.ans[question][3][2])
				B3_var.set(db.ans[question][3][3])
				B4_var.set(db.ans[question][3][4])
			if temp == db.ques[question][4]:
				B1_var.set(db.ans[question][4][1])
				B2_var.set(db.ans[question][4][2])
				B3_var.set(db.ans[question][4][3])
				B4_var.set(db.ans[question][4][4])

		quesnans.B1.pack(padx=100, pady=9, side="left")
		quesnans.B2.pack(padx=100, pady=9, side="right")
		quesnans.B4.pack(padx=100, pady=9, side="right")
		quesnans.B3.pack(padx=100, pady=9, side="left")

		but_frame1.pack(fill=X)
		but_frame2.pack(side="bottom", fill=X)

		but_frame.pack(side="bottom", fill=X, pady=7, padx=5)
		tot_frame.pack(side="bottom", fill=X, pady=8)

	T1=Thread(target=quesnans()).start()						# threading for running the timer() and quesnans() at the same time
	T2=Thread(target=timer()).start()

	if questionif >= 1:
		destroy()

start_frame = Frame(main, bg="#45B39D")

name_label = Label(start_frame,text="KNOW \n\n YOUR \n\n KNOWLEDGE!", relief=SUNKEN, font=("Jokerman",45), bg="#FA8072", fg="BLACK")
name_label.pack(fill=X, pady=115, padx=90, side="left")

one = Button(start_frame, text="PLAY", width=10, height=2, font=("AR DARLING", 16), command=gamefn, bg="#34495E", fg="white")
one.pack(pady=125, padx=40)

#three = Button(start_frame, text="CREDITS", width=10, height=2, font=("AR DARLING", 16), bg="#34495E", fg="white")
#three.pack(pady=65, padx=40)

four = Button(start_frame, text="EXIT", width=10, height=2, command=exit, font=("AR DARLING", 16), bg="#34495E", fg="white")
four.pack(pady=120, padx=40)

start_frame.pack(fill=X)
main.mainloop()

#gamefn()
