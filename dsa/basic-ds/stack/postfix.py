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
    # print(token_lst)

    for token in token_lst:
        if token in "ABCDEFGHIJKLMNOPRSTUVWXYZ" or token in "0123456789":
            postfix_str.append(token)
        elif token == "(":
            op_stack.push(token)
        elif token == ")":
            n = op_stack.size()
            for __ in range(n):
                top_item = op_stack.pop()
                if top_item == "(":
                    break
                postfix_str.append(top_item)
        elif token in "*/+-":
            if op_stack.is_empty():
                op_stack.push(token)
            elif op_prec[token] <= op_prec[op_stack.peek()]:
                n = op_stack.size()
                for __ in range(n):
                    top_item = op_stack.peek()
                    if op_prec[top_item] >= op_prec[token]: 
                        postfix_str.append(op_stack.pop())
                op_stack.push(token)
            else:
                op_stack.push(token)
    if not op_stack.is_empty():
        n = op_stack.size()
        for __ in range(n):
            postfix_str.append(op_stack.pop())

    return ''.join(postfix_str)


def main():
    str_symbol= ['( A + B ) * ( C * D )', 'A + B * C + D', 'A * B + C * D', 'A + B + C + D', '( A + B ) * C']
    for symbol in str_symbol:
        print(f'postfix of {symbol} = {in2post(symbol)}')


    # print(f'postfix of {str_symbol[1]} = {in2post(str_symbol[1])}')


if __name__ == "__main__":
    main()
