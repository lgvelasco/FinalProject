from tkinter import *
import Screenplay as sp


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
        self.analyze_bt = Button(self.frame, text='Analyze')
        self.analyze_bt.config(font=("Courier", 30))
        self.analyze_bt.grid(row=1, column=3, padx=250)

        self.exit_bt = Button(self.frame, text='Exit', command=self.close)
        self.exit_bt.config(font=("Courier", 30))
        self.exit_bt.grid(row=2, column=3, padx=250)

    def close(self):
        exit(0)


def run_textentry():
    window = Tk(screenName="Screenplay Analyzer")
    poker_game = TextEntry(window)
    window.mainloop()


if __name__ == "__main__":
    run_textentry()
