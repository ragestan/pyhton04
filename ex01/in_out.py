from typing import Callable


def square(x: int | float) -> int | float:
    """
    Calculate the square of a number.

    Args:
        x (int | float): The number to square.

    Returns:
        int | float: The square of x.

    Raises:
        None
    """
    return x * x


def pow(x: int | float) -> int | float:
    """
    Calculate a number raised to itself.

    Args:
        x (int | float): The number to raise to itself.

    Returns:
        int | float: x raised to the power of x.

    Raises:
        None
    """
    return x ** x


def outer(x: int | float, function: Callable) -> Callable:
    """
    Create a closure that applies a function to x repeatedly.

    Returns an inner function that maintains state of x and applies
    the given function to it each time inner() is called. After each
    call, x is updated to the result of the function application.

    Args:
        x (int | float): Initial value for the calculation.
        function (Callable): Function to apply to x.

    Returns:
        Callable: An inner function that applies function to x and
                  updates x for the next call.

    Raises:
        None
    """
    count = 0

    def inner() -> float:
        """
        Apply the function to x and update x for next call.

        Maintains state across multiple calls using nonlocal x.
        Each invocation returns the result of function(x) and
        updates x to that result.

        Args:
            None

        Returns:
            float: Result of applying function to x.

        Raises:
            None
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
