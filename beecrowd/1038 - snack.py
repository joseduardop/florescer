# 1038 - Lanche

# le o codigo do item e a quantidade
codigo, qtd = input().split()
codigo = int(codigo)
qtd = int(qtd)

# tabela de precos do lanche
preco = 0.0
if codigo == 1:
    preco = 4.00
if codigo == 2:
    preco = 4.50
if codigo == 3:
    preco = 5.00
if codigo == 4:
    preco = 2.00
if codigo == 5:
    preco = 1.50

total = preco * qtd
print(f"Total: R$ {total:.2f}")
