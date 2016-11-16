#Joshua Hinojosa
#Mr. Davis
#Adv. Comp. Programming
#10/11/16

'''This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>.'''

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import csv
root = Tk()


def showversion():
    messagebox.showinfo("About", "Menu Example"+"\n"+"version .1")

def clr_entry(): #clears all entries and resets check boxes to default when cancel button is clicked
    onevar.set(False)
    twovar.set(False)
    threevar.set(False)
    name.delete(0,'end')
    name.focus()

def write_entry():  #writes all entries and values of the check buttons selected to a csv file
    with open("entrydata.csv", "a") as f:
        f.write(name.get()+","+str(onevar.get())+","+str(twovar.get())+","+str(threevar.get()))
        f.write('\n')
    messagebox.showinfo("Complete!","Data Saved!")
    f.close()
    onevar.set(False)
    twovar.set(False)
    threevar.set(False)
    name.delete(0, 'end')
    name.focus()

root.option_add('*tearOff', FALSE)
topMenu = Menu()
#creates menu and submenus (File and Help)
root.config(menu = topMenu)
subMenu= Menu(topMenu)
topMenu.add_cascade(label = "File", menu = subMenu)
subMenu.add_command(label="Exit", command=root.quit)

helpMenu = Menu(topMenu)
topMenu.add_cascade(label = "Help", menu = helpMenu)
helpMenu.add_command(label="About", command=showversion)

#Creates frame and variables for buttons and entries
username=StringVar()
content = ttk.Frame(root, padding=(3,3,12,12))
frame = ttk.Frame(content, borderwidth=5, relief="sunken", width=200, height=100)
namelbl = ttk.Label(content, text="Name")
name = ttk.Entry(content, textvariable=username)

onevar = BooleanVar()
twovar = BooleanVar()
threevar = BooleanVar()

onevar.set(False)
twovar.set(False)
threevar.set(False)

#******BUTTONS********
one = ttk.Checkbutton(content, text="One", variable=onevar, onvalue=True)
two = ttk.Checkbutton(content, text="Two", variable=twovar, onvalue=True)
three = ttk.Checkbutton(content, text="Three", variable=threevar, onvalue=True)
ok = ttk.Button(content, text="Okay", command=write_entry)
cancel = ttk.Button(content, text="Cancel", command=clr_entry)
#Puts items on the grid and makes them visible in GUI
content.grid(column=0, row=0, sticky=(N, S, E, W))
frame.grid(column=0, row=0, columnspan=3, rowspan=2, sticky=(N, S, E, W))
namelbl.grid(column=3, row=0, columnspan=2, sticky=(N, W), padx=5)
name.grid(column=3, row=1, columnspan=2, sticky=(N, E, W), pady=5, padx=5)
one.grid(column=0, row=3)
two.grid(column=1, row=3)
three.grid(column=2, row=3)
ok.grid(column=3, row=3)
cancel.grid(column=4, row=3)

#Configures the rows and columns to maintain proportion when expanding window
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
content.columnconfigure(0, weight=3)
content.columnconfigure(1, weight=3)
content.columnconfigure(2, weight=3)
content.columnconfigure(3, weight=1)
content.columnconfigure(4, weight=1)
content.rowconfigure(1, weight=1)

name.focus()
root.mainloop()