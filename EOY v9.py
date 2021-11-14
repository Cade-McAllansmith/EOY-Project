from tkinter import *
from tkinter import ttk
from datetime import datetime, timedelta
from tkinter import font
from tkinter.font import families
import re
 
root = Tk()
root.geometry("305x100")
root.config(bg = "#6fa8dc")

lastselected = ""
total_price = 0
DELIVERY_CHARGE = 3
PIZZA_PRICE = 8.5
GOURMET_PRICE = 13.5
pizza_p = 0
pizza_numb = 1
lcv = 0
lcv2 = 0
pizzas_numb = [0]*12
pizzas_numbtotal = [0]*12
pizzas_s = 0
multi = [0]*5
pizzas = "Hawiian","Pepperoni","Cheese","Ham & Cheese","Beef & Onion","Vegetarian","Cheesy Garlic","Chicken, Bacon & Aioli","Chicken & Camembert","Buffalo Chicken","Italian Parmesan","Double Bacon Cheeseburger"
o_display_text = ""
 
 
def initialize():
    global firstmenu
    global name
    global menus
    menus = 1
   
    firstmenu = Toplevel()
    firstmenu.geometry("305x175")
    firstmenu.config(bg = "#6fa8dc")
   
    name_msg = Label(firstmenu,text="Name:", bg = "#6fa8dc", font="10")
    name_msg.place(x=0, y=10)
    name = Entry(firstmenu)
    name.place(x=160, y=10)
    next1 = Button(firstmenu, text="Next", bg = "#cc4125", font=("candara 10 roman"), command=lambda: next_1())
    next1.place(x=15, y=110, width=125, height=37)
    cancel_order1 = Button(firstmenu, text="Cancel Order", bg = "#cc4125", font=("candara 10 roman"), command=lambda: cancel_order())
    cancel_order1.place(x=165, y=110, width=125, height=37)
 
 
 
def delivery2():
    initialize()
    global delivery_
    global cus_address
    global cus_pnumber
    delivery_ = 1
    cus_address_msg = Label(firstmenu,text="Customer Address:", bg = "#6fa8dc", font=("candara 10 roman"))
    cus_address_msg.place(x=0, y=40)
    cus_address = Entry(firstmenu)
    cus_address.place(x=160, y=40)
   
    cus_pnumber_msg = Label(firstmenu,text="Customer Phone Number:", bg = "#6fa8dc", font=("candara 10 roman"))
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
    global c_instruct
    global d_instruct
    menus = 2
    def comboclick(event):
        global pizza_numb
        global optionlist
        pizza_numb = pizza_numbox.get()
        button_enable()
        optionlist = [""]*0
        if lcv > 0:
            undo.config(state = "normal")
       
 
    secondmenu = Toplevel()
    secondmenu.geometry("643x395")
    secondmenu.config(bg = "#6fa8dc")
   
    title_msg2 = Label(secondmenu, text="Tony's Pizza Company", bg = "#6fa8dc", font=("candara 13 roman"))
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
   
    button_1 = Button(secondmenu, text="Hawiian", bg = "#cc4125", font=("candara 10 roman"), command=lambda: b1())
    button_1.place(x=23, y=60, width=125, height=37)
    button_2 = Button(secondmenu, text="Pepperoni", bg = "#cc4125", font=("candara 10 roman"), command=lambda: b2())
    button_2.place(x=203, y=60, width=125, height=37)
    button_3 = Button(secondmenu, text="Cheese", bg = "#cc4125", font=("candara 10 roman"), command=lambda: b3())
    button_3.place(x=383, y=60, width=125, height=37)
    button_4 = Button(secondmenu, text="Ham & Cheese", bg = "#cc4125", font=("candara 10 roman"), command=lambda: b4())
    button_4.place(x=23, y=105, width=125, height=37)
    button_5 = Button(secondmenu, text="Beef & Onion", bg = "#cc4125", font=("candara 10 roman"), command=lambda: b5())
    button_5.place(x=203, y=105, width=125, height=37)
    button_6 = Button(secondmenu, text="Vegetarian", bg = "#cc4125", font=("candara 10 roman"), command=lambda: b6())
    button_6.place(x=383, y=105, width=125, height=37)
    button_7 = Button(secondmenu, text="Cheesy Garlic", bg = "#cc4125", font=("candara 10 roman"), command=lambda: b7())
    button_7.place(x=23, y=150, width=125, height=37)
    button_8 = Button(secondmenu, text="""Chicken, Bacon &
    Aioli""", bg = "#cc4125", font=("candara 10 roman"), command=lambda: b8())
    button_8.place(x=203, y=150, width=125, height=37)
    button_9 = Button(secondmenu, text="""Chicken &
    Camembert""", bg = "#cc4125", font=("candara 10 roman"), command=lambda: b9())
    button_9.place(x=383, y=150, width=125, height=37)
    button_10 = Button(secondmenu, text="Buffalo Chicken", bg = "#cc4125", font=("candara 10 roman"), command=lambda: b10())
    button_10.place(x=23, y=195, width=125, height=37)
    button_11 = Button(secondmenu, text="Italian Parmesan", bg = "#cc4125", font=("candara 10 roman"), command=lambda: b11())
    button_11.place(x=203, y=195, width=125, height=37)
    button_12 = Button(secondmenu, text="""Double Bacon
    Cheeseburger""", bg = "#cc4125", font=("candara 10 roman"), command=lambda: b12())
    button_12.place(x=383, y=195, width=125, height=37)
   
    c_instruct_msg = Label(secondmenu, text="Customer Instructions/Preferences:", bg = "#6fa8dc", font=("candara 10 roman"))
    c_instruct_msg.place(x=15, y=260)
    c_instruct = Entry(secondmenu, bg = "#6fa8dc")
    c_instruct.place(x=15, y=240, width=297)
    if delivery_ == 1:
        d_instruct = Entry(secondmenu, bg = "#6fa8dc")
        d_instruct.place(x=333, y=240, width=297)
        d_instruct_msg = Label(secondmenu, text="Delivery Instructions/Preferences:", bg = "#6fa8dc", font=("candara 10 roman"))
        d_instruct_msg.place(x=333, y=260)
 
    undo = Button(secondmenu, text="""Undo Last Pizza
    Selection""", bg = "#cc4125", state = "disabled", font=("candara 10 roman"), command=lambda: undo_())
    undo.place(x=23, y=343, width=105, height=37)
    o_display = Label(secondmenu, text="", bg = "#cc4125", relief="raised", borderwidth=2, font=("candara 10 roman"))
    o_display.place(x=178, y=285, width=175, height=95)
    cancel_order2 = Button(secondmenu, text="Cancel Order", bg = "#cc4125", font=("candara 10 roman"), command=lambda: cancel_order())
    cancel_order2.place(x=403, y=343, width=105, height=37)
    next2 = Button(secondmenu, text="Next", bg = "#cc4125", font=("candara 10 roman"), command=lambda: next_2())
    next2.place(x=521, y=343, width=105, height=37)
 
def undo_():
    global pizza_p
    global lcv
    global o_display_text
    lcv = lcv - 1
    o_display_text = ("\n".join(o_display_text.split("\n")[:-2]))
    o_display_text = o_display_text + "\n"
    o_display.config(text="{}" .format (o_display_text))
    pizza_p = pizza_p - 1
    if lcv < 1:
        undo.config(state = "disabled")
    button_enable()
    for lcv4 in range(12):
        if lastselected == pizzas[lcv4]:
            pizzas_numbtotal[lcv4] = pizzas_numbtotal[lcv4] - 1
 
def button_enable():
    if pizza_p == int(pizza_numb) or pizza_p < int(pizza_numb):
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
    global lastselected
    pizzas_numb[0] = pizzas_numb[0] + 1
    pizzas_numbtotal[0] = pizzas_numbtotal[0] + 1
    lastselected = "Hawiian"
    calc()
 
def b2():
    global lastselected
    pizzas_numb[1] = pizzas_numb[1] + 1
    pizzas_numbtotal[1] = pizzas_numbtotal[1] + 1
    lastselected = "Pepperoni"
    calc()
 
def b3():
    global lastselected
    pizzas_numb[2] = pizzas_numb[2] + 1
    pizzas_numbtotal[2] = pizzas_numbtotal[2] + 1
    lastselected = "Cheese"
    calc()
 
def b4():
    global lastselected
    pizzas_numb[3] = pizzas_numb[3] + 1
    pizzas_numbtotal[3] = pizzas_numbtotal[3] + 1
    lastselected = "Ham & Cheese"
    calc()
 
def b5():
    global lastselected
    pizzas_numb[4] = pizzas_numb[4] + 1
    pizzas_numbtotal[4] = pizzas_numbtotal[4] + 1
    lastselected = "Beef & Onion"
    calc()
 
def b6():
    global lastselected
    pizzas_numb[5] = pizzas_numb[5] + 1
    pizzas_numbtotal[5] = pizzas_numbtotal[5] + 1
    lastselected = "Vegetarian"
    calc()
 
def b7():
    global lastselected
    pizzas_numb[6] = pizzas_numb[6] + 1
    pizzas_numbtotal[6] = pizzas_numbtotal[6] + 1
    lastselected = "Cheesy Garlic"
    calc()
 
def b8():
    global lastselected
    pizzas_numb[7] = pizzas_numb[7] + 1
    pizzas_numbtotal[7] = pizzas_numbtotal[7] + 1
    lastselected = "Chicken, Bacon & Aioli"
    calc()
 
def b9():
    global lastselected
    pizzas_numb[8] = pizzas_numb[8] + 1
    pizzas_numbtotal[8] = pizzas_numbtotal[8] + 1
    lastselected = "Chicken & Camembert"
    calc()
 
def b10():
    global lastselected
    pizzas_numb[9] = pizzas_numb[9] + 1
    pizzas_numbtotal[9] = pizzas_numbtotal[9] + 1
    lastselected = "Buffalo Chicken"
    calc()
 
def b11():
    global lastselected
    pizzas_numb[10] = pizzas_numb[10] + 1
    pizzas_numbtotal[10] = pizzas_numbtotal[10] + 1
    lastselected = "Italian Parmesan"
    calc()
 
def b12():
    global lastselected
    pizzas_numb[11] = pizzas_numb[11] + 1
    pizzas_numbtotal[11] = pizzas_numbtotal[11] + 1
    lastselected = "Double Bacon Cheeseburger"
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
    if pizza_p == int(pizza_numb) or pizza_p > int(pizza_numb):
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
    lcv = lcv + 1
    if lcv > 0:
            undo.config(state = "normal")
 
 
def next_2():
    global date
    global Date
    global thirdmenu
    global yplace
    global menus
    menus = 3
    if delivery_ == 0:
        yplace = 0
    else:
        yplace = 40
 
    thirdmenu = Toplevel()
    thirdmenu.config(bg = "#6fa8dc")
 
    date = datetime.now()
    Date = date.strftime("%d/%m/%y")
    date_l = Label(thirdmenu, text="{}".format (Date), bg = "#6fa8dc", font=("candara 10 roman"))
    date_l.place(x=5,y=0)
 
    title_msg3 = Label(thirdmenu, text="Tony's Pizza Company", bg = "#6fa8dc", font=("candara 13 roman"))
    title_msg3.place(x=240, y=0, anchor="ne")
 
    o_name = name.get()
    o_nametext = Label(thirdmenu, text= "{}" .format (o_name), bg = "#6fa8dc", font=("candara 10 roman"))
    o_nametext.place(x=122,y=50, anchor="center")
 
    if delivery_ == 1:
        subtitle_msg = Label(thirdmenu, text="Delivery Order", bg = "#6fa8dc", font=("candara 10 roman"))
        subtitle_msg.place(x=140, y=25)
        o_address = cus_address.get()
        o_addresstext = Label(thirdmenu, text= "{}" .format (o_address), bg = "#6fa8dc", font=("candara 10 roman"))
        o_addresstext.place(x=122, y=70, anchor="center")
        o_cus_pnumber = cus_pnumber.get()
        o_cus_pnumbertext = Label(thirdmenu, text= "{}" .format (o_cus_pnumber), bg = "#6fa8dc", font=("candara 10 roman"))
        o_cus_pnumbertext.place(x=122, y=90, anchor="center")
        output()
    else:
        subtitle_msg = Label(thirdmenu, text="Pickup Order", bg = "#6fa8dc", font=("candara 10 roman"))
        subtitle_msg.place(x=145, y=25)
        output()
 
def output():
    global pizzas
    global total_price
    global pizzas_s
    global price
    global pricetext
    global pizza
    global pizzatext
    global yplace
    price = [0]*int(pizza_numb)
    pricetext = [0]*int(pizza_numb)
    pizzatext = [0]*int(pizza_numb)
    pizza = [0]*int(pizza_numb)
    for lcv2 in range(7):
        if pizzas_numbtotal[lcv2] > 0:
            pizzas_s = pizzas_s + 1
            multi[pizzas_s - 1] = pizzas_numbtotal[lcv2]
            if multi[pizzas_s - 1] > 1:
                pizzatext[pizzas_s - 1] = pizzas[lcv2] + " x" + str(multi[pizzas_s - 1]) + ":"
            else:
                pizzatext[pizzas_s - 1] = pizzas[lcv2] + ":"
            pizza[pizzas_s - 1] = "{}" .format (pizzatext[pizzas_s - 1])
            price[pizzas_s - 1] = PIZZA_PRICE * int(multi[pizzas_s - 1])
            pricetext[pizzas_s - 1] = str(price[pizzas_s - 1])
            total_price = total_price + price[pizzas_s - 1]
    for lcv2 in range(8,12):
        if pizzas_numbtotal[lcv2] > 0:
            pizzas_s = pizzas_s + 1
            multi[pizzas_s - 1] = pizzas_numbtotal[lcv2]
            if multi[pizzas_s - 1] > 1:
                pizzatext[pizzas_s - 1] = pizzas[pizzas_s - 1] + " x" + str(multi[pizzas_s - 1]) + ":"
            else:
                pizzatext[pizzas_s - 1] = pizzas[pizzas_s - 1] + ":"
            pizza[pizzas_s - 1] = "{}" .format (pizzatext[pizzas_s - 1])
            price[pizzas_s - 1] = GOURMET_PRICE * int(multi[pizzas_s - 1])
            pricetext[pizzas_s - 1] = str(price[pizzas_s - 1])
            total_price = total_price + price[pizzas_s - 1]
    if delivery_ == 1:
        total_price = total_price + DELIVERY_CHARGE
 
    if delivery_ == 0:
        totalprice_msg = "Total Cost:"
    else:
        totalprice_msg = "Pizzas Cost:"
 
    if pizzas_s == 1:
        pizza1 = Label(thirdmenu, text= "{}" .format (pizzatext[0]), bg = "#6fa8dc", font=("candara 10 roman"))
        pizza1.place(x=140, y=(yplace+70), anchor="e")
        price1 = Label(thirdmenu, text= "{}" .format (pricetext[0]), bg = "#6fa8dc", font=("candara 10 roman"))
        price1.place(x=140, y=(yplace+70), anchor="w")

        if delivery_ == 0:
            total_price_msg = Label(thirdmenu, text= "{}" .format (totalprice_msg), bg = "#6fa8dc", font=("candara 10 roman"))
            total_price_msg.place(x=140, y=(yplace+90), anchor="e")
            total_price_ = Label(thirdmenu, text= "{}" .format (total_price), bg = "#6fa8dc", font=("candara 10 roman"))
            total_price_.place(x=140, y=(yplace+90), anchor="w")
            c_instruct_msg = c_instruct.get()
            c_instruct_msg = re.sub("(.{25})", "\\1\n", c_instruct_msg, 0, re.DOTALL)
            customer_msg = Label(thirdmenu, text= "{}" . format (c_instruct_msg), bg = "#6fa8dc", font=("candara 10 roman"))
            customer_msg.place(x=122, y=(yplace+110), anchor="n")
            aao = Button(thirdmenu, text="""Accept Another
            Order""", bg = "#cc4125", font=("candara 10 roman"), command=lambda: cancel_order())
            aao.place(x=15, y=(yplace+170), width=105, height=37)
            exit_ = Button(thirdmenu, text="Exit", bg = "#cc4125", font=("candara 10 roman"), command=lambda: quit())
            exit_.place(x=230, y=(yplace+170), width=105, height=37, anchor = "ne")
            thirdmenu.geometry("245x222")

        else:
            pizzas_price_msg = Label(thirdmenu, text= "{}" .format (totalprice_msg), bg = "#6fa8dc", font=("candara 10 roman"))
            pizzas_price_msg.place(x=140, y=(yplace+90), anchor="e")
            pizzasprice = total_price-3
            pizzas_price_ = Label(thirdmenu, text= "{}" .format (pizzasprice), bg = "#6fa8dc", font=("candara 10 roman"))
            pizzas_price_.place(x=140, y=(yplace+90), anchor="w")
            delivery_price = Label(thirdmenu, text= "+ $3 Delivery cost =", bg = "#6fa8dc", font=("candara 10 roman"))
            delivery_price.place(x=122, y=(yplace+110), anchor="center")
            total_price_msg = Label(thirdmenu, text= "Total Cost:", bg = "#6fa8dc", font=("candara 10 roman"))
            total_price_msg.place(x=140, y=(yplace+130), anchor="e")
            total_price_ = Label(thirdmenu, text= "{}" .format (total_price), bg = "#6fa8dc", font=("candara 10 roman"))
            total_price_.place(x=140, y=(yplace+130), anchor="w")
            c_instruct_msg = c_instruct.get()
            c_instruct_msg = re.sub("(.{25})", "\\1\n", c_instruct_msg, 0, re.DOTALL)
            customer_msg = Label(thirdmenu, text= "{}" . format (c_instruct_msg), bg = "#6fa8dc", font=("candara 10 roman"))
            customer_msg.place(x=122, y=(yplace+150), anchor="n")
            d_instruct_msg = d_instruct.get()
            d_instruct_msg = re.sub("(.{25})", "\\1\n", d_instruct_msg, 0, re.DOTALL)
            delivery_msg = Label(thirdmenu, text= "{}" . format (d_instruct_msg), bg = "#6fa8dc", font=("candara 10 roman"))
            delivery_msg.place(x=122, y=(yplace+210), anchor="n")
            aao = Button(thirdmenu, text="""Accept Another
            Order""", bg = "#cc4125", font=("candara 10 roman"), command=lambda: cancel_order())
            aao.place(x=15, y=(yplace+270), width=105, height=37)
            exit_ = Button(thirdmenu, text="Exit", bg = "#cc4125", font=("candara 10 roman"), command=lambda: quit())
            exit_.place(x=230, y=(yplace+270), width=105, height=37, anchor = "ne")
            thirdmenu.geometry("245x362")

    if pizzas_s == 2:
        pizza1 = Label(thirdmenu, text= "{}" .format (pizzatext[0]), bg = "#6fa8dc", font=("candara 10 roman"))
        pizza1.place(x=140, y=(yplace+70), anchor="e")
        price1 = Label(thirdmenu, text= "{}" .format (pricetext[0]), bg = "#6fa8dc", font=("candara 10 roman"))
        price1.place(x=140, y=(yplace+70), anchor="w")
        pizza2 = Label(thirdmenu, text= "{}" .format (pizzatext[1]), bg = "#6fa8dc", font=("candara 10 roman"))
        pizza2.place(x=140, y=(yplace+90), anchor="e")
        price2 = Label(thirdmenu, text= "{}" .format (pricetext[1]), bg = "#6fa8dc", font=("candara 10 roman"))
        price2.place(x=140, y=(yplace+90), anchor="w")

        if delivery_ == 0:
            total_price_msg = Label(thirdmenu, text= "{}" .format (totalprice_msg), bg = "#6fa8dc", font=("candara 10 roman"))
            total_price_msg.place(x=140, y=(yplace+110), anchor="e")
            total_price_ = Label(thirdmenu, text= "{}" .format (total_price), bg = "#6fa8dc", font=("candara 10 roman"))
            total_price_.place(x=140, y=(yplace+110), anchor="w")
            c_instruct_msg = c_instruct.get()
            c_instruct_msg = re.sub("(.{25})", "\\1\n", c_instruct_msg, 0, re.DOTALL)
            customer_msg = Label(thirdmenu, text= "{}" . format (c_instruct_msg), bg = "#6fa8dc", font=("candara 10 roman"))
            customer_msg.place(x=122, y=(yplace+130), anchor="n")
            aao = Button(thirdmenu, text="""Accept Another
            Order""", bg = "#cc4125", font=("candara 10 roman"), command=lambda: cancel_order())
            aao.place(x=15, y=(yplace+190), width=105, height=37)
            exit_ = Button(thirdmenu, text="Exit", bg = "#cc4125", font=("candara 10 roman"), command=lambda: quit())
            exit_.place(x=230, y=(yplace+190), width=105, height=37, anchor = "ne")
            thirdmenu.geometry("245x242")

        else:
            pizzas_price_msg = Label(thirdmenu, text= "{}" .format (totalprice_msg), bg = "#6fa8dc", font=("candara 10 roman"))
            pizzas_price_msg.place(x=140, y=(yplace+110), anchor="e")
            pizzasprice = total_price-3
            pizzas_price_ = Label(thirdmenu, text= "{}" .format (pizzasprice), bg = "#6fa8dc", font=("candara 10 roman"))
            pizzas_price_.place(x=140, y=(yplace+110), anchor="w")
            delivery_price = Label(thirdmenu, text= "+ $3 Delivery cost =", bg = "#6fa8dc", font=("candara 10 roman"))
            delivery_price.place(x=122, y=(yplace+130), anchor="center")
            total_price_msg = Label(thirdmenu, text= "Total Cost:", bg = "#6fa8dc", font=("candara 10 roman"))
            total_price_msg.place(x=140, y=(yplace+150), anchor="e")
            total_price_ = Label(thirdmenu, text= "{}" .format (total_price), bg = "#6fa8dc", font=("candara 10 roman"))
            total_price_.place(x=140, y=(yplace+150), anchor="w")
            c_instruct_msg = c_instruct.get()
            c_instruct_msg = re.sub("(.{25})", "\\1\n", c_instruct_msg, 0, re.DOTALL)
            customer_msg = Label(thirdmenu, text= "{}" . format (c_instruct_msg), bg = "#6fa8dc", font=("candara 10 roman"))
            customer_msg.place(x=122, y=(yplace+170), anchor="n")
            d_instruct_msg = d_instruct.get()
            d_instruct_msg = re.sub("(.{25})", "\\1\n", d_instruct_msg, 0, re.DOTALL)
            delivery_msg = Label(thirdmenu, text= "{}" . format (d_instruct_msg), bg = "#6fa8dc", font=("candara 10 roman"))
            delivery_msg.place(x=122, y=(yplace+230), anchor="n")
            aao = Button(thirdmenu, text="""Accept Another
            Order""", bg = "#cc4125", font=("candara 10 roman"), command=lambda: cancel_order())
            aao.place(x=15, y=(yplace+290), width=105, height=37)
            exit_ = Button(thirdmenu, text="Exit", bg = "#cc4125", font=("candara 10 roman"), command=lambda: quit())
            exit_.place(x=230, y=(yplace+290), width=105, height=37, anchor = "ne")
            thirdmenu.geometry("245x342")

    if pizzas_s == 3:
        pizza1 = Label(thirdmenu, text= "{}" .format (pizzatext[0]), bg = "#6fa8dc", font=("candara 10 roman"))
        pizza1.place(x=140, y=(yplace+70), anchor="e")
        price1 = Label(thirdmenu, text= "{}" .format (pricetext[0]), bg = "#6fa8dc", font=("candara 10 roman"))
        price1.place(x=140, y=(yplace+70), anchor="w")
        pizza2 = Label(thirdmenu, text= "{}" .format (pizzatext[1]), bg = "#6fa8dc", font=("candara 10 roman"))
        pizza2.place(x=140, y=(yplace+90), anchor="e")
        price2 = Label(thirdmenu, text= "{}" .format (pricetext[1]), bg = "#6fa8dc", font=("candara 10 roman"))
        price2.place(x=140, y=(yplace+90), anchor="w")
        pizza3 = Label(thirdmenu, text= "{}" .format (pizzatext[2]), bg = "#6fa8dc", font=("candara 10 roman"))
        pizza3.place(x=140, y=(yplace+110), anchor="e")
        price3 = Label(thirdmenu, text= "{}" .format (pricetext[2]), bg = "#6fa8dc", font=("candara 10 roman"))
        price3.place(x=140, y=(yplace+110), anchor="w")

        if delivery_ == 0:
            total_price_msg = Label(thirdmenu, text= "{}" .format (totalprice_msg), bg = "#6fa8dc", font=("candara 10 roman"))
            total_price_msg.place(x=140, y=(yplace+130), anchor="e")
            total_price_ = Label(thirdmenu, text= "{}" .format (total_price), bg = "#6fa8dc", font=("candara 10 roman"))
            total_price_.place(x=140, y=(yplace+130), anchor="w")
            c_instruct_msg = c_instruct.get()
            c_instruct_msg = re.sub("(.{25})", "\\1\n", c_instruct_msg, 0, re.DOTALL)
            customer_msg = Label(thirdmenu, text= "{}" . format (c_instruct_msg), bg = "#6fa8dc", font=("candara 10 roman"))
            customer_msg.place(x=122, y=(yplace+150), anchor="n")
            aao = Button(thirdmenu, text="""Accept Another
            Order""", bg = "#cc4125", font=("candara 10 roman"), command=lambda: cancel_order())
            aao.place(x=15, y=(yplace+210), width=105, height=37)
            exit_ = Button(thirdmenu, text="Exit", bg = "#cc4125", font=("candara 10 roman"), command=lambda: quit())
            exit_.place(x=230, y=(yplace+210), width=105, height=37, anchor = "ne")
            thirdmenu.geometry("245x262")
            
        else:
            pizzas_price_msg = Label(thirdmenu, text= "{}" .format (totalprice_msg), bg = "#6fa8dc", font=("candara 10 roman"))
            pizzas_price_msg.place(x=140, y=(yplace+130), anchor="e")
            pizzasprice = total_price-3
            pizzas_price_ = Label(thirdmenu, text= "{}" .format (pizzasprice), bg = "#6fa8dc", font=("candara 10 roman"))
            pizzas_price_.place(x=140, y=(yplace+130), anchor="w")
            delivery_price = Label(thirdmenu, text= "+ $3 Delivery cost =", bg = "#6fa8dc", font=("candara 10 roman"))
            delivery_price.place(x=122, y=(yplace+150), anchor="center")
            total_price_msg = Label(thirdmenu, text= "Total Cost:", bg = "#6fa8dc", font=("candara 10 roman"))
            total_price_msg.place(x=140, y=(yplace+170), anchor="e")
            total_price_ = Label(thirdmenu, text= "{}" .format (total_price), bg = "#6fa8dc", font=("candara 10 roman"))
            total_price_.place(x=140, y=(yplace+170), anchor="w")
            c_instruct_msg = c_instruct.get()
            c_instruct_msg = re.sub("(.{25})", "\\1\n", c_instruct_msg, 0, re.DOTALL)
            customer_msg = Label(thirdmenu, text= "{}" . format (c_instruct_msg), bg = "#6fa8dc", font=("candara 10 roman"))
            customer_msg.place(x=122, y=(yplace+190), anchor="n")
            d_instruct_msg = d_instruct.get()
            d_instruct_msg = re.sub("(.{25})", "\\1\n", d_instruct_msg, 0, re.DOTALL)
            delivery_msg = Label(thirdmenu, text= "{}" . format (d_instruct_msg), bg = "#6fa8dc", font=("candara 10 roman"))
            delivery_msg.place(x=122, y=(yplace+250), anchor="n")
            aao = Button(thirdmenu, text="""Accept Another
            Order""", bg = "#cc4125", font=("candara 10 roman"), command=lambda: cancel_order())
            aao.place(x=15, y=(yplace+310), width=105, height=37)
            exit_ = Button(thirdmenu, text="Exit", bg = "#cc4125", font=("candara 10 roman"), command=lambda: quit())
            exit_.place(x=230, y=(yplace+310), width=105, height=37, anchor = "ne")
            thirdmenu.geometry("245x402")

    if pizzas_s == 4:
        pizza1 = Label(thirdmenu, text= "{}" .format (pizzatext[0]), bg = "#6fa8dc", font=("candara 10 roman"))
        pizza1.place(x=140, y=(yplace+70), anchor="e")
        price1 = Label(thirdmenu, text= "{}" .format (pricetext[0]), bg = "#6fa8dc", font=("candara 10 roman"))
        price1.place(x=140, y=(yplace+70), anchor="w")
        pizza2 = Label(thirdmenu, text= "{}" .format (pizzatext[1]), bg = "#6fa8dc", font=("candara 10 roman"))
        pizza2.place(x=140, y=(yplace+90), anchor="e")
        price2 = Label(thirdmenu, text= "{}" .format (pricetext[1]), bg = "#6fa8dc", font=("candara 10 roman"))
        price2.place(x=140, y=(yplace+90), anchor="w")
        pizza3 = Label(thirdmenu, text= "{}" .format (pizzatext[2]), bg = "#6fa8dc", font=("candara 10 roman"))
        pizza3.place(x=140, y=(yplace+110), anchor="e")
        price3 = Label(thirdmenu, text= "{}" .format (pricetext[2]), bg = "#6fa8dc", font=("candara 10 roman"))
        price3.place(x=140, y=(yplace+110), anchor="w")
        pizza4 = Label(thirdmenu, text= "{}" .format (pizzatext[3]), bg = "#6fa8dc", font=("candara 10 roman"))
        pizza4.place(x=140, y=(yplace+130), anchor="e")
        price4 = Label(thirdmenu, text= "{}" .format (pricetext[3]), bg = "#6fa8dc", font=("candara 10 roman"))
        price4.place(x=140, y=(yplace+130), anchor="w")
        
        if delivery_ == 0:
            total_price_msg = Label(thirdmenu, text= "{}" .format (totalprice_msg), bg = "#6fa8dc", font=("candara 10 roman"))
            total_price_msg.place(x=140, y=(yplace+150), anchor="e")
            total_price_ = Label(thirdmenu, text= "{}" .format (total_price), bg = "#6fa8dc", font=("candara 10 roman"))
            total_price_.place(x=140, y=(yplace+150), anchor="w")
            c_instruct_msg = c_instruct.get()
            c_instruct_msg = re.sub("(.{25})", "\\1\n", c_instruct_msg, 0, re.DOTALL)
            customer_msg = Label(thirdmenu, text= "{}" . format (c_instruct_msg), bg = "#6fa8dc", font=("candara 10 roman"))
            customer_msg.place(x=122, y=(yplace+170), anchor="n")
            aao = Button(thirdmenu, text="""Accept Another
            Order""", bg = "#cc4125", font=("candara 10 roman"), command=lambda: cancel_order())
            aao.place(x=15, y=(yplace+250), width=105, height=37)
            exit_ = Button(thirdmenu, text="Exit", bg = "#cc4125", font=("candara 10 roman"), command=lambda: quit())
            exit_.place(x=230, y=(yplace+250), width=105, height=37, anchor = "ne")
            thirdmenu.geometry("245x302")

        else:
            pizzas_price_msg = Label(thirdmenu, text= "{}" .format (totalprice_msg), bg = "#6fa8dc", font=("candara 10 roman"))
            pizzas_price_msg.place(x=140, y=(yplace+150), anchor="e")
            pizzasprice = total_price-3
            pizzas_price_ = Label(thirdmenu, text= "{}" .format (pizzasprice), bg = "#6fa8dc", font=("candara 10 roman"))
            pizzas_price_.place(x=140, y=(yplace+150), anchor="w")
            delivery_price = Label(thirdmenu, text= "+ $3 Delivery cost =", bg = "#6fa8dc", font=("candara 10 roman"))
            delivery_price.place(x=122, y=(yplace+170), anchor="center")
            total_price_msg = Label(thirdmenu, text= "Total Cost:", bg = "#6fa8dc", font=("candara 10 roman"))
            total_price_msg.place(x=140, y=(yplace+190), anchor="e")
            total_price_ = Label(thirdmenu, text= "{}" .format (total_price), bg = "#6fa8dc", font=("candara 10 roman"))
            total_price_.place(x=140, y=(yplace+190), anchor="w")
            c_instruct_msg = c_instruct.get()
            c_instruct_msg = re.sub("(.{25})", "\\1\n", c_instruct_msg, 0, re.DOTALL)
            customer_msg = Label(thirdmenu, text= "{}" . format (c_instruct_msg), bg = "#6fa8dc", font=("candara 10 roman"))
            customer_msg.place(x=122, y=(yplace+210), anchor="n")
            d_instruct_msg = d_instruct.get()
            d_instruct_msg = re.sub("(.{25})", "\\1\n", d_instruct_msg, 0, re.DOTALL)
            delivery_msg = Label(thirdmenu, text= "{}" . format (d_instruct_msg), bg = "#6fa8dc", font=("candara 10 roman"))
            delivery_msg.place(x=122, y=(yplace+270), anchor="n")
            aao = Button(thirdmenu, text="""Accept Another
            Order""", bg = "#cc4125", font=("candara 10 roman"), command=lambda: cancel_order())
            aao.place(x=15, y=(yplace+330), width=105, height=37)
            exit_ = Button(thirdmenu, text="Exit", bg = "#cc4125", font=("candara 10 roman"), command=lambda: quit())
            exit_.place(x=230, y=(yplace+330), width=105, height=37, anchor = "ne")
            thirdmenu.geometry("245x422")
            
    if pizzas_s == 5:
        pizza1 = Label(thirdmenu, text= "{}" .format (pizzatext[0]), bg = "#6fa8dc", font=("candara 10 roman"))
        pizza1.place(x=140, y=(yplace+70), anchor="e")
        price1 = Label(thirdmenu, text= "{}" .format (pricetext[0]), bg = "#6fa8dc", font=("candara 10 roman"))
        price1.place(x=140, y=(yplace+70), anchor="w")
        pizza2 = Label(thirdmenu, text= "{}" .format (pizzatext[1]), bg = "#6fa8dc", font=("candara 10 roman"))
        pizza2.place(x=140, y=(yplace+90), anchor="e")
        price2 = Label(thirdmenu, text= "{}" .format (pricetext[1]), bg = "#6fa8dc", font=("candara 10 roman"))
        price2.place(x=140, y=(yplace+90), anchor="w")
        pizza3 = Label(thirdmenu, text= "{}" .format (pizzatext[2]), bg = "#6fa8dc", font=("candara 10 roman"))
        pizza3.place(x=140, y=(yplace+110), anchor="e")
        price3 = Label(thirdmenu, text= "{}" .format (pricetext[2]), bg = "#6fa8dc", font=("candara 10 roman"))
        price3.place(x=140, y=(yplace+110), anchor="w")
        pizza4 = Label(thirdmenu, text= "{}" .format (pizzatext[3]), bg = "#6fa8dc", font=("candara 10 roman"))
        pizza4.place(x=140, y=(yplace+130), anchor="e")
        price4 = Label(thirdmenu, text= "{}" .format (pricetext[3]), bg = "#6fa8dc", font=("candara 10 roman"))
        price4.place(x=140, y=(yplace+130), anchor="w")
        pizza5 = Label(thirdmenu, text= "{}" .format (pizzatext[4]), bg = "#6fa8dc", font=("candara 10 roman"))
        pizza5.place(x=140, y=(yplace+150), anchor="e")
        price5 = Label(thirdmenu, text= "{}" .format (pricetext[4]), bg = "#6fa8dc", font=("candara 10 roman"))
        price5.place(x=140, y=(yplace+150), anchor="w")

        if delivery_ == 0:
            total_price_msg = Label(thirdmenu, text= "{}" .format (totalprice_msg), bg = "#6fa8dc", font=("candara 10 roman"))
            total_price_msg.place(x=140, y=(yplace+170), anchor="e")
            total_price_ = Label(thirdmenu, text= "{}" .format (total_price), bg = "#6fa8dc", font=("candara 10 roman"))
            total_price_.place(x=140, y=(yplace+170), anchor="w")
            c_instruct_msg = c_instruct.get()
            c_instruct_msg = re.sub("(.{25})", "\\1\n", c_instruct_msg, 0, re.DOTALL)
            customer_msg = Label(thirdmenu, text= "{}" . format (c_instruct_msg), bg = "#6fa8dc", font=("candara 10 roman"))
            customer_msg.place(x=122, y=(yplace+190), anchor="n")
            aao = Button(thirdmenu, text="""Accept Another
            Order""", bg = "#cc4125", font=("candara 10 roman"), command=lambda: cancel_order())
            aao.place(x=15, y=(yplace+250), width=105, height=37)
            exit_ = Button(thirdmenu, text="Exit", bg = "#cc4125", font=("candara 10 roman"), command=lambda: quit())
            exit_.place(x=230, y=(yplace+250), width=105, height=37, anchor = "ne")
            exit_ = Button(thirdmenu, text="Exit", bg = "#cc4125", font=("candara 10 roman"), command=lambda: quit())
            exit_.place(x=230, y=(yplace+250), width=105, height=37, anchor = "ne")
            thirdmenu.geometry("245x302")

        else:
            pizzas_price_msg = Label(thirdmenu, text= "{}" .format (totalprice_msg), bg = "#6fa8dc", font=("candara 10 roman"))
            pizzas_price_msg.place(x=140, y=(yplace+170), anchor="e")
            pizzasprice = total_price-3
            pizzas_price_ = Label(thirdmenu, text= "{}" .format (pizzasprice), bg = "#6fa8dc", font=("candara 10 roman"))
            pizzas_price_.place(x=140, y=(yplace+170), anchor="w")
            delivery_price = Label(thirdmenu, text= "+ $3 Delivery cost =", bg = "#6fa8dc", font=("candara 10 roman"))
            delivery_price.place(x=122, y=(yplace+190), anchor="center")
            total_price_msg = Label(thirdmenu, text= "Total Cost:", bg = "#6fa8dc", font=("candara 10 roman"))
            total_price_msg.place(x=140, y=(yplace+210), anchor="e")
            total_price_ = Label(thirdmenu, text= "{}" .format (total_price), bg = "#6fa8dc", font=("candara 10 roman"))
            total_price_.place(x=140, y=(yplace+210), anchor="w")
            c_instruct_msg = c_instruct.get()
            c_instruct_msg = re.sub("(.{25})", "\\1\n", c_instruct_msg, 0, re.DOTALL)
            customer_msg = Label(thirdmenu, text= "{}" . format (c_instruct_msg), bg = "#6fa8dc", font=("candara 10 roman"))
            customer_msg.place(x=122, y=(yplace+230), anchor="n")
            d_instruct_msg = d_instruct.get()
            d_instruct_msg = re.sub("(.{25})", "\\1\n", d_instruct_msg, 0, re.DOTALL)
            delivery_msg = Label(thirdmenu, text= "{}" . format (d_instruct_msg), bg = "#6fa8dc", font=("candara 10 roman"))
            delivery_msg.place(x=0, y=(yplace+290), anchor="nw")
            aao = Button(thirdmenu, text="""Accept Another
            Order""", bg = "#cc4125", font=("candara 10 roman"), command=lambda: cancel_order())
            aao.place(x=15, y=(yplace+350), width=105, height=37)
            exit_ = Button(thirdmenu, text="Exit", bg = "#cc4125", font=("candara 10 roman"), command=lambda: quit())
            exit_.place(x=230, y=(yplace+350), width=105, height=37, anchor = "ne")
            thirdmenu.geometry("245x442")  

def quit():
    root.destroy()
 
def cancel_order():
    global lastselected
    global total_price
    global pizza_p
    global pizza_numb
    global lcv
    global lcv2
    global pizzas_numb
    global pizzas_numbtotal
    global pizzas_s
    global multi
    global o_display_text
    lastselected = ""
    total_price = 0
    pizza_p = 0
    pizza_numb = 1
    lcv = 0
    lcv2 = 0
    pizzas_numb = [0]*12
    pizzas_numbtotal = [0]*12
    pizzas_s = 0
    multi = [0]*5
    o_display_text = ""
    if menus == 1:
        firstmenu.destroy()
    elif menus == 2:
        firstmenu.destroy()
        secondmenu.destroy()
    else:
        firstmenu.destroy()
        secondmenu.destroy()
        thirdmenu.destroy()
   
 
#photo = PhotoImage(file="E:/testlogo.png")
#labelphoto = Label(root, image=photo, width=30, height=16)
#labelphoto.place(x=300, y=10, anchor="ne")

title_msg = Label(root, text="Tony's Pizza Company", bg = "#6fa8dc", font=("candara 13 roman"))
title_msg.place(x=78, y=0)
 
pickup = Button(root, text="Pickup", bg = "#cc4125", font=("candara 10 roman"), command=lambda: pickup2())
pickup.place(x=15, y=40, width=125, height=37)
 
delivery = Button(root, text="Delivery", bg = "#cc4125", font=("candara 10 roman"), command=lambda: delivery2())
delivery.place(x=165, y=40, width=125, height=37)
 
root.mainloop()