import time 
from timeit import Timer
    
def linear_func():
    sum = 0
    start = time.time()
    for i in range(100):
        sum+=i
    end = time.time()
    return end-start 

def main():
    print(f"the time takes for linear_func is {linear_func()}")
    #using timeit module 
    n = 1000
    t1 = Timer("linear_func", "from __main__ import linear_func")
    print(f"the average compute time for {n} iterations is {t1.timeit(number=n)} milliseconds")

if __name__ == "__main__":
    main()
