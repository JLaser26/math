def absolute(x: int|float) -> int|float:
    if x < 0:
        return 0 - x
    return x

def power(a: int, b: int) -> int:
    if b == 0:
        return 1
    return a * power(a, b - 1)

def factorial(x: int) -> int:
    if x == 0: return 1
    if x == 1: return 1
    if x == 2: return 2

    return x * factorial(x-1)

def GCD(a: int, b: int) -> int:
    while b != 0:
        a, b = b , a % b
    return a

def LCM(a: int, b: int) -> int:
    return absolute(a*b) // GCD(a, b)

#just for fun
def sine(x: int|float) -> int|float:
    return x - (power(x, 3)/factorial(3)) + (power(x, 5)/factorial(5)) - (power(x, 7)/factorial(7)) + (power(x, 9)/factorial(9))
