def suma(*args):  # comvencion en python para recibir varios valores en un parametro
    total = 0
    for valor in args:
        total+=valor
    return total

resul = suma(10, 20, 30, 40, 50)
print(resul)

def usurios_autentificados(**kwargs): # convencion en python parra recibir varios parametros
    print(kwargs)

usurios_autentificados(codi=True, facilito=False) # agrupa los argumentos en un dicionario clave/valor

def combinacion(requerido, *args, **kwargs):
    print(requerido)
    print(args)
    print(kwargs)

combinacion("Valor requerido", 10, 20, valor_uno=False, valor_dos=True)