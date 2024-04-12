from tkinter import *
import tkinter as tk
import datetime
import time
import sqlite3
import webbrowser
import subprocess
import sys
import os
from math import sin,cos
import math
from tkmacosx import Button
from time import time, sleep
import pygame



#import datetime
#from datetime import datetime
#from datetime import date
#from datetime import date

#colour selection
Blue = ["light blue", "powder blue"]
Dark = ['#%02x%02x%02x' % (36, 36, 36), '#%02x%02x%02x' % (61, 61, 61)]
Light = ['#%02x%02x%02x' % (255, 255, 255), '#%02x%02x%02x' % (200, 200, 200)]
Pink = ['#%02x%02x%02x' % (241, 223, 235), '#%02x%02x%02x' % (245, 188, 245)]
Red = ['#%02x%02x%02x' % (255, 130, 130), '#%02x%02x%02x' % (255, 110, 110)]

#Main Functions
home = Tk()
home.title('Ceyaltiran - The Student Efficiency Software')
home.geometry("1920x1080")
Mycolour = Blue
home.configure(background=Mycolour[0])

#creates a database if it donst exist
conn = sqlite3.connect('database.db') ##connects to database
c = conn.cursor() #create cursor

c.execute("""CREATE TABLE IF NOT EXISTS tasks (
		task text, 
		repetition text
  )""")


c.execute("""CREATE TABLE IF NOT EXISTS repetition_tasks (
		repetition_task text, 
		repetition_repetition text,
		date1 text,
		active text
  )""")

c.execute("""CREATE TABLE IF NOT EXISTS book (
		title text,
		data text
  )""")
conn.commit() #commit changes
conn.close() #Close Connection

################################################################ SEARCH BAR ##########################################################################
#https://stackoverflow.com/questions/4216985/call-to-operating-system-to-open-url
def search():
	URL = "https://www.google.com.tr/search?q=" + SearchBarEntry.get() #this will 
	if sys.platform == 'darwin':    # in case of OS X
		subprocess.Popen(['open', URL])
	else:
		webbrowser.open_new_tab(URL)
	#clears the search bar input values
	SearchBarEntry.delete(0,"end")


################################################################ BACKGROUND CHANGER ######################$###########################################

