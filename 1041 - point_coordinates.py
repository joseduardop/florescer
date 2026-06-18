# 1041 - Coordenadas de um Ponto

# le as coordenadas x e y do ponto
x, y = input().split()
x = float(x)
y = float(y)

# origem é quando os dois sao zero
if x == 0:
    if y == 0:
        print("Origem")

# em cima de um dos eixos (mas nao na origem)
if x == 0:
    if y != 0:
        print("Eixo Y")
if y == 0:
    if x != 0:
        print("Eixo X")

# os quatro quadrantes
if x > 0:
    if y > 0:
        print("Q1")
    if y < 0:
        print("Q4")
if x < 0:
    if y > 0:
        print("Q2")
    if y < 0:
        print("Q3")
