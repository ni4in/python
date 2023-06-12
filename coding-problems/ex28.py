"""
why there is an error in the code and how we can fix it
"""


def foo(a, b):
    print(a + b)


x = (
    foo(2, 3) * 10
)  # this is producing None*10 because the return from the function is None
