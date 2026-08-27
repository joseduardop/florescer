codigo1 = int(input('digite o código do primeiro produto: '))
quantidade1 = int(input('digite a quantidade do primeiro produto: '))
valor1 = float(input('digite o valor unitário do primeiro produto: '))

codigo2 = int(input('digite o código do segundo produto: '))
quantidade2 = int(input('digite a quantidade do segundo produto: '))
valor2 = float(input('digite o valor unitário do segundo produto: '))

total = (quantidade1 * valor1) + (quantidade2 * valor2)

print(f'VALOR A PAGAR: R$ {total:.2f}')
