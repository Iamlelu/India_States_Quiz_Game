import tkinter


class SCORE:
    def __init__(self):
        self.score = 0

    def creator(self):
        self.score_name_label = tkinter.Label(text=f'score - {self.score}'.upper(), font=("Helvetica",9))
        self.score_name_label.grid(row=1, column=0, columnspan=2, pady=5)

    def score_updater(self):
        self.score_name_label.destroy()
        self.score += 1
        self.creator()
