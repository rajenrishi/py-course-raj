# Assignment: 53
# Write a Python class named Library. Add an instance method to display the
# book details: Book name, Author, Genre (Eg: Comedy, Kids), Published Year (1999, 2000).
# Pass the above book details when creating book object.
# Use a class variable to maintain the count of number of books added.
# Add a class method to display number of books.


class Library:
    # Class variable to hold number of books in library
    total_books = 0

    def __init__(self, bk_name, bk_author, bk_genre, bk_pub_yr):
        self.bk_name = bk_name
        self.bk_author = bk_author
        self.bk_genre = bk_genre
        self.bk_pub_yr = bk_pub_yr
        Library.total_books = Library.total_books + 1

    @classmethod
    def disp_books_count(cls):
        print("Total number of books in the library are: ", cls.total_books)


# Add three books
b1_lib = Library("book1", "book_author1", "books_genre1", 2001)
b2_lib = Library("book2", "book_author2", "books_genre2", 2002)
b3_lib = Library("book3", "book_author3", "books_genre3", 2003)

# Display number of books
Library.disp_books_count()
