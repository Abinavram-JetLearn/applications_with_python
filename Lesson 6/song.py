from tkinter import *
import os
import pygame
pygame.init()
from tkinter import filedialog

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

index = 0
paused = False
playlist = []

def loadmusic():
    global index, playlist
    files = filedialog.askopenfilenames(filetypes=[("Audio Files", "*.mp3 *.wav *.ogg")])
    if files:
        playlist = list(files)
        index = 0
        nowplayingcardtextsong.config(text= os.path.basename(playlist[index]))

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
consoleback = Button(consolecard, text = "⏮️", bg= BUTTON, fg= "white", font=("Segoe UI", 15), width= 15,)
consoleback.grid(row = 0, column = 0, padx= 10, pady= 5)
consoleplay = Button(consolecard, text = "▶️", bg= BUTTON, fg= "white", font=("Segoe UI", 15), width= 15,)
consoleplay.grid(row = 0, column = 1, padx= 10, pady= 5)
consoleforward = Button(consolecard, text = "⏩", bg= BUTTON, fg= "white", font=("Segoe UI", 15), width= 15,)
consoleforward.grid(row = 0, column = 2, padx= 10, pady= 5)
consolestop = Button(consolecard, text = "Stop", bg= BUTTON, fg= "white", font=("Segoe UI", 15), width= 15,)
consolestop.grid(row = 1, column = 0, padx= 10, pady= 5)
consoleload = Button(consolecard, text = "📂Load", bg= BUTTON, fg= "white", font=("Segoe UI", 15), width= 15,command= loadmusic)
consoleload.grid(row = 1, column = 1, padx= 10, pady= 5)
consolepause = Button(consolecard, text = "⏸️", bg= BUTTON, fg= "white", font=("Segoe UI", 15), width= 15,)
consolepause.grid(row = 1, column = 2, padx= 10, pady= 5)
volume = Label(screen, text = "🔊", bg= CARD, fg= "white", font=("Segoe UI", 15), width= 50)
volume.pack(padx= 10, pady= 5)
volumescale = Scale(screen, from_=0, to=100, orient = 'horizontal', bg= CARD, fg= "white", font=("Segoe UI", 10), length= 350,)
volumescale.pack(padx= 10, pady= 5)



screen.mainloop()