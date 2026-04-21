from tkinter import *


screen = Tk()
screen.title("Login Me")
screen.geometry("600x600")

BG = "#1C022B"
CARD = "#2C0A3F"
MUSIC_PLAYLIST = "#510347"
UnSat_Text = "#5d5d5d"
BUTTON = "#FF00C8"

screen.config(background="#1C022B")

title = Label(screen, text="Music Player🎤🎼🎵🎶", bg="#1C022B", fg="white", font=("Segoe UI", 25))
title.pack(padx= 10, pady = 30)

#Now Playing Card
nowplayingcard = Frame(screen, bg=CARD)
nowplayingcardtext = Label(nowplayingcard, text="Now Playing:", bg= CARD, fg=UnSat_Text, font=("Segoe UI", 15))
nowplayingcardtextsong = Label(nowplayingcard, text="[PlaceHolder]", bg= CARD, fg="white", font=("Segoe UI", 20))

nowplayingcard.pack(padx = 10, pady = 5, fill= "x")
nowplayingcardtext.pack(padx = 10, pady = 5)
nowplayingcardtextsong.pack(padx = 10, pady = 5)

#Console Card
consolecard = Frame(screen, bg= CARD)
consolecard.pack(padx = 10, pady = 5, fill= "x")
consoleback = Button(consolecard, text = "<<", bg= BUTTON, fg= "white", font=("Segoe UI", 15), width= 6,)
consoleback.grid(row = 0, column = 0, padx= 10, pady= 5)
consoleplay = Button(consolecard, text = "||", bg= BUTTON, fg= "white", font=("Segoe UI", 15), width= 6,)
consoleplay.grid(row = 0, column = 1)

screen.mainloop()