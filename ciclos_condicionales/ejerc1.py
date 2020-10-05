import os
os.system('cls')
# Dado un diccionario, el cual almacena las calificaciones de un alumno,
# siendo las llaves los nombres de las materia y los valores las calificación, 
# mostrar en pantalla el promedio del alumno.

print('Promedio del alumno ')
calificaciones = {"calculo":10, "dibujo":5, "matematica": 8}
suma = 0
contador = 0
for indice, valor in calificaciones.items():
    suma = suma + valor
    contador+=1
    print(indice, valor)

print('Promedio de Notas es: ', suma/contador)