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
            print(op_stack.items)
        elif token == ")":
            for __ in range(op_stack.size()):
                top_item = op_stack.pop()
                if top_item == "(":
                    break
                postfix_str.append(top_item)
        elif token in "*/+-":
            if op_stack.is_empty():
                op_stack.push(token)
            if op_prec[token] <= op_prec[op_stack.peek()]:
                for __ in range(op_stack.size()):
                    top_item = op_stack.peek()
                    if top_item == "(":
                        break
                    postfix_str.append(top_item)

    return postfix_str, op_stack.items


x, y = in2post("( A + B ) * C")
print(x, y)
