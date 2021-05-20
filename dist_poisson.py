from math import factorial


def poisson(x, lam):
    k = x
    euler = 2.718281828459045235360287
    up = (euler ** -lam) * (lam ** k)
    down = factorial(k)
    result = round(up / down, 6) * 100
    
    print(result)


poisson() # type your values
