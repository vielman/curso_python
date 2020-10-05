titulo = "Curso de Python"

for caracter in titulo:
    if caracter == "P":
        break
    print(caracter)

for caracter in titulo:
    if caracter == "P":
        continue
    print(caracter)