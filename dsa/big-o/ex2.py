import time
from timeit import Timer


def sum_of_n(n):
    """sum to total numbers

    Returns:
        _type_: _description_
    """
    total = 0
    for i in range(n):
        total += i
    return total


def main():
    """main function"""
    # using timeit module
    iterations = 1000
    times = Timer("linear_func", "from __main__ import linear_func")
    print(
        f"the average compute time for {iterations} iterations is {times.timeit(number=iterations)} milliseconds"
    )


if __name__ == "__main__":
    main()
