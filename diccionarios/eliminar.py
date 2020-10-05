diccionario = {"a":1, "b":2, "c":3, "d":4, "e":5,  "f":6, "g":7, "h":8}

del diccionario["a"] # eliminar llave-valor
valor = diccionario.pop("b") # igual 

diccionario = {} # elimina todos los valores
diccionario.clear() # otro metodo para elimina todos los valores
print(valor)
print(len(diccionario))
print(diccionario)