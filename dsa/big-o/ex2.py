import time 
from timeit import Timer
    
def sum_of_n(n):
    total = 0
    for i in range(n):
        total+=i
    return total

def main():
    print(f"the time takes for linear_func is {linear_func()}")
    #using timeit module 
    n = 1000
    t1 = Timer("linear_func", "from __main__ import linear_func")
    print(f"the average compute time for {n} iterations is {t1.timeit(number=n)} milliseconds")

if __name__ == "__main__":
    main()
