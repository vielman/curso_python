class Triangulo:
    numero = 2

    @staticmethod
    def area(base, altura):
        return (base * altura) / Triangulo.numero

print(Triangulo.area(10,20))
print(Triangulo.area(3,5))