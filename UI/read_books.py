from BLL import book_controller
from helper import print_book_detail, print_book_list, book_id_req

def read_books():
    read_books = book_controller.get_all_read_books()
    print('\n   ==== Read Books ====\n')
    print_book_list(read_books)
    book_id = book_id_req()
    while book_id:           
        if book_id == '0':
            print("\n   ==== Read Books ====\n")
            print_book_list(read_books)
            book_id = book_id_req()
        else:
            for x in read_books:
                if x.id == int(book_id):
                    print_book_detail(x)
                    break
            book_id = book_id_req()