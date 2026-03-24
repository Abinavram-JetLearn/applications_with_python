from tkinter import *

screen = Tk()
screen.title("Pizza App")
screen.geometry("800x600")
screen.state("zoomed")

BGCol = "#09122b"
TITLECol ="#072347"
HEADINGCol = "#849cdf"
PARACol = "#50649a"
CARDCol = "#273048"

pizzas = [
    {"name": "Margherita", "price": 8.99, "desc": "Tomato, mozzarella, basil"},
    {"name": "Supreme Pizza", "price": 10.99, "desc": "Tomato, mozzarella, basil, spicy chicken, jalapeños"},
    {"name": "Pepperoni Feast", "price": 9.99, "desc": "Tomato, mozzarella, pepperoni"},
    {"name": "BBQ Chicken", "price": 11.49, "desc": "BBQ sauce, mozzarella, grilled chicken, red onions"},
    {"name": "Veggie Delight", "price": 9.49, "desc": "Tomato, mozzarella, peppers, onions, mushrooms, olives"},
    {"name": "Hawaiian", "price": 10.49, "desc": "Tomato, mozzarella, ham, pineapple"}
]
SIZES = {
    "Small (8\")":   0.00,
    "Medium (10\")": 2.00,
    "Large (12\")":  4.00,
    "XL (14\")":     6.00,
}

CRUSTS = {
    "Thin":    0.00,
    "Classic": 0.00,
    "Thick":   1.50,
    "Stuffed": 2.50,
    "Mega Stuffed": 5.50,
}

EXTRAS = {
    "Extra Cheese":     1.50,
    "Jalapenos":        0.75,
    "Mushrooms":        1.00,
    "Olives":           0.75,
    "Sun-dried Tomato": 1.25,
    "Fresh Basil":      0.50,
}

screen.config(background= BGCol)
title = Label(screen, text="Super Pizza | Not Authentic Italien food", bg=TITLECol, fg=HEADINGCol, font=("calabri", 25, "bold"))
chooseyourpizzaframe = Frame(screen, bg= CARDCol, highlightthickness= 1, highlightbackground = PARACol, borderwidth= 15)
chooseyourpizza = Label(chooseyourpizzaframe, text = "Choose your Pizza!", bg=TITLECol, fg=HEADINGCol, font=("calabri", 12))

title.pack(padx= 20)
chooseyourpizza.pack(padx= 20, pady= 30, anchor="w")
chooseyourpizzaframe.place(x= 20, y= 200, width= 200, height=50)
screen.mainloop()