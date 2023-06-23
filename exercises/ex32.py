"""
what will be the following output 
"""

c = 1


def foo():
    c = 2
    return c


c = 3
print(foo())  # the variable has a value inside the function scope
