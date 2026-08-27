xf = float(input('digite a coordenada x do primeiro ponto: '))
yf = float(input('digite a coordenada y do primeiro ponto: '))
x0 = float(input('digite a coordenada x do segundo ponto: '))
y0 = float(input('digite a coordenada y do segundo ponto: '))

distancia = ((xf - x0)**2 + (yf - y0)**2)**(1/2)

print(f'a distância entre ({x0},{y0}) e ({xf},{yf}) é de {distancia:.4f}')