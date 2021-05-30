# Pedindo ao usuário um valor em algarísmos romanos para convertê-los para valores numéricos
def alg_romanos(v):
    conv = [["I", 1],["V", 5],["X", 10],["L", 50],["C", 100],["D", 500],["M", 1000]]
    #Array onde ficarão os números convertidos porém não somados/subtraídos
    numerico_ns = list()
    for letra in v:
        for corr in conv:
            if letra == corr[0]:
                numerico_ns.append(corr[1])
            else:
                print("Você inseriu um valor inválido")
                return -1

    return numerico_ns
