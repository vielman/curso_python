def crear_usuario(nombre='', apellido='', edad=10): # 3 parametros por defecto
    return {
        'nombre' : nombre,
        'apellido' : apellido,
        'nombre_completo' : "{} {}".format(nombre, apellido),
        'edad' : edad
    }

codi = crear_usuario(apellido="perez", nombre="Jose") # 3 argumentos desordenado y puedo omitir un argumento
print(codi["nombre"])
print(codi["apellido"])
print(codi["edad"])
