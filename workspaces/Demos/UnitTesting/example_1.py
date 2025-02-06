import math


def multiply(a, b):
    return a * b


def sin(angle):
    rad = math.pi * angle / 180
    return math.sin(rad)

def fib(n):
    a = 0
    b = 1
    ans = a
    for i in range(n):
        ans = a + b
        a = b

    return ans
