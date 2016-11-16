#Joshua Hinojosa
#Mr. Davis
#Adv. Comp. Programming
#10/28/16

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
def showprogress(*args):
    global selcheck
    p.config(value=50)
    selcheck=True
def submit():
    global selcheck
    if selcheck==True:      #checks to see if user chose a country
        p.config(value=100)
        selcheck=False
    else:
        messagebox.showinfo("", "Please choose a country!")
        pass
def clear():        #resets users choices and entries
    l.selection_set(0)
    p.config(value=0)
    tbox.delete('1.0', END)
def progdescript():             #shows description of the program
    messagebox.showinfo("About", """ Travel Log
    Version .1
    This is an interactive travel log program that allows
    the user to choose a country from a list and to enter
    text into a textbox with a progress bar to track the
    user's progress and it.""")
root=Tk()
root.title("Travel Log")
root.option_add('*tearOff', FALSE)  #removes the default dashes of the submenu
topMenu = Menu()
#creates menu and submenus (File and Help)
root.config(menu = topMenu)
subMenu= Menu(topMenu)
topMenu.add_cascade(label = "File", menu = subMenu)
subMenu.add_command(label="Exit", command=root.quit)

helpMenu = Menu(topMenu)
topMenu.add_cascade(label = "Help", menu = helpMenu)
helpMenu.add_command(label="About", command=progdescript)

countries=("United States", "United Kingdom", "Canada", "Mexico", "Korea", "China","India",
"Australia", "France", "Italy", "Germany", "Ukraine", "Russia", "Sweden", "Ireland", "Scotland")
cnames=StringVar(value=countries)
user_entry=StringVar()
mainframe = Frame(root, width=200, height=200)  #creates the mainframe and size of window
mainframe.grid(column=0, row=0, sticky=(N,S,E,W))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)
#Creates frame and content within the mainframe
content = ttk.Frame(root, padding=(5, 5, 12, 0)) #creates frame where the content of GUI will be shown
content.grid(column=0, row=0, sticky=(N,S,E,W))
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0,weight=1)

######Buttons
clr=Button(content, text="Clear", command=clear) #creates clear button which clears all of the users choices and entries in textbox
clr.grid(row=2, column=2, padx=5,pady=5,sticky=N)
submt=Button(content, text="Submit", command=submit) #creates submit button that
submt.grid(row=1, column=2, padx=5,pady=5, sticky=N)
##Text Box
descript_lbl=Label(content, text="Description")
descript_lbl.grid(column=0, row=4, padx=5, pady=5)
tbox=Text(content, height=10, width=20)
tbox.grid(column=0,row=5, padx=5, pady=5)
###Listbox
country_lbl=Label(content,text="Country")               #gives users a choice of countries to choose from in a listbox
country_lbl.grid(column=0, row=0, padx=4, pady=4, sticky=N)
l=Listbox(content, height=9, listvariable=cnames)
l.grid(column=0, row=1,rowspan=2, sticky=(N,W), padx=10,pady=10)
s = ttk.Scrollbar(content, orient=VERTICAL, command=l.yview)    #creates a scroll bar for user to use with mouse
s.grid(column=1, row=1, padx=5, pady=5,sticky=(N,W,E,S))
l['yscrollcommand'] = s.set
ttk.Sizegrip().grid(column=1, row=1, sticky=(S,E))
content.grid_columnconfigure(1, weight=1)
content.grid_rowconfigure(1, weight=1)
content.grid_columnconfigure(0, weight=1)
content.grid_rowconfigure(0, weight=1)
###Progress Bar
p = ttk.Progressbar(content, orient=VERTICAL, length=200) #creates a progress bar that tracks user's progress
p.grid(column=3, row=1, padx=5, pady=5, sticky=(N,W))
l.bind('<<ListboxSelect>>', showprogress)
l.selection_set(0)
selcheck=False
root. mainloop()