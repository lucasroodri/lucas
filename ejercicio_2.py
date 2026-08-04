class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def escribirNombre(self):
        print(f"Nombre: {self.nombre}")
    

class Estudiante(Persona):
    def __init__(self, nombre, edad, grado):
        super().__init__(nombre, edad)
        self.grado = grado
    
    def escribirGrado(self):
        print(f"Grado: {self.grado}")

estudiante = Estudiante("Lucas", 23, "Teleco")
estudiante.escribirNombre()
estudiante.escribirGrado()

#---------------------------
class Animal:
    def comer(self):
        print("El animal come")

class Mamifero(Animal):
    def amamantar(self):
        print("El animla amamanta")

class Ave(Animal):
    def volar(self):
        print("El animal vuela")

class Murcielago(Mamifero, Ave):
    def murcielago(self):
        super().volar()

murcielago = Murcielago()
murcielago.comer()
murcielago.volar()
murcielago.amamantar()

murcielago.murcielago()