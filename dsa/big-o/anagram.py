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
    






def main():
    word1 = 'python'
    word2 = 'tlphon'
    print(anagram_sol1(word1, word2))


if __name__== "__main__":
    main()