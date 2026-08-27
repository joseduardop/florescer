# 1037 - Intervalo

# le um valor qualquer com ponto flutuante
valor = float(input())

# vou testar faixa por faixa, com if aninhado pra dizer onde cai
# se nao cair em nenhuma, sobra o "Fora de intervalo"
achou = False

if valor >= 0:
    if valor <= 25:
        print("Intervalo [0,25]")
        achou = True
    if valor > 25:
        if valor <= 50:
            print("Intervalo (25,50]")
            achou = True
    if valor > 50:
        if valor <= 75:
            print("Intervalo (50,75]")
            achou = True
    if valor > 75:
        if valor <= 100:
            print("Intervalo (75,100]")
            achou = True

if not achou:
    print("Fora de intervalo")
