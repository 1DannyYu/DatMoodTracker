def add_book(books, isbn, title, genre):
    books.append((isbn, title, genre))
    return books
def remove_book(books, isbn, title, genre):
    books.remove((isbn, title, genre))
    return books