# Thought Logger v3.0
# Source Code
# Developer: moiSentineL (www.github.com/moiSentineL)
# Website: www.github.com/moiSentineL/ThoughtLogger


def thoughtlogger():
    
    # Imports
    import datetime
    import os
    import glob
    import time
    import tkinter as tk
    import sys
    import pyautogui as gui
    from tkinter.constants import TRUE
    from tkinter import Toplevel
    import webbrowser as wb
    from tkinter import StringVar, font, messagebox
    from configparser import ConfigParser
    from tkinter.ttk import Style, Button

    # Tkinter window initialize
    global main
    main = tk.Tk()

    # Essential Variables/Functions:
        # Variables for log file.
    userlocation = os.path.expanduser('~')
    documentslocation = str(os.path.join(userlocation, 'Documents'))
    thoughtloggerdir = os.path.join(documentslocation, "Thought Logger")
    
    if os.path.exists(thoughtloggerdir) == True:
        pass
    else:
        os.mkdir(thoughtloggerdir)

    profile1log = documentslocation + r"\Thought Logger\profile1.log"
    profile2log = documentslocation + r"\Thought Logger\profile2.log"

        # Variable for .ini file.
    inifile = documentslocation + r"\Thought Logger\thoughtlogger.ini"
    ini = ConfigParser()
    ini.read(inifile)

    # Functions
    def logfilecreation():
        
        # Function to create the log files for the first time with headings.
        for i in [profile1log, profile2log]:
            if os.path.exists(i) == True:
                pass
            else:
                log1 = open(profile1log, 'w')
                log1.write('--------ThoughtLogger--------\n----------Profile 1----------\n\n')
                log1.close()

                log2 = open(profile2log, 'w')
                log2.write('--------ThoughtLogger--------\n----------Profile 2----------\n\n')
                log2.close()  
    logfilecreation()

    def inifileconfig():
        
        # Function to create and configure .ini file
        if os.path.exists(inifile) == True:
            if ini.has_option('CustomText', 'text'):
                customtextprev =ini.get('CustomText', 'text')
                ini["ThoughtLogger"]={'CustomText': customtextprev,
                                'BackgroundColor': '#000000',
                                'FontColor': '#fff'}
                cfgfile = open(inifile,'w')
                ini.remove_section('CustomText')
                ini.write(cfgfile)
                cfgfile.close()
            else:
                pass
        else:
            ini["ThoughtLogger"]={'CustomText': 'ThoughtLogger',
                            'BackgroundColor': '#000000',
                            'FontColor': '#fff'}

            cfgfile = open(inifile,'w')
            ini.write(cfgfile)
            cfgfile.close() 
    inifileconfig()
    
    def findlatestlog():
        
        # Function to find the latest edited log file to open.
        folder_path = thoughtloggerdir
        file_type = '\*log'
        global files
        files = glob.glob(folder_path + file_type)

        if files:
            global latestlog, head, tail
            latestlog = max(files, key=os.path.getmtime)
        else:
            pass

    def seelog():
        # Function to open log file.
        try:
            findlatestlog()
            if os.path.exists(latestlog) == True:
                wb.open(latestlog)
                time.sleep(0.1)
                gui.hotkey('ctrl', 'end')
            else:
                tk.messagebox.showerror("File Does Not Exist", "No log file exists. Restart the Application.")
        except FileNotFoundError as e:
            tk.messagebox.showerror("File Does Not Exist", "No log file exists. Restart the Application.")
        except NameError as e:
            tk.messagebox.showerror("File Already Does Not Exist", "No log file exists. Restart the application")
        
    def exit(a):
        # Function to exit program.
        main.destroy()

    def deletelogwindow():
        # Function to delete the log file.
        
        # New window initialise
        new = Toplevel(main)

        def deletelog():
            if str(var.get()) == '1':
                if os.path.exists(profile1log) == True:
                    askyesorno = tk.messagebox.askyesno("Are you sure?", "Do you really want to delete your log?")
                    if askyesorno == True:
                        os.remove(profile1log)
                        tk.messagebox.showinfo("Log Deleted", "Your log has been deleted successfully.")
                    else:
                        pass
                else:
                    tk.messagebox.showerror("File Already Does Not Exist", "The file 'profile1.log' already does not exist.")
            elif str(var.get()) == '2':
                if os.path.exists(profile2log) == True:
                    askyesorno = tk.messagebox.askyesno("Are you sure?", "Do you really want to delete your log?")
                    if askyesorno == True:
                        os.remove(profile2log)
                        tk.messagebox.showinfo("Log Deleted", "Your log has been deleted successfully.")
                    else:
                        pass
                else:
                    tk.messagebox.showerror("File Already Does Not Exist", "The file 'profile2.log' already does not exist.")
            else:
                tk.messagebox.showerror("File Already Does Not Exist", "The log files already does not exist.")
            
            logfilecreation()
        
        def sel():
            selection = "You selected the Profile " + str(var.get())
            label.config(text = selection)
        
        var = tk.IntVar()

        # Radiobuttons
        R1 = tk.Radiobutton(new, text="Profile 1", variable=var, value=1,font=("Roboto",10), command=sel, bg= bgcolor, fg= fcolor)
        R1.grid(row = 2, column = 1, sticky = tk.W, padx= 5)

        R2 = tk.Radiobutton(new, text="Profile 2", variable=var, value=2,font=("Roboto",10), command=sel, bg= bgcolor, fg= fcolor)
        R2.grid(row = 3, column = 1, sticky = tk.W, padx= 5)

        # Labels
            # Label for delete which profile
        delete = tk.Label(new, text = "Delete which profile?", font=("Roboto",12,'bold'), bg= bgcolor, fg= fcolor) 
        delete.grid(row = 1, column = 1, columnspan=3, sticky = tk.W, pady = 5, padx= 5)
            # Label for selected profile.
        label = tk.Label(new, font=("Roboto",12,'bold'), bg= bgcolor, fg= fcolor)
        label.grid(row=4, column=1, columnspan=3, sticky=tk.W, padx= 5, pady = 5)

        # Buttons
            # Button to delete.
        delbutton = Button(new, text= "Delete", command=deletelog, width= 9)
        delbutton.grid(row= 5, column= 1, sticky= tk.W, pady = 5, padx= 5)

        # (RECOMMENDED TO NOT TOUCH) Window Placement tweaks.
        window_height = 175
        window_width = 230
        screen_width = main.winfo_screenwidth()
        screen_height = main.winfo_screenheight()
        x_cordinate = int((screen_width/2) - (window_width/2))
        y_cordinate = int((screen_height/2.5) - (window_height/2))

        # (RECOMMENDED TO NOT TOUCH) Window Metadeta.
        new.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
        new.title('Really?')
        new.resizable(False, False)
        new.configure(background=bgcolor)
        new.grab_set()

    # Profiles
    class profile1:
        
        # Class for Profile 1

        def entry(key):
            # Function to make entrying with a keypress possible.
            if logentry.get() == '':
                pass
            else:

                ts = time.time()
                sttime = datetime.datetime.fromtimestamp(ts).strftime('%d/%m/%y; %I:%M:%S %p : ')

                log = open(profile1log, "a")
                logwrite = log.write(sttime + logentry.get() + '\n')

                log.close()

                logentry.delete(0, 'end')
    
    class profile2:
        
        # Class for Profile 2

        def entry(key):
            # Function to make entrying with a keypress possible.
            if logentry.get() == '':
                pass
            else:

                ts = time.time()
                sttime = datetime.datetime.fromtimestamp(ts).strftime('%d/%m/%y; %I:%M:%S %p : ')

                log = open(profile2log, "a")
                logwrite = log.write(sttime + logentry.get() + '\n')

                log.close()

                logentry.delete(0, 'end')

    # Customizations
    customtextvar = StringVar() 
    customtext = ini.get("ThoughtLogger", "CustomText")[0:22]
    customtextvar.set(customtext)
    bgcolor = ini.get("ThoughtLogger", "BackgroundColor")
    fcolor = ini.get("ThoughtLogger", "FontColor")
    buttonstyle = Style()
    buttonstyle.configure('TButton', font= ('Roboto', 10),activeforeground = fcolor)
    
    # Keybinds
    main.bind('<Return>', profile1.entry)
    main.bind('<Shift-Return>', profile2.entry)
    main.bind('<Escape>', exit)

    # Labels and Entries
        # Label text
    l1 = tk.Label(main, text = "Entry: ", font=("Roboto",12,'bold'), bg= bgcolor, fg= fcolor) 
    l1.grid(row = 1, column = 1, sticky = tk.W, pady = 15, padx= 5)
        # Entry for text
    logentry = tk.Entry(main, width= 47, bd=3)
    logentry.grid(row = 1, column = 2, pady = 2, columnspan= 5, sticky=tk.W)
    logentry.focus()
        # Custom Text
    custom = tk.Label(main, textvariable= customtextvar, font=("Roboto",12,'bold'), bg= bgcolor, fg= fcolor, anchor='w', width=22) 
    custom.grid(row = 2, column = 1, sticky = tk.W, padx= 5, columnspan=3)
   
    # Buttons
        # Button to open log file.
    seelog = Button(main, text= "See Log", command=seelog, width= 9)
    seelog.grid(row= 2, column= 5, sticky= tk.W )
        # Button to delete log file.
    deletelog = Button(main, text= "Delete Log",  command=deletelogwindow, width= 12)
    deletelog.grid(row= 2, column= 4, sticky= tk.E, padx= 15)

    # (RECOMMENDED TO NOT TOUCH) Window Placement tweaks.
    window_height = 100
    window_width = 462
    screen_width = main.winfo_screenwidth()
    screen_height = main.winfo_screenheight()
    x_cordinate = int((screen_width/2) - (window_width/2))
    y_cordinate = int((screen_height/2.5) - (window_height/2))

    # (RECOMMENDED TO NOT TOUCH) Window Metadeta.
    main.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
    main.title('ThoughtLogger')
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