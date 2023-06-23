#Apply functions to dictionary items

from functools import reduce 
d = {"a": 1, "b": 2, "c": 3}

print(sum(d.values()))

print(reduce(lambda a,b:a+b, d.values()))

print(sum([1,2,3]))