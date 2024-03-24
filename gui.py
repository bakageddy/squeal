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
        return self.input_field.get()


def init(title: str) -> tk.Tk:
    window = tk.Tk()
    window.title(title)
    return window
