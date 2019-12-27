import logging

from app import books


logger = logging.getLogger('scraping.menu')


USER_CHOICE = '''
Enter one of the following:

- 'b' to look at 5-star books
- 'c' to look at the cheapest books
- 'n' to just get the next available book on the catalogue
- 'q' to exit
'''


def print_best_books():
    logger.info('Finding best books by rating...')
    best_books = sorted(books, key=lambda x: x.rating * -1)[:8]
    for book in best_books:
        print(book)


def print_cheapest_books():
    logger.info('Finding best books by price...')
    cheapest_books = sorted(books, key=lambda x: x.price)[:8]
    for book in cheapest_books:
        print(book)


books_generator = (x for x in books)


def get_next_book():
    logger.info('Getting next book from generator of all books...')
    print(next(books_generator))


def menu():
    user_input = input(USER_CHOICE)
    while user_input != 'q':
        if user_input == 'b':
            print_best_books()
        elif user_input == 'c':
            print_cheapest_books()
        elif user_input == 'n':
            get_next_book()
        else:
            print('Please choose valid command')
        user_input = input(USER_CHOICE)
    logger.debug('Terminating program...')


menu()
