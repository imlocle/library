# print details of book
def print_book_detail(book):
    print(f"""
    ID: {book.id}
    Title: {book.title}
    Author: {book.author}
    Description: {book.description}
    """)

# inputs for books
def input_book_details():
    title = input('\nTitle: ')
    author = input('Author: ')
    description = input('Description: ')
    return title,author,description

# print book from search
def print_book_search(book):
    print(f'    [{book.id}] {book.title}')

def print_book_list(books):
    for x in books:
        print_book_search(x)
