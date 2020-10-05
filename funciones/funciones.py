def saluda():   # definir funcion 
    print("Hola Mundo")

saluda() # llamar funcion

def crear_mensaje(nombre): # parametros
    return  "Hola {}, bienvenido al curso de Python 3".format(nombre) 

nuevo = crear_mensaje("Eduardo")
print(nuevo)

def suma(val1, val2, val3):
    return val1 + val2 + val3 # retornar valor

suma = suma(10, 20, 30)
print(suma)

def obtener_curso():
    return "Curso de Python", "Basico", 3.6 # retornar varios valores

curso, nivel, version = obtener_curso()
print(curso, nivel, version)