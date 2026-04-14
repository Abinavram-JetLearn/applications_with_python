from tkinter import *
import qrcode
from PIL import Image, ImageTk
from tkinter import messagebox

screen = Tk()
screen.title("Login Me")
screen.geometry("500x500")
screen.config(background="purple")

title = Label(screen, text="Qr Code Generator", bg="purple", fg="black", font=("Verdana", 28, "bold"))
title.pack(padx = 5, pady = 20)

qrcode_img = Label(screen)
qrcode_img.pack(padx = 5, pady = 20)

placeholder = Image.open("3. GUI Python\Lesson 5\placeholder_img.png")
placeholder = placeholder.resize((150, 150))
img_tk = ImageTk.PhotoImage(placeholder)
qrcode_img.config(image= img_tk)
qrcode_img.image = img_tk

def QRCodeGpS():
    data = qrcodeurlgenerate.get()
    filename = qrcodefilename.get()
    if data == "" or filename == "":
        messagebox.showerror("Error!", "Please answer all the fields")
    else:
        qrcodeimgupdate = qrcode.make(data)
        qrcodeimgupdate.save(f"3. GUI Python\Lesson 5\SavedQrCodes\{filename}.png")
        qrcodeimgup_date = Image.open(f"3. GUI Python\Lesson 5\SavedQrCodes\{filename}.png")
        qrcodeimgup_date = qrcodeimgup_date.resize((150, 150))
        img_tk = ImageTk.PhotoImage(qrcodeimgup_date)
        qrcode_img.config(image= img_tk)
        qrcode_img.image = img_tk

qrcodeurlgeneratelabel = Label(screen, text="Url", bg="purple", fg="black", font=("Verdana", 10, "bold"))
qrcodeurlgeneratelabel.pack(padx = 110, pady= 2, anchor="w")

qrcodeurlgenerate = Entry(screen, bg="#402357", fg="black", font=("Verdana", 15, "bold"))
qrcodeurlgenerate.pack(padx = 10)

qrcodefilenamelabel = Label(screen, text="Filename", bg="purple", fg="black", font=("Verdana", 10, "bold"))
qrcodefilenamelabel.pack(padx = 110, pady= 2, anchor="w")

qrcodefilename = Entry(screen, bg="#402357", fg="black", font=("Verdana", 15, "bold"))
qrcodefilename.pack(padx = 10)

qrcodesubmitbutton = Button(screen, text="Generate QrCode!", bg="#CF10B2", fg="black", font=("Verdana", 25, "bold"), command= QRCodeGpS)
qrcodesubmitbutton.pack(padx = 10, pady = 20)

screen.mainloop()