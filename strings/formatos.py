texto = "   curso de Python 3, Python Basico   "

resultado = texto.capitalize()
print(resultado)

resultado1 = texto.swapcase()
print(resultado1)

resultado2 = texto.upper()
print(resultado2)

resultado3 = texto.lower()
print(resultado3)

print(resultado3.isupper())
print(resultado3.islower())

print(texto.title())

print(texto.replace("Python", "ruby"))

print(texto.replace("Python", "ruby", 1))

print(texto.strip())

curso = "Python"
version = "3"

resultado4 = "Curso de %s %s" %(curso, version)
print(resultado4)

resultado5 = "Curso de {} {}".format(curso, version)
print(resultado5)

resultado6 = "Curso de {a} {b}".format(a=curso, b=version)
print(resultado6)
