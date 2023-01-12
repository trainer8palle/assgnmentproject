import sys


def make_num(num,func):
    if func == None:
        return num
    else:
        return func(num)


def zero(func= None):
    return make_num(0,func)


def one(func= None):
    return make_num(1,func)


def two(func= None):
    return make_num(2, func)


def three(func= None):
    return make_num(3,func)


def four(func= None):
    return make_num(4,func)


def five(func= None):
    return make_num(5,func)


def six(func= None):
    return make_num(6,func)


def seven(func = None):
    return make_num(7, func)


def eight(func=None):
    return make_num(8, func)

def nine(func= None):
    return make_num(9, func)

def times(right):
  sum = lambda left :  left * right
  return  sum

print(seven(times(eight())))
print(three(times(eight())))
print(three(times(five())))

def my_function(a, b, c):
  pass
s = "one"

function = locals()[s]
print(function())
