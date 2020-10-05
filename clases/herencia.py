class Animal:
    def comer(self):
        print("Comiendo")
    
    def dormir(self):
        print("Durmiendo")
    
    def comun(self):
        print("Este es un metodo de Animal")

class Mascota:
    def fecha_adopcion(self, fecha):
        self.fecha_de_adopcion = fecha
    
    def comun(self):
        print("Este es un metodo de Mascota")

class Perro(Animal, Mascota): # herencia multiple
    def __init__(self, nombre):
        self.nombre = nombre

    def ladrar(self):
        print("Ladrando")

    def comun(self):
        print("Este es un metodo de Perro")

class Gato(Animal): # herencia
    def ronroneo(self):
        print("Ronroneo")

firulais = Perro("Firulais")
firulais.ladrar()
firulais.comer()
firulais.dormir()
firulais.fecha_adopcion("Hoy")
print(firulais.fecha_de_adopcion)
firulais.comun() # lo tomoa de la principal

bola_de_nieve = Gato()
bola_de_nieve.ronroneo()
bola_de_nieve.comer()
bola_de_nieve.dormir()