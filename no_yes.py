#Joshua Hinojosa
#Mr. Davis
#Adv. Comp. Programming
#9/12/16

from tkinter import *
from tkinter import ttk
from tkinter import messagebox

def sayhi():
    messagebox.showinfo("", "Hi!")

def checkedbutton():
    box1=var1.get()
    box2=var2.get()

    if box1==0:
        hi_button.config(state="disabled")
    elif box1==1:
        hi_button.config(state="!disabled")
        if box2==1:
            hi_button.config(state="disabled")
            
    elif box2==0:
        hi_button.config(state="disabled")

    elif box2==1:
        hi_button.config(state="disabled")
        if box1==1:
            hi_button.config(state="disabled")
        
root = Tk()
root.title("Check Box")
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe = ttk.Frame(root,width=100,height=175,relief="sunken")
mainframe.grid(column=0, row=0, sticky=(N,S,E,W))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

var1=IntVar()
var2=IntVar()


checklbl=ttk.Label(mainframe, text="Check yes or no:")
checklbl.grid(column=2,row=2, sticky=(N,W))

yes_check=ttk.Checkbutton(mainframe, text="yes", command=checkedbutton, variable=var1)
yes_check.grid(column=2,row=5, sticky=(N,W))

no_check=ttk.Checkbutton(mainframe, text="no", command=checkedbutton, variable=var2)
no_check.grid(column=2,row=7, sticky=(N,W))

hi_button=ttk.Button(mainframe, text='Hi',state="disabled", command=sayhi)
hi_button.grid(column=4,row=9, sticky=(S,E))

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

root.mainloop()
