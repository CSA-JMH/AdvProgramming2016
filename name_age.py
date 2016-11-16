#Joshua Hinojosa
#Mr. Davis
#Adv. Comp. Programming
#9/16/16

from tkinter import *
from tkinter import ttk
import tkinter

def submit():
    try:
        ename=uname.get()
        eage=int(uage.get())
        egender=gender.get()
        if ename!="" and ename!="Name":
            if egender!="":
                name_entry.delete(0, "end")
                name_entry.insert(0, "Name")
                age_entry.delete(0,"end")
                age_entry.insert(0, "Age")
                gender.set("")

                
    except ValueError:
        pass

    
root = Tk()
root.title("Name & Age")

mainframe = tkinter.Frame(root,  borderwidth=5,bg="hot pink", relief="sunken")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

uname = StringVar()
uage= StringVar()
name_entry = ttk.Entry(mainframe, width=15, textvariable=uname)
name_entry.grid(column=1, row=1, sticky=(N,W))
age_entry=ttk.Entry(mainframe, width=15, textvariable=uage)
age_entry.grid(column=1, row=4, sticky=(N,W))

name_entry.insert(0, "Name")
age_entry.insert(0, "Age")

gender = StringVar()

male_rbutton = ttk.Radiobutton(mainframe, text='Male', variable=gender, value='male')
male_rbutton.grid(column=1, row=8, sticky=S)
female_rbutton = ttk.Radiobutton(mainframe, text='Female', variable=gender, value='female')
female_rbutton.grid(column=2, row=8, sticky=S)
other_rbutton = ttk.Radiobutton(mainframe, text='Other', variable=gender, value='other')
other_rbutton.grid(column=3, row=8, sticky=S)
submit_button=ttk.Button(mainframe, text='Submit', command=submit)
submit_button.grid(column=2, row=10, sticky=S)

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

name_entry.focus()
root.bind('<Return>', submit)
root.mainloop()
