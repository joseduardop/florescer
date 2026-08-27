# 1013 - O Maior

# le os tres valores na mesma linha
a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)

# pega o maior entre A e B com uma formula
maior = (a + b + abs(a - b)) // 2

# agora compara esse resultado com o terceiro valor
maior = (maior + c + abs(maior - c)) // 2

print(maior, "eh o maior")
