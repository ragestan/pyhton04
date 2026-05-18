from typing import Callable


def square(x: int | float) -> int | float:
    """
    Calculate the square of a number.
    """
    return x * x


def pow(x: int | float) -> int | float:
    """
    Calculate a number raised to itself.
    """
    return x ** x


def outer(x: int | float, function: Callable) -> Callable:
    """
    Create a closure that applies a function to x repeatedly.
    """
    count = 0

    def inner() -> float:
        """
        Apply the function to x and update x for next call.
        """
        nonlocal x, count
        result = function(x)
        x = result
        count += 1
        return result

    return inner


def main() -> None:
    """
    Test the outer function with square and pow functions.
    """


if __name__ == "__main__":
    main()
