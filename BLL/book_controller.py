from DAL.Models.book import Book
from DAL import book_services

def get_all_books():
    books = []
    db_call = book_services.get_all_books_db()
    for x in db_call:
        books.append(Book(title=x[1], author=x[2], description=x[3], read=x[4], id=x[0]))
    return books

def add_new_book(title, author, description, read):
    book = Book(title=title, author=author, description=description, read=read)
    book_services.add_book_db(book)

def search_book_id(book_id):
    db_call = book_services.search_book_id_db(book_id)
    book = Book(title=db_call[1], author=db_call[2], description=db_call[3],id=db_call[0], read=db_call[4])
    return book

def update_book(book_id, new_title=None, new_author=None, new_description=None, new_read=None):
    db_call = book_services.update_book_db(book_id, new_title, new_author, new_description, new_read)
    return Book(title=db_call[1], author=db_call[2], description=db_call[3],read=db_call[4] ,id=db_call[0])

def search_books_keyword(keyword):
    books =[]
    db_call = book_services.search_books_keyword_db(keyword)
    for x in db_call:
        books.append(Book(title=x[1], author=x[2], description=x[3],read=x[4], id=x[0]))
    return books

def get_all_read_books():
    books = []
    db_call = book_services.get_all_read_books_db()
    for x in db_call:
        books.append(Book(title=x[1], author=x[2], description=x[3],read=x[4],id=x[0]))
    return books


    




