tupla = (10, 20, 30, 40, 50)

# Necesito obtener el primero, 
# el segundo y el último elemento; 
# Para lograr esto tendremos un par de opciones;
#  trabajando con índices y sin ellos. Veamos.

primero = tupla[0]
segundo = tupla[1]
ultimo = tupla[-1]

print(primero)
print(segundo)
print(ultimo)

primero1, segundo2, _, _, ultimo3 = tupla
print(primero1)
print(segundo2)
print(ultimo3)