"""
Create a script that generates a file where all letters of the English alphabet are listed two in each line. The inside of the text file would look like:

ab
cd
ef

and so on.
"""
import string

# index = ord("a")
# for i in range(0, 26, 2):
#     print(f"{chr(index+i)+chr(index+i+1)}")

# solution 2 using zip

with open("resources/ex43.txt", "w", encoding="utf-8") as file:
    for x, y in zip(string.ascii_lowercase[0::2], string.ascii_lowercase[1::2]):
        file.write(x + y+'\n')
