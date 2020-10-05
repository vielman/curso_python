import os
os.system('cls')
# Dado una lista de frases ingresadas por el usuario, 
# mostrar en pantalla todas aquellas que sean palíndromo.
palindromo = []
print('lista de frases ')
for numero in range(1,5):
    print('Ingrese la frases #', numero )
    texto = input("Ingrese una palabra: ").lower()
    rever = texto[::-1]
    if texto == rever:
        palindromo.append(rever)

print('lista de frases palíndromo')    
for indice, valor in enumerate(palindromo):
    print(valor)