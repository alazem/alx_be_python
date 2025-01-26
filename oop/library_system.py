class Book:
    def __init__(self, title, author):
        """
        Initialize a Book instance.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
        """
        self.title = title
        self.author = author

    def __str__(self):
        """
        Return a string representation of the Book.

        Returns:
            str: A string in the format 'Book: title by author'.
        """
        return f"Book: {self.title} by {self.author}"

class EBook(Book):
    def __init__(self, title, author, file_size):
        """
        Initialize an EBook instance.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
            file_size (int): The file size of the eBook in KB.
        """
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self):
        """
        Return a string representation of the EBook.

        Returns:
            str: A string in the format 'EBook: title by author, File Size: file_sizeKB'.
        """
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"

class PrintBook(Book):
    def __init__(self, title, author, page_count):
        """
        Initialize a PrintBook instance.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
            page_count (int): The number of pages in the book.
        """
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        """
        Return a string representation of the PrintBook.

        Returns:
            str: A string in the format 'PrintBook: title by author, Page Count: page_count'.
        """
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"

class Library:
    def __init__(self):
        """
        Initialize a Library instance with an empty list of books.
        """
        self.books = []

    def add_book(self, book):
        """
        Add a book to the library.

        Args:
            book (Book): An instance of Book, EBook, or PrintBook.
        """
        self.books.append(book)

    def list_books(self):
        """
        Print details of all books in the library.
        """
        for book in self.books:
            print(book)
