def anagram_sol0(word1, word2):
    for letter in word1:
        if letter not in word2:
            return False
    return True

def anagram_sol1(word1, word2_list):
    """here we will use checking off method to check if the leter from word1 is present in word2 and if present replaces by None 

    Args:
        word1 (string): first word
        word2 (string): second word
    """
    word2_list = list(word2_list)
    index1=0
    is_anagram = True
    while index1 < len(word1) and is_anagram:
        index2=0
        is_continue = True
        while index2 < len(word2_list) and is_continue:
            if word1[index1] == word2_list[index2]:
                # to make sure that if repeating letters will be handeled
                word2_list[index2] = None 
                is_anagram = True
                is_continue = False
            else:
                is_anagram = False
                is_continue = True
                index2+=1
        index1+=1
    return is_anagram

def anagram_sol2(word1, word2):
    word1_list = list(word1)
    word2_list = list(word2)
    word1_list.sort()
    word2_list.sort()
    index=0
    while index < len(word1_list):
        if word1_list[index] != word2_list[index]:
            return False
        index+=1
    return True

def anagram_sol4(word1,word2):
    counter1 = [0]*26
    counter2 = [0]*26
    offset = ord('a')
    for letter in word1:
        counter1[ord(letter)-offset]+=1
    for letter in word2:
        counter2[ord(letter)-offset]+=1
    for index in range(26):
        if counter1[index] != counter2[index]:
            return False
    return True



def main():


if __name__== "__main__":
    main()