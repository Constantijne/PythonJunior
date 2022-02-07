import json
import sqlite3


def import_json():
    with open('books-data-source.json') as f:
        bookshelf = json.load(f)
    return bookshelf


def generate_database(book):
    conn = sqlite3.connect('books_db.db')
    cur = conn.cursor()
    i = 1
    b_title, b_author, b_isbn = book[1]['title'], book[1]['authors'], book[1]['isbn']

    print(b_title, b_author, b_isbn)
    cur.execute("""CREATE TABLE IF NOT EXISTS books_db(
       name_b varchar,
       author varchar, 
       isbn integer);
    """)
    conn.commit()
    cur.execute(
        """Insert into books_db(name_b, author, isbn)
        values('one', 'b_author', 1)""")
    conn.commit()
    return 'Done!'


books = import_json()
for i in range(5):
    print(books[i]['title'])

print(generate_database(books))
