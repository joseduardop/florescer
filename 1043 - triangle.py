# 1043 - Triangulo

# le os tres valores reais
a, b, c = input().split()
a = float(a)
b = float(b)
c = float(c)

# condicao pra formar triangulo: cada lado menor que a soma dos outros dois
forma = False
if a < b + c:
    if b < a + c:
        if c < a + b:
            forma = True

if forma:
    perimetro = a + b + c
    print(f"Perimetro = {perimetro:.1f}")

if not forma:
    # A e B sao as bases, C a altura do trapezio
    area = (a + b) * c / 2
    print(f"Area = {area:.1f}")
