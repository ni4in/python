"""
Please use the 'resources/company1.json' file and use Python to print out its content.
"""

import json

with open("resources/company1.json", "r", encoding="utf-8") as file:
    data = json.load(file)

print(data)
