import os
os.system('cls')
# Crear una lista la cual almacene 10 números positivos ingresados 
# por el usuario, mostrar en pantalla: la suma de todos los números, 
# el promedio, el número mayor y el número menor.

print('lista de 10 números positivos ')
lista = []
suma = 0
for numero in range(1,11):
    print('Ingrese el Valor #', numero )
    valor = int(input())
    lista.append(valor)
    suma = suma + valor
    
promedio = suma/numero
print('Las Suma de todos los Numeros es: ', suma, 'El Promedio es: ', promedio)
print('La mayor Notas es: ', max(lista), 'El numero menor es: ', min(lista))