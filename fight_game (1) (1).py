#Joshua Hinojosa
#Mr. Davis
#Adv. Comp. Programming
#10/14/16

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
import random

global plyr1hp, plyr2hp
root = Tk()
root.title("Fighter Street")

def showversion():              #has a message box pull up with program title and version
    messagebox.showinfo('About','''Fighter Street
version .1''')
p1atkcodes=('BT', 'UBD', 'PS')
p2atkcodes=('TS', 'HD', 'Tsr')

p1attacks={'BT':15, 'UBD':25, 'PS':10}
p2attacks={'TS':12,'HD':26, 'Tsr':7}
player1hp=StringVar()
player2hp=StringVar()
p1cardstats=StringVar()
p2cardstats=StringVar()
player1cards=('Back Therapy', 'Umbrella Beat Down', 'Pepper Spray')
p1cardnames = StringVar(value=player1cards)
player2cards=('Toe Stepper', 'Hug of Death', 'Taser')
p2cardnames = StringVar(value=player2cards)
winvar=StringVar()
losevar=StringVar()
plyr1hp='20'
plyr2hp='20'

def showstats(*args):
    p1cardselect = lbox1.curselection()
    if len(p1cardselect)==1:
        idx = int(p1cardselect[0])
        code = p1atkcodes[idx]
        name = player1cards[idx]
        attkdmg = p1attacks[code]

    p1cardstats.set("Attack: "+ str(attkdmg))

def fight():
    '''once you click fight button you attack with card selected and a random amount of damage is
    done with the attack stat as maximum amount of damage that can be dealt and player 2's card
    is chosen at random that does a random amount of damage with attach stat as maximum amount of damage'''
    global plyr1hp, plyr2hp
    p1cardselect = lbox1.curselection()
    if len(p1cardselect) == 1:
        idx = int(p1cardselect[0])
        code = p1atkcodes[idx]
        name = player1cards[idx]
        p1attkdmg = random.randint(10,p1attacks[code])
    p2cardchoices=player2cards
    randomcard=random.choice(p2cardchoices)
    p2cardselect=randomcard
    if p2cardselect=='Toe Stepper':
        idx=0
        code = p2atkcodes[idx]
        name = player1cards[idx]
        p2attkdmg = random.randint(5, p2attacks[code])
        p2cardstats.set(str(p2cardselect)+ " -> "+"Attack: " + str(p2attacks[code]))
    elif p2cardselect=='Hug of Death':
        idx = 1
        code = p2atkcodes[idx]
        name = player1cards[idx]
        p2attkdmg = random.randint(5, p2attacks[code])
        p2cardstats.set(str(p2cardselect) + " -> " + "Attack: " + str(p2attacks[code]))
    elif p2cardselect=='Taser':
        idx = 2
        code = p2atkcodes[idx]
        name = player1cards[idx]
        p2attkdmg = random.randint(5, p2attacks[code])
        p2cardstats.set(str(p2cardselect) + " -> " + "Attack: " + str(p2attacks[code]))
    plyr1hp=int(plyr1hp)
    plyr2hp=int(plyr2hp)
    plyr2hp=plyr2hp-p1attkdmg
    plyr1hp = plyr1hp - p2attkdmg
    if plyr1hp<=0:               #if a players health is equal or below 0 then it shows the winner and loser
        losevar.set("Player 1")     #and disables fight button
        winvar.set("Player 2")
        player1hp.set(str(0))
        player2hp.set(str(plyr2hp))
        fight_btn.configure(state='disabled')
    elif plyr2hp<=0:
        losevar.set("Player 2")
        winvar.set("Player 1")
        player1hp.set(str(plyr1hp))
        player2hp.set(str(0))
        fight_btn.configure(state='disabled')
    else:
        player1hp.set(str(plyr1hp))
        player2hp.set(str(plyr2hp))
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

#creates the mainframe and sets window size
mainframe = Frame(root, width=300, height=375)
mainframe.grid(column=0, row=0, sticky=(N,S,E,W))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)
#Creates frame and content within the mainframe
content = ttk.Frame(root, padding=(5, 5, 12, 0))
content.grid(column=0, row=0, sticky=(N,S,E,W))
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0,weight=1)
#Player labels and HP's
player1_lbl=Label(content, text='Player 1')
player1_lbl.grid(column=0,row=0, padx=15, pady=4)
player1hp_lbl=Label(content, text='HP: ')
player1hp_lbl.grid(column=0,row=1,padx=15, pady=4)
player2_lbl=Label(content, text='Player 2')
player2_lbl.grid(column=3,row=0,padx=15, pady=4)
player2hp_lbl=Label(content, text='HP: ')
player2hp_lbl.grid(column=3,row=1,padx=15, pady=4)
p1hp=Label(content, textvariable=player1hp)
p1hp.grid(column=1,row=1,padx=15, pady=4)
p2hp=Label(content, textvariable=player2hp)
p2hp.grid(column=4,row=1,padx=15, pady=4)

#Payer card stats
p1stats_lbl=Label(content, text='Stats')
p1stats_lbl.grid(column=0, row=6)
p1stats=Label(content, textvariable=p1cardstats)
p1stats.grid(column=0, row=7)
p2stats_lbl=Label(content, text='Stats')
p2stats_lbl.grid(column=3, row=6)
p2stats=Label(content, textvariable=p2cardstats)
p2stats.grid(column=3, row=7)

#Makes listbox where player can choose cards from
lbox1=Listbox(content, listvariable=p1cardnames, height=8)
lbox1.grid(row=2, column=0, rowspan=4,padx=15,pady=4)
lbox2=Listbox(content, state='disabled',listvariable=p2cardnames, height=8)
lbox2.grid(row=2, column=3, rowspan=4,padx=15, pady=4)

#fight button that begins the fight
fight_btn=Button(content, text='Fight', command=fight)
fight_btn.grid(row=5, column=2, padx=15,pady=4)

#Shows who won the fight
wins_lbl=Label(content, text='Wins')
wins_lbl.grid(row=1, column=2,padx=15, pady=4)
loses_lbl=Label(content, text='Loses')
loses_lbl.grid(row=3, column=2,padx=15, pady=1)
wins=Label(content, textvariable=winvar)
wins.grid(column=2,row=0,padx=15, pady=4)
loses=Label(content, textvariable=losevar)
loses.grid(column=2,row=2,padx=15, pady=1)

# Set the starting state of the interface
#sets default of selecting first card
winvar.set("----")
losevar.set("----")
lbox1.bind('<<ListboxSelect>>', showstats)
lbox1.selection_set(0)
player1hp.set(plyr1hp)
player2hp.set(plyr2hp)

root.mainloop()