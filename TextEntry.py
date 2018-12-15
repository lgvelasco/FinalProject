from tkinter import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import Screenplay2 as sp


class TextEntry(object):
    def __init__(self, window):
        self.window = window
        myfont = ("Times New Roman", 18)
        # bgcolor = "#1ABC9C"
        bgcolor = "#FAD7A0"
        window.title("Screenplay Entry")
        window.geometry("1400x700")
        window.resizable(0, 0)

        self.frame = Frame(master=window, bg=bgcolor)
        self.frame.pack_propagate(0)  # Don't allow the widgets inside to determine the frame's width / height
        self.frame.pack(fill=BOTH, expand=1)  # Expand the frame to fill the root window

        # Text entry
        self.txt = Text(self.frame, borderwidth=3, relief="sunken")
        self.txt.config(font=myfont, undo=True, wrap='word')
        self.txt.grid(row=1, column=0, sticky="nsew", padx=2, pady=2, rowspan=4)

        # Scrollbar
        scrollb = Scrollbar(self.frame, command=self.txt.yview)
        scrollb.grid(row=1, column=1, sticky='nsew', rowspan=4)
        self.txt['yscrollcommand'] = scrollb.set

        # Buttons
        self.analyze_bt = Button(self.frame, text='Analyze', command=self.show_everything)
        self.analyze_bt.config(font=("Courier", 30))
        self.analyze_bt.grid(row=1, column=3, padx=250)

        self.exit_bt = Button(self.frame, text='Exit', command=self.close)
        self.exit_bt.config(font=("Courier", 30))
        self.exit_bt.grid(row=2, column=3, padx=250)

    def close(self):
        exit(0)

    # Reads the text box and adds it to new file, to be able to work with Screenplay2 class
    def write_to_textanalyzer(self):
        text_ta = open('TextAnalyzer.txt', 'w')
        text = self.txt.get("1.0", 'end-1c')
        text_ta.write(text)
        text_ta.close()

    def show_sentiment_graph(self, title):
        annieh = sp.Screenplay(title)
        self.fig = annieh.plot_sentiment()
        root3 = Toplevel(self.window)
        self.canvas = FigureCanvasTkAgg(self.fig, master=root3)
        self.canvas.get_tk_widget().pack()
        self.canvas.draw()

    def show_bar_graph(self, title):
        annieh = sp.Screenplay(title)
        self.fig = annieh.plot_characters()
        root3 = Toplevel(self.window)
        self.canvas = FigureCanvasTkAgg(self.fig, master=root3)
        self.canvas.get_tk_widget().pack()
        self.canvas.draw()

    def show_everything(self):
        self.write_to_textanalyzer()
        self.show_sentiment_graph('TextAnalyzer.txt')
        self.show_bar_graph('TextAnalyzer.txt')

def run_textentry():
    window = Tk(screenName="Screenplay Analyzer")
    poker_game = TextEntry(window)
    window.mainloop()


if __name__ == "__main__":
    run_textentry()
