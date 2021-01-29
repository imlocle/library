from BLL import book_controller
from UI import view_all_books, read_books
from helper import print_book_detail, input_book_details, print_book_search, print_book_list

def menu():
    print("""
    ==== Book Manager ====\n
    1. View All Books
    2. Add A New Book
    3. Edit A Book
    4. Search Books Using Keywords
    5. Read Books
    6. Save and Exit  
    """)

def app():
    while True:
        try:
            menu()
            response = int(input("Choose [1-6]: "))
            # View All
            if response == 1:
                view_all_books.view_all_books()
            # Add Book
            elif response == 2:
                print("\n   ==== Add A New Books ====\n")
                print('Please enter the following information:')
                title, author, description, read = input_book_details()
                book_controller.add_new_book(title, author, description, read)
                print(f"\n{title} by {author} is Saved!")
                print('Return press <Enter>')
                input()
            # Edit Book
            elif response == 3:
                print("\n   ==== Edit A Book ====\n")
                print("Here are the available books:\n")
                for x in book_controller.get_all_books():
                    print_book_search(x)
                print('\nEnter the Book ID of the book you want to edit, or return press <Enter>.')
                book_id = input('Book ID: ')
                if book_id:
                    update_book = book_controller.search_book_id(book_id)
                    print('Input the following information. To leave a field unchanged, hit <Enter>')
                    print_book_detail(update_book)
                    title, author, description, read = input_book_details()
                    if read == '':
                        read = update_book.read
                    update_book = book_controller.update_book(book_id, title, author, description, read)
                    print_book_detail(update_book)
                    print('\nBook is updated!')
                    print('Return press <Enter>')
                    input()
            # Search with Keyword
            elif response == 4:
                print("\n   ==== Search ====\n")
                print('Please type in a keyword')
                keyword = input('Search: ')
                books = book_controller.search_books_keyword(keyword)
                if len(books) < 1:
                    print(f'\nThere are no books with keyword: [{keyword}]')
                else:
                    print(f'\nThe following books matched your keyword: [{keyword}]\n')
                    print_book_list(books)
                    print('\nEnter the Book ID to see more details, or return press <Enter>.\n')
                    book_id = input('Book ID: ')
                    while book_id:
                        keyword_in_book = False
                        for x in books:
                            if x.id == int(book_id):
                                keyword_in_book = True
                                print_book_detail(x)
                        if keyword_in_book is False:
                            print(f'The book with ID [{book_id}] does not have the keyword [{keyword}]')
                        print('\nTo view details enter the book ID, or return press <Enter>.')
                        book_id = input('Book ID: ')
            # Read Books
            elif response == 5:
                read_books.read_books()
            elif response == 6:
                print("Library saved")
                break
            else:
                print('\nInvalid input')
                print('Return press <Enter>')
                input()
        except Exception as ex:
            print('\nA possible error has occured or invalid input')
            print('Return press <Enter>')
            #print(ex)
            input()

app()