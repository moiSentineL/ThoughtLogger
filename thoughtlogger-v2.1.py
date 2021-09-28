# Thought Logger v2.1
# Source Code
# Developer: moiSentineL (www.github.com/moiSentineL)
# Website: www.github.com/moiSentineL/Thought-Logger



def thoughtlogger():
    # Function Imports

    import datetime
    import os
    import time
    import tkinter as tk
    import sys
    from tkinter.constants import TRUE
    import webbrowser as wb
    from tkinter import StringVar, font, messagebox
    from configparser import ConfigParser
    from tkinter.ttk import Style, Button

    # Tkinter window initialize
    global main
    main = tk.Tk()

    #Global Variables/Functions:
        # Variables for log file.
    userlocation = os.path.expanduser('~')
    documentslocation = str(os.path.join(userlocation, 'Documents'))
    thoughtloggerdir = os.path.join(documentslocation, "Thought Logger")
    if os.path.exists(thoughtloggerdir) == True:
        pass
    else:
        os.mkdir(thoughtloggerdir)
    thoughtloggerlog = documentslocation + r"\Thought Logger\thoughtlogger.log"
        # Variable for .ini file.
    inifile = documentslocation + r"\Thought Logger\thoughtlogger.ini"
    ini = ConfigParser()
    ini.read(inifile)

    # Functions
    if os.path.exists(inifile) == True:
        pass
    else:
        # Function to create .ini file
        
        ini["ThoughtLogger"]={'CustomText': 'ThoughtLogger',
                        'BackgroundColor': '#000000',
                        'FontColor': '#fff'}

        cfgfile = open(inifile,'w')
        ini.write(cfgfile)
        cfgfile.close()  
    def entrywithenter(key):
        # Function to make entrying with a keypress possible.
        if logentry.get() == '':
            pass
        else:

            ts = time.time()
            sttime = datetime.datetime.fromtimestamp(ts).strftime('%d/%m/%y; %I:%M:%S %p : ')

            log = open(thoughtloggerlog, "a")
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

            log = open(thoughtloggerlog, "a")
            logwrite = log.write(sttime + logentry.get() + '\n')

            log.close()

            logentry.delete(0, 'end')
    def seelog():
        # Function to open log file.
        if os.path.exists(thoughtloggerlog) == True:
            wb.open(thoughtloggerlog)
        else:
            tk.messagebox.showerror("File Does Not Exist", "The file 'thoughtlogger.log' does not exist. Make a log first.")
    def exit(a):
        # Function to exit program.
        main.destroy()
    def deletelog():
        # Function to delete the log file.
        if os.path.exists(thoughtloggerlog) == True:
            askyesorno = tk.messagebox.askyesno("Are you sure?", "Do you really want to delete your log?")
            if askyesorno == True:
                os.remove(thoughtloggerlog)
                tk.messagebox.showinfo("Log Deleted", "Your log has been deleted successfully.")
            else:
                pass
        else:
            tk.messagebox.showerror("File Already Does Not Exist", "The file 'thoughtlogger.log' already does not exist.")
    
    # Customizations
    customtextvar = StringVar() 
    customtext = ini.get("ThoughtLogger", "CustomText")[0:22]
    customtextvar.set(customtext)
    bgcolor = ini.get("ThoughtLogger", "BackgroundColor")
    fcolor = ini.get("ThoughtLogger", "FontColor")
    buttonstyle = Style()
    buttonstyle.configure('TButton', font= ('Roboto', 10),activeforeground = fcolor)
    
    # Keybinds
    main.bind('<Return>', entrywithenter)
    main.bind('<Escape>', exit)

    # Labels and Entries
        # Label text
    l1 = tk.Label(main, text = "Entry: ", font=("Roboto",12,'bold'), bg= bgcolor, fg= fcolor) 
    l1.grid(row = 1, column = 1, sticky = tk.W, pady = 15, padx= 5)
        # Entry for text
    logentry = tk.Entry(main, width= 37, bd=3)
    logentry.grid(row = 1, column = 2, pady = 2, columnspan= 3, sticky=tk.W)
        # Custom Text
    custom = tk.Label(main, textvariable= customtextvar, font=("Roboto",12,'bold'), bg= bgcolor, fg= fcolor, anchor='w', width=22) 
    custom.grid(row = 2, column = 1, sticky = tk.W, padx= 5, columnspan=3)
   
    # Buttons
        # Button to open log file.
    seelog = Button(main, text= "See Log", command=seelog, width= 9)
    seelog.grid(row= 2, column= 5, sticky= tk.W )
        # Button to delete log file.
    deletelog = Button(main, text= "Delete Log",  command=deletelog, width= 12)
    deletelog.grid(row= 2, column= 4, sticky= tk.E, padx= 15)
        # Button to entry the text.
    logentry_button = Button(main, text= "Entry", command=entrywithbutton, width= 6)
    logentry_button.grid(row= 1, column= 5, padx = 24)

    # (RECOMMENDED TO NOT TOUCH) Window Placement tweaks.
    window_height = 100
    window_width = 462
    screen_width = main.winfo_screenwidth()
    screen_height = main.winfo_screenheight()
    x_cordinate = int((screen_width/2) - (window_width/2))
    y_cordinate = int((screen_height/2.5) - (window_height/2))

    # (RECOMMENDED TO NOT TOUCH) Window Metadeta.
    main.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
    main.title('Thought Logger')
    main.resizable(False, False)
    main.configure(background=bgcolor)
    main.mainloop()

# Exception Handling
try:
    thoughtlogger()
except Exception as e:
    from tkinter import messagebox 
    messagebox.showerror("Error","Something Went Wrong.\n\nIf this issue persists, please report it on https://github.com/moiSentineL/Thought-Logger")
    exit()


# Thank you for downloading and supporting moiSentineL.