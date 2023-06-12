"""
Write a python function that takes a text file as input and returns the number of words contained in the file
"""


with open("resources/words1.txt", "r", encoding="utf-8") as file:
    line = file.read()
    words_no = len(line.split(" "))
    print(words_no)
