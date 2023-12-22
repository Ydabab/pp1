class EBook():
    def __init__(self, title, author, number_of_pages, current_page):
        self.title = title
        self.author = author
        self.number_of_pages = number_of_pages
        self.current_page = current_page
        self.is_open = False
    def book_status(self):
        print(f"Title: {self.title}\nAuthor: {self.author}\nNumber of pages: {self.number_of_pages}\nCurrent page: {self.current_page}")
    def open_book(self):
        self.is_open = True
    def close_book(self):
        self.is_open = False
    def read_book(self, pages):
        if self.is_open == True:
            self.current_page = self.current_page + pages
        else:
            print("Book is closed")

book = EBook("Harry Potter", "JK Rowling", 300, 83)
book.open_book()
book.book_status()
book.read_book(9)
book.book_status()
book.close_book()
book.read_book(3)