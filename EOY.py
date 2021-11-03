from tkinter import *
from datetime import datetime, timedelta

root = Tk()
root.geometry("305x100")
root.config(bg = "#6fa8dc")

def initialize():
    global firstmenu
    firstmenu = Toplevel()
    firstmenu.geometry("305x100")
    firstmenu.config(bg = "#6fa8dc")
    name_msg = Label(firstmenu,text="Name:", bg = "#6fa8dc")
    name_msg.place(x=0, y=10)
    name = Entry(firstmenu)
    name.place(x=160, y=10)


def delivery2():
    initialize()
    cus_address_msg = Label(firstmenu,text="Customer Address:", bg = "#6fa8dc")
    cus_address_msg.place(x=0, y=40)
    cus_address = Entry(firstmenu)
    cus_address.place(x=160, y=40)
    
    cus_pnumber_msg = Label(firstmenu,text="Customer Phone Number:", bg = "#6fa8dc")
    cus_pnumber_msg.place(x=0, y=70)
    cus_pnumber = Entry(firstmenu)
    cus_pnumber.place(x=160, y=70)

def pickup2():
    initialize()


title_msg = Label(root, text="Tony's Pizza Company", bg = "#6fa8dc")
title_msg.place(x=92, y=0)

pickup = Button(root, text="Pickup", bg = "#cc4125", command=lambda: pickup2())
pickup.place(x=15, y=40, width=125, height=37)

delivery = Button(root, text="Delivery", bg = "#cc4125", command=lambda: delivery2())
delivery.place(x=165, y=40, width=125, height=37)

root.mainloop()