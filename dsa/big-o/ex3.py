from timeit import Timer


def sum_of_n(n=100):
    """sum to n numbers

    Args:
        n (_type_): _description_

    Returns:
        _type_: _description_
    """
    return n * (n + 1) / 2


def main():
    """main function"""
    iterations = 1000
    times = Timer("sum_of_n", "from __main__ import sum_of_n")
    print(
        f"average time for {1000} iterations is {times.timeit(number=iterations)} milliseconds "
    )


if __name__ == "__main__":
    main()
