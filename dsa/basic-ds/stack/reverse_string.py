from stack import Stack

def rev_string(my_str):
    s=Stack()
    s.items = list(my_str)
    rev_list = []
    for index in range(s.size()):
        rev_list.append(s.pop())
    return ''.join(rev_list)

def main():
    my_str = "Hello"
    print(rev_string(my_str))

if __name__ == "__main__":
    main()
