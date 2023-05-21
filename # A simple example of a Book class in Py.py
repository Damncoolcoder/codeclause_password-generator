# A simple example of a Book class in Python

# Define the Book class
class Book:
    # Initialize the attributes of the book
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = True # A book is available by default

    # Define a method to display the book information
    def display(self):
        print("Title:", self.title)
        print("Author:", self.author)
        print("ISBN:", self.isbn)
        print("Available:", self.available)

    # Define a method to borrow the book
    def borrow(self):
        # Check if the book is available
        if self.available:
            # Set the availability to False
            self.available = False
            print("You have borrowed the book:", self.title)
        else:
            # Print an error message if the book is not available
            print("Sorry, the book is not available.")

    # Define a method to return the book
    def return_book(self):
        # Check if the book is not available
        if not self.available:
            # Set the availability to True
            self.available = True
            print("You have returned the book:", self.title)
        else:
            # Print an error message if the book is already available
            print("You cannot return a book that is already available.")
