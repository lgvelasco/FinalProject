from tkinter import *
from PIL import ImageTk, Image
import TextEntry as te
import Screenplay2 as sp
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


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
        for i in range(4):
            self.canvas.append(Canvas(master=self.poster, width=380, height=400, bg="#A2D9CE", highlightthickness=0))
            self.canvas[i].grid(row=0, column=i)

        self.poster.grid(row=1, column=0, columnspan=5)

        # Adding posters to canvas
        size = 200, 500
        im = Image.open('Annie_Hall.jpg')
        im.thumbnail(size)
        self.canvas[0].image = ImageTk.PhotoImage(im)
        self.canvas[0].create_image(20, 60, image=self.canvas[0].image, anchor='nw')

        im = Image.open('Pulp_Fiction.jpg')
        im.thumbnail(size)
        self.canvas[1].image = ImageTk.PhotoImage(im)
        self.canvas[1].create_image(20, 60, image=self.canvas[1].image, anchor='nw')

        im = Image.open('La_La_Land.jpg')
        im.thumbnail(size)
        self.canvas[2].image = ImageTk.PhotoImage(im)
        self.canvas[2].create_image(20, 60, image=self.canvas[2].image, anchor='nw')

        im = Image.open('Requiem_For_A_Dream.jpg')
        im.thumbnail(size)
        self.canvas[3].image = ImageTk.PhotoImage(im)
        self.canvas[3].create_image(20, 60, image=self.canvas[3].image, anchor='nw')

        # Buttons
        self.bt1 = Button(self.frame, text='"Annie Hall"', command=self.annieh)
        self.bt1.config(font=("Courier", 30))
        self.bt1.grid(row=2, column=0)

        self.bt2 = Button(self.frame, text='Pulp Fiction', command=self.pulp)
        self.bt2.config(font=("Courier", 30))
        self.bt2.grid(row=2, column=1)

        self.bt3 = Button(self.frame, text='La La Land', command=self.lala)
        self.bt3.config(font=("Courier", 30))
        self.bt3.grid(row=2, column=2)

        self.bt4 = Button(self.frame, text='Requiem For A Dream', command=self.requiem)
        self.bt4.config(font=("Courier", 30))
        self.bt4.grid(row=2, column=3)

        self.analyze_bt = Button(self.frame, text="Analyze your own Screenplay", command=self.analyzer_opener)
        self.analyze_bt.config(font=("Courier", 30))
        self.analyze_bt.grid(row=3, columnspan=4, pady=100)

    # Opens the text entry so that the user can enter its own screenplay
    def analyzer_opener(self):
        root2 = Toplevel(self.window)
        analyzer = te.TextEntry(root2)

    # Shows the sentiment graph
    def show_sentiment_graph(self, title):
        annieh = sp.Screenplay(title)
        self.fig = annieh.plot_sentiment()
        root3 = Toplevel(self.window)
        self.canvas = FigureCanvasTkAgg(self.fig, master=root3)
        self.canvas.get_tk_widget().pack()
        self.canvas.draw()

    # Show characters bar graph
    def show_bar_graph(self, title):
        annieh = sp.Screenplay(title)
        self.fig = annieh.plot_characters()
        root3 = Toplevel(self.window)
        self.canvas = FigureCanvasTkAgg(self.fig, master=root3)
        self.canvas.get_tk_widget().pack()
        self.canvas.draw()

    # Show sentiment and bar graph
    def annieh(self):
        self.show_sentiment_graph('Annie_Hall.txt')
        self.show_bar_graph('Annie_Hall.txt')

    def pulp(self):
        self.show_sentiment_graph('Pulp_Fiction_Clean.txt')
        self.show_bar_graph('Pulp_Fiction_Clean.txt')

    def lala(self):
        self.show_sentiment_graph('La_La_Land_Clean.txt')
        self.show_bar_graph('La_La_Land_Clean.txt')

    def requiem(self):
        self.show_sentiment_graph("Requiem_For_A_Dream.txt")
        self.show_bar_graph("Requiem_For_A_Dream.txt")


window = Tk(screenName="Screenplay Analyzer")
poker_game = GUI(window)
window.mainloop()
