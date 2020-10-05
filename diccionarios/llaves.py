diccionario = {"a":1, "b":2, "c":3, "d":4, "e":5,  "f":6, "g":7, "h":8}
print(diccionario)

resultado = diccionario.keys() # ver todas las llaves del diccionario
resultado = tuple(resultado) # convertimos a tupla
print(resultado)

resultado1 = diccionario.values() # ver todos los valores del diccionario
resultado1 = list(resultado1) # convertimos a lista
print(resultado1)

resultado2 = diccionario.items() # ver todos los valores del diccionario
print(resultado2)