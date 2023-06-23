"""
Create a script that generates a file where all letters of the English alphabet are listed three in each line. The inside of the text file would look like:

abc
def
ghi

and so on.

"""


import string

LETTERS = string.ascii_lowercase + " "


with open("resources/ex44.txt", "w", encoding="utf-8") as file:
    for x, y, z in zip(LETTERS[0::3], LETTERS[1::3], LETTERS[2::3]):
        file.write(x + y + z + "\n")
