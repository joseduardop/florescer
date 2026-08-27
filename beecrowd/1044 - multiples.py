# 1044 - Multiplos

# le os dois inteiros
a, b = input().split()
a = int(a)
b = int(b)

# sao multiplos se um divide o outro sem resto
multiplos = False
if a % b == 0:
    multiplos = True
if b % a == 0:
    multiplos = True

if multiplos:
    print("Sao Multiplos")
if not multiplos:
    print("Nao sao Multiplos")
