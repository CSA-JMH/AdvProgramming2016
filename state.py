#Joshua Hinojosa
#Mr. Davis
#Adv. Comp. Programming
#9/16/16

from tkinter import *
from tkinter import ttk
from tkinter import messagebox

root = Tk()
root.title("State")

def name_state(*args):
    try:
        getstate=str(statevar.get())
        getname=str(uname.get())
        if getname=="":             #checks to see if name entered 
            messagebox.showinfo("","Please enter name!")
            state.set("")
            prntstate.set("")
        else:
            prntstate.set("Hi" + " " + getname + " " + "from" + " " + getstate +"!")
    except ValueError:
        pass
    
mainframe = ttk.Frame(root, padding="3 3 12 12", relief="sunken") #creates frame around content 
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

uname = StringVar()
statevar = StringVar()
prntstate=StringVar()

name = ttk.Entry(mainframe, width=15, textvariable=uname)
name.grid(column=1, row=1, sticky=(N,W))

namelbl=ttk.Label(mainframe, text="Name")   #name label
namelbl.grid(column=0,row=1, sticky=N)
statelbl=ttk.Label(mainframe, text="State") #state label
statelbl.grid(column=0,row=2, sticky=N)

state = ttk.Combobox(mainframe, state="readonly", textvariable=statevar) #creates dropdown selection
state['values'] = ('Texas', 'California', 'New York', 'Colorado', 'Arkansas')
state.grid(column=1, row=2, sticky=(N,W))

ttk.Label(mainframe, textvariable=prntstate).grid(column=1, row=4, sticky=(S))

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

name.focus()
state.bind('<<ComboboxSelected>>', name_state)
root.mainloop()
