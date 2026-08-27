valor = float(input('digite o valor monetário: '))

centavos = round(valor * 100)

nota100 = centavos // 10000
centavos -= nota100 * 10000

nota50 = centavos // 5000
centavos -= nota50 * 5000

nota20 = centavos // 2000
centavos -= nota20 * 2000

nota10 = centavos // 1000
centavos -= nota10 * 1000

nota5 = centavos // 500
centavos -= nota5 * 500

nota2 = centavos // 200
centavos -= nota2 * 200

moeda1 = centavos // 100
centavos -= moeda1 * 100

moeda50c = centavos // 50
centavos -= moeda50c * 50

moeda25c = centavos // 25
centavos -= moeda25c * 25

moeda10c = centavos // 10
centavos -= moeda10c * 10

moeda5c = centavos // 5
centavos -= moeda5c * 5

moeda1c = centavos

print(f'{nota100} nota(s) de R$ 100,00')
print(f'{nota50} nota(s) de R$ 50,00')
print(f'{nota20} nota(s) de R$ 20,00')
print(f'{nota10} nota(s) de R$ 10,00')
print(f'{nota5} nota(s) de R$ 5,00')
print(f'{nota2} nota(s) de R$ 2,00')
print(f'{moeda1} moeda(s) de R$ 1,00')
print(f'{moeda50c} moeda(s) de R$ 0,50')
print(f'{moeda25c} moeda(s) de R$ 0,25')
print(f'{moeda10c} moeda(s) de R$ 0,10')
print(f'{moeda5c} moeda(s) de R$ 0,05')
print(f'{moeda1c} moeda(s) de R$ 0,01')
