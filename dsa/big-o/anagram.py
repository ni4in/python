def anagram_sol0(word1, word2):
    for letter in word1:
        if letter not in word2:
            return False
    return True


def anagram_sol1(word1, word2):
    """here we will use checking off method to check if the leter from word1 is present in word2 and if present replaces by None

    Args:
        word1 (_type_): _description_
        word2 (_type_): _description_
    """
    pos1 = 0
    is_match = True
    while pos1 < len(word1) and is_match:
        is_continue = True
        pos2 = 0
        while pos2 < len(word2) and is_continue:
            if word1[pos1] == word2[pos2]:
                is_continue = False
                is_match = True
            else:
                pos2 += 1
                is_continue = True
                is_match = False
        pos1 += 1
    return is_match


def main():
    word1 = "python"
    word2 = "typhoz"
    print(anagram_sol1(word1, word2))


if __name__ == "__main__":
    main()
