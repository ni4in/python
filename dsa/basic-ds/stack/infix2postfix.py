"""module for infix to postfix conversion"""
from stack import Stack


def infix2postfix(expr_str):
    """infix to postfix conversion

    Args:
        expr_str (_type_): _description_

    Returns:
        _type_: _description_
    """
    op_stack = Stack()
    out = []
    symbols = {"+": 1, "-": 1, "*": 2, "/": 2}
    operator_symbol = "+-*/"

    for item in expr_str:
        # print(f'item = {item}, stack = {op_stack.items}, out = {out}')
        if item in operator_symbol:
            if op_stack.is_empty():
                op_stack.push(item)
            elif symbols[op_stack.peek()] >= symbols[item]:
                for __ in range(op_stack.size()):
                    out.append(op_stack.pop())
                op_stack.push(item)
            else:
                op_stack.push(item)
        else:
            out.append(item)

    print(f"stack = {op_stack.items}, out = {out}")

    if not op_stack.is_empty():
        for __ in range(op_stack.size()):
            out.append(op_stack.pop())

    return "".join(out)


def main():
    str_symbs = ["A+B*C+D", "A*B+C*D", "A+B+C+D"]
    for symbol in str_symbs:
        print(infix2postfix(symbol))


if __name__ == "__main__":
    main()
