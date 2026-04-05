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
EXTRAS_NUM = {
    "Extra Cheese":     IntVar(),
    "Jalapenos":        IntVar(),
    "Mushrooms":        IntVar(),
    "Olives":           IntVar(),
    "Sun-dried Tomato": IntVar(),
    "Fresh Basil":      IntVar(),
}

pizza = StringVar(value = "Margerita")
size_pizza = StringVar(value = "Medium")
crust = StringVar(value = "Classic")
pizzas_qua = IntVar(value = 1)

screen.config(background= BGCol)
title = Label(screen, text="Super Pizza | Not Authentic Italien food", bg=TITLECol, fg=HEADINGCol, font=("calabri", 25, "bold"))
chooseyourpizzaframe = Frame(screen, bg= CARDCol, highlightthickness= 1, highlightbackground = PARACol, borderwidth= 15)
chooseyourpizza = Label(screen, text = "Choose your Pizza!", bg=TITLECol, fg=HEADINGCol, font=("calabri", 12))
title.pack(padx= 20)
chooseyourpizza.pack(padx= 20, pady= 15, anchor="w")

for i, p in enumerate(pizzas):
    Radiobutton(chooseyourpizzaframe, text= f"{p["name"]} | Cost: ${p['price']}", variable= pizza, value = p["price"], bg= BGCol, fg=HEADINGCol,  font=("calabri", 12, "bold"), justify = "left").grid(row= i//3, column =i%3, padx = 5, pady = 10)

chooseyourpizzaframe.pack(anchor= "w")

left_frame = Frame(screen, bg= BGCol)
left_frame.pack(side="left", fill="both", expand= True, padx= 20, pady= 10)
left_frame_canvas = Canvas(left_frame, bg= BGCol)
left_frame_canvas.pack(side="left", fill="both", expand= True, padx= 20, pady= 10)
left_frame_scrollbar = Scrollbar(left_frame, orient="vertical")
left_frame_scrollbar.pack(side= "right", fill= Y)
left_frame_canvas.config(yscrollcommand=left_frame_scrollbar.set)

right_frame = Frame(screen, bg= BGCol)
right_frame.pack(side="right", fill="both", expand= True, padx= 20, pady= 10)

chooseyoursize = Label(left_frame, text = "Choose your Size!", bg=TITLECol, fg=HEADINGCol, font=("calabri", 12)).pack(padx= 20, pady= 15, anchor="w")

for k, v in SIZES. items():
    Radiobutton(left_frame, text = f"{k} | Cost: ${v}", variable= size_pizza, value = v, bg= BGCol, fg=HEADINGCol,  font=("calabri", 12, "bold"), justify = "left").pack(padx= 10, pady = 5, anchor= "w")

chooseyourcrust = Label(left_frame, text = "Choose your Crust!", bg=TITLECol, fg=HEADINGCol, font=("calabri", 12)).pack(padx= 20, anchor="w")

for k, v in CRUSTS. items():
    Radiobutton(left_frame, text = f"{k} | Cost: ${v}", variable= size_pizza, value = v, bg= BGCol, fg=HEADINGCol,  font=("calabri", 12, "bold"), justify = "left").pack(padx= 10, anchor= "w")

extra_frame = Frame(left_frame, bg= BGCol)
extra_frame.pack()
i = 0
for k, v in EXTRAS_NUM. items():
    Checkbutton(extra_frame, text=k, variable=v, bg= BGCol, fg=HEADINGCol,  font=("calabri", 12, "bold")).grid(row= i//3, column= i%3, sticky= "w", padx= 5)
    i += 1



screen.mainloop()