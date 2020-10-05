def saludo(nombre : str) -> None: # sirven de guia para que el codigo sea legible
    print("Hola" + nombre)

def suma(num1 : int, num2 : int = 100) -> int:
    return num1 + num2

nombre = "Eduardo"
saludo(nombre)

print(suma(57.7, 89.0))