from tkinter import *
from tkinter import ttk

screen = Tk()
screen.title("💰Currency exchange💰")
screen.geometry("600x600")
conversion_rate = {

# USD
"USD:INR":83.1,
"USD:GBP":0.75,

# INR
"INR:USD":0.012,
"INR:GBP":0.0090,

# GBP
"GBP:USD":1.33,
"GBP:INR":110.7

}
screen.config(background="white")
title = Label(screen, text="Money Converter", fg="black", font=("verdana", 35, "bold"))
title2 = Label(screen, text="Type in an amount and see what its worth", fg="black", font=("verdana", 12, "bold"))

ihaveframe = Frame(screen, bg= "yellow", highlightthickness= 1, highlightbackground = "yellow")
ihavetext = Label(ihaveframe, text="I have...", bg="yellow", fg="black", font=("verdana", 12, "bold"))
ihaveentry = Entry(ihaveframe, font=("verdana", 30, "bold"))
names = ["USD", "GBP", "INR"]
fromcurrency = StringVar(value=names[1])
ihavedropdownofcurrencies = ttk.Combobox(ihaveframe, font=("verdana", 20, "bold" ), textvariable= fromcurrency, values= names, state="readonly")
title.pack(pady= 10)
title2.pack(pady= 10)
ihaveframe.place(x= 50, y= 150, width=500, height=200)
ihavetext.pack(padx= 10, pady= 10, anchor="w")
ihaveentry.pack(padx= 10, pady= 10)
ihavedropdownofcurrencies.pack(padx= 10, pady= 10)
labelshowingdown = Label(screen, text="⇊", fg="black", font=("verdana", 20, "bold"))
labelshowingdown.place(x=300, y=360)#

end_currency = StringVar(value="0")
urecieveframe = Frame(screen, bg= "ivory2", highlightthickness= 1, highlightbackground = "ivory2")
urecievetext = Label(urecieveframe, text="You Recieve...", bg="ivory2", fg="black", font=("verdana", 12, "bold"))
urecieveentry = Label(urecieveframe, textvariable=f"{end_currency}", font=("verdana", 30, "bold"))
tocurrency = StringVar(value=names[0])
urecievedropdownofcurrencies = ttk.Combobox(urecieveframe, font=("verdana", 20, "bold" ), textvariable= tocurrency, values= names, state="readonly")
urecieveframe.place(x= 50, y= 400, width=500, height=200)
urecievetext.pack(padx= 10, pady= 10, anchor="w")
urecieveentry.pack(padx= 10, pady= 10)
urecievedropdownofcurrencies.pack(padx= 10, pady= 10)
screen.mainloop()