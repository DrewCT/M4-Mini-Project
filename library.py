from book import Book
from user import User
from author import Author

books = []
users = []
authors = []

def add_book():
    title = input("Enter book title: ")
    author_name = input("Enter author name: ")
    genre = input("Enter genre: ")
    publication_date = input("Enter publication date (YYYY): ")
    book = Book(title, author_name, genre, publication_date)
    books.append(book)
    print(f"Book '{title}' added successfully!")

def display_books():
    if books:
        print("Books available in the library:")
        for book in books:
            print(book.display_details())
    else:
        print("No books available.")

def borrow_book():
    user_id = input("Enter user ID: ")
    title = input("Enter the title of the book to borrow: ")
    user = next((u for u in users if u.get_library_id() == user_id), None)
    book = next((b for b in books if b.get_title().lower() == title.lower()), None)
    if user and book:
        if user.borrow_book(book):
            print(f"Book '{title}' borrowed successfully by {user.get_name()}.")
        else:
            print(f"Sorry, the book '{title}' is currently unavailable.")
    else:
        print("User or Book not found.")

def return_book():
    user_id = input("Enter user ID: ")
    title = input("Enter the title of the book to return: ")
    user = next((u for u in users if u.get_library_id() == user_id), None)
    book = next((b for b in books if b.get_title().lower() == title.lower()), None)
    if user and book:
        user.return_book(book)
        print(f"Book '{title}' returned successfully.")
    else:
        print("User or Book not found.")

def add_user():
    name = input("Enter user name: ")
    library_id = input("Enter library ID: ")
    user = User(name, library_id)
    users.append(user)
    print(f"User '{name}' added successfully!")

def display_users():
    if users:
        print("Users in the system:")
        for user in users:
            print(user.view_details())
    else:
        print("No users available.")

def add_author():
    name = input("Enter author name: ")
    biography = input("Enter biography: ")
    author = Author(name, biography)
    authors.append(author)
    print(f"Author '{name}' added successfully!")

def display_authors():
    if authors:
        print("Authors in the system:")
        for author in authors:
            print(author.view_details())
    else:
        print("No authors available.")

def main_menu():
    while True:
        print("\nMain Menu:")
        print("1. Book Operations")
        print("2. User Operations")
        print("3. Author Operations")
        print("4. Quit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            book_menu()
        elif choice == "2":
            user_menu()
        elif choice == "3":
            author_menu()
        elif choice == "4":
            print("Exiting the system...")
            break
        else:
            print("Invalid option, please try again.")

def book_menu():
    while True:
        print("\nBook Operations:")
        print("1. Add a new book")
        print("2. Borrow a book")
        print("3. Return a book")
        print("4. Display all books")
        print("5. Back to Main Menu")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_book()
        elif choice == "2":
            borrow_book()
        elif choice == "3":
            return_book()
        elif choice == "4":
            display_books()
        elif choice == "5":
            break
        else:
            print("Invalid option, please try again.")

def user_menu():
    while True:
        print("\nUser Operations:")
        print("1. Add a new user")
        print("2. Display all users")
        print("3. Back to Main Menu")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_user()
        elif choice == "2":
            display_users()
        elif choice == "3":
            break
        else:
            print("Invalid option, please try again.")

def author_menu():
    while True:
        print("\nAuthor Operations:")
        print("1. Add a new author")
        print("2. Display all authors")
        print("3. Back to Main Menu")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_author()
        elif choice == "2":
            display_authors()
        elif choice == "3":
            break
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main_menu()