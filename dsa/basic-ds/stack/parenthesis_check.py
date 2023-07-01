from stack import Stack 

def para_check(symbol_str):
    para_stack = Stack()
    for symbol in symbol_str:       
        if symbol == "(":
            para_stack.push("(")
        elif symbol == ")":
            para_stack.pop()
        elif para_stack.is_empty:
            break
        else:
            pass
        
    if para_stack.is_empty():
        return f"unbalanced symbol"
    else:
        return f"balanced symbol"

def para_check_general(symbol_str):
    open_symbol = {'(':0, '[':1, '{':2}
    close_symbol = {')':0, ']':1, '}':2}
    para_stack = Stack()
    is_check = True
    index = 0
    while index < len(symbol_str) and is_check:
        print(para_stack.items, is_check, index)
        symbol = symbol_str[index]
        if symbol in open_symbol.keys():
            para_stack.push(symbol)
        elif symbol in close_symbol.keys():
            if para_stack.is_empty():
                print("empty but symbol exists")
                is_check = False
            elif open_symbol[para_stack.peek()] != close_symbol[symbol]:
                print("not same loop")
                is_check = False 
            else:
                para_stack.pop()
        index+=1
        
    if para_stack.is_empty() and is_check:
        return f"balanced"
    else:
        return f"unbalanced"
        
def main():
    symbol = "[([]{})"
    print(para_check_general(symbol))

if __name__ == "__main__":
    main()