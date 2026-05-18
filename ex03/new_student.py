import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    """
    Generate a random 15-character ID.

    Creates a random string consisting of lowercase ASCII letters.

    Args:
        None

    Returns:
        str: A random 15-character string of lowercase letters.

    Raises:
        None
    """
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    """
    Represents a student with name, surname, and auto-generated login and ID.

    Attributes:
        name (str): The student's first name.
        surname (str): The student's last name.
        active (bool): Whether the student is active (default: True).
        login (str): Auto-generated login from name and surname (not initializable).
        id (str): Auto-generated random ID (not initializable).
    """

    name: str
    surname: str
    active: bool = True
    login: str = field(init=False)
    id: str = field(init=False)

    def __post_init__(self) -> None:
        """
        Initialize non-initializable fields after dataclass initialization.

        Generates login from first letter of name + surname (capitalized)
        and creates a random ID using generate_id().

        Args:
            None

        Returns:
            None

        Raises:
            None
        """
        self.login = self.name[0].upper() + self.surname
        self.id = generate_id()


def main() -> None:
    """
    Test the Student dataclass.

    Args:
        None

    Returns:
        None

    Raises:
        None
    """
    pass


if __name__ == "__main__":
    main()
