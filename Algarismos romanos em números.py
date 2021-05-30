# Pedindo ao usuário um valor em algarísmos romanos para convertê-los para valores numéricos (O algarismo máximo é o M nesta situação)
def alg_romanos(v):
    # Array base para relacionar os algarismos romanos com os números
    conv = [["I", 1],["V", 5],["X", 10],["L", 50],["C", 100],["D", 500],["M", 1000]]
    # Array onde ficarão os números convertidos porém não somados/subtraídos
    numerico_ns = list()
    # Relaciona os números com as letras a partir da array 'conv'
    for letra in v:
        for corr in conv:
            if letra == corr[0]:
                numerico_ns.append(corr[1])
            # Se a letra não fazer parte dos algarismos romanos até 1000, retorne -1
            # (Esse valor vai definir se o usuário colocou um valor inválido)
            elif letra not in "IVXLCDM":
                return -1

    # Retorna os números que foram relacionados, mas de forma separada e sem alterar a ordem na qual foi escrita
    return numerico_ns

# Função que interpreta a ordem dos números e gera uma resposta.
def int_romanos(n):
    # Essa variável será o valor final retornado
    num_final = 0
    # Relacionando com a função anterior, se o usuário colocar um valor inválido, será retornado o texto
    # 'Você inseriu um valor inválido'.
    if n == -1:
        return "Você inseriu um valor inválido."
    # Caso apenas algarismos corretos tenham sido adicionados
    else:
        for alg in n:
            # Caso existam mais de 3 de um mesmo algarismo, o valor será inválido
            if n.count(alg) > 3:
                return "Você inseriu um valor inválido."
            else:
                # Caso o número seja menor que o seguinte e seja 1, 10 ou 100,
                # subtraia-o do num_final (valor que será retornado)
                if n[n.index(alg)+1] > alg and alg == 1 or alg == 10 or alg == 100:
                        num_final -= alg
                # Caso o número seja maior ou igual que o seguinte, some ao num_final
                elif n[n.index(alg)+1] <= alg:
                        num_final += alg
    # Retorna o valor já completo e tratado caso tudo esteja certo.
    return num_final

# Rodando o código
while True:
    perg = input("Coloque um valor em algarismos romanos:\n _ ")
    print("=-"*30 + f"{int_romanos(alg_romanos(perg))}" + "=-"*30)