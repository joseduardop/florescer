nome = input('digite seu nome: ')
sal = float(input('digite seu salário fixo: '))
vendas = float(input('digite o total recebido em vendas: '))

salb = sal + (0.15 * vendas)

print(f'seu salário final, com o bonus, é: {salb:.2f} ')