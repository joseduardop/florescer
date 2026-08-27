# 1042 - Sort Simples

# le os tres inteiros guardando a ordem original
a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)

# guardo a sequencia original antes de mexer
orig = [a, b, c]

# ordeno em ordem crescente com trocas
if a > b:
    a, b = b, a
if a > c:
    a, c = c, a
if b > c:
    b, c = c, b

# primeiro a ordem crescente
print(a)
print(b)
print(c)

# linha em branco
print()

# depois a sequencia como foi lida
print(orig[0])
print(orig[1])
print(orig[2])