def ChangeBG(value): #changes the background or text depending on the color chosen
	canvas1.delete("all")
	canvas2.delete("all")
	canvas3.delete("all")

	if value == "Blue":
		Mycolour = Blue
		SearchBarLabel.config(fg="black")
		date_label.config(fg="black")
		task_entry_label.config(fg='black')
		task_listbox.config(fg='black')
		timer.config(fg='black')
		book_data_text.config(fg='black')
		title_entry_label.config(fg='black')
		title_entry_label.config(fg='black')
		SearchBarEntry.config(fg='black')
		task_entry.config(fg='black')
		title_entry.config(fg='black')


	elif value == "Dark":
		Mycolour = Dark
		SearchBarLabel.config(fg="White")
		date_label.config(fg="white")
		task_entry_label.config(fg='white')
		task_listbox.config(fg='white')
		timer.config(fg='white')
		book_data_text.config(fg='white')
		title_entry_label.config(fg='white')
		book_data_text.config(highlightbackground='white')
		SearchBarEntry.config(fg='white')
		task_entry.config(fg='white')
		title_entry.config(fg='white')


	elif value == 'Red':
		Mycolour = Red
		SearchBarLabel.config(fg="black")
		date_label.config(fg="black")
		task_entry_label.config(fg='black')
		task_listbox.config(fg='black')
		timer.config(fg='black')
		book_data_text.config(fg='black')
		title_entry_label.config(fg='black')
		title_entry_label.config(fg='black')
		SearchBarEntry.config(fg='black')
		task_entry.config(fg='black')
		title_entry.config(fg='black')

	#configures the changes to all componenets
	home.config(background= Mycolour[0])
	frame_digital_clock.config(background=Mycolour[0])
	frame_to_do_list.config(background= Mycolour[0])
	canvas.config(background= Mycolour[0])
	timer.config(background= Mycolour[0])
	frame_search.config(background= Mycolour[0])
	frame_notebook.config(background= Mycolour[0])
	SearchBarEntry.config(highlightbackground=Mycolour[0], bg=Mycolour[1])
	SearchBarLabel.config(bg=Mycolour[0])
	SearchButton.config(highlightbackground=Mycolour[0])
	colourSelect.config(background=Mycolour[0])
	task_entry.config(background=Mycolour[0], bg=Mycolour[1])
	repetition_listbox.config(background=Mycolour[0])
	task_listbox.config(background=Mycolour[0])
	add_task.config(highlightbackground=Mycolour[0])
	delete.config(highlightbackground=Mycolour[0])
	clear.config(highlightbackground=Mycolour[0])
	date_label.config(background=Mycolour[0], highlightbackground=Mycolour[0])
	start_button.config(highlightbackground=Mycolour[0])
	stop_button.config(highlightbackground=Mycolour[0])
	delete_button.config(highlightbackground=Mycolour[0])
	save_button.config(highlightbackground=Mycolour[0])
	task_entry_label.config(background=Mycolour[0])
	task_entry.config(highlightbackground=Mycolour[0], bg=Mycolour[1])
	canvas1.config(background= Mycolour[0], highlightbackground=Mycolour[0])
	canvas2.config(background= Mycolour[0], highlightbackground=Mycolour[0])
	canvas3.config(background= Mycolour[0], highlightbackground=Mycolour[0])
	canvas4.config(background= Mycolour[0], highlightbackground=Mycolour[0])
	frame_search.config(background= Mycolour[0], highlightbackground=Mycolour[0])
	frame_to_do_list.config(background= Mycolour[0], highlightbackground=Mycolour[0])
	frame_notebook.config(background= Mycolour[0], highlightbackground=Mycolour[0])
	frame_digital_clock.config(background= Mycolour[0], highlightbackground=Mycolour[0])
	pages_optionmenu.config(background=Mycolour[0])
	title_entry.config(highlightbackground=Mycolour[0], bg=Mycolour[1])
	book_data_text.config(background=Mycolour[0])
	title_entry_label.config(background=Mycolour[0])
	save_button.config(background=Mycolour[0])
	delete_button.config(background=Mycolour[0])
	start_button.config(background=Mycolour[0])
	stop_button.config(background=Mycolour[0])



	if value == 'Blue':
		border1(canvas1, 20, 3, 470, 710, 15, 'black')
		border2(canvas2, 5, 10, 405, 700, 15, 'black')
		border3(canvas3, 50, 5, 400, 180, 15, 'black')

	elif value == 'Dark':
		border1(canvas1, 20, 3, 470, 710, 15, 'white')
		border2(canvas2, 5, 10, 405, 700, 15, 'white')
		border3(canvas3, 50, 5, 400, 180, 15, 'white')

	else:
		border1(canvas1, 20, 3, 470, 710, 15, 'black')
		border2(canvas2, 5, 10, 405, 700, 15, 'black')
		border3(canvas3, 50, 5, 400, 180, 15, 'black')






##################################### TO DO LIST #####################################################################################################

def save(): #saves data into database
	conn = sqlite3.connect('database.db')
	c = conn.cursor()	

	repetition = repetition_click_listbox.get() 
	if repetition != "Never": #checks which database to insert the task to

		date1 = str(datetime.datetime.now().year) + ' ' + str(datetime.datetime.now().month) + ' ' + str(datetime.datetime.now().day)

		c.execute("INSERT INTO repetition_tasks VALUES (:repetition_task, :repetition_repetition, :date1, :active)", #insert values into table

		{
			'repetition_task': task_entry.get(),
			'repetition_repetition': repetition_click_listbox.get(),
			'date1': date1,
			'active': "yes!"
		})

	else:
		#insert values into table
		c.execute("INSERT INTO tasks VALUES (:task, :repetition)",
			{
				'task': task_entry.get(),
				'repetition': repetition_click_listbox.get()
			})

	conn.commit()
	conn.close()
	insert()


