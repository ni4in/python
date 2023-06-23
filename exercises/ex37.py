"""
Create a function that takes a text file as input and returns the number of words contained in the text file. Please take into consideration that a comma can separate some words with no space. For example, "Hi, it's me." would need to be counted as three words. For your convenience, you can use the text file in the attachment.ˀ
"""


def advanced_word_counter(path):
    with open(path, "r", encoding="utf-8") as file:
        line = file.read()
        replaced_line = line.replace(",", " ")
        word_lst = replaced_line.split(" ")
        print(word_lst)
        return len(word_lst)


print(advanced_word_counter("resources/words2.txt"))
