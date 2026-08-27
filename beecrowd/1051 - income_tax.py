# 1051 - Imposto de Renda

# le o salario com duas casas decimais
salario = float(input())

# a taxa incide so sobre o que ultrapassa cada faixa (progressivo)
imposto = 0.0

if salario > 2000.00:
    # parte entre 2000 e 3000 paga 8%
    faixa = min(salario, 3000.00) - 2000.00
    imposto += faixa * 0.08
if salario > 3000.00:
    # parte entre 3000 e 4500 paga 18%
    faixa = min(salario, 4500.00) - 3000.00
    imposto += faixa * 0.18
if salario > 4500.00:
    # o que passar de 4500 paga 28%
    faixa = salario - 4500.00
    imposto += faixa * 0.28

if imposto == 0:
    print("Isento")
if imposto > 0:
    print(f"R$ {imposto:.2f}")
