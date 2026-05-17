from tkinter import *

screen = Tk()
screen.title("Caeser Cypher encryption")
screen.geometry("700x700")

#Colors
BG = "#1C022B"
CARD = "#2C0A3F"
MUSIC_PLAYLIST = "#510347"
UnSat_Text = "#5d5d5d"
BUTTON = "#FF00C8"

screen.config(background=BG)

def Cypher():
    global encrypted
    text = EntryTextBox.get()
    shift = EntryShiftScale.get()
    encrypted = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                encrypted += chr((ord(char) - 65 + shift) % 26 + 65)
            elif char.islower():
                encrypted += chr((ord(char) - 97 + shift) % 26 + 97)
        else:
            encrypted += char
    with open("encrypted_text.txt", "w") as file:
        file.write(encrypted)
        file.close()


title = Label(screen, text="Caesar Cypher", bg=BG, fg=UnSat_Text , font=("verdana", 30, "bold"))
EntryTextLabel = Label(screen, text="Paste or type the sentence you want to cypher", bg=BG, fg=UnSat_Text , font=("verdana", 14, "bold"))
EntryTextBox = Entry(screen, bg=BG, fg=CARD , font=("verdana", 28, "bold"))
EntryShiftLabel = Label(screen, text="Shift the slider to make a cypher", bg=BG, fg=UnSat_Text , font=("verdana", 14, "bold"))
EntryShiftScale = Scale(screen, from_=1, to=25, orient = 'horizontal', bg= CARD, fg= "white", font=("Segoe UI", 10), length= 350)
SubmitButton = Button(screen, bg=BG, fg=UnSat_Text , font=("verdana", 28, "bold"), text="Submit", command= Cypher)

title.pack(padx = 10, pady = 20)
EntryTextLabel.pack(padx = 10)
EntryTextBox.pack(padx = 10, pady = 20)
EntryShiftLabel.pack(padx = 10)
EntryShiftScale.pack(padx = 10, pady = 20)
SubmitButton.pack(padx= 10, pady= 20)

screen.mainloop()