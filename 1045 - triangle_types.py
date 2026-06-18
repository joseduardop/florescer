# 1045 - Tipos de Triangulos

# le os tres lados
a, b, c = input().split()
a = float(a)
b = float(b)
c = float(c)

# ordeno em ordem decrescente pra A ser o maior lado
if a < b:
    a, b = b, a
if a < c:
    a, c = c, a
if b < c:
    b, c = c, b

# primeiro verifica se forma triangulo
if a >= b + c:
    print("NAO FORMA TRIANGULO")

if a < b + c:
    # classifica pelo lado maior ao quadrado
    if a * a == b * b + c * c:
        print("TRIANGULO RETANGULO")
    if a * a > b * b + c * c:
        print("TRIANGULO OBTUSANGULO")
    if a * a < b * b + c * c:
        print("TRIANGULO ACUTANGULO")

    # equilatero: os tres iguais
    if a == b:
        if b == c:
            print("TRIANGULO EQUILATERO")

    # isosceles: exatamente dois iguais
    if a == b:
        if b != c:
            print("TRIANGULO ISOSCELES")
    if b == c:
        if a != b:
            print("TRIANGULO ISOSCELES")
    if a == c:
        if a != b:
            print("TRIANGULO ISOSCELES")
