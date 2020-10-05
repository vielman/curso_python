lista = []

for x in range(0, 5):
    lista.append(x)

print(lista)

estructura = [ x for  x in range(0,10)] #lista

print(estructura)

estructura1 = tuple(( x for  x in range(0,100) 
    if x % 2 == 0 
        if x < 50 ) ) #tupla, que solo muestra los numeros pares

print(estructura1)

dicionario = { indice:valor
    for indice, valor in enumerate(estructura1) }

print(dicionario)
