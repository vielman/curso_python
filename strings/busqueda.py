mensaje = "Este es un texto un poco grande en cuanto a longitud de caracteres se refiere"
resultado = mensaje.count("e")
print(resultado)

resultado1 = "texto" in mensaje # verificar si esta dentro de la cadena
print(resultado1)

resultado2 = mensaje.find("texto") # catura la posicion de la primera letra que aparece dentro de la cedana
print(resultado2)

resultado2 = mensaje[resultado2: resultado2 + len("texto") ] # extraer el fraccion del texto
print(resultado2)

resultado3 = mensaje.startswith("Este") # verifica si la cadena esta de primero
print(resultado3)

resultado4 = mensaje.endswith("e") # verifica si la cadena esta de ultimo
print(resultado4)