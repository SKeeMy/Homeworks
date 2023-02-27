import math


def truefibvalue_sqrt(n):
    return n == int(math.sqrt(n)) ** 2

def truefibvalue(n):
    return trueFibValue_sqrt(5 * n * n + 4) or trueFibValue_sqrt(5 * n * n - 4)

def check(N):
    for n in N:
        if not trueFibValue(n):
            return False
            exit()
    return True


