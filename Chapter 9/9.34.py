from tkinter import *

class UserAccount:
    def __init__ (self, name, street, city, state, zip_):
        self.next = None
        self.previous = None
        self.name = name 
        self.street = street
        self.city = city 
        self.state = state
        self.zip_ = zip_

class AddressBook:     
    def __init__(self):
        self.first = None 
        self.last = None 
        self.current = None
        self.count = 1

    def add(self, name, street, city, state, zip_):
        new_account = UserAccount(name, street, city, state, zip_)
        if count == 1:
            self.first = new_account
            self.count += 1

        if not self.first:
            self.first = self.last = self.current = new_account
        else:
            self.last.next = new_account
            new_account.previous = self.last 
            self.last = new_account 
            self.current = self.last 

    def get_current_account(self):
        return self.current

    def goto_previous(self):
        if self.current and self.current.previous:
            self.current = self.current.previous 
        return self.get_current_account()

    def goto_next(self):
        if self.current and self.current.next:
            self.current = self.current.next 
        return self.current

AddressBook()


entry_list = AddressBook()
        
def add():
    name = name_entry.get()
    street = street_entry.get()
    city = city_entry.get()
    state = state_entry.get()
    zip_ = zip_entry.get()
    if name or street or city or state or zip_:
        entry_list.add(name, street, city, state, zip_)
        clear_entries()
        update_display()

def clear_entries():
    NAME.set('')
    STREET.set('')
    CITY.set('')
    STATE.set('')
    ZIP.set('')

    # name_entry.delete(0, tkinter.END)
    # street_entry.delete(0, tkinter.END)
    # city_entry.delete(0, tkinter.END)
    # state_entry.delete(0, tkinter.END)
    # zip_entry.delete(0, tkinter.END)

def update_display():
    entry = entry_list.get_current_account()
    if entry:
        {
        ZIP.set(entry.zip_)}
    else:
        clear_entries()

def previous():
    entry_list.goto_previous()
    update_display()

def next_():
    entry_list.goto_next()
    update_display()

def first():
    print()

def last():
    print()

window = Tk()
window.title('Address Book')
window.geometry('335x120')

#Mainscreen for 'NAME' and 'STREET'
mainscreen = Frame(window)
mainscreen.grid(row = 1, column = 1)
Label(mainscreen, text = 'Name').grid(row = 1, column = 1, padx = 3)
NAME = StringVar()
name_entry = Entry(mainscreen, width = 30, textvariable = NAME)
name_entry.grid(row = 1, column = 2)

Label(mainscreen, text = 'Street').grid(row = 2, column = 1, padx = 3)
STREET = StringVar()
street_entry = Entry(mainscreen, width = 30, textvariable = STREET)
street_entry.grid(row = 2, column = 2)

#Mainframe for 'CITY', 'STATE' and 'ZIP'

mainframe = Frame(window)
mainframe.grid(row = 2, column = 1)

Label(mainframe, text = 'City').grid(row = 3, column = 1, padx = 10)
CITY = StringVar()
city_entry = Entry(mainframe, width = 10, textvariable = CITY)
city_entry.grid(row = 3, column = 2) 

Label(mainframe, text = 'State').grid(row = 3, column = 3)
STATE = StringVar()
state_entry = Entry(mainframe, width = 5, textvariable = STATE, text = S)
state_entry.grid(row = 3, column = 4)

Label(mainframe, text = 'ZIP').grid(row = 3, column = 5)
ZIP = StringVar()
zip_entry = Entry(mainframe, width = 5, textvariable = ZIP)
zip_entry.grid(row = 3, column = 6)

#frame for buttons
frame = Frame(window)
frame.grid(row = 3, column = 1)

a = Button(frame, text = 'Add', command = add)
a.grid(row = 1, column = 1)
b = Button(frame, text = 'First', command = first)
b.grid(row = 1, column = 2)
c = Button(frame, text = 'Next', command = next_)
c.grid(row = 1, column = 3)
d = Button(frame, text = 'Previous', command = previous)
d.grid(row = 1, column = 4)
e = Button(frame, text = 'Last', width = 2, command = last)
e.grid(row = 1, column = 5)

window.mainloop()