def insert(): #inserts all the tasks unless there repetition is off
	task_listbox.delete(0,'end')
	conn = sqlite3.connect('database.db')
	c = conn.cursor()

	c.execute("SELECT *, oid FROM tasks") #selects the all the records
	records = c.fetchall()
	print_records = ''

	for record in records: #inserts the records into the lisbox appropriately
		print_records =  str(record[0]) + ' ' + str(record[1]) + "\n"
		task_listbox.insert(END, print_records) 

	#gets the records 
	c.execute("SELECT *, oid FROM repetition_tasks WHERE active = 'yes!'") #slects appropriate records to insert into listbox
	records = c.fetchall()
	print_records = ''
	for record in records: #inserts the records into the lisbox appropriately
		print_records =  str(record[0]) + ' '  + str(record[1]) + "\n"
		task_listbox.insert(END, print_records)
		repetition = record[1]
		
	task_entry.delete(0, END)
	repetition_click_listbox.set("Never")

	conn.commit()
	conn.close()

def findID(): #finds the primary key by searching for the task name in the database
	global ID
	conn = sqlite3.connect('database.db')
	c = conn.cursor()
	task_name = task_listbox.get(ANCHOR).split(' ' + repetition_type)[0] #gets task name from listbox

	find_repetition_type()

	if repetition_type[0] == "N": #checks which database to find the primary key from 
		c.execute("SELECT oid, * FROM tasks WHERE task=?", (str(task_name),)) #finds the primary key using the task name
		ID = c.fetchall()[0][0]
	else:
		c.execute("SELECT oid, repetition_task FROM repetition_tasks WHERE repetition_task=?", (str(task_name),)) #finds the primary key using the task name
		ID = c.fetchall()[0][0]

	conn.commit()
	conn.close()

def find_repetition_type():
	global repetition_type
	#gets the ID and repetition typr from listbox
	string = task_listbox.get(ANCHOR)
	string = string.split()
	repetition_type = string[-1]


def delete():
	find_repetition_type()

	findID()

	conn = sqlite3.connect('database.db')
	c = conn.cursor()
	task_name = task_listbox.get(ANCHOR).split(' ' + repetition_type)[0] #gets task name from listbox

	if repetition_type[0] == "N": #checks if the repetition task is never
		c.execute("DELETE FROM tasks WHERE oid = ?", (ID,)) 
	else: 
		c.execute("DELETE FROM repetition_tasks WHERE oid = ?", (ID,)) 

	task_listbox.delete(ANCHOR) #deletes the task from the listbox 
	conn.commit()
	conn.close()


def clear():
	find_repetition_type()
	findID()

	conn = sqlite3.connect('database.db')
	c = conn.cursor()

	c.execute("SELECT oid, * FROM repetition_tasks")  #selects all the records

	if repetition_type == "Never":

		task_listbox.delete(ANCHOR)
		c.execute("DELETE from tasks WHERE oid = " + str(ID)) #deletes the records

	else:
		date1_y,date1_m,date1_d = str(datetime.datetime.now().year), str(datetime.datetime.now().month), str(datetime.datetime.now().day) #gets todays date
		#changes the date so that the program can determine when to display the task again	
		date1 = (date1_y+" "+date1_m+" "+date1_d)
		
		c.execute("UPDATE repetition_tasks SET date1=? WHERE oid=?", (date1,ID)) #changes the date so that the program can determine when to display the task again in the database
		c.execute("UPDATE repetition_tasks SET active = 'no!' WHERE oid="+str(ID)) #allows the program to detect the task has been cleared and it will be displayed the next day or week depending on the repetition type they have chosen
		task_listbox.delete(ANCHOR)

	#commit changes
	conn.commit()
	# Close Connection
	conn.close()
	check()



