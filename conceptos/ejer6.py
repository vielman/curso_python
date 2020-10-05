import os
os.system('cls')
#Calcular el número de vueltas que da una llanta en 1 km, 
# dado que el diámetro de la llanta es de 50 cm, 
# mostrar el resultado en pantalla.

print('Calcular el número de vueltas que da una llanta en 1 km')
PI = 3.1416 #valor de pi para calcular la circunferencia
diametro = float(input("Ingresa el diametro de la llanta en centimetros: "))
kilometro = float(input("ingresa la distsncia en Kilometros: "))


centimetros = kilometro*100000 #convertir kilometros a centimetros
circunferencia = PI * diametro # aqui se calcula de la llanta lo que nos va a dar la distancia recorrida en centimetros

vuelta_km = kilometro/(circunferencia/centimetros) # se ccalcula el total de vueltas

print('vueltas que da una llanta: ', vuelta_km)

