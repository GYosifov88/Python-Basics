needed_book = input()
is_needed_book_found = False
number_of_checked_books = 0
current_book = input()
while current_book != 'No More Books':

    if current_book == needed_book:
        is_needed_book_found = True
        break

    number_of_checked_books += 1
    current_book = input()

if is_needed_book_found:
    print(f'You checked {number_of_checked_books} books and found it.')
else:
    print('The book you search is not here!')
    print(f'You checked {number_of_checked_books} books.')