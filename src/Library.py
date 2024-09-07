from src.Book import Book
from src.User import User


class Library:
    def __init__(self):
        self.__books = []
        self.__users = []
        self.__checked_out_books = []
        self.__checked_in_books = []

    # Getters
    def get_books(self):
        return self.__books

    def get_users(self):
        return self.__users

    def get_checked_out_books(self):
        return self.__checked_out_books

    def get_checked_in_books(self):
        return self.__checked_in_books

    # 1.1 Add Book
    def add_book(self, isbn, title, author):
        book = Book(isbn, title, author)
        self.__books.append(book)

    # 1.2 List All Books
    def list_all_books(self):
        for book in self.__books:
            print(book)

    # 2.1 Check out book
    def check_out_book(self, isbn, dni, due_date):
        # Verificar que el libro esté en la biblioteca
        book = next((b for b in self.__books if b.get_isbn() == isbn), None)
        if not book:
            return f"Unable to find the data for the values: ISBN {isbn} and DNI: {dni}"

        # Verificar que el usuario esté registrado
        user = next((u for u in self.__users if u.get_dni() == dni), None)
        if not user:
            return f"Unable to find the data for the values: ISBN {isbn} and DNI: {dni}"

        # Verificar que el libro esté disponible
        if not book.is_available():
            return f"Book {isbn} is not available"

        # Registrar el préstamo
        book.set_available(False)
        self.__checked_out_books.append([isbn, dni, due_date])
        user.increment_checkouts()
        return f"User {dni} checked out book {isbn}"

    # 2.2 Check in book
    def check_in_book(self, isbn, dni, returned_date):
        # Verificar que el libro esté en la biblioteca
        book = next((b for b in self.__books if b.get_isbn() == isbn), None)
        if not book:
            return f"Book {isbn} is not available"

        # Verificar que el libro esté en préstamo
        checked_out = next((entry for entry in self.__checked_out_books if entry[0] == isbn), None)
        if not checked_out:
            return f"Book {isbn} is not available"

        # Registrar la devolución
        book.set_available(True)
        self.__checked_out_books.remove(checked_out)
        self.__checked_in_books.append([isbn, dni, returned_date])
        user = next((u for u in self.__users if u.get_dni() == dni), None)
        if user:
            user.increment_checkins()
        return f"Book {isbn} checked in by user {dni}"

    # Utils
    def add_user(self, dni, name):
        self.__users.append(User(dni, name))
