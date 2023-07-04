from stack import Stack 
def in2post(symbol_str):
    op_prec = {}
    op_prec["("] = 1
    op_prec["+"] = 2
    op_prec["-"] = 2
    op_prec["*"] = 3
    op_prec["/"] = 3
    op_stack = Stack()
    postfix_str = []
    token_lst = symbol_str.split()
    for token in token_lst:
        if token in "ABCDEFGHIJKLMNOPRSTUVWXYZ" or token in "0123456789":
            postfix_str.append(token)
        elif token == "(":
            op_stack.push(token)
        elif token == ")":
            # if token is a right paranthesis we have to pop all the operators till it raches the left parenthesis
            top_item = op_stack.pop()
            while top_item != '(':
                postfix_str.append(top_item)
                top_item = op_stack.pop()
        else:
            # if token is an operator then push the operator to stack but make sure to flush out all the operators which have higher and equal precedence before pushing
            # Error handling should be done for checking the empty stack 
            while not op_stack.is_empty and op_prec[token] <= op_prec[op_stack.peek()]:
                    postfix_str.append(op_stack.pop()) 
            op_stack.push(token)
    # if the stack is not empty flush the remaining operators to the output
    while not op_stack.is_empty():
        postfix_str.append(op_stack.pop())
    return ''.join(postfix_str)

def main():
    # # str_symbol= ['( A + B ) * ( C * D )', 'A + B * C + D', 'A * B + C * D', 'A + B + C + D', '( A + B ) * C']
    # for symbol in str_symbol:
    #     print(f'postfix of {symbol} = {in2post(symbol)}')
    print(in2post('( A + B ) * ( C + D )'))

if __name__ == "__main__":
    main()
