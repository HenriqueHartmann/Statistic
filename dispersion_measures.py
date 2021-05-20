def average(values):
    sum = 0
    for v in values:
        sum += v
    
    return sum / len(values)

def variance(values):
    avg = average(values)
    sum = 0
    n = len(values)
    for v in values:
        sum += pow((v - avg), 2)
    
    return sum / (n - 1)

def standard_deviation(values):
    v = variance(values)
    
    return round(pow(v, 1/2), 6)

def coefficient_variation(values): 
    avg = average(values)
    s = standard_deviation(values)

    # cv = Coefieciente de Variação
    #       cv <= 15% - Baixo
    # 15% > cv <= 30% - Médio
    #       cv >  30% - Alto
    return s / avg * 100 

def print_result(values):
    avg = average(values)
    v = variance(values)
    s = standard_deviation(values)
    cv = coefficient_variation(values)

    print("Média", avg)
    print("Variância", v)
    print("Desvio Padrão", s)
    print("Coeficiente de Variação", cv)
    print("\n")


data = [] # type your values

print_result(data)
