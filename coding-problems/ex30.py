"""
Why is there an error in the code and how would you fix it
"""


def foo(a=1, b=2):
    return a + b


# x = foo - 1 # the foo function is called with out brakets


def foo_correct(a=1, b=2):
    return a + b


print(foo() - 1)
