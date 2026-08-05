class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre 
        self._edad = edad     

    @property #Decorador especial. Indica que lo de abajo es un getter. No hara falta poner () cuando se llame al getter
    def nombre(self): #Getter
        return self.__nombre

    @nombre.setter #Se crea el setter relacionado con el anterior getter
    def nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre

    @nombre.deleter
    def nombre(self):
        del self.__nombre

lucas = Persona("Lucas",23)
print(lucas.nombre) #Parece que se esta accediendo a una propiedad, pero en realidad es una funcion de la clase

lucas.nombre = "Marcos" #Se usa el setter. Pero sigue pareciendo que se esta accediendo a un atributo. De forma que se no se pueda acceder a __nombre
print(lucas.nombre)

#Con el deleter se puede borrar el atributo:
del lucas.nombre #Esta es la unica manera de usar el deleter. si no existiera daria error
#print(lucas.nombre) #Dara error ya que se ha borrado el nombre
