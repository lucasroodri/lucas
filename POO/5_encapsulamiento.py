class MiClase:
    def __init__(self):
        self._atributo_privado = "Valor" #Al empezar con _ le dices a Python que es un atributo privado
        self.__atributo_superprivado = "Privado" #Al empezar con __ le dices a Python que es un atributo super privado

    def __hablar(self): #Tambien se pueden crear metodos super privados
        print("Hola")


objeto = MiClase()
print(objeto._atributo_privado) #Aunque empieze por _ se puede acceder al atributo
#print(objeto.__atributo_superprivado) #Da error por que no se puede acceder a ese atributo
#objeto.__hablar()  #El metodo es privado. Dará error

#GETTERS Y SETTERS
class Persona:
    def __init__(self, nombre, edad):
        self._nombre = nombre #Con el _ se indica que no se deberia de acceder directamente a la propiedad
        self._edad = edad     #Para acceder a ellos, se deben usar los getters

    def get_nombre(self): #Getter
        return self._nombre

    def set_nombre(self, nuevo_nombre): #Setter
        self._nombre = nuevo_nombre

lucas = Persona("Lucas",23)
print(lucas.get_nombre())

lucas.set_nombre("Marcos")
print(lucas.get_nombre())