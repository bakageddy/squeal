import tkinter as tk


class Input:
    def __init__(self, frame, label_buf):
        self.frame = frame
        self.label_buf = label_buf
        self.input_buf = tk.StringVar()

    def create(self):
        self.label = tk.Label(self.frame, text=self.label_buf)
        self.input_field = tk.Entry(self.frame, textvariable=self.input_buf)

    def set_grid_loc(self, row, col):
        self.label.grid(row=row, column=col)
        self.input_field.grid(row=row, column=(col + 1))

    def get_input(self):
        self.input_field.get()


def init(title: str) -> tk.Tk:
    window = tk.Tk()
    window.title(title)
    return window


window = init("My Tkinter GUI")
frame = tk.Frame(window)
frame.grid()

book_id = Input(frame, "Book ID:")
book_id.create()
book_id.set_grid_loc(0, 0)

author = Input(frame, "Author: ")
author.create()
author.set_grid_loc(1, 0)
