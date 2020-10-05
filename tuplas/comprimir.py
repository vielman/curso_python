tupla1 = (1,2,3,4,5,6)

uno, *dos, cinco, seis = tupla1

print(uno)
print(dos)
print(cinco)
print(seis)

tupla = (1, 2, 3, 4, 5, 6)
lista = [10, 20, 30, 40]
tupla_dos = (10,200,300,400)

resultado = zip(tupla, lista, tupla_dos)
resultado = tuple(resultado)
resultado1 = list(resultado)
print('tupla',resultado)
print('Lista', resultado1)
