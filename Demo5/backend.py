import sqlite3


def connect():
    conn = sqlite3.connect('books.db')
    cur = conn.cursor()
    cur.execute(
        "CREATE TABLE IF NOT EXISTS book(id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn INTEGER)")  # noqa ignore=E501
    conn.commit()
    conn.close()


def insert(title, author, year, isbn):
    conn = sqlite3.connect('books.db')
    cur = conn.cursor()
    cur.execute("INSERT INTO book VALUES (NULL,?,?,?,?)", (title, author, year, isbn))  # noqa ignore=E501
    conn.commit()
    conn.close


def view():
    conn = sqlite3.connect('books.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM book")
    rows = cur.fetchall()
    conn.close

    return rows


def search(title="", author="", year="", isbn=""):
    conn = sqlite3.connect('books.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=?",  # noqa ignore=E501
                (title, author, year, isbn))
    rows = cur.fetchall()
    conn.close

    return rows


def delete(id):
    conn = sqlite3.connect('books.db')
    cur = conn.cursor()
    cur.execute("DELETE FROM book WHERE id=?", (id,))
    conn.commit()
    conn.close


def update(id, title, author, year, isbn):
    conn = sqlite3.connect('books.db')
    cur = conn.cursor()
    cur.execute("UPDATE book SET title=?, author=?, year=?, isbn=? WHERE id=?",
                (title, author, year, isbn, id))
    conn.commit()
    conn.close


connect()

# insert("the g3losa", "mahrous", 1997, 1593576842)
# update(4, "The doctor", "Disha", 1997, 1478523690)
# delete(4)
# print(view())
# print(search(author="Nasser"))