#checks if its time for the repetition tasks can be displayed again
def check():
	conn = sqlite3.connect('database.db')
	c = conn.cursor()

	date1_y,date1_m,date1_d = str(datetime.datetime.now().year), str(datetime.datetime.now().month), str(datetime.datetime.now().day) #gets todays date
	date3 = (date1_y+" "+date1_m+" "+date1_d) #formats the date
	c.execute("SELECT oid, * FROM repetition_tasks")
	records= c.fetchall()

	for record in records:
		date2 = record[3]
		date2_y, date2_m, date2_d = date2.split(' ')[0], date2.split(' ')[1], date2.split(' ')[2] #sorts the date in a appropriate format so that calculations can be made
		repetition, active = record[2], record[4]

		if active == 'no!':
			date_diff = ((int(date1_y)*365.25 + int(date1_m)*30.4167 + int(date1_d)) - (int(date2_y)*365.25 + int(date2_m)*30.4167 + int(date2_d))) #calculates the date difference between now and the time the user cleared the task

			if repetition == 'Daily':
				if date_diff >= 1:
					TaskToInsert = (str(record[1]) + " " + str(record[2]))
					task_listbox.insert(0, TaskToInsert)

					c.execute("UPDATE repetition_tasks SET date1=? WHERE oid=?", (date3,record[0])) #changes the date so that the program can determine when to display the task again in the database
					c.execute("UPDATE repetition_tasks SET active=? WHERE oid=?", ("yes!", record[0])) #shows that the task hasnt yet been cleared, hence called 'active'

			elif repetition == 'Weekly':
				if date_diff >= 7:
					TaskToInsert = (str(record[1]) + " " + str(record[2]))
					task_listbox.insert(0, TaskToInsert)
					
					c.execute("UPDATE repetition_tasks SET active=? WHERE oid=?", ("yes!", record[0])) #shows that the task hasnt yet been cleared, hence called 'active'
					c.execute("UPDATE repetition_tasks SET date1=? WHERE oid=?", (date3,record[0])) #changes the date so that the program can determine when to display the task again in the database
		
	conn.commit()
	conn.close()
	

	home.after(10000, lambda: check())





def get_selected_row(event): #displays the task selected into task_entry box
	find_repetition_type() #gets repition type
	findID() #gets the ID
	conn = sqlite3.connect('database.db')
	c = conn.cursor()

	if repetition_type == 'Never': #selects the task name through the database
		c.execute("SELECT *, oid FROM tasks WHERE oid ="+str(ID)) 
	else:
		c.execute("SELECT *, oid FROM repetition_tasks WHERE oid ="+str(ID))
	task_name = c.fetchall()[0][0]
	task_entry.delete(0, END)
	task_entry.insert(END, task_name) #displays the task into task_entry box

	conn.commit()
	conn.close()


##################################### POMODORO STOP WATCH #############################################################################################

#https://stackoverflow.com/questions/30246709/tkinter-analog-clock-refreshing-how-does-after-function-work
global pi
pi = math.pi 

def DrawClockBackground(radius, center, line):  #function drawing the backgroud of the clock where center is the centre coordiantes for x and y, and line is the markings on the sides of the clock
	drawcircle(radius + (radius/30), "dark grey", center) #black background
	drawcircle(radius, "ivory3", center) #grey backgroud
	drawcircle(radius/80, "dark grey", center) #central point/needle articulation
	canvas.create_line(center, center - (line - (line/15)), center, center - (line - (line/5))) #creates 0th min marking line
	canvas.create_line(center + (line - (line/15)), center, center + (line - (line/5)), center) #creates the 15th min marking line
	canvas.create_line(center, center + (line - (line/15)), center, center + (line - (line/5))) #creates 30th min marking line
	canvas.create_line(center - (line - (line/15)), center, center - (line - (line/5)), center) #creates 45th min marking line

def drawcircle(ClockBorder,colour, center): #draw a circle based on center from the given coordinates, radius and colour
	left_point,top_point,right_point,bottom_point=center-ClockBorder, center-ClockBorder, center+ClockBorder, center+ClockBorder
	canvas.create_oval(left_point,top_point,right_point,bottom_point, fill=colour)

def start_timer(): #gets the time when the button was pressed
	global clock_run
	initialTime = (datetime.datetime.now().microsecond)/60000000 + (datetime.datetime.now().second)/60 + (datetime.datetime.now().minute) + (datetime.datetime.now().hour)*3600 #inital time when the program was started
	initial_second, initial_minute, initial_hour = datetime.datetime.now().second, datetime.datetime.now().minute, datetime.datetime.now().hour
	change_in_second, change_in_minute, change_in_hour = 0,0,0
	clock_run=True
	Time(initialTime, initial_second, initial_minute, initial_hour, change_in_second, change_in_minute, change_in_hour)

