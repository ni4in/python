"""
Create a function that takes any string as input and return the number of words for that string
"""


def get_number_of_words(string):
    return len((string.split(" ")))


print(f"Number of words is {get_number_of_words('Hello World')}")
