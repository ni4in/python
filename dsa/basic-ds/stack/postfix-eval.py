from stack import Stack

def postfix_eval(post_str):
    post_str_list = post_str.split()
    mul_stack = Stack()
    
    for token in post_str_list:
        if token in '0123456789':
            mul_stack.push(int(token))
        else:
            operand2 = mul_stack.pop()
            operand1 = mul_stack.pop()
            result = do_math(token, operand1, operand2)
            mul_stack.push(result)
        return mul_stack.pop()


def do_math(op, op1, op2):    
    if op == '+':
        return op1+op2
    elif op == '-':
        return op1 - op2
    elif op == '*':
        return op1*op2
    elif op == '/':
        return op1/op2
    else:
        raise Exception("Unknown Operator")

def main():
    #make sure you give space seperated symbols
    symbol = '7 8 + 3 2 + /'   
    print(postfix_eval(symbol))
    try:
        do_math('%',4,2)
    except:
        print(4%2)


if __name__ == "__main__":
    main()