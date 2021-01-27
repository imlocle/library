from BLL import bookcontroller
from helper import print_book_detail, input_book_details, print_book_search, print_book_list

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
    while True:
        try:
            menu()
            response = int(input("Choose [1-5]: "))
            # View All
            if response == 1:
                print("\n==== View All Books ====\n")
                all_books = bookcontroller.get_all_books()
                if len(all_books) < 1:
                    print("There are no books. Please add some.")
                else:
                    print_book_list(all_books)
                    print('\nTo view details enter the book ID, or return press <Enter>.')
                    print('\nPress <0> to View All Books')
                    book_id = input('\nBook ID: ')
                    while book_id:
                        if book_id == '0':
                            print("\n==== View All Books ====\n")
                            print_book_list(all_books)
                            print('\nTo view details enter the book ID, or return press <Enter>.')
                            print('\nPress <0> to View All Books')
                            book_id = input('\nBook ID: ')
                        else:
                            print_book_detail(bookcontroller.search_book_id(book_id))
                            print('\nTo view details enter the book ID, or return press <Enter>.')
                            book_id = input('\nBook ID: ')
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
                print('\nEnter the Book ID of the book you want to edit, or return press <Enter>.')
                book_id = input('Book ID: ')
                if book_id:
                    update_book = bookcontroller.search_book_id(book_id)
                    print('Input the following information. To leave a field unchanged, hit <Enter>')
                    print_book_detail(update_book)
                    title, author, description = input_book_details()
                    update_book = bookcontroller.update_book(book_id, title, author, description)
                    print_book_detail(update_book)
                    print('\nBook is updated!')
                    print('Return press <Enter>')
                    input()
            # Search with Keyword
            elif response == 4:
                print("\n==== Search ====\n")
                print('Please type in a keyword')
                keyword = input('Search: ')
                books = bookcontroller.search_books_keyword(keyword)
                if len(books) < 1:
                    print(f'\nThere are no books with keyword: [{keyword}]')
                else:
                    print(f'\nThe following books matched your keyword: [{keyword}]\n')
                    print_book_list(books)
                    print('\nEnter the Book ID to see more details, or return press <Enter>.\n')
                    book_id = int(input('Book ID: '))
                    while book_id:
                        keyword_in_book = False
                        for x in books:
                            if x.id == book_id:
                                keyword_in_book = True
                                print_book_detail(x)
                        if keyword_in_book is False:
                            print(f'The book with ID [{book_id}] does not have the keyword [{keyword}]')
                        print('\nTo view details enter the book ID, or return press <Enter>.')
                        book_id = int(input('Book ID: '))
            # Leave Program
            elif response == 5:
                print("Library saved")
                break
            else:
                print('\nInvalid input')
                print('Return press <Enter>')
                input()
        except:
            print('\nA possible error has occured or invalid input')
            print('Return press <Enter>')
            input()

app()