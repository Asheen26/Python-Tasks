class Book:
    def __init__(self,title,author,isbn):
        self.title=title
        self.author=author
        self.isbn=isbn


class library(Book):
    def __init__(self):
        self.books=[]
        
        
    def add_book(self,book):
        self.books.append(book)
        print(f"Book {book.title} added to library")

    def remove_book(self,isbn):
        for book in self.books:
            if book.isbn==isbn:
                self.books.remove(book)  
                return(f"Book {book.title} removed") 
            else:
                return(f"Book not available to remove")

    def search_book_by_title(self,title):
        for book in self.books:
            if book.title==title:
                return(f"Book {book.title} by {book.author}, {book.isbn} is available") 
            else:
                return("Not available")
        



book1 = Book("Python Programming", "Vini", "0001")
book2 = Book("Django", "Rodrygo", "0002")
book3 = Book("Views", "Fede", "0003")

lib=library()
lib.add_book(book1)
lib.add_book(book2)
lib.add_book(book3)
r=lib.remove_book("0003")
print(r)

s=lib.search_book_by_title("Python Programming")
print(s)


        
                


