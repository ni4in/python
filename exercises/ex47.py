"""
Create a script that iterates through text files(in 'resources/letters') and checks if strings p, y, t, h, o, or n are found in the text file's content. If any of those strings is found, append that string to a list.
"""

from pathlib import Path

PATH = "resources/letters"
STR = "python"

if not Path(PATH).exists():
    print("Directory didnt exists")

files = sorted(Path(PATH).glob("*.txt"))

lst = []
for file in files:
    with open(file, "r", encoding="utf-8") as txt:
        letter = txt.read().strip("\n")
        if letter in STR:
            lst.append(letter)

print(lst)
