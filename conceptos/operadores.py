variable_uno = 10
variable_dos = 18

mayor = variable_uno > variable_dos
menor = variable_uno < variable_dos

mayor_igual = variable_uno >= variable_dos
menor_igual = variable_uno <= variable_dos

igual = variable_uno == variable_dos
diferente = variable_uno != variable_dos

print(mayor)
print(menor)
print(mayor_igual)
print(menor_igual)
print(igual)
print(diferente)

# operados logicos
print('----------Logicos---------------')

resultado = True and True and mayor
print(resultado)

resultado1 = True or True or mayor
print(resultado1)

resultado2 = not False
print(resultado2)