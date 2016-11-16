#Joshua Hinojosa
#Mr. Davis
#Adv. Comp. Programming
#11/4/16
#v1.0
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
def num_days(*args):      #checks what month is selected and shows the amount of days that can be chosen depending on the month
    if month.get()=="Jan":
        day_cbox['values'] = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14',
                              '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26',
                              '27', '28', '29', '30', '31')
    elif month.get()=="Mar":
        day_cbox['values'] = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14',
                              '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26',
                              '27', '28', '29', '30', '31')
    elif month.get()=="May":
        day_cbox['values'] = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14',
                              '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26',
                              '27', '28', '29', '30', '31')
    elif month.get()=="July":
        day_cbox['values'] = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14',
                              '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26',
                              '27', '28', '29', '30', '31')
    elif month.get() == "Aug":
        day_cbox['values'] = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14',
                              '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26',
                              '27', '28', '29', '30', '31')
    elif month.get()=="Oct":
        day_cbox['values'] = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14',
                              '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26',
                              '27', '28', '29', '30', '31')
    elif month.get()=="Dec":
        day_cbox['values'] = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14',
                              '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26',
                              '27', '28', '29', '30', '31')

    elif month.get()=='Apr':
        day_cbox['values'] = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14',
                              '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26',
                              '27', '28', '29', '30')
    elif month.get()=="June":
        day_cbox['values'] = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14',
                              '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26',
                              '27', '28', '29', '30')
    elif month.get()=="Sept":
        day_cbox['values'] = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14',
                              '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26',
                              '27', '28', '29', '30')
    elif month.get()=="Nov":
        day_cbox['values'] = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14',
                              '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26',
                              '27', '28', '29', '30')
    elif month.get()=='Feb':
        day_cbox['values'] = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14',
                              '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26',
                              '27', '28')

def progdescript():             #shows the version number and description of the program
    messagebox.showinfo("About", '''Database Entry
                        Version 1.0
                        This is a user-friendly program where the user can enter
                        in data for an item and then it records it to a csv file for
                        the user to view.''')

def price_calc(*args):
    try:
        checkpo=False
        try: #checks to see if there's already a po with that 9 digit number
            f=open('orderdatabase.csv','r')
            for line in f:
                l=line.replace("\n","")
                list=l.split(",")
                if list[0]==po.get():
                    messagebox.showinfo("Error!","P.O. number already in use")
                    checkpo=True
            f.close()
        except FileNotFoundError:
            pass
        if checkpo==False:
            if po.get()=="":                             #checks to see if user has filled all required fields up to this point
                messagebox.showinfo("", "PO is required!")
                shipping.set('')
            elif len(str(int(po.get())))<9 or len(str(int(po.get())))>9:
                messagebox.showinfo("", "PO must be 9 digits long")
                shipping.set('')
            elif fname.get()=="":
                messagebox.showinfo("", "First Name is required!")
                shipping.set('')
            elif lname.get()=="":
                messagebox.showinfo("", "Last Name is required!")
                shipping.set('')
            elif strtaddr1.get()=="":
                messagebox.showinfo("", "Street Address is required!")
                shipping.set('')
            elif statesvar.get()=="":
                messagebox.showinfo("", "State is required!")
                shipping.set('')
            elif city.get() == "":
                messagebox.showinfo("", "City is required!")
                shipping.set('')
            elif zipcode.get() == "":
                messagebox.showinfo("", "Zip Code is required!")
                shipping.set('')
            elif tbox.get('1.0', END)=="":
                messagebox.showinfo("", "Description is required!")
                shipping.set('')
            elif price.get() == "":
                messagebox.showinfo("", "Price is required!")
                shipping.set('')
            else:
                ship=shipping.get()
                p=float(price.get())
                if ship=='One Day Shipping($5.99)':
                    shipprice=5.99
                elif ship=='Two Day Shipping($3.99)':
                    shipprice=3.99
                else:
                    shipprice=0
                itemtax=float(p*.0825)
                itemtax="%.2f" % itemtax
                tax.set(str(itemtax))
                totalprice=p+float(itemtax)+shipprice
                totalprice=str("%.2f" % totalprice)
                tax.set(str(itemtax))
                total.set(totalprice)
    except ValueError:
        messagebox.showinfo("Error", "PO must be a digit!")
        shipping.set('')
    try:
        if len(str(int(zipcode.get()))) < 5 or len(str(int(zipcode.get()))) > 5:
            messagebox.showinfo("", "Zip must be 5 digits long")
            shipping.set('')
    except ValueError:
        messagebox.showinfo("Error", "Zip must be a digit!")
        shipping.set('')
