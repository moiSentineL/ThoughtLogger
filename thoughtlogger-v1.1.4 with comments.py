# Thought Logger v1.1.4
# Source Code
# Developer: moiSentineL (www.github.com/moiSentineL)
# Files: www.github.com/moiSentineL/Thought-Logger

# Code:

# Function Imports
import datetime
import os
import time
import tkinter as tk
import sys
import webbrowser as wb
from tkinter import font
from tkinter import messagebox

# Tkinter window initialize
main = tk.Tk()

# Labels and Entries
    # Label text
l1 = tk.Label(main, text = "Entry: ", font=("Calibri",12), bg= "black", fg= "white") 
l1.grid(row = 2, column = 0, sticky = tk.W, pady = 15, padx= 5)
    # Entry for text
logentry = tk.Entry(main, width= 37)
logentry.grid(row = 2, column = 1, pady = 2) 

# Functions
def entrywithenter(key):
    # Function to make entrying with a keypress possible.
    if logentry.get() == '':
        pass
    else:

        ts = time.time()
        sttime = datetime.datetime.fromtimestamp(ts).strftime('%d/%m/%y; %I:%M:%S %p : ')

        log = open("log.txt", "a")
        logwrite = log.write(sttime + logentry.get() + '\n')

        log.close()

        logentry.delete(0, 'end')
def entrywithbutton():
    # Function to make entrying with button possible.
    if logentry.get() == '':
        pass
    else:

        ts = time.time()
        sttime = datetime.datetime.fromtimestamp(ts).strftime('%d/%m/%y; %I:%M:%S %p : ')

        log = open("log.txt", "a")
        logwrite = log.write(sttime + logentry.get() + '\n')

        log.close()

        logentry.delete(0, 'end')
def seelog():
    # Function to open log file.
    if os.path.exists('log.txt') == True:
        wb.open("log.txt")
    else:
        tk.messagebox.showerror("File Does Not Exist", "The file 'log.txt' does not exist. Make a log first.\n\nIf this issue persists, report it on https://github.com/moiSentineL/Thought-Logger")
def exit(a):
    # Function to exit program.
    main.destroy()

# Keybindings
main.bind('<Return>', entrywithenter)
main.bind('<Escape>', exit)

# Buttons
    # Button to open log file.
seelog = tk.Button(main, text= "See Log", command=seelog)
seelog.grid(row= 4, column= 2, sticky= tk.W)
    # Button to entry the text.
logentry_button = tk.Button(main, text= "ok", command=entrywithbutton)
logentry_button.grid(row= 2, column= 2, padx = 15)

# (RECOMMENDED TO NOT TOUCH) Window Placement tweaks.
window_height = 95
window_width = 425
screen_width = main.winfo_screenwidth()
screen_height = main.winfo_screenheight()
x_cordinate = int((screen_width/2) - (window_width/2))
y_cordinate = int((screen_height/2.5) - (window_height/2))

# (RECOMMENDED TO NOT TOUCH) Window Metadeta.
main.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
main.title('Thought Logger')
main.resizable(False, False)
main.configure(background='black')
main.mainloop()



# Thank you for downloading and supporting moiSentineL.
