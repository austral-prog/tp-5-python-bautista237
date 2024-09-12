class Library:
    def __init__(self) -> None:
        self.books = []
        self.users = []

    def add_book(self, book: Book) -> None:
        self.books.append(book)

    def remove_book(self, book_id: int) -> None:
        self.books = [book for book in self.books if book.get_book_id() != book_id]

    def add_user(self, user: User) -> None:
        self.users.append(user)

    def remove_user(self, user_id: int) -> None:
        self.users = [user for user in self.users if user.get_user_id() != user_id]

    def find_book_by_id(self, book_id: int) -> Book | None:
        for book in self.books:
            if book.get_book_id() == book_id:
                return book
        return None

    def find_user_by_id(self, user_id: int) -> User | None:
        for user in self.users:
            if user.get_user_id() == user_id:
                return user
        return None
