import time
from timeit import Timer


def sum_n():
    """_summary_

    Returns:
        _type_: _description_
    """
     = 0
    start = time.time()
    for i in range(100):
        sum += i
    end = time.time()
    return end - start


def main():
    """_summary_"""
    print(f"the time takes for sum of n is {sum_n()}")
    # using timeit module
    iterations = 1000
    times = Timer("linear_func", "from __main__ import linear_func")
    print(
        f"the average compute time for {iterations} iterations is {times.timeit(number=iterations)} milliseconds"
    )


if __name__ == "__main__":
    main()
