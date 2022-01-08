#!/usr/bin/env python
# coding: utf-8

# In[1]:


#tkinter - standard Python interface to the Tcl/Tk GUI toolkit   
from tkinter import *
import math as m 

#constant is a type of variable whose value cannot be changed
PINK = '#e2979c'
RED = '#e7305b'
GREEN = '#9bdeac'
YELLOW = '#f7f5dd'
FONT = ('Courier', 25, 'normal')
WORK_TIME = 1
SHORT_BREAK = 5
LONG_BREAK = 20
#reps - repitition 
reps = 0
timer = None

def reset_timer():
    #after_cancel() - in order to cancel or stop a particular schedule of a callback function
    window.after_cancel(timer)
    #itemconfig() - configure resources of an item TAGORID
    canvas.itemconfig(timer_text, text = '00:00')
    title_label.config(text = 'Timer')
    check_marks.config(text = '')
    #global keyword allows you to modify the variable outside of the current scope
    global reps
    reps = 0
    
def start_timer():
    #global keyword allows you to modify the variable outside of the current scope
    global reps
    reps += 1
    work_time = WORK_TIME * 60
    short_break = SHORT_BREAK * 60
    long_break = LONG_BREAK * 60
    #8th repitition - if statement
    if reps % 8 == 0:
        count_down(long_break)
        title_label.config(text = 'Relax!', fg = RED)
    #1st/3rd/5th/7th repitition - elif statement
    elif reps % 2 == 0:
        count_down(short_break)
        title_label.config(text = 'Relax!', fg = PINK)
    #work - else statement
    else:
        count_down(work_time)
        title_label.config(text = 'Go back to work!', fg = GREEN)
        
def count_down(count):
    #floor() - returns the largest integer not greater than x
    #m.floor(300.16) - 300.0
    #minutes
    count_min = m.floor(count / 60)
    #seconds
    count_sec = count % 60
    if count_sec < 10:
        #0:9 - 0:09 - formatting
        count_sec = f'0{count_sec}'
    #itemconfig() - need to configure the Canvas item dynamically
    #text = '00:00' - formatting
    canvas.itemconfig(timer_text, text = f'{count_min}:{count_sec}')
    if count > 0:
        #global keyword allows you to modify the variable outside of the current scope
        global timer
        #after() - calls the callback function
        #1000 ms - 1s - time it takes to call the function
        timer = window.after(1000, count_down, count - 1)
    else:
        #note - create a checkmark for every completed session
        start_timer()
        marks = ''
        #2 reps = 1 work session and 1 break
        work_session = m.floor(reps / 2)
        for _ in range(work_session):
            marks += '✓'
        check_marks.config(text = marks)
        
#Tk() - allows you to register and unregister a callback function which will be called from the Tk mainloop
window = Tk()
window.title('Pomodoro Technique Clock')
#padx and pady - a distance - designating external padding on each side of the slave widget
window.config(padx = 100, pady = 50, bg = YELLOW)
#fg - foreground color / bg - background color
#Label - this widget implements a display box where you can place text or image
title_label = Label(text = 'Timer', fg = GREEN, bg = YELLOW, font = FONT)
title_label.grid(column = 1, row = 0)

#fg - foreground color / bg - background color
canvas = Canvas(width = 200, height = 225, bg = YELLOW, highlightthickness = 0)
#PhotoImage - to display images in labels, buttons, canvases, and text widgets
p_img = PhotoImage(file = 'tomato.png')
#c.create_image(x, y, option, ...)
#c.create_image() - this constructor returns the integer ID number of the image object for that canvas
canvas.create_image(100, 112, image = p_img)
#c.create_text() - this returns the object ID of the text object on canvas
timer_text = canvas.create_text(100, 125, text = '00:00', fill = 'white', font = FONT)
canvas.grid(column = 1, row = 1)

#command calls the function
start_button = Button(text = 'Start', highlightthickness = 0, command = start_timer)
start_button.grid(column = 0, row = 2)
#command calls the function
reset_button = Button(text = 'Reset', highlightthickness = 0, command = reset_timer)
reset_button.grid(column = 2, row = 2)
#fg - foreground color / bg - background color
check_marks = Label(fg = GREEN, bg = YELLOW)
check_marks.grid(column = 1, row = 3)

#mainloop() - tells Python to run the Tkinter event loop
window.mainloop()


# In[ ]:




