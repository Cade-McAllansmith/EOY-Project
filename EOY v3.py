from tkinter import *
from tkinter import ttk
from datetime import datetime, timedelta

root = Tk()
root.geometry("305x100")
root.config(bg = "#6fa8dc")

pizza_p = 0
pizza_num = 1
lcv = 1
pizzas_num[1] = 0
pizzas_num[2] = 0
pizzas_num[3] = 0
pizzas_num[4] = 0
pizzas_num[5] = 0
pizzas_num[6] = 0
pizzas_num[7] = 0
pizzas_num[8] = 0
pizzas_num[9] = 0
pizzas_num[10] = 0
pizzas_num[11] = 0
pizzas_num[12] = 0
pizzas[1] = "Hawiian"
pizzas[2] = "Pepperoni"
pizzas[3] = "Cheese"
pizzas[4] = "Ham & Cheese"
pizzas[5] = "Beef & Onion"
pizzas[6] = "Vegetarian"
pizzas[7] = "Cheesy Garlic"
pizzas[8] = "Chicken, Bacon & Aioli"
pizzas[9] = "Chicken & Camembert"
pizzas[10] = "Buffalo Chicken"
pizzas[11] = "Italian Parmesan"
pizzas[12] = "Double Bacon Cheeseburger"

def initialize():
    global firstmenu
    global menus
    menus = 1
   
    firstmenu = Toplevel()
    firstmenu.geometry("305x175")
    firstmenu.config(bg = "#6fa8dc")
    
    name_msg = Label(firstmenu,text="Name:", bg = "#6fa8dc")
    name_msg.place(x=0, y=10)
    name = Entry(firstmenu)
    name.place(x=160, y=10)
    next1 = Button(firstmenu, text="Next", bg = "#cc4125", command=lambda: next_1())
    next1.place(x=15, y=110, width=125, height=37)
    cancel_order1 = Button(firstmenu, text="Cancel Order", bg = "#cc4125", command=lambda: cancel_order())
    cancel_order1.place(x=165, y=110, width=125, height=37)



def delivery2():
    initialize()
    global delivery_
    delivery_ = 1
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
    global delivery_
    delivery_ = 0

def next_1():
    global secondmenu
    global menus
    global button_1
    global button_2
    global button_3
    global button_4
    global button_5
    global button_6
    global button_7
    global button_8
    global button_9
    global button_10
    global button_11
    global button_12
    menus = 2
    def comboclick(event):
        global pizza_num
        pizza_num = pizza_numbox.get()
        

    secondmenu = Toplevel()
    secondmenu.geometry("643x327")
    secondmenu.config(bg = "#6fa8dc")
    
    title_msg2 = Label(secondmenu, text="Tony's Pizza Company", bg = "#6fa8dc")
    title_msg2.place(x=23, y=0)
    nums = [
        "1",
        "2",
        "3",
        "4",
        "5"
    ]
    pizza_numbox = ttk.Combobox(secondmenu, value = nums, state = "readonly")
    pizza_numbox.current(0)
    pizza_numbox.bind("<<ComboboxSelected>>", comboclick)
    pizza_numbox.place(x=15, y=30)
    
    button_1 = Button(secondmenu, text="Hawiian", bg = "#cc4125", command=lambda: b1())
    button_1.place(x=23, y=60, width=125, height=37)
    button_2 = Button(secondmenu, text="Pepperoni", bg = "#cc4125", command=lambda: b2())
    button_2.place(x=203, y=60, width=125, height=37)
    button_3 = Button(secondmenu, text="Cheese", bg = "#cc4125", command=lambda: b3())
    button_3.place(x=383, y=60, width=125, height=37)
    button_4 = Button(secondmenu, text="Ham & Cheese", bg = "#cc4125", command=lambda: b4())
    button_4.place(x=23, y=105, width=125, height=37)
    button_5 = Button(secondmenu, text="Beef & Onion", bg = "#cc4125", command=lambda: b5())
    button_5.place(x=203, y=105, width=125, height=37)
    button_6 = Button(secondmenu, text="Vegetarian", bg = "#cc4125", command=lambda: b6())
    button_6.place(x=383, y=105, width=125, height=37)
    button_7 = Button(secondmenu, text="Cheesy Garlic", bg = "#cc4125", command=lambda: b7())
    button_7.place(x=23, y=150, width=125, height=37)
    button_8 = Button(secondmenu, text="""Chicken, Bacon & 
    Aioli""", bg = "#cc4125", command=lambda: b8())
    button_8.place(x=203, y=150, width=125, height=37)
    button_9 = Button(secondmenu, text="""Chicken & 
    Camembert""", bg = "#cc4125", command=lambda: b9())
    button_9.place(x=383, y=150, width=125, height=37)
    button_10 = Button(secondmenu, text="Buffalo Chicken", bg = "#cc4125", command=lambda: b10())
    button_10.place(x=23, y=195, width=125, height=37)
    button_11 = Button(secondmenu, text="Italian Parmesan", bg = "#cc4125", command=lambda: b11())
    button_11.place(x=203, y=195, width=125, height=37)
    button_12 = Button(secondmenu, text="""Double Bacon 
    Cheeseburger""", bg = "#cc4125", command=lambda: b12())
    button_12.place(x=383, y=195, width=125, height=37)
    
    c_instruct = Entry(secondmenu, bg = "#6fa8dc")
    c_instruct.place(x=15, y=240, width=297)
    if delivery_ == 1:
        d_instruct = Entry(secondmenu, bg = "#6fa8dc")
        d_instruct.place(x=333, y=240, width=297)

    undo = Button(secondmenu, text="""Undo Last Pizza 
    Selection""", bg = "#cc4125")
    undo.place(x=23, y=285, width=105, height=37)
    o_display = Label(secondmenu, text="", bg = "#cc4125", relief="raised", borderwidth=2)
    o_display.place(x=203, y=285, width=125, height=37)
    cancel_order2 = Button(secondmenu, text="Cancel Order", bg = "#cc4125", command=lambda: cancel_order())
    cancel_order2.place(x=403, y=285, width=105, height=37)
    next2 = Button(secondmenu, text="Next", bg = "#cc4125", command=lambda: next_2())
    next2.place(x=521, y=285, width=105, height=37)

def b1():
    pizzas.num[1] =+ 1
    calc()

def b2():
    pizzas.num[2] =+ 1
    calc()

def b3():
    pizzas.num[3] =+ 1
    calc()

def b4():
    pizzas.num[4] =+ 1
    calc()

def b5():
    pizzas.num[5] =+ 1
    calc()

def b6():
    pizzas.num[6] =+ 1
    calc()

def b7():
    pizzas.num[7] =+ 1
    calc()

def b8():
    pizzas.num[8] =+ 1
    calc()

def b9():
    pizzas.num[9] =+ 1
    calc()

def b10():
    pizzas.num[10] =+ 1
    calc()

def b11():
    pizzas.num[11] =+ 1
    calc()

def b12():
    pizzas.num[12] =+ 1
    calc()


def calc():
    global pizza_p
    global button_1
    global button_2
    global button_3
    global button_4
    global button_5
    global button_6
    global button_7
    global button_8
    global button_9
    global button_10
    global button_11
    global button_12
    global pizza_num
    pizza_p = pizza_p + 1
    if pizza_p == int(pizza_num):
        button_1.config(state = "disabled")
        button_2.config(state = "disabled")
        button_3.config(state = "disabled")
        button_4.config(state = "disabled")
        button_5.config(state = "disabled")
        button_6.config(state = "disabled")
        button_7.config(state = "disabled")
        button_8.config(state = "disabled")
        button_9.config(state = "disabled")
        button_10.config(state = "disabled")
        button_11.config(state = "disabled")
        button_12.config(state = "disabled")
    if pizzas.num[1] > 0:
        o_display_text = o_display_text + "Hawiian" + "\n"
        o_display.config(text="{}" .format (o_display_text))



def next_2():
    global date
    global Date
    
    thirdmenu = Toplevel()
    thirdmenu.geometry("245x500")
    thirdmenu.config(bg = "#6fa8dc")

    date = datetime.now()
    Date = date.strftime("%d/%m/%y")
    date_l = Label(thirdmenu, text="{}".format (Date), bg = "#6fa8dc")
    date_l.place(x=5,y=0)

    title_msg3 = Label(thirdmenu, text="Tony's Pizza Company", bg = "#6fa8dc")
    title_msg3.place(x=116, y=0)
    if delivery_ == 1:
        subtitle_msg = Label(thirdmenu, text="Delivery Order", bg = "#6fa8dc")
        subtitle_msg.place(x=140, y=18)
        output()
    else:
        subtitle_msg = Label(thirdmenu, text="Pickup Order", bg = "#6fa8dc")
        subtitle_msg.place(x=145, y=18)
        output()

def output():
    yes = 0

def cancel_order():
    if menus == 1:
        firstmenu.destroy()
    else:
        firstmenu.destroy()
        secondmenu.destroy()
    

title_msg = Label(root, text="Tony's Pizza Company", bg = "#6fa8dc")
title_msg.place(x=92, y=0)

pickup = Button(root, text="Pickup", bg = "#cc4125", command=lambda: pickup2())
pickup.place(x=15, y=40, width=125, height=37)

delivery = Button(root, text="Delivery", bg = "#cc4125", command=lambda: delivery2())
delivery.place(x=165, y=40, width=125, height=37)

root.mainloop()