#Joshua Hinojosa
#Adv. Comp. Programming
#Mr. Davis
#9/2/16

from tkinter import *
from tkinter import ttk
import csv

def calculate(*args):
    try:
        nums="0123456789"
        uitem= str(item.get())
        if uitem in nums: #checks to see of item entered is a num
            pass
        else:
            infile=open("items and shipping.txt", "r")
            data = infile.readlines()
            itemcost=0
            for line in data:         #reads txt file to find the item entered and gets price
                if uitem.lower() in line.lower():
                    items=line.split()
                    itemcost=items[-1]
                    itemcost=int(itemcost)
                else:
                    pass
            infile.close()
            salestax=.0825*itemcost       #calculates sales tax on item
            
            shipdays_entry.focus()
            shipping= int(shipdays.get())   #gets shipping days entered
            shipcost=0
            if shipping==2:             #determines shipping cost of item
                shipcost=25
                tax.set("$"+(str(salestax))) #displays sales tax
                total.set("$"+(str(itemcost+salestax+shipcost))) #displays order total
            elif shipping==3:
                shipcost=10
                tax.set("$"+(str(salestax))) #displays sales tax
                total.set("$"+(str(itemcost+salestax+shipcost))) #displays order total
            elif shipping==5:
                shipcost=5
                tax.set("$"+(str(salestax))) #displays sales tax
                total.set("$"+(str(itemcost+salestax+shipcost))) #displays order total
            else:
                pass
            
    except ValueError:
        pass
    
root = Tk()
root.title("Order Form")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

item = StringVar()
tax = StringVar()
shipdays=StringVar()
total=StringVar()

item_entry = ttk.Entry(mainframe, width=15, textvariable=item)
item_entry.grid(column=3, row=2, sticky=(W, E))

shipdays_entry = ttk.Entry(mainframe, width=1, textvariable=shipdays)
shipdays_entry.grid(column=3, row=3, sticky=(W, E))

ttk.Label(mainframe, textvariable=tax).grid(column=3, row=5, sticky=(W))
ttk.Label(mainframe, textvariable=total).grid(column=4, row=6, sticky=(W))

ttk.Label(mainframe, text="Item").grid(column=10, row=2, sticky=W)
ttk.Label(mainframe, text="Shipping Days(2,3,5)").grid(column=10, row=3, sticky=E)
ttk.Label(mainframe, text="Tax").grid(column=10, row=4, sticky=W)
ttk.Label(mainframe, text="Total:").grid(column=3, row=5, sticky=(W,S))


for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

item_entry.focus()
root.bind('<Return>', calculate)

root.mainloop()
