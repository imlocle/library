import sqlite3

conn = sqlite3.connect('library.db')
conn.execute('''CREATE TABLE IF NOT EXISTS books
            (id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            author TEXT,
            description CHAR(100),
            read INTEGER );
            ''')

# Add new column
# conn.execute('''
#         ALTER TABLE books
#         ADD COLUMN read INTEGER;
# ''')

def cursor():
    return sqlite3.connect('library.db').cursor()

def get_all_books_db():
    c = cursor()
    with c.connection:
        c.execute('SELECT * From books')
        rows=c.fetchall()
    return rows

def add_book_db(book):
    c = cursor()
    with c.connection:
        c.execute('INSERT INTO books (title, author, description, read) VALUES (?,?,?,?)', 
        (book.title, book.author, book.description, book.read))
    return c.lastrowid

def search_book_id_db(book_id):
    c = cursor()
    with c.connection:
        c.execute('SElECT * FROM books WHERE id=?', (book_id,))
        book=c.fetchone()
    return book

def update_book_db(book_id, new_title=None, new_author=None, new_description=None, new_read=None):
    print(new_read)
    c = cursor()
    with c.connection:
        if new_title:
            c.execute('UPDATE books SET title=? WHERE id=?', (new_title, book_id,))
        if new_author:
            c.execute('UPDATE books SET author=? WHERE id=?', (new_author, book_id,))
        if new_description:
            c.execute('UPDATE books SET description=? WHERE id=?', (new_description, book_id,))
        if new_read is not None:
            print('db')
            print(new_read)
            c.execute('UPDATE books SET read=? WHERE id=?', (new_read, book_id))
    return search_book_id_db(book_id)

def search_books_keyword_db(keyword):
    c = cursor()
    with c.connection:
        c.execute("SELECT * FROM books WHERE title LIKE ?",(f'%{keyword}%',))
        rows = c.fetchall()
    return rows

def get_all_read_books_db():
    c = cursor()
    with c.connection:
        c.execute('SELECT * From books WHERE read=1')
        rows=c.fetchall()
    return rows
