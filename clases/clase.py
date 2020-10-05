class Usuario: # definir clase

    def __init__(self, username='', correo='', nombre=''):
        self.username = username 
        self.correo = correo
        self.nombre = nombre

    def saluda(self): # por comvencion se usa self para nombrar el parametro dentro de una clases
        return "Hola, soy un usuario " + self.nombre
    
    def mostrar_username(self): # atributos
        print(self.username)

    def mostrar_nombre(self):
        print(self.nombre)

    def crear_nombre(self, nombre):
        self.nombre = nombre

codi = Usuario("Codi","codi@gmail.com","Codigo") # instanciar clase o crear un objeto
facilito = Usuario()


print(codi.saluda())