def retrieve():
    if po.get()!="":
        try:
            f=open('orderdatabase.csv','r')
            for line in f:
                l=line.replace("\n","")
                list=l.split(",")
                print(list)
                if list[0]==po.get(): #if the proper PO number is found, the remaining variables are filled in
                    po.set(list[0])
                    fname.set(list[1])
                    lname.set(list[2])
                    strtaddr1.set(list[3])
                    strtaddr2.set(list[4])
                    statesvar.set(list[5])
                    city.set(list[6])
                    zipcode.set(list[7])
                    tbox.delete('1.0',END)
                    tbox.insert('1.0',list[8])
                    price.set(list[9])
                    tax.set(list[10])
                    shipping.set(list[11])
                    total.set(list[12])
                    month.set(list[13])
                    day.set(list[14])
                    year.set(list[15])
                    messagebox.showinfo("Success","Order successfully retrieved!")
                    break
                else:
                    messagebox.showinfo("Error!","Entered PO does not exist!")
            f.close()
        except FileNotFoundError:
            messagebox.showinfo("Error!", "Entered PO does not exist!")
    else:
        messagebox.showinfo("Error!","No P.O. number found")
def submit():
    try:
        checkpo=False
        try: #checks to see if there's already a po with that 9 digit number
            f=open('orderdatabase.csv','r')
            for line in f:
                l=line.replace("\n","")
                list=l.split(",")
                if list[0]==po.get():
                    messagebox.showinfo("Error!","P.O. number already in use")
                    checkpo=True
            f.close()
        except FileNotFoundError:
            pass
        if checkpo==False:
            if po.get() == "":                                  #checks to see if user has filled all required fields
                messagebox.showinfo("", "PO is required!")
            elif fname.get() == "":
                messagebox.showinfo("", "First Name is required!")
            elif lname.get() == "":
                messagebox.showinfo("", "Last Name is required!")
            elif strtaddr1.get() == "":
                messagebox.showinfo("", "Street Address is required!")
            elif statesvar.get() == "":
                messagebox.showinfo("", "State is required!")
            elif city.get() == "":
                messagebox.showinfo("", "City is required!")
            elif zipcode.get() == "":
                messagebox.showinfo("", "Zip Code is required!")
            elif tbox.get('1.0', END) == "":
                messagebox.showinfo("", "Description is required!")
            elif price.get() == "":
                messagebox.showinfo("", "Price is required!")
            elif shipping.get() == "":
                messagebox.showinfo("", "Shipping is required!")
            elif month.get() == "":
                messagebox.showinfo("", "Month is required!")
            elif day.get() == "":
                messagebox.showinfo("", "Day is required!")
            elif year.get() == "":
                messagebox.showinfo("", "Year is required!")
            else:
                if tbox.get('1.0', END) != "\n":
                    descript = str(tbox.get('1.0', END)).replace("\n", " ")
                with open("orderdatabase.csv", "a") as f:
                    f.write(po.get()+','+str(fname.get())+','+str(lname.get())+','+str(strtaddr1.get())+','+str(strtaddr2.get())+','+str(statesvar.get())+','+str(city.get())+','+str(zipcode.get())+','+str(descript)+","+str(price.get())+','+str(tax.get())+','+str(shipping.get())+','+str(total.get())+','+str(month.get())+','+str(day.get())+','+str(year.get()))
                    f.write('\n')
                messagebox.showinfo("Complete!", "Data Saved!")
                f.close()
                po_entry.delete(0, 'end')                   #resets all the user entries
                fname_entry.delete(0, 'end')
                lname_entry.delete(0, 'end')
                strtaddr1_entry.delete(0, 'end')
                strtaddr2_entry.delete(0, 'end')
                states_cbox.set('')
                city_entry.delete(0, 'end')
                zip_entry.delete(0, 'end')
                tbox.delete('1.0', END)
                price_entry.delete(0, END)
                tax.set("...")
                ship_cbox.set('')
                total.set("...")
                month_cbox.set('')
                day_cbox.set('')
                year_cbox.set('')
    except FileNotFoundError:
        pass
