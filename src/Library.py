from typing import List, Optional
from Book import Book
from User import User

class Library:
    def __init__(self) -> None:
        self.books: List[Book] = []
        self.users: List[User] = []

    def add_book(self, book: Book) -> None:
        self.books.append(book)

    def remove_book(self, book_id: int) -> None:
        self.books = [book for book in self.books if book.get_book_id() != book_id]

    def add_user(self, user: User) -> None:
        self.users.append(user)

    def remove_user(self, user_id: int) -> None:
        self.users = [user for user in self.users if user.get_user_id() != user_id]

    def find_book_by_id(self, book_id: int) -> Optional[Book]:
        for book in self.books:
            if book.get_book_id() == book_id:
                return book
        return None

    def find_user_by_id(self, user_id: int) -> Optional[User]:
        for user in self.users:
            if user.get_user_id() == user_id:
                return user
        return None
