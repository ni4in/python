#Ranges of strings

my_range = range(1,21)


print(list(map(str,my_range)))



my_list = list(my_range)

print(list(map(lambda x:x**2, my_list)))


def even(x):
    if x%2 == 0:
        return True
    else:
        return False
    

print(list(filter(even,my_list)))

from functools import reduce

max_fun = lambda a,b:a if a>b else b

f = [1,2,1,3,2]

print((reduce(max_fun,f)))