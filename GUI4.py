from tkinter import *
from PIL import ImageTk, Image


class GUI(object):
    def __init__(self, window):
        self.window = window
        myfont = ("Times New Roman", 18)
        bgcolor = "#1ABC9C"
        # bgcolor = "#FAD7A0"
        window.title("Final Project Luis Guillermo Velasco")
        window.geometry("1400x700")
        window.resizable(0, 0)

        self.frame = Frame(master=window, bg=bgcolor)
        self.frame.pack_propagate(0)  # Don't allow the widgets inside to determine the frame's width / height
        self.frame.pack(fill=BOTH, expand=1)  # Expand the frame to fill the root window

        photo = PhotoImage(file="Annie_Hall.jpg")
        b = Button(self.frame, image=photo, height=50, width=150)
        b.grid(row=0, column=1)


window = Tk(screenName="Screenplay Analyzer")
poker_game = GUI(window)
window.mainloop()
