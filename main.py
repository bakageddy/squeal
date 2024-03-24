import tkinter as tk
import sqlite3
import gui


cx = sqlite3.connect("./tutorial.db")
cur = cx.cursor()
cur.execute(
    "CREATE TABLE IF NOT EXISTS library(bookid, isbn, author, title, publisher)"
)


def insert_record(_):
    records = {}
    for k, v in inputs.items():
        records[k] = v[1].get_input()
        if (records[k] == ''):
            return None

    book_id = records['book_id']
    isbn = records['isbn']
    author = records['author']
    publisher = records['publisher']
    title = records['title']
    query = f"INSERT INTO library VALUES (\"{book_id}\", \"{isbn}\", \"{author}\", \"{title}\", \"{publisher}\");"
    cur.execute(query)
    cx.commit()


window = gui.init("My Tkinter GUI")
frame = tk.Frame(window)
frame.grid()

inputs = {
    "book_id": ["Book ID:", None],
    "author": ["Author: ", None],
    "title": ["Title: ", None],
    "publisher": ["Publisher: ", None],
    "isbn": ["ISBN", None],
}

i = 0
for k, v in inputs.items():
    v[1] = gui.Input(frame, v[0])
    v[1].create()
    v[1].set_grid_loc(i, 0)
    i += 1

submit = tk.Button(frame, text="Submit")
submit.grid(row=i, column=3)
submit.bind("<Return>", insert_record)

window.mainloop()

cur.close()
cx.close()
