from BLL import bookcontroller
from helper import print_book_detail, input_book_details, print_book_search

def menu():
    print("""
    ==== Book Manager ====\n
    1. View All Books
    2. Add A New Book
    3. Edit A Book
    4. Search For Books Using Keywords
    5. Save and Exit  
    """)

def app():
    try:
        while True:
            menu()
            response = int(input("Choose [1-5]: "))
            # View All
            if response == 1:
                print("\n==== View All Books ====\n")
                for x in bookcontroller.get_all_books():
                    print_book_search(x)
                print('\nTo view details enter the book ID, to return press <Enter>.')
                book_id = input('Book ID: ')
                while book_id:
                    print_book_detail(bookcontroller.search_book_id(book_id))
                    print('\nTo view details enter the book ID, to return press <Enter>.')
                    book_id = input('Book ID: ')
            # Add Book
            elif response == 2:
                print("\n==== Add A New Books ====\n")
                print('Please enter the following information:')
                title, author, description = input_book_details()
                bookcontroller.add_new_book(title, author, description)
                print(f"\n{title} by {author} is Saved!")
                print('Return press <Enter>')
                input()
            # Edit Book
            elif response == 3:
                print("\n==== Edit A Book ====\n")
                print("Here are the available books:\n")
                for x in bookcontroller.get_all_books():
                    print_book_search(x)
                print('\nEnter the Book ID of the book you want to edit; to return press <Enter>.')
                book_id = input('Book ID: ')
                if book_id:
                    update_book = bookcontroller.search_book_id(book_id)
                    print('Input the following information. To leave a field unchanged, hit <Enter>')
                    print_book_detail(update_book)
                    title, author, description = input_book_details()
                    update_book = bookcontroller.update_book(book_id, title, author, description)
                    print_book_detail(update_book)
                    print('Book is updated!')
                    print('Return press <Enter>')
                    input()
            # Search with Keyword
            elif response == 4:
                print("\n==== Search ====\n")
                print('Please type in a keyword')
                keyword = input('Search: ')
                books = bookcontroller.search_books_keyword(keyword)
                print('The following books matched your query.\n')
                for x in books:
                    print_book_search(x)
                print('\nEnter the Book ID to see more details, or <ENTER> to return\n')
                book_id = input('Book ID: ')
                while book_id:
                    print_book_detail(bookcontroller.search_book_id(book_id))
                    print('\nTo view details enter the book ID, to return press <Enter>.')
                    book_id = input('Book ID: ')
            # Leave Program
            elif response == 5:
                print("Library saved")
                break
            else:
                print('Invalid input')
                print('Return press <Enter>')
                input()
    except:
        print('A possible error has occured')
        print('Return press <Enter>')
        input()

app()