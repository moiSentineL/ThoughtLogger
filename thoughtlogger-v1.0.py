
import datetime
import time
import tkinter as tk
import sys
from tkinter import font

#main window
main = tk.Tk()
main.resizable(False, False)  # This code helps to disable maindows from resizing
# main.attributes('-alpha', 0.5)
main.configure(background='black')
#code for window placement
window_height = 60
window_width = 425

screen_width = 1920
screen_height = 800

x_cordinate = int((screen_width/2) - (window_width/2))
y_cordinate = int((screen_height/2) - (window_height/2))

#labels and entries
l1 = tk.Label(main, text = "Entry: ", font=("Calibri",12), bg= "black", fg= "white") 
l1.grid(row = 2, column = 0, sticky = tk.W, pady = 15, padx= 5)
 

logentry = tk.Entry(main, width= 37)
logentry.grid(row = 2, column = 1, pady = 2, ) 

def entrywithenter(key):

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

    if logentry.get() == '':
        pass
    else:

        ts = time.time()
        sttime = datetime.datetime.fromtimestamp(ts).strftime('%d/%m/%y; %I:%M:%S %p : ')

        log = open("log.txt", "a")
        logwrite = log.write(sttime + logentry.get() + '\n')

        log.close()

        logentry.delete(0, 'end')
    
main.bind('<Return>', entrywithenter)

logentry_button = tk.Button(main, text= "ok", command=entrywithbutton)
logentry_button.grid(row= 2, column= 2, padx = 15)

main.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
main.title('Thought Logger')
main.mainloop()

# def newwindow():
#     newWindow = tk.Toplevel(main) 
#     newWindow.title("Log") 
#     newWindow.geometry("600x720") 

#     logread = open("D:\Extra\Software\Thought Logger\log.txt", "r").readlines()

#     logtext = tk.Label(newWindow, text= ">".join(logread), width= 60, justify= tk.LEFT)
#     logtext.grid(row=0, column=0)