def Time(initialTime, initial_second, initial_minute, initial_hour, change_in_second, change_in_minute, change_in_hour):#calculates the change in time (stopwatch)
	DrawClockBackground(200, 250, 200)

	change_in_time = (datetime.datetime.now().microsecond)/60000000 + (datetime.datetime.now().second)/60 + (datetime.datetime.now().minute) + (datetime.datetime.now().hour)*3600  - initialTime
	change_in_second, change_in_minute, change_in_hour = datetime.datetime.now().second - initial_second, datetime.datetime.now().minute - initial_minute, datetime.datetime.now().hour - initial_hour
	if change_in_second < 0:
		change_in_second = change_in_second + 60
		change_in_minute = change_in_minute - 1
	if change_in_minute < 0:
		change_in_minute = change_in_minute + 60
		change_in_hour = change_in_hour - 1
	
	tick(change_in_time, change_in_time, change_in_second, change_in_minute, change_in_hour)
	
	if clock_run==True:
		home.after(1000, lambda: Time(initialTime, initial_second, initial_minute, initial_hour, change_in_second, change_in_minute, change_in_hour))
	else: 
		timer.config(text='00:00:00')


def tick(Minute, change_in_time, change_in_second, change_in_minute, change_in_hour): #redraws the minute hand roughly every 3 seconds
	Minute = (Minute-15)*6
	x1, y1, x2, y2 = 250 - (200/10) * cos(math.radians(Minute)), 250 - (200/10) * sin(math.radians(Minute)), 250 + (200/1.6) * cos(math.radians(Minute)), 250 + (200/1.6) * sin(math.radians(Minute))
	canvas.create_line(x1, y1, x2, y2)
	
	angle = math.degrees(math.atan((y2-y1)/(x2-x1)))
	if change_in_second < 10: #manipulates the numbers into a digital clock format (HH:MM:SS)
		change_in_second = '0' + str(change_in_second)
	if change_in_minute < 10:
		change_in_minute = '0' + str(change_in_minute)
	if change_in_hour <10:
		change_in_hour = '0' + str(change_in_hour)

	if  60 <= int(angle) <=90:
		timer.config(text='Break Time')
		pygame.mixer.init()
		pygame.mixer.music.load("5 min break.mp3")
		pygame.mixer.music.play()

	else:
		timer.config(text=str(change_in_hour) + ':' + str(change_in_minute) + ':' + str(change_in_second))





def stop_clock(): #Stops the clock
	global clock_run
	clock_run=False

########################################################## NOTEPAD #####################################################################################

def save_page(): #saves changes to the pages and title
	option_menu = pages_click_optionmenu.get()
	conn = sqlite3.connect('database.db') 
	title, book_data = title_entry.get(), book_data_text.get("1.0",'end-1c')
	c = conn.cursor()
	if option_menu == 'New Page':
		c.execute("INSERT INTO book VALUES (:title, :data)",
			{
				'title': title,
				'data': book_data
			})
	else:
		c.execute("UPDATE book SET title=? WHERE oid=?", (title, page_ID,))
		c.execute("UPDATE book SET data=? WHERE oid=?", (book_data, page_ID,))
	conn.commit()
	conn.close()
	pages_click_optionmenu.set(str(title))
	selectPages()

def delete_page(): #deletes the selected page
	conn = sqlite3.connect('database.db')
	c = conn.cursor()
	if pages_click_optionmenu.get() == 'New Page':
		return

	c.execute("DELETE FROM book WHERE oid =?", (page_ID,)) #deletes the record

	conn.commit()
	conn.close()
	title_entry.delete(0, END) #removes data from title entry
	book_data_text.delete('1.0', END) #removes data from the page
	pages_click_optionmenu.set('New Page')
	selectPages()

