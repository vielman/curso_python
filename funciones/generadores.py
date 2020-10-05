# se utilisa para la generacion de secuencias de datos
def tabla_multiplicar(numero, maximo=10):
    for posicion in range(1, maximo+1):
        # Yield retorna el valor de la multiplicacion sin ternanar la funcion
        yield numero * posicion, numero, posicion

for resultado, numero, posicion in tabla_multiplicar(9):
    print(numero, " * ", posicion, " = ", resultado)