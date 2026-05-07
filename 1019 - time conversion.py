secs = int(input('digite o tempo, em segundos: '))

mins = secs // 60
secsf = secs % 60

horas = mins // 60
mins = mins % 60

print(f'{secs} segundos, são: {horas} horas, {mins} minutos e {secsf} segundos.')