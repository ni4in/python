from timeit import Timer

def func_lin():
    """O(n) linear function

    Args:
        lst (_type_): _description_
    """
    for i in range(100):
        


def main():
    t1 = Timer("func_lin()","from __main__ import func_lin")
    print(f"Linear compute for {t1.timeit(number=10000)} milliseconds")

if __name__ == "__main__":
    main()