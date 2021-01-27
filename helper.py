# print details of book
def print_book_detail(book):
    print(f'\nID: {book.id}')
    print(f'Title: {book.title}')
    print(f'Author: {book.author}')
    print(f'Description: {book.description}\n')

# inputs for books
def input_book_details():
    title = input('Title: ')
    author = input('Author: ')
    description = input('Description: ')
    return title,author,description

# print book from search
def print_book_search(book):
    print(f'[{book.id}] {book.title}')