"""
Create a script that generates a text file with all letters of the English alphabet inside it, one letter per line.
"""
import string

index = ord("a")

with open("resources/alphabet.txt", "w", encoding="utf-8") as file:
    for i in range(26):
        file.write(chr(index + i) + "\n")


# a second solution is by using string module

with open("resources/alphabet2.txt", "w", encoding="utf-8") as file:
    for alphabet in string.ascii_lowercase:
        file.write(alphabet + "\n")
