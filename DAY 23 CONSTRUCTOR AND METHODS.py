class Book:
    def __init__(self, title, author): 
        self.title = title 
        self.author = author
    
    def display_info(self):
        print(f"Title: {self.title}")
        print (f"Author: {self.author}")
    
# CREATE BOOK
book1 = Book("To Kill a Mockingbird", "Harper Lee")
book1.display_info()
    