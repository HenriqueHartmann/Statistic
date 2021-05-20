def bernoulli(s, n):
    p = s / n
    q = 1 - p
    v = p * (1 - p)

    print("Probabilidade de Sucesso: {}".format(round(p, 4)))
    print("Probabilidade de Fracasso: {}".format(round(q, 4)))
    print("Variância:", round(v, 4))


bernoulli() # type your values
