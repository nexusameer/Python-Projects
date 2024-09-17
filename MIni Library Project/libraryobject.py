from libraryclass import *

Ameer = Library(['Python', 'C sharp', 'C plus plus', 'Algorithm'], "Sir Sadiq Library")

while True:
    print(f"Welcome to the {Ameer.name} Library")
    print("\nSelect a choice:")
    print("1. Display Books")
    print("2. Lend a Book")
    print("3. Add a Book")
    print("4. Return a Book")
    choice1 = int(input('Enter a Choice='))

    if choice1 == 1:
        Ameer.display_books()
    
    elif choice1 == 2:
        user = input("Enter Your name: ")
        book = input("Enter a book for lend: ")
        Ameer.lend_book(user, book)
    
    elif choice1 == 3:
        book = input("Enter the book you want to add: ")
        Ameer.add_book(book)

    elif choice1 == 4:
        book = input("Enter the book you want to return: ")
        Ameer.return_b1ook(book)
