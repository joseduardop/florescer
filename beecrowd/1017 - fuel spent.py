consumo = 12 #transformar em input
vmedia = int(input('digite a velocidade média durante a viagem, em km/h: '))
tempo = int(input('digite quanto tempo a viagem levou, em horas: '))

deltas = (vmedia*tempo)/consumo

print(f'a distancia percorrida total, foi de: {deltas:.3f}')