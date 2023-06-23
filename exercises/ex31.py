"""
what will be the following script output.
"""
c = 1


def foo():
    return c


c = 3
print(
    foo()
)  # will check for the name within function scope and will look at global scope if didnt find inside the function scope