#https://stackoverflow.com/questions/17580218/changing-the-options-of-a-optionmenu-when-clicking-a-button
def selectPages(): #gets the titles of all the books and puts it in the drop down menu
	pages_optionmenu['menu'].delete(0, 'end')
	conn = sqlite3.connect('database.db') 
	c = conn.cursor()

	c.execute("SELECT *, oid FROM book") #selects all data from the table

	records = c.fetchall()
	pages_optionmenu['menu'].add_command(label='New Page', command=tk._setit(pages_click_optionmenu, 'New Page'))
	for i in records: #puts all the titles of the pages in the drop down box
		options = str(i[0])
		pages_optionmenu['menu'].add_command(label=options, command=tk._setit(pages_click_optionmenu, options))
	conn.commit()
	conn.close()

def callback(*args): #inputs the title and book data into the appropriate text widget
	global page_ID #allows all the modules to find the ID 
	title = pages_click_optionmenu.get()
	
	if title == 'New Page': #checks if the user is trying to make a new page
		title_entry.delete(0, END)
		book_data_text.delete('1.0', END)
		return #stops the execution of the module
	
	conn = sqlite3.connect('database.db') 
	c = conn.cursor()

	c.execute("SELECT oid, * FROM book WHERE title=?", (str(title),)) #slects the appropriate record so that the primary key can be found and the data of the note pad can be inserted
	record=c.fetchall()
	title_entry.delete(0, END)
	book_data_text.delete('1.0', END)
	title_entry.insert(END, record[0][1]) #inserts the title into the entry box
	book_data_text.insert(END, record[0][2]) #inserts the data of the page into the text box
	page_ID=record[0][0] #identifies the primary key 

	conn.commit()
	conn.close()





#creates canvas for so that the curved borders can be created
canvas1 = Canvas(home, background=Mycolour[0], highlightbackground=Mycolour[0], width=500, height=750)
canvas1.grid(row=2, column=0, ipady=10, rowspan=2)

canvas2 = Canvas(home, background=Mycolour[0], highlightbackground=Mycolour[0], width=1080, height=40)
canvas2.grid(row=0, column=0, columnspan=3, pady=20, rowspan=2)

canvas3 = Canvas(home, background=Mycolour[0], highlightbackground=Mycolour[0], width=410, height=760)
canvas3.grid(row=2, column=2, pady=20, rowspan=2)

canvas4 = Canvas(home, background=Mycolour[0], highlightbackground=Mycolour[0], width=500, height=200)
canvas4.grid(row=3, column=1, pady=15)


#creates the frames so everything is organied and canvas for clock
frame_search = LabelFrame(home, width=1080, height=40, background=Mycolour[0], bd=0)
frame_search.grid(row=0, column=0, columnspan=3, pady=0, padx=0)

frame_to_do_list = LabelFrame(home, width=500, height=750, background=Mycolour[0], bd=0)
frame_to_do_list.grid(row=1, column=0, pady=20, rowspan=3, padx=0)


#creates date title
date = datetime.datetime.now()
date = date.strftime("%B %d, %Y")
date_label = Label(home, text=date, bg=Mycolour[0], font=("", 40))
date_label.grid(row=1, column=1, pady=0, padx=0)


canvas = Canvas(home, width=500, height=500, background=Mycolour[0], highlightthickness=0)
canvas.grid(row=2, column=1)

frame_notebook = LabelFrame(home, width=400, height=750, background=Mycolour[0], bd=0)
frame_notebook.grid(row=1, column=2, pady=15, rowspan=3, padx=0)

frame_digital_clock = LabelFrame(home, width=500, height=200, background=Mycolour[0], bd=0)
frame_digital_clock.grid(row=3, column=1, pady=0, padx=0)


#SEARCHBAR WIDGETS
#create Entry box
SearchBarEntry = Entry(frame_search, width=120, highlightbackground=Mycolour[0], bd=0.5 ,insertwidth=1,bg=Mycolour[1])
SearchBarEntry.grid(row=1, column=1, padx=20, pady=(10, 0))

# Create text box label
SearchBarLabel = Label(frame_search, text="Search", bg=Mycolour[0])
SearchBarLabel.grid(row=1, column=0, pady=(10, 0), padx=10)
#creates button button
SearchButton = Button(frame_search, text="Search", highlightbackground=Mycolour[0], command= search, borderless=True)
SearchButton.grid(row=1, column=2, pady=(19, 10), ipadx=10, ipady=5)

#create dropdown box
colourSelect_click = StringVar(frame_search)
colourSelect_click.set("Blue")
colourSelect = OptionMenu(frame_search, colourSelect_click, "Blue", "Dark", 'Red', command=ChangeBG)
colourSelect.grid(row=1, column=3, pady=(10,0), padx=10)
colourSelect.configure(bg=Mycolour[0])


#TO DO LIST WIDGETS
#create text box 
task_entry_label = Label(frame_to_do_list, text='Task: ', font=('', 16), bg=Mycolour[0])
task_entry_label.grid(row=1, column=0, pady=5, padx=0)
task_entry = Entry(frame_to_do_list, highlightbackground=Mycolour[0], bd=0.5 ,insertwidth=1,bg=Mycolour[1], font=('', 16))
task_entry.grid(row=1, column=1, pady=10, padx=10)

#create repetition list box
repetition_click_listbox = StringVar(frame_to_do_list)
repetition_listbox = OptionMenu(frame_to_do_list, repetition_click_listbox, "Never", "Daily", "Weekly")
repetition_listbox.grid(row=1, column=2)
repetition_listbox.configure(bg=Mycolour[0])

#https://github.com/gn03249822/Python-GUI-Bookstore
#create list box
task_listbox = Listbox(frame_to_do_list, bg=Mycolour[0], font=("", 30), height=16, width=22)
task_listbox.grid(row=4, column=0, columnspan=4, pady=4)
task_listbox.bind('<<ListboxSelect>>', get_selected_row)

#creates buttons
add_task = Button(frame_to_do_list, text= "save", command=save, borderless=True, width=70)
add_task.grid(row=1, column=3)

delete = Button(frame_to_do_list, text="delete", command =delete, borderless=True, width=70)
delete.grid(row=0, column=3)

clear = Button(frame_to_do_list, text='clear', command = clear, borderless=True, width=70)
clear.grid(row=0, column=2)




#CLOCK WIDGETS
#creates image buttons for starting the clock
#https://stackoverflow.com/questions/4297949/image-on-a-button
start_image = PhotoImage(file='startB.png')
stop_image = PhotoImage(file='stopB.png')

start_button = Button(frame_digital_clock, image=start_image,command=start_timer, borderless=True, bd=4, background=Mycolour[0])
start_button.grid(row=0,column=0, padx=10)

stop_button = Button(frame_digital_clock, image=stop_image, bd=4,command=stop_clock, borderless=True, background=Mycolour[0])
stop_button.grid(row=0,column=1, padx=10)

timer = Label(frame_digital_clock,text='00:00:00' ,width=10, height=1, font=('',60), highlightbackground='black', highlightthickness=3, bg=Mycolour[0])
timer.grid(row=1, column=0, columnspan=2)




#NOTEBOOK WIDGETS
#creates image buttons for delete and save, and creates listbox for the pages
pages_click_optionmenu = StringVar(frame_notebook)
pages_optionmenu = OptionMenu(frame_notebook, pages_click_optionmenu,' ')
pages_optionmenu.config(width=24, font=('Helvetica', 12), bg=Mycolour[0])
pages_optionmenu.grid(row=0, column=0, pady=5, padx=5, columnspan=2)
pages_click_optionmenu.set('New Page')
pages_click_optionmenu.trace("w", callback)

save_image = PhotoImage(file='save.png')
save_button = Button(frame_notebook, image=save_image, bd=4, command=save_page, borderless=True, background=Mycolour[0])
save_button.grid(row=0, column=2, pady=5)

delete_image = PhotoImage(file='delete.png')
delete_button = Button(frame_notebook, image=delete_image, bd=4, command=delete_page, borderless=True, background=Mycolour[0])
delete_button.grid(row=0, column=3, pady=5)

title_entry_label = Label(frame_notebook, text= 'Title: ', bg=Mycolour[0])
title_entry_label.grid(row=1, column=0)
title_entry = Entry(frame_notebook, bg=Mycolour[0], width=25, bd=0.5 ,insertwidth=1, font=('', 16), highlightbackground=Mycolour[0])
title_entry.grid(row=1, column=1, padx=5, pady=5, columnspan=3)


book_data_text = Text(frame_notebook, width=34, height=29, font=('', 16), bg=Mycolour[0], highlightbackground='black', highlightthickness=0.5)
book_data_text.grid(row=2, column=0, columnspan=4, padx=5, pady=0)
book_data_text.insert(END, 'Type here: ')



#https://stackoverflow.com/questions/51425633/tkinter-how-to-make-a-rounded-corner-text-widget
def border1(canvas, x, y, width, height, curve, colour): #creates a border for the widows by drawing lines
    #creates the curved lines
    canvas1.create_arc(x, y, x+2*curve, y+2*curve, start= 90, extent=90, style="arc", fill=colour, outline=colour)
    canvas1.create_arc(x+width-2*curve, y+height-2*curve, x+width, y+height, start=270, extent=90, style="arc", fill=colour, outline=colour)
    canvas1.create_arc(x+width-2*curve, y, x+width, y+2*curve, start=  0, extent=90, style="arc", fill=colour, outline=colour)
    canvas1.create_arc(x, y+height-2*curve, x+2*curve, y+height, start=180, extent=90, style="arc", fill=colour, outline=colour)
    
    #creates straight lines
    canvas1.create_line(x+curve, y, x+width-curve, y, fill=colour)
    canvas1.create_line(x+curve, y+height, x+width-curve, y+height, fill=colour)
    canvas1.create_line(x, y+curve, x, y+height-curve, fill=colour)
    canvas1.create_line(x+width, y+curve, x+width, y+height-curve, fill=colour)

def border2(canvas, x, y, width, height, curve, colour): 
    canvas3.create_arc(x, y, x+2*curve, y+2*curve, start=90, extent=90, style="arc", fill=colour, outline=colour)
    canvas3.create_arc(x+width-2*curve, y+height-2*curve, x+width, y+height, start=270, extent=90, style="arc", fill=colour, outline=colour)
    canvas3.create_arc(x+width-2*curve, y, x+width, y+2*curve, start= 0, extent=90, style="arc", fill=colour, outline=colour)
    canvas3.create_arc(x, y+height-2*curve, x+2*curve, y+height, start=180, extent=90, style="arc", fill=colour, outline=colour)
    
    canvas3.create_line(x+curve, y, x+width-curve, y, fill=colour)
    canvas3.create_line(x+curve, y+height, x+width-curve, y+height, fill=colour)
    canvas3.create_line(x, y+curve, x, y+height-curve, fill=colour)
    canvas3.create_line(x+width, y+curve, x+width, y+height-curve, fill=colour)

def border3(canvas, x, y, width, height, curve, colour): 
	canvas4.create_arc(x, y, x+2*curve,   y+2*curve, start= 90, extent=90, style="arc", fill=colour, outline=colour)
	canvas4.create_arc(x+width-2*curve, y+height-2*curve, x+width, y+height, start=270, extent=90, style="arc", fill=colour, outline=colour)
	canvas4.create_arc(x+width-2*curve, y, x+width, y+2*curve, start=  0, extent=90, style="arc", fill=colour, outline=colour)
	canvas4.create_arc(x, y+height-2*curve, x+2*curve, y+height, start=180, extent=90, style="arc", fill=colour, outline=colour)
	
	canvas4.create_line(x+curve, y, x+width-curve, y, fill=colour)
	canvas4.create_line(x+curve, y+height, x+width-curve, y+height, fill=colour)
	canvas4.create_line(x, y+curve, x, y+height-curve, fill=colour)
	canvas4.create_line(x+width, y+curve, x+width, y+height-curve, fill=colour)



border1(canvas1, 20, 3, 470, 710, 15, 'black')
border2(canvas2, 5, 10, 405, 700, 15, 'black')
border3(canvas3, 50, 5, 400, 180, 15, 'black')







#calls the check() and insert() and DrawClockBackground() function
insert()
check()
DrawClockBackground(200, 250, 200)
selectPages()

home.mainloop()