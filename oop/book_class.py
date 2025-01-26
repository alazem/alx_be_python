class Book:
    def __init__(self, title, author, year):
        """
        Constructor to initialize a Book instance.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
            year (int): The publication year of the book.
        """
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        """
        Destructor to handle deletion of a Book instance.
        Prints a message indicating the title of the book being deleted.
        """
        print(f"Deleting {self.title}")

    def __str__(self):
        """
        String representation of the Book instance.
        Returns:
            str: A human-readable string representation of the book.
        """
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """
        Official representation of the Book instance.
        Returns:
            str: A string that recreates the Book instance.
        """
        return f"Book('{self.title}', '{self.author}', {self.year})"
