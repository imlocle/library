from BLL import book_controller
from helper import print_book_detail, print_book_list, book_id_req

def view_all_books():
    print("\n   ==== View All Books ====\n")
    all_books = book_controller.get_all_books()
    if len(all_books) < 1:
        print("There are no books. Please add some.")
    else:
        print_book_list(all_books)
        book_id = book_id_req()
        while book_id:
            if book_id == '0':
                print("\n   ==== View All Books ====\n")
                print_book_list(all_books)
                book_id = book_id_req()
                print('\nPress <0> to view all books')
            else:
                for x in all_books:
                    if x.id == int(book_id):
                        print_book_detail(x)
                        break
                print('\nPress <0> to view all books')
                book_id = book_id_req()