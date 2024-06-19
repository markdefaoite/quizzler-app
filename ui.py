from tkinter import *

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.canvas = Canvas(width=300, height=250)
        self.canvas.grid(row=1, column=0, columnspan=2)

        self.score_label = Label(text="score: 0")
        self.score_label.grid(row=0, column=1)

        self.true_img = PhotoImage(file="images/true.png")
        self.false_img = PhotoImage(file="images/false.png")

        self.true_button = Button(image=self.true_img, highlightthickness=0)
        self.true_button.grid(row=2, column=0)

        self.false_button = Button(image=self.false_img, highlightthickness=0)
        self.false_button.grid(row=2, column=1)

        self.window.mainloop()