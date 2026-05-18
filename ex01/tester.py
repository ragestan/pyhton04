from in_out import outer, square, pow as ft_pow


def main() -> None:
    """
    Test the outer function with square and pow functions.

    Args:
        None

    Returns:
        None

    Raises:
        None
    """
    my_counter = outer(3, square)
    print(my_counter())
    print(my_counter())
    print(my_counter())
    print("---")
    another_counter = outer(1.5, ft_pow)
    print(another_counter())
    print(another_counter())
    print(another_counter())


if __name__ == "__main__":
    main()
