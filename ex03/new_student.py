import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    """
    Generate a random 15-character ID.
    """
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    """
    Represents a student with name, surname, and auto-generated login and ID.
    """

    name: str
    surname: str
    active: bool = True
    login: str = field(init=False)
    id: str = field(init=False)

    def __post_init__(self) -> None:
        """
        Initialize non-initializable fields after dataclass initialization.
        """
        self.login = self.name[0].upper() + self.surname
        self.id = generate_id()


def main() -> None:
    """
    Test the Student dataclass.
    """


if __name__ == "__main__":
    main()
