# print details of book
def print_book_detail(book):
    print(book.title)
    if book.read is None or book.read=='':
        book.read = 0
    read = 'Yes' if book.read > 0 else 'No'
    print(f"""
    ID: {book.id}
    Title: {book.title}
    Author: {book.author}
    Description: {book.description}
    Read: {read}
    """)

# inputs for books
def input_book_details():
    title = input('\nTitle: ')
    author = input('Author: ')
    description = input('Description: ')
    read = input('Read? (Y/N): ')
    if read.lower() == 'y':
        read = 1
    elif read.lower() == 'n':
        read = 0
    return title,author,description, read

# print book from search
def print_book_search(book):
    print(f'    [{book.id}] {book.title}')

def print_book_list(books):
    for x in books:
        print_book_search(x)

def book_id_req():
    print('\nTo view details enter the book ID, or return press <Enter>.')
    book_id = input('\nBook ID: ')
    return book_id
