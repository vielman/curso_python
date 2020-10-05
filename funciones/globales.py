animal = 'Leon' # es una variable global

def mostrar_animal():
    global animal # definimos la variable global
    animal = 'Ballena' # es una variable local
    print(animal)

mostrar_animal()
print(animal)