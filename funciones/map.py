def cuadrado(numero):
     return numero * numero

lista = [1,2,3,4,5]
resultado = map(cuadrado, lista)

lista_resultado = list(resultado)
print(lista_resultado)

# refactor con  lambdas

lista = [1,2,3,4,5]
resultado1 = map(lambda numero: numero * numero , lista)

lista_resultado1 = list(resultado1)
print(lista_resultado1)