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
        window

        self.frame = Frame(master=window, bg=bgcolor)
        self.frame.pack_propagate(0)  # Don't allow the widgets inside to determine the frame's width / height
        self.frame.pack(fill=BOTH, expand=1)  # Expand the frame to fill the root window

        self.label = Label(self.frame, text="sgdfg", bg=bgcolor, fg="white")
        self.label.grid(row=5)
        self.label.config(font=("Courier", 44))
        self.label2 = Label(self.frame, text='title', bg=bgcolor, fg="White")
        self.label2.grid(row=0, columnspan=2)
        self.label2.config(font=("Courier", 20))

        self.bt1 = Button(self.frame, text='"Annie Hall"')
        self.bt1.config(font=("Courier", 30))
        self.bt1.grid(row=1, column=1)

        self.bt2 = Button(self.frame, text='Pulp Fiction')
        self.bt2.config(font=("Courier", 30))
        self.bt2.grid(row=1, column=2)

        self.bt3 = Button(self.frame, text='Test')
        self.bt3.config(font=("Courier", 30))
        self.bt3.grid(row=1, column=3)

        self.bt4 = Button(self.frame, text='Test')
        self.bt4.config(font=("Courier", 30))
        self.bt4.grid(row=1, column=4)

        # # canvas for posters
        # self.poster = Frame(master=self.frame)
        # self.canvas = []
        # for i in range(5):
        #     self.canvas.append(Canvas(master=self.poster, width=250, height=400, bg="#A2D9CE", highlightthickness=0))
        #     self.canvas[i].grid(row=0, column=i)
        #
        # self.poster.grid(row=2, padx=75, columnspan=5)
        #
        # # Adding posters to canvas
        # size = 200, 500
        # im = Image.open('Annie_Hall.jpg')
        # im.thumbnail(size)
        # self.canvas[0].image = ImageTk.PhotoImage(im)
        # self.canvas[0].create_image(20, 60, image=self.canvas[0].image, anchor='nw')
        #
        # im = Image.open('Pulp_Fiction.jpg')
        # im.thumbnail(size)
        # self.canvas[1].image = ImageTk.PhotoImage(im)
        # self.canvas[1].create_image(20, 60, image=self.canvas[1].image, anchor='nw')
        # self.bt2 = Button(self.frame, text="Exit Game", bg="black", fg="yellow")
        # self.bt2.grid(row=2, column=2)


window = Tk(screenName="Screenplay Analyzer")
poker_game = GUI(window)
window.mainloop()
