import os
import math
os.system('cls')
def tang(grados):
    return math.tan(math.radians(grados))
# Calcular y mostrar en pantalla la longitud de la sombra de un edificio de 20 metros de altura 
# cuando el ángulo que forman los rayos del sol con el suelo es de 22º.
print('Calcular la longitud de la sombra de un edificio')
cateto_opuesto = int(input("Cateto opuesto (altura): "))
tangente = int(input("Ángulo de elevación: "))

# Cateto adyacente: es la longitud de la sombra
cateto_adyacente = cateto_opuesto / tang(tangente) 

print('Longitud de la sombra: ', cateto_adyacente)

