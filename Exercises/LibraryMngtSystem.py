## Write a Library class with no_of_books and books as two instance variables.
# Write a program to create a Library from this Library class and show how you can print all books using different methods.
# Show that your program doesn't persist the books after the program is stopped.

##------------ Code -----------#
class Library :
    def __init__(self):
        self.no_of_books = 0
        self.books = []
        
    def books(self) :
        return self.no_of_books
    
    def addBook(self, book) :
        self.books.append(book)
        self.no_of_books = len(self.books)
    
    def showInfo(self) :
        print(f"The library has {self.no_of_books} book/s.")
        for book in self.books:
            print(book)
    
l1 = Library()
l1.addBook("Harry Potter")
l1.showInfo()