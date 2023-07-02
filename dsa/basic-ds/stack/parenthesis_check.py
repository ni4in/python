from stack import Stack 


def para_check(symbol_str):
    """Paranthesis checker for : [,(,{,})] 

    Args:
        symbol_str (_type_): string with symbols

    Returns:
        _type_: string literal
    """
    # creating symbol templates and the key - value pairs
    open_symbol = {'(':0, '[':1, '{':2}
    close_symbol = {')':0, ']':1, '}':2}
    # initialising the stack
    para_stack = Stack()
    #to check the unbalance condition during symbol iteration and exit the loop is exists 
    is_check = True
    index = 0
    while index < len(symbol_str) and is_check:
        symbol = symbol_str[index]
        #checking for opening symbols
        if symbol in open_symbol.keys():
            para_stack.push(symbol)
        #checking for closing symbols
        elif symbol in close_symbol.keys():
            # check is stack is empty and still a close symbol exists resulting in unbalance
            if para_stack.is_empty():
                # exit the loop if exists
                is_check = False
            # check if the closing symbol is equal to opening symbol , if not, exit the loop
            elif close_symbol[symbol] != open_symbol[para_stack.peek()] :
                is_check = False 
            else:
                # if both of the above condition fails, then there is a balance exists and pop out the symbol
                para_stack.pop()
        else:
            pass
        index+=1
    # to check if the stack is empty and check the balance flag 
    if para_stack.is_empty() and is_check:
        return f"balanced"
    else:
        return f"unbalanced"
        
def main():
    symbol = "A(B(C(D)E)F}"
    print(para_check(symbol))

if __name__ == "__main__":
    main()