
from pathlib import Path

PATH = "resources/letters/"

files = Path(PATH)
txt_files = list(files.glob('*.txt'))
print(txt_files[0].name)
letters = []
for file in txt_files:
    with open(PATH+file.name, "r", encoding="utf-8") as text_file:
        letters.append(text_file.read().strip("\n"))

letters.sort()
print(letters)
