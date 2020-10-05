diccionario = {}
diccionario["nombre"] = "Codi" # agrgar llave con su valor

valor = diccionario["nombre"] # obtener un valor

diccionario["nombre"] = 90
print(diccionario)
print(valor)

diccionario1 = {"a":1, "b":2, "c":3, "a":4}
resultado = diccionario1["a"] # muestra el valor de la llave
print(resultado)

resultado1 = "z" in diccionario1 # verifica si existe la llave
print(resultado1)

resultado2 = diccionario1.get("a") # muetra el valor de la llave, no da error si la llae no existe
print(resultado2)

resultado3 = diccionario1.get("z", "la llave no existe") # si la llave no existe muestra el mensaje
print(resultado3)

resultado4 = diccionario1.setdefault("z", {}) # si no existe la llave lo crea
print(resultado4)
print(diccionario1)