def freq_abs(data):
    count_data = {}
    k = 0

    while k < len(data):
        count = 0
        for i in data:
            if i == data[k]:
                count += 1
                count_data[i] = count
        k += 1
    
    return count_data

def freq_rel(data):
    fas = freq_abs(data)
    fr = {}

    for i in fas:
        fr[i] = fas[i] / len(data)
    
    return fr

def freq_rel_per(data):
    fr = freq_rel(data)
    frp = {}

    for i in fr:
        frp[i] = str(int(fr[i] * 100)) + "%"

    return frp

def print_all(data):
    data.sort()
    print("Frequência absoluta: ", freq_abs(data))
    print("Frequência relativa: ", freq_rel(data))
    print("Frequência relativa percentual: ", freq_rel_per(data))


data = [] # type your values

print_all(data)
