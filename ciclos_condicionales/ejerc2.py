import os
os.system('cls')
# A partir del diccionario del ejercicio anterior, mostrar en pantalla 
# la materia con mejor promedio.

print('Materia con mejor promedio ')
calificaciones = {"calculo":10, "dibujo":5, "matematica": 8}
lista = []
for indice, valor in calificaciones.items():
    lista.append(valor)
    print(indice, valor)

print('La mayor Notas es: ', max(lista))