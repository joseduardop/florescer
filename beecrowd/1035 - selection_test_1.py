# 1035 - Teste de Selecao 1

# le os quatro inteiros na mesma linha
a, b, c, d = input().split()
a = int(a)
b = int(b)
c = int(c)
d = int(d)

# vou checando uma condicao dentro da outra
# se qualquer uma falhar, cai direto pro "nao aceitos"
aceito = False
if b > c:
    if d > a:
        if c + d > a + b:
            if c > 0:
                if d > 0:
                    if a % 2 == 0:
                        aceito = True

if aceito:
    print("Valores aceitos")
if not aceito:
    print("Valores nao aceitos")
