# Pedindo ao usuário um valor em algarísmos romanos para convertê-los para valores numéricos (O algarismo máximo é o M nesta situação)
def alg_romanos(v):
    conv = [["I", 1],["V", 5],["X", 10],["L", 50],["C", 100],["D", 500],["M", 1000]]
    #Array onde ficarão os números convertidos porém não somados/subtraídos
    numerico_ns = list()
    for letra in v:
        for corr in conv:
            if letra == corr[0]:
                numerico_ns.append(corr[1])
            else:
                return -1


    return numerico_ns

def int_romanos(n=list()):
    num_final = 0
    if n == -1:
        return "Você inseriu um valor inválido."
    else:
        for alg in n:
            if n[n.index(alg)+1] > alg and alg == 1 or alg == 10 or alg == 100:
                num_final -= alg
            elif n[n.index(alg)+1] <= alg:
                if n.count(alg) > 3:
                    return "Você inseriu um valor inválido."
                else:
                    num_final += alg
    return num_final
