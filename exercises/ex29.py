'''
why do you get an error and how would you fix it
'''

def foo(a=2,b):  # non default argument follows default argument 
    return a+b

def foo_correct(b, a=2):
    return a+b

