from math import factorial

def binomial(x, p, n):
    k = x

    fup = factorial(n)
    fdown = factorial(n - k) * factorial(k)
    fr = fup / fdown
    result = (fr * ((p ** k) * ((1 - p) ** (n - k)))) * 100
    result = round(result, 2)

    print(result, "%")

def average(p, n):
    print(n * p)

def variance(n, p, q):
    print(n * p * q)


binomial() # type your values
average() # type your values
variance() # type your values