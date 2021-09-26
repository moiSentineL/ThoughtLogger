# Thought Logger v2
# Source Code
# Developer: moiSentineL (www.github.com/moiSentineL)
# Files: www.github.com/moiSentineL/Thought-Logger


def thoughtlogger():

    # Function Imports

    import datetime
    import os
    import time
    import tkinter as tk
    import sys
    from tkinter.constants import TRUE
    import webbrowser as wb
    from tkinter import StringVar, font
    from tkinter import messagebox
    import configparser

    # Tkinter window initialize
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

    # Functions
    if os.path.exists(inifile) == True:
        pass
    else:
        def createini():
            # Function to create .ini file
            write_config = configparser.ConfigParser()

            write_config.add_section("CustomText")
            write_config.set("CustomText","text","Thought Logger")

            cfgfile = open(inifile,'w')
            write_config.write(cfgfile)
            cfgfile.close()
        createini()
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

    # Keybindings
    main.bind('<Return>', entrywithenter)
    main.bind('<Escape>', exit)

    # Labels and Entries
        # Label text
    l1 = tk.Label(main, text = "Entry: ", font=("Roboto",12), bg= "black", fg= "white") 
    l1.grid(row = 1, column = 1, sticky = tk.W, pady = 15, padx= 5)
        # Entry for text
    logentry = tk.Entry(main, width= 37)
    logentry.grid(row = 1, column = 2, pady = 2, columnspan= 3, sticky=tk.W)
        # Custom Text
        # Extra Code
    read_config = configparser.ConfigParser()
    read_config.read(inifile)
    var = StringVar()
    customtext = str(read_config.get("CustomText", "text"))
    var.set(customtext)
        # Main Code
    custom = tk.Label(main, textvariable= var, font=("Roboto",12), bg= "black", fg= "white") 
    custom.grid(row = 2, column = 1, sticky = tk.S, padx= 5, columnspan=3)

    # Buttons
        # Button to open log file.
    seelog = tk.Button(main, text= "See Log", command=seelog)
    seelog.grid(row= 2, column= 5, sticky= tk.W )
        # Button to delete log file.
    deletelog = tk.Button(main, text= "Delete Log", command=deletelog)
    deletelog.grid(row= 2, column= 4, sticky= tk.E, padx= 15)
        # Button to entry the text.
    logentry_button = tk.Button(main, text= "ok", command=entrywithbutton)
    logentry_button.grid(row= 1, column= 5, padx = 17, ipadx= 8)

    # (RECOMMENDED TO NOT TOUCH) Window Placement tweaks.
    window_height = 100
    window_width = 435
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


try:
    thoughtlogger()
except Exception as e:
    from tkinter import messagebox 
    messagebox.showerror("Error","Something Went Wrong.\n\nIf this issue persists, please report it on https://github.com/moiSentineL/Thought-Logger")
    exit()


# Thank you for downloading and supporting moiSentineL.
