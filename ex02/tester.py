from callLimit import callLimit


@callLimit(3)
def f() -> None:
    """Test function f with limit of 3 calls."""
    print("f()")


@callLimit(1)
def g() -> None:
    """Test function g with limit of 1 call."""
    print("g()")


def main() -> None:
    """
    Test the callLimit decorator.

    Args:
        None

    Returns:
        None

    Raises:
        None
    """
    for i in range(3):
        f()
        g()


if __name__ == "__main__":
    main()
