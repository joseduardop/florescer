# 1036 - Formula de Bhaskara

import math ## rola usar ** 0.5

# le os tres valores de ponto flutuante
a, b, c = input().split()
a = float(a)
b = float(b)
c = float(c)

# delta da formula de bhaskara
delta = b * b - 4 * a * c

# nao da pra calcular se A for zero (divisao por zero)
# nem se o delta for negativo (raiz de negativo)
impossivel = False
if a == 0:
    impossivel = True
if delta < 0:
    impossivel = True

if impossivel:
    print("Impossivel calcular")

if not impossivel:
    r1 = (-b + math.sqrt(delta)) / (2 * a)
    r2 = (-b - math.sqrt(delta)) / (2 * a)
    print(f"R1 = {r1:.5f}")
    print(f"R2 = {r2:.5f}")
