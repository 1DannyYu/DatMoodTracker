import library

books = [(9780007348695, 'The Cat In The Hat', 'Fiction - Children'),
        (9780747532699, "Harry Potter and the Philosopher's Stone", 'Fiction - Children')]

books = library.add_book(books, 9780520201798, 'Frankenstein', 'Fiction - Horror')
books = library.remove_book(books, 9780007348695, 'The Cat In The Hat', 'Fiction - Children')
print(books)