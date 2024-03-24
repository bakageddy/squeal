import sqlite3
import gui


cx = sqlite3.connect("./tutorial.db")
cur = cx.cursor()
cur.execute(
    "CREATE TABLE IF NOT EXISTS library(bookid, isbn, author, title, publisher)"
)

gui.window.mainloop()
