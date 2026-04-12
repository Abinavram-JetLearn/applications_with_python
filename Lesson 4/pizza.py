from tkinter import *
from tkinter import messagebox

screen = Tk()
screen.title("Pizza App")
screen.geometry("800x600")
screen.state("zoomed")

BGCol = "#09122b"
TITLECol ="#072347"
HEADINGCol = "#849cdf"
PARACol = "#50649a"
CARDCol = "#273048"
lines= []
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
size_pizza = StringVar(value = "Medium (10\")")
crust = StringVar(value = "Classic")
pizzas_qua = IntVar(value = 1)

screen.config(background= BGCol)
title = Label(screen, text="Super Pizza | Not Authentic Italian food", bg=TITLECol, fg=HEADINGCol, font=("calabri", 25, "bold"))
chooseyourpizzaframe = Frame(screen, bg= CARDCol, highlightthickness= 1, highlightbackground = PARACol, borderwidth= 15)
chooseyourpizza = Label(screen, text = "Choose your Pizza!", bg=TITLECol, fg=HEADINGCol, font=("calabri", 12))
title.pack(padx= 20)
chooseyourpizza.pack(padx= 20, pady= 15, anchor="w")

for i, p in enumerate(pizzas):
    Radiobutton(chooseyourpizzaframe, text= f"{p["name"]} | Cost: ${p['price']}", variable= pizza, value = p["name"], bg= BGCol, fg=HEADINGCol,  font=("calabri", 12, "bold"), justify = "left").grid(row= i//3, column =i%3, padx = 5, pady = 10)

chooseyourpizzaframe.pack(anchor= "w")

mainframe = Frame(screen, bg= BGCol)
mainframe.pack(fill="both", expand="True", padx= 10, pady= 10)

left_frame = Frame(mainframe, bg= BGCol)
left_frame.pack(side="left", fill="both", expand= True, pady= 10)
left_frame_canvas = Canvas(left_frame, bg= BGCol, borderwidth= 0, highlightthickness= 0)
left_frame_canvas.pack(side="left", fill="both", expand= True, padx= 20, pady= 20)
left_frame_scrollbar = Scrollbar(left_frame, orient="vertical", command= left_frame_canvas.yview)
left_frame_scrollbar.pack(side= "right", fill= Y)
scroll_frame = Frame(left_frame_canvas, bg= BGCol)
left_frame_canvas.create_window((0,0), window= scroll_frame, anchor= "nw")
scroll_frame.bind("<Configure>",
    lambda e: left_frame_canvas.configure(scrollregion=left_frame_canvas.bbox("all")))
left_frame_canvas.bind_all("<MouseWheel>", lambda e: left_frame_canvas.yview_scroll(-1*(e.delta//120), "units"))

right_frame = Frame(mainframe, bg= BGCol)
right_frame.pack(side="right", fill="both", expand= True, padx= 20, pady= 10)
recipt_your_order = Label(right_frame, text = "Your order", bg=TITLECol, fg=HEADINGCol, font=("calabri", 12)).pack(padx= 20, pady= 20)
summary_label = Label(
    right_frame,
    text="",
    bg=BGCol, fg=PARACol,
    font=("Calibri", 11),
    justify="left",
    anchor="nw",
    padx=12, pady=12,
    wraplength=260,
)

def update_summary(*_):
    global lines
    chosen = next((p for p in pizzas if p["name"] == pizza.get()),pizzas[0])
    base = chosen["price"]
    s_cost = SIZES.get(size_pizza.get(), 0.0)
    c_cost = CRUSTS.get(crust.get(), 0.0)
    extras = [(k, EXTRAS[k]) for k, v in EXTRAS_NUM.items() if v.get()]
    e_cost = sum(c for _, c in extras)
    total_cost = (s_cost + c_cost + e_cost + base) * pizzas_qua.get()
    lines = [
        f"Pizza: {chosen["name"]}, ${chosen["price"]}",
        f"Size: {size_pizza.get()}, ${s_cost}",
        f"Crust: {crust.get()}, ${c_cost}",
    ]
    if extras:
        lines.append("Extras:")
        lines += ["  + %s  (+$%.2f)" % (k, c) for k, c in extras]
    lines.append(f"Total: {pizzas_qua.get()}, ${round(total_cost, 2)}")
    summary_label.config(text= "\n".join(lines))

summary_label.pack(fill="both", expand=True)
qty_frame = Frame(right_frame, bg=BGCol)
qty_frame.pack(pady=8)

Label(qty_frame, text="Quantity:", bg=BGCol, fg=HEADINGCol,
      font=("Calibri", 12)).pack(side="left", padx=4)
Button(qty_frame, text="-", bg=CARDCol, fg=HEADINGCol, font=("Calibri", 12, "bold"),
       command=lambda: [pizzas_qua.set(max(1, pizzas_qua.get()-1)), update_summary()]).pack(side="left")
Label(qty_frame, textvariable=pizzas_qua, bg=BGCol, fg=HEADINGCol,
      font=("Calibri", 12, "bold"), width=3).pack(side="left")
Button(qty_frame, text="+", bg=CARDCol, fg=HEADINGCol, font=("Calibri", 12, "bold"),
       command=lambda: [pizzas_qua.set(pizzas_qua.get()+1), update_summary()]).pack(side="left")
def place_order():
    global lines
    messagebox.showinfo("Order Placed!", "\n".join(lines))

    pizza.set("Margherita")
    size_pizza.set('Medium (10")')
    crust.set("Classic")
    pizzas_qua.set(1)
    for v in EXTRAS_NUM.values():
        v.set(0)

Button(
    right_frame,
    text="🍕  Place Order",
    bg="#1a6b2a", fg="white",
    font=("Calibri", 13, "bold"),
    activebackground="#24943a", activeforeground="white",
    relief="flat", cursor="hand2",
    padx=10, pady=8,
    command=place_order,
).pack(fill="x", padx=10, pady=(4, 12))


chooseyoursize = Label(scroll_frame, text = "Choose your Size!", bg=TITLECol, fg=HEADINGCol, font=("calabri", 12)).pack(padx= 20, pady= 20, anchor="w")

for k, v in SIZES. items():
    Radiobutton(scroll_frame, text = f"{k} | Cost: ${v}", variable= size_pizza, value = k, bg= BGCol, fg=HEADINGCol,  font=("calabri", 12, "bold"), justify = "left").pack(padx= 10, pady = 5, anchor= "w")

chooseyourcrust = Label(scroll_frame, text = "Choose your Crust!", bg=TITLECol, fg=HEADINGCol, font=("calabri", 12)).pack(padx= 20, anchor="w")

for k, v in CRUSTS. items():
    Radiobutton(scroll_frame, text = f"{k} | Cost: ${v}", variable= crust, value = k, bg= BGCol, fg=HEADINGCol,  font=("calabri", 12, "bold"), justify = "left").pack(padx= 10, anchor= "w")

extra_frame = Frame(scroll_frame, bg= BGCol)
extra_frame.pack()
i = 0
for k, v in EXTRAS_NUM. items():
    Checkbutton(extra_frame, text=k, variable=v, bg= BGCol, fg=HEADINGCol,  font=("calabri", 12, "bold")).grid(row= i//3, column= i%3, sticky= "w", padx= 5)
    i += 1

for var in [pizza, size_pizza, crust] + list(EXTRAS_NUM.values()):
    var.trace_add("write", update_summary)
update_summary()
screen.mainloop()