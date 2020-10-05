def funcion():
  return "String", (1,2,3), [1,2,3], None

resultado = funcion()
print(resultado)


def suma(a, b=0):
  return a+b

print(suma(a=100))

print("verdadero" if 10 > 5  else "Falso")

print("biembenido" + str(3))