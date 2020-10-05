import os
os.system('cls')
print('Cual es tu nombre?')
nombre = input()

# otra forma de visualizar el texto del input
edad = int(input('Cual es tu edad?\n'))

print('Cual es tu peso?')
peso = float(input())

print('Estas Autrizado?(si/no)')
autorizado = input() == "si"

print('Hola ', nombre)
print('Edad ', edad)
print('Peso ', peso)
print('Autorizado ', autorizado)

