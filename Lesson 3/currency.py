from tkinter import *
from tkinter import ttk
from tkinter import messagebox

screen = Tk()
screen.title("💰Currency exchange💰")
screen.geometry("600x600")
conversion_rate = {

# USD
"USD:EUR":0.87,
"USD:JPY":147.2,
"USD:GBP":0.75,
"USD:CNY":7.18,
"USD:AUD":1.53,
"USD:CAD":1.35,
"USD:INR":83.1,

# EUR
"EUR:USD":1.15,
"EUR:JPY":169.2,
"EUR:GBP":0.86,
"EUR:CNY":8.25,
"EUR:AUD":1.76,
"EUR:CAD":1.55,
"EUR:INR":95.5,

# JPY
"JPY:USD":0.0068,
"JPY:EUR":0.0059,
"JPY:GBP":0.0051,
"JPY:CNY":0.048,
"JPY:AUD":0.0104,
"JPY:CAD":0.0092,
"JPY:INR":0.56,

# GBP
"GBP:USD":1.33,
"GBP:EUR":1.16,
"GBP:JPY":196.5,
"GBP:CNY":9.59,
"GBP:AUD":2.05,
"GBP:CAD":1.80,
"GBP:INR":110.7,

# CNY
"CNY:USD":0.14,
"CNY:EUR":0.12,
"CNY:JPY":20.5,
"CNY:GBP":0.10,
"CNY:AUD":0.21,
"CNY:CAD":0.19,
"CNY:INR":11.6,

# AUD
"AUD:USD":0.65,
"AUD:EUR":0.57,
"AUD:JPY":94.0,
"AUD:GBP":0.49,
"AUD:CNY":4.68,
"AUD:CAD":0.88,
"AUD:INR":54.3,

# CAD
"CAD:USD":0.74,
"CAD:EUR":0.65,
"CAD:JPY":108.6,
"CAD:GBP":0.56,
"CAD:CNY":5.33,
"CAD:AUD":1.14,
"CAD:INR":61.4,

# INR
"INR:USD":0.012,
"INR:EUR":0.010,
"INR:JPY":1.78,
"INR:GBP":0.0090,
"INR:CNY":0.086,
"INR:AUD":0.018,
"INR:CAD":0.016
}

screen.config(background="white")

def Clear(event = None):
    if event.keysym == "BackSpace":
        ihaveentry.delete(0,END)
        return
    else:
        Conversionbind()

def Swap():
    fr = fromcurrency.get()
    to = tocurrency.get()
    fromcurrency.set(to)
    tocurrency.set(fr)
    Conversionbind()

def Conversionbind(event = None):
    try:
        if ihaveentry.get().isdigit():
            ihaveentry_value = float(ihaveentry.get())
        fr = fromcurrency.get()
        to = tocurrency.get()
        if fr == to:
            end_currency.set(ihaveentry_value)
        else:
            frto = f"{fr}:{to}"
            if frto in conversion_rate:
                rate = conversion_rate[frto]
                ending = ihaveentry_value * rate
            end_currency.set(f"{ending:.2f}")
    except:
        messagebox.showerror("Error with text", "Only Use Numbers")

title = Label(screen, text="Money Converter", fg="black", font=("verdana", 35, "bold"))
title2 = Label(screen, text="Type in an amount and see what its worth", fg="black", font=("verdana", 12, "bold"))

ihaveframe = Frame(screen, bg= "yellow", highlightthickness= 1, highlightbackground = "yellow")
ihavetext = Label(ihaveframe, text="I have...", bg="yellow", fg="black", font=("verdana", 12, "bold"))
ihaveentry = Entry(ihaveframe, font=("verdana", 30, "bold"))
names = ["USD", "GBP", "INR", "EUR", "JPY", "CNY", "AUD", "CAD"]
fromcurrency = StringVar(value=names[1])
ihavedropdownofcurrencies = ttk.Combobox(ihaveframe, font=("verdana", 20, "bold" ), textvariable= fromcurrency, values= names, state="readonly")
title.pack(pady= 10)
title2.pack(pady= 10)
ihaveframe.place(x= 50, y= 150, width=500, height=200)
ihavetext.pack(padx= 10, pady= 10, anchor="w")
ihaveentry.pack(padx= 10, pady= 10)
ihaveentry.bind("<KeyRelease>", Clear)
ihaveentry.bind("<BackSpace>", Clear)
ihavedropdownofcurrencies.pack(padx= 10, pady= 10)
ihavedropdownofcurrencies.bind("<<ComboboxSelected>>", Conversionbind)
labelshowingdown = Button(screen, text="⇈⇊", fg="black", font=("verdana", 10, "bold"), command= Swap)
labelshowingdown.place(x=300, y=360)#

end_currency = StringVar(value="0")
urecieveframe = Frame(screen, bg= "ivory2", highlightthickness= 1, highlightbackground = "ivory2")
urecievetext = Label(urecieveframe, text="You Recieve...", bg="ivory2", fg="black", font=("verdana", 12, "bold"))
urecieveentry = Label(urecieveframe, textvariable=f"{end_currency}", font=("verdana", 30, "bold"))
tocurrency = StringVar(value=names[0])
urecievedropdownofcurrencies = ttk.Combobox(urecieveframe, font=("verdana", 20, "bold" ), textvariable= tocurrency, values= names, state="readonly")
urecievedropdownofcurrencies.bind("<<ComboboxSelected>>", Conversionbind)
urecieveframe.place(x= 50, y= 400, width=500, height=200)
urecievetext.pack(padx= 10, pady= 10, anchor="w")
urecieveentry.pack(padx= 10, pady= 10)
urecievedropdownofcurrencies.pack(padx= 10, pady= 10)



screen.mainloop()