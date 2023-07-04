""" module that converts a decimal to any base via using stack """
from stack import Stack


def dec2base(num, base):
    """converting a decimal number to any base

    Args:
        num (_type_): _description_
        base (_type_): _description_

    Returns:
        _type_: _description_
    """
    digits = "0123456789ABCDEF"
    bin_stack = Stack()
    quotient = num
    while quotient > 0:
        remainder = quotient % base
        quotient = quotient // base
        bin_stack.push(remainder)
    bin_str = ""
    for __ in range(bin_stack.size()):
        bin_str += str(digits[bin_stack.pop()])

    return bin_str


def main():
    """_summary_"""
    num = 255
    base = 16
    print(dec2base(num, base))


if __name__ == "__main__":
    main()
