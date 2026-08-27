deltas = int(input('digite a distância percorrida: '))
gas = float(input('digite o total de combustível gasto: '))

consumo = (deltas/gas)

print(f'o consumo total, foi de: {consumo:.3f} km/L')