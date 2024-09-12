class Book:
    def __init__(self, title: str, author: str, book_id: int) -> None:
        self.title = title
        self.author = author
        self.book_id = book_id

    def get_title(self) -> str:
        return self.title

    def get_author(self) -> str:
        return self.author

    def get_book_id(self) -> int:
        return self.book_id

    def set_title(self, new_title: str) -> None:
        self.title = new_title

    def set_author(self, new_author: str) -> None:
        self.author = new_author

    def __str__(self) -> str:
        return f"Book: {self.title} by {self.author}, ID: {self.book_id}"

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Book):
            return self.book_id == other.book_id
        return False
