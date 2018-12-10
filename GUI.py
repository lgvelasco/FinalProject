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

        # canvas for posters
        self.poster = Frame(master=self.frame)
        self.canvas = []
        for i in range(5):
            # set the background to green to simulate a table and set the border thickness to 0
            self.canvas.append(Canvas(master=self.poster, width=250, height=400, bg="#A2D9CE", highlightthickness=0))
            self.canvas[i].grid(row=0, column=i)

        self.poster.grid(row=1, padx=75)

        # Adding posters to canvas
        size = 200, 500
        im = Image.open('Annie_Hall.jpg')
        im.thumbnail(size)
        self.canvas[0].image = self.canvas[0].image = ImageTk.PhotoImage(im)
        self.canvas[0].create_image(20, 60, image=self.canvas[0].image, anchor='nw')

        im = Image.open('Pulp_Fiction.jpg')
        im.thumbnail(size)
        self.canvas[1].image = self.canvas[1].image = ImageTk.PhotoImage(im)
        self.canvas[1].create_image(20, 60, image=self.canvas[1].image, anchor='nw')






window = Tk(screenName="Poker")
poker_game = GUI(window)
window.mainloop()