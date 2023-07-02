from stack import Stack

def dec2bin(num):
    bin_stack = Stack()
    quotient = num
    while quotient > 0:
        remainder = quotient % 2
        quotient = quotient//2
        bin_stack.push(remainder)
    bin_str = ''
    for __ in range(bin_stack.size()):
        bin_str+=str(bin_stack.pop())
    
    return bin_str


def main():
    num = 100
    print(dec2bin(num))

if __name__ == "__main__":
    main()
