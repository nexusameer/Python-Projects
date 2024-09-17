class Library:
    def __init__(self, book_list, name):
        """
        Initialize the Library with a list of books and a name.
        """
        self.book_list = book_list
        self.name = name
        self.lend_dict = {}

    def display_books(self):
        """
        Display the list of books in the library.
        """
        print("We have the following books in our library:")
        for book in self.book_list:
            print(book)

    def lend_book(self, user, book):
        """
        Lend a book to a user if it is available.
        """
        if book in self.book_list:
            if book not in self.lend_dict:
                self.lend_dict[book] = user
                print("Book has been lent to", user)
                self.book_list.remove(book)
            else:
                print(f"Book is already borrowed by {self.lend_dict[book]}")
        else:
            print("Book not available in the library")

    def add_book(self, book):
        """
        Add a book to the library.
        """
        self.book_list.append(book)
        print("Book has been added successfully")

    def return_book(self, book):
        """
        Return a book to the library.
        """
        if book in self.lend_dict:
            user = self.lend_dict.pop(book)
            self.book_list.append(book)
            print(f"Book returned by {user}")
        else:
            print("Book was not borrowed from this library")


# Example Usage
library = Library(["Book1", "Book2", "Book3"], "My Library")
library.display_books()

library.lend_book("User1", "Book1")
library.display_books()

library.return_book("Book1")
library.display_books()
