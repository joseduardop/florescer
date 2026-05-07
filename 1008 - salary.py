numfuncionario = int(input('digite o número de funcionário: '))
horastrabalhadas = int(input('digite o número de horas trabalhadas: '))
salarioporhora = float(input('digite o salário por hora: '))

salariofinal = (salarioporhora * horastrabalhadas)

print(f'o funcionário de número {numfuncionario}, vai receber {salariofinal:.2f}')
