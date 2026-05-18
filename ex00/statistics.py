from typing import Any


def ft_statistics(*args: Any, **kwargs: Any) -> None:
    """
    Calculate and display statistics for given data.
    """
    if not args:
        for key in kwargs.keys():
            print("ERROR")
        return

    data = sorted([float(x) for x in args])
    n = len(data)

    results = {}

    for key, stat_type in kwargs.items():
        try:
            if stat_type == "mean":
                mean_val = sum(data) / n
                results["mean"] = f"mean : {mean_val}"
            elif stat_type == "median":
                if n % 2 == 0:
                    median_val = (data[n // 2 - 1] + data[n // 2]) / 2
                else:
                    median_val = data[n // 2]
                results["median"] = f"median : {median_val}"
            elif stat_type == "quartile":
                # 25th percentile (Q1)
                q1_idx = int(n * 0.25)
                q1 = data[q1_idx]
                # 75th percentile (Q3)
                q3_idx = int(n * 0.75)
                q3 = data[q3_idx]
                results["quartile"] = f"quartile : [{q1}, {q3}]"
            elif stat_type == "std":
                mean_val = sum(data) / n
                variance = sum((x - mean_val) ** 2 for x in data) / n
                std_val = variance ** 0.5
                results["std"] = f"std : {std_val}"
            elif stat_type == "var":
                mean_val = sum(data) / n
                variance = sum((x - mean_val) ** 2 for x in data) / n
                results["var"] = f"var : {variance}"
        except (ValueError, ZeroDivisionError):
            print("ERROR")

    for value in results.values():
        print(value)


def main() -> None:
    """
    Main function
    """


if __name__ == "__main__":
    main()
