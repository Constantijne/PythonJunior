import json
import sqlite3


def connect_to_db():
    return sqlite3.connect('books_db.db')


class FromJSONToDB:
    @staticmethod
    def import_json():
        with open('books-data-source.json') as f:
            bookshelf = json.load(f)
        return bookshelf

    @staticmethod
    def generate_database(book, step):
        cur = connect_to_db().cursor()
        cur.execute(
            f"""Insert into books_db(name_b, author, status) 
            values('{book[step]["title"]}', '{', '.join([i for i in book[step]["authors"]])}', 
            '{book[step]["status"]}'); """)
        return ''


class IsAdmin:
    @staticmethod
    def is_correct_user(u_login, u_password):
        if u_login != 'admin' and u_password != 'admin':
            return False
        return True


class GetBooks:
    @staticmethod
    def by_author(author_name):
        cur = connect_to_db().cursor()
        cur.execute(f"""Select * from books_db where author = '{author_name}';""")
        result_of_search = cur.fetchall()
        return result_of_search

    @staticmethod
    def by_name(book_name):
        cur = connect_to_db().cursor()
        cur.execute(f"""Select * from books_db where name_b = '{book_name}';""")
        result_of_search = cur.fetchall()
        return result_of_search


while True:
    menu_mode = input("What U want to do?\n>")
    if menu_mode == '/add':
        getAccess = IsAdmin.is_correct_user(input('Enter login: '), input('Enter password: '))
        books = FromJSONToDB.import_json()
        if getAccess is True:
            for i in range(len(books)):
                FromJSONToDB.generate_database(books, i)
            print("All rows added to the books_db.db from JSON-file! Have a nice day!)")
        else:
            print("Wrong login or password!")
    elif menu_mode == '/quit':
        print("Thank U for using my application. Goodbye!")
        break
    elif menu_mode == '/help':
        print("/add - Add rows to DB\n/search - Search book\n/help - Get command list\n/quit - Exit from program")
    elif menu_mode == '/search':
        more_menu_mode = input('1.By author\n2.By name\n>')
        if more_menu_mode.lower() == 'author' or more_menu_mode == 1:
            getBook = GetBooks.by_author(input("Enter authors names: "))
            for i in range(len(getBook)):
                print(f"{i + 1}. Title of the book: {getBook[i][0]}, "
                      f"Author(s): {getBook[i][1]}, "
                      f"Status of the book: {getBook[i][2]}")
        elif more_menu_mode.lower() == 'name' or more_menu_mode == 2:
            getBook = GetBooks.by_name(input("Enter book name: "))
            for i in range(len(getBook)):
                print(f"{i + 1}. Title of the book: {getBook[i][0]}, "
                      f"Author(s): {getBook[i][1]}, "
                      f"Status of the book: {getBook[i][2]}")
        else: print("Wrong menu item!")
    else:
        print("Wrong command !")
