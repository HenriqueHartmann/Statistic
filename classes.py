from math import ceil

def average(values):
    sum = 0
    for v in values:
        sum += v
    
    return sum / len(values)

def amplitude(values):
    return values[-1] - values[0]

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

def calc_qtd_classes(values):
    values.sort()

    amp = amplitude(values)
    n = len(values)
    s = standard_deviation(values)
    rc = n ** (1 / 3)

    up = amp * rc
    down = 3.49 * s
    print("oxi:", down)

    k = 1 + (up / down)

    return ceil(k)

def div_classes(values):
    k = calc_qtd_classes(values)
    amp = amplitude(values)
    
    return round(amp / (k - 1), 2)

def inferior_limit(values):
    c = div_classes(values)
    
    return round(values[0] - (c / 2), 2)

def calc_fa(n1, n2, values):
    count = 0
    for i in values:
        if i >= n1 and i < n2:
            count += 1

    return count

def calc_divs(values):
    i = 0
    qtd_classes = calc_qtd_classes(values)
    class_range = {}
    c = div_classes(values)
    il = inferior_limit(values)
    val = il

    while i < qtd_classes:
        aux = val
        if i == 0:
            val += 0.01
        aux = round(aux, 2)
        val = round(val + c, 2)
        fa = calc_fa(aux, val, values)
        fr = fa / len(values)
        fp = fr * 100
        class_range[i] = "{} |- {} fa: {} fr: {} fp: {}".format(aux, val, fa, fr, fp)
        i += 1
    
    return class_range

def print_result(values):
    k = calc_qtd_classes(values)
    c = div_classes(values)
    il = inferior_limit(values)
    cd = calc_divs(values)

    print("O database será dividido em %d partes do mesmo tamanho."%(k))
    print("O comprimento de cada classe será de", c)
    print("O limite inferior da primeira classe", il)

    print("Classes de []")
    for i in cd:
        print(cd[i])


data = [] # type your values
data.sort()

print_result(data)
