from new_student import Student


def main() -> None:
    """
    Test the Student dataclass.

    Tests basic student creation and attribute generation.

    Args:
        None

    Returns:
        None

    Raises:
        None
    """
    student = Student(name="Edward", surname="agle")
    print(student)


if __name__ == "__main__":
    main()