root=Tk()
root.minsize(600, 600) #sets the minimum size the window can be shrinked
root.maxsize(950,925) #sets the maximum size the window can expand
root.title("Final Order Rorm")
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

mainframe = ttk.Frame(root, width=550, height=575)  #creates the mainframe and size of window
mainframe.grid(column=0, row=0, sticky=(N,S,E,W))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

#Creates frame and content within the mainframe
content = ttk.Frame(root, padding=(3, 3, 12, 0)) #creates frame where the content of GUI will be shown
content.grid(column=0, row=0, sticky=(N,S,E,W))
content2=ttk.Frame(root, padding=(3, 3, 12, 0))
content2.grid(column=4, row=0, sticky=(N,S,E,W))
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0,weight=1)
content.grid_columnconfigure(1, weight=1)
content.grid_rowconfigure(1, weight=1)
content.grid_columnconfigure(0, weight=1)
content.grid_rowconfigure(0, weight=1)
content.grid_columnconfigure(2, weight=1)
content.grid_rowconfigure(2, weight=1)
content.grid_columnconfigure(3, weight=1)
content.grid_rowconfigure(3, weight=1)
content.grid_columnconfigure(4, weight=1)
content.grid_columnconfigure(5, weight=1)
content.grid_columnconfigure(6, weight=1)
content.grid_columnconfigure(7, weight=1)
content.grid_rowconfigure(4, weight=1)
content.grid_rowconfigure(5, weight=1)
content.grid_rowconfigure(6, weight=1)
content.grid_rowconfigure(7, weight=1)
content.grid_rowconfigure(8, weight=1)
content.grid_rowconfigure(9, weight=1)
ttk.Sizegrip().grid(column=4, row=8, sticky=(S,E)) #adds size grip in bottom left corner for expanding the window

######Varaiables
po=StringVar()
fname=StringVar()
lname=StringVar()
strtaddr1=StringVar()
strtaddr2=StringVar()
city=StringVar()
zipcode=StringVar()
itemprice=StringVar()
statesvar=StringVar()
price=StringVar()
tax=StringVar()
shipping=StringVar()
total=StringVar()
month=StringVar()
day=StringVar()
year=StringVar()

######Labels
po_lbl=Label(content, text="PO(9 digits)")
po_lbl.grid(column=0, row=0, padx=4, pady=4, sticky=(N,W))
fname_lbl=Label(content, text="First Name")
fname_lbl.grid(column=0,row=1, padx=4, pady=4, sticky=(N,W))
lname_lbl=Label(content, text="Last Name")
lname_lbl.grid(column=0, row=2, padx=4, pady=4, sticky=(N,W))
strtaddr1_lbl=Label(content, text="Street Address")
strtaddr1_lbl.grid(column=0, row=3, padx=4, pady=4, sticky=(N,W))
strtaddr2_lbl=Label(content, text="Street Address(2)")
strtaddr2_lbl.grid(column=0, row=4, padx=4, pady=4, sticky=(N,W))
states_lbl=Label(content, text='State')
states_lbl.grid(column=0, row=5, padx=4, pady=4, sticky=(N,W))
city_lbl=Label(content, text='City')
city_lbl.grid(column=2, row=5, padx=4, pady=4, sticky=(N,W))
zip_lbl=Label(content, text='Zip')
zip_lbl.grid(column=0, row=6, padx=4, pady=4, sticky=(N,W))
descript_lbl=Label(content, text="Item Description")
descript_lbl.grid(column=0, row=7, padx=5, pady=5)
price_lbl=Label(content2, text="Price $")
price_lbl.grid(column=4, row=0, padx=4, pady=4, sticky=(N,E))
tax_lbl=Label(content2, text="Tax $")
tax_lbl.grid(column=4, row=1, padx=4, pady=4, sticky=(N,E))
calctax=Label(content2, textvariable=tax)
calctax.grid(column=5, row=1, padx=4, pady=4, sticky=W)
ship_lbl=Label(content2, text='Shipping')
ship_lbl.grid(column=4, row=2, padx=4, pady=4, sticky=(N,E))
total_lbl=Label(content2, text="Total $")
total_lbl.grid(column=4, row=4, padx=4, pady=4, sticky=(N,E))
calc_total=Label(content2, textvariable=total)
calc_total.grid(column=5, row=4, padx=4, pady=4, sticky=W)
date_lbl=Label(content2, text="Purchase Date")
date_lbl.grid(column=4, row=5, padx=4, pady=4, sticky=(N,E))
month_lbl=Label(content2, text="Month")
month_lbl.grid(column=4, row=6, padx=4, pady=4, sticky=(E))
day_lbl=Label(content2, text="Day")
day_lbl.grid(column=5, row=6, padx=4, pady=4, sticky=(W))
year_lbl=Label(content2, text="Year")
year_lbl.grid(column=6, row=6, padx=4, pady=4, sticky=(W))

######Entries
po_entry=Entry(content, width=9, textvariable=po)
po_entry.grid(column=1, columnspan=2, row=0, padx=4, pady=4, sticky=(N,W))
fname_entry=Entry(content, width=20,textvariable=fname)
fname_entry.grid(column=1, columnspan=2, row=1, padx=4, pady=4, sticky=(N,W))
lname_entry=Entry(content, width=20,textvariable=lname)
lname_entry.grid(column=1, columnspan=2, row=2, padx=4, pady=4, sticky=(N,W))
strtaddr1_entry=Entry(content, width=30,textvariable=strtaddr1)
strtaddr1_entry.grid(column=1, columnspan=2, row=3, padx=4, pady=4, sticky=(N,W))
strtaddr2_entry=Entry(content, width=30,textvariable=strtaddr2)
strtaddr2_entry.grid(column=1, columnspan=2, row=4, padx=4, pady=4, sticky=(N,W))
city_entry=Entry(content,width=20,textvariable=city)
city_entry.grid(column=3, row=5, padx=4, pady=4, sticky=(N,W))
zip_entry=Entry(content,width=20,textvariable=zipcode)
zip_entry.grid(column=1, row=6, padx=4, pady=4, sticky=(N,W))
tbox=Text(content, height=10, width=25, wrap='word')
tbox.grid(column=0,row=8,columnspan=2, padx=5, pady=5)
price_entry=Entry(content2, textvariable=price)
price_entry.grid(column=5, row=0, padx=4, pady=4, sticky=(N,E))

#a dropdown list of states a user can choose from
states_cbox=ttk.Combobox(content, width=3,state='readonly',textvariable=statesvar)
states_cbox['values']=("AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA", "HI", "ID",
        "IL", "IN", "IA", "KS","KY", "LA", "ME", "MD", "MA", "MI", "MN", "MS", "MO",
        "MT", "NE", "NV", "NH", "NJ", "NM", "NY","NC", "ND", "OH", "OK", "OR", "PA",
        "RI", "SC", "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY")
states_cbox.grid(column=1, row=5, padx=4, pady=4, sticky=(N,W))
ship_cbox=ttk.Combobox(content2, state='readonly', textvariable=shipping)
ship_cbox['value']=['One Day Shipping($5.99)', 'Two Day Shipping($3.99)', 'Four Day Shipping(Free)']
ship_cbox.grid(column=5, row=3, padx=4, pady=4, sticky=(W))
month_cbox=ttk.Combobox(content2, width=4, state='readonly', textvariable=month)
month_cbox['values']=('Jan','Feb', 'Mar', 'Apr', 'May', 'June', 'July', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec')
month_cbox.grid(column=4, row=7, padx=4, pady=4, sticky=E)
day_cbox=ttk.Combobox(content2, width=2, state='readonly', textvariable=day)
day_cbox.grid(column=5, row=7, padx=4, pady=4, sticky=W)
year_cbox=ttk.Combobox(content2, width=4, state='readonly', textvariable=year)
year_cbox['values'] = ('2016','2017','2018','2019','2020','2021','2022','2023','2024','2025','2026','2027'
                       ,'2028','2029','2030','2031','2032','2033','2034','2035','2036','2037','2038','2039','2040')
year_cbox.grid(column=6, row=7, columnspan=2,padx=4, pady=4, sticky=W)
#####Buttons
submit_btn=Button(content2, text="Submit", command=submit)
submit_btn.grid(column=4, row=8, columnspan=2, padx=4, pady=20, sticky=(N))
retrieve_btn=Button(content2, text="Retrieve", command=retrieve)
retrieve_btn.grid(column=4, row=9, columnspan=2, padx=4, pady=10, sticky=(N))
month_cbox.bind('<<ComboboxSelected>>', num_days)
ship_cbox.bind('<<ComboboxSelected>>', price_calc)
po_entry.focus()
tax.set("...")
total.set("...")
root.mainloop()
