import os
os.system('cls')
# Convertir la cantidad de dólares ingresados por un usuario a bolivares 
# y mostrar el resultado en pantalla.

print('Convertir Dolares a Bolibares')
dolar = float(input('Ingrese la cantidad en Dolares\n'))
taza = float(input('Ingrese la Taza de cambio\n'))

bolivares = dolar * taza

print('Monto en Bolivares: ', bolivares)