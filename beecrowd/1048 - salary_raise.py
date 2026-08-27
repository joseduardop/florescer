# 1048 - Aumento de Salario

# le o salario atual do funcionario
salario = float(input())

# descobre o percentual de reajuste pela faixa
percentual = 0
if salario <= 400.00:
    percentual = 15
if salario > 400.00:
    if salario <= 800.00:
        percentual = 12
if salario > 800.00:
    if salario <= 1200.00:
        percentual = 10
if salario > 1200.00:
    if salario <= 2000.00:
        percentual = 7
if salario > 2000.00:
    percentual = 4

reajuste = salario * percentual / 100
novo = salario + reajuste

print(f"Novo salario: {novo:.2f}")
print(f"Reajuste ganho: {reajuste:.2f}")
print(f"Em percentual: {percentual} %")
