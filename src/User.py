class User:
    def __init__(self, name: str, user_id: int) -> None:
        self.name = name
        self.user_id = user_id

    def get_name(self) -> str:
        return self.name

    def get_user_id(self) -> int:
        return self.user_id

    def set_name(self, new_name: str) -> None:
        self.name = new_name

    def __str__(self) -> str:
        return f"User: {self.name}, ID: {self.user_id}"

    def __eq__(self, other: object) -> bool:
        if isinstance(other, User):
            return self.user_id == other.user_id
        return False
