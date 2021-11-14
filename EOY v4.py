from tkinter import *
from tkinter import ttk
from datetime import datetime, timedelta
 
root = Tk()
root.geometry("305x100")
root.config(bg = "#6fa8dc")
 
pizza_p = 0
pizza_numb = 1
lcv = 0
pizzas_numb = [0]*12
pizzas = "Hawiian","Pepperoni","Cheese","Ham & Cheese","Beef & Onion","Vegetarian","Cheesy Garlic","Chicken, Bacon & Aioli","Chicken & Camembert","Buffalo Chicken","Italian Parmesan","Double Bacon Cheeseburger"
o_display_text = ""
 
 
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
    global o_display
    global undo
    menus = 2
    def comboclick(event):
        global pizza_numb
        global optionlist
        pizza_numb = pizza_numbox.get()
        button_enable()
        optionlist = [""]*0
        if lcv != 0:
            undo.config(state = "normal")
        
 
    secondmenu = Toplevel()
    secondmenu.geometry("643x395")
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
    Selection""", bg = "#cc4125", state = "disabled", command=lambda: undo_())
    undo.place(x=23, y=343, width=105, height=37)
    o_display = Label(secondmenu, text="", bg = "#cc4125", relief="raised", borderwidth=2)
    o_display.place(x=178, y=285, width=175, height=95)
    cancel_order2 = Button(secondmenu, text="Cancel Order", bg = "#cc4125", command=lambda: cancel_order())
    cancel_order2.place(x=403, y=343, width=105, height=37)
    next2 = Button(secondmenu, text="Next", bg = "#cc4125", command=lambda: next_2())
    next2.place(x=521, y=343, width=105, height=37)
 
def undo_():
    global pizza_p
    global lcv
    lcv = lcv - 1
    o_display_text = optionlist[(lcv-1)]
    optionlist[lcv-2] = ""
    o_display.config(text="{}" .format (o_display_text))
    pizza_p = pizza_p - 1
    if lcv == 0:
        undo.config(state = "disabled")
    button_enable()

def button_enable():
    if pizza_p != int(pizza_numb):
        button_1.config(state = "normal")
        button_2.config(state = "normal")
        button_3.config(state = "normal")
        button_4.config(state = "normal")
        button_5.config(state = "normal")
        button_6.config(state = "normal")
        button_7.config(state = "normal")
        button_8.config(state = "normal")
        button_9.config(state = "normal")
        button_10.config(state = "normal")
        button_11.config(state = "normal")
        button_12.config(state = "normal")
 
def b1():
    pizzas_numb[0] = pizzas_numb[0] + 1
    calc()
 
def b2():
    pizzas_numb[1] = pizzas_numb[1] + 1
    calc()
 
def b3():
    pizzas_numb[2] = pizzas_numb[2] + 1
    calc()
 
def b4():
    pizzas_numb[3] = pizzas_numb[3] + 1
    calc()
 
def b5():
    pizzas_numb[4] = pizzas_numb[4] + 1
    calc()
 
def b6():
    pizzas_numb[5] = pizzas_numb[5] + 1
    calc()
 
def b7():
    pizzas_numb[6] = pizzas_numb[6] + 1
    calc()
 
def b8():
    pizzas_numb[7] = pizzas_numb[7] + 1
    calc()
 
def b9():
    pizzas_numb[8] = pizzas_numb[8] + 1
    calc()
 
def b10():
    pizzas_numb[9] = pizzas_numb[9] + 1
    calc()
 
def b11():
    pizzas_numb[10] = pizzas_numb[10] + 1
    calc()
 
def b12():
    pizzas_numb[11] = pizzas_numb[11] + 1
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
    global pizza_numb
    global o_display_text
    global optionlist
    global lcv
    optionlist = [""]*5
    pizza_p = pizza_p + 1
    if pizza_p == int(pizza_numb):
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
    if pizzas_numb[0] > 0:
        o_display_text = o_display_text + "Hawiian" + "\n"
        o_display.config(text="{}" .format (o_display_text))
        pizzas_numb[0] = 0
    elif pizzas_numb[1] > 0:
        o_display_text = o_display_text + "Pepperoni" + "\n"
        o_display.config(text="{}" .format (o_display_text))
        pizzas_numb[1] = 0
    elif pizzas_numb[2] > 0:
        o_display_text = o_display_text + "Cheese" + "\n"
        o_display.config(text="{}" .format (o_display_text))
        pizzas_numb[2] = 0
    elif pizzas_numb[3] > 0:
        o_display_text = o_display_text + "Ham & Cheese" + "\n"
        o_display.config(text="{}" .format (o_display_text))
        pizzas_numb[3] = 0
    elif pizzas_numb[4] > 0:
        o_display_text = o_display_text + "Beef & Onion" + "\n"
        o_display.config(text="{}" .format (o_display_text))
        pizzas_numb[4] = 0
    elif pizzas_numb[5] > 0:
        o_display_text = o_display_text + "Vegetarian" + "\n"
        o_display.config(text="{}" .format (o_display_text))
        pizzas_numb[5] = 0
    elif pizzas_numb[6] > 0:
        o_display_text = o_display_text + "Cheesy Garlic" + "\n"
        o_display.config(text="{}" .format (o_display_text))
        pizzas_numb[6] = 0
    elif pizzas_numb[7] > 0:
        o_display_text = o_display_text + "Chicken, Bacon & Aioli" + "\n"
        o_display.config(text="{}" .format (o_display_text))
        pizzas_numb[7] = 0
    elif pizzas_numb[8] > 0:
        o_display_text = o_display_text + "Chicken & Camembert" + "\n"
        o_display.config(text="{}" .format (o_display_text))
        pizzas_numb[8] = 0
    elif pizzas_numb[9] > 0:
        o_display_text = o_display_text + "Buffalo Chicken" + "\n"
        o_display.config(text="{}" .format (o_display_text))
        pizzas_numb[9] = 0
    elif pizzas_numb[10] > 0:
        o_display_text = o_display_text + "Italian Parmesan" + "\n"
        o_display.config(text="{}" .format (o_display_text))
        pizzas_numb[10] = 0
    elif pizzas_numb[11] > 0:
        o_display_text = o_display_text + "Double Bacon Cheeseburger" + "\n"
        o_display.config(text="{}" .format (o_display_text))
        pizzas_numb[11] = 0
    optionlist[lcv] = (o_display_text)
    lcv = lcv + 1
    if lcv != 0:
            undo.config(state = "normal")
 
 
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