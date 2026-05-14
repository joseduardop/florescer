from math import pi

numA = float(input('digite o valor do número A: '))
numB = float(input('digite o valor do número B: '))
numC = float(input('digite o valor do número C: '))

#a) the area of the rectangled triangle that has base A and height C.

areatriangulo = (numA * numC)/2

print(f'a area do triangulo de base {numA} e altura {numC}, é: {areatriangulo}')

#b) the area of the radius's circle C. (pi = 3.14159)

areacirculo = pi * (numC ** 2)

print(f'a area do circulo de raio {numC}, é: {areacirculo}')

#c) the area of the trapezium which has A and B by base, and C by height.

areatrapezio = ((numA + numB) * numC)/2

print(f'a area do trapezio de bases {numA} e {numB}, e altura {numC}, é: {areatrapezio}')

#d) the area of ​​the square that has side B.

areaquadrado = numB ** 2

print(f'a area do quadrado de lado {numB}, é: {areaquadrado}')

#e) the area of the rectangle that has sides A and B.

arearetangulo = numA * numB

print(f'a area do retangulo de lados {numA} e {numB}, é: {arearetangulo}')