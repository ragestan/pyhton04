from typing import Any, Callable


def callLimit(limit: int) -> Callable:
    """
    Decorator that limits the number of times a function can be called.
    """
    count = 0

    def callLimiter(function: Callable) -> Callable:
        """
        Decorator that limits calls to a function.
        """
        def limit_function(*args: Any, **kwargs: Any) -> Any:
            """
            Execute function if call limit not reached.
            """
            nonlocal count
            if count < limit:
                count += 1
                return function(*args, **kwargs)
            else:
                print(f"Error: {function} call too many times")

        return limit_function

    return callLimiter


def main() -> None:
    """
    Test the callLimit decorator with sample functions.
    """


if __name__ == "__main__":
    main()
