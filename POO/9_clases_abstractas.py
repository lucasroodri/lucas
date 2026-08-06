from abc import ABC, abstractmethod #ABC = Abstract Base Class

class Persona(ABC):
    def __init__(self, nombre, edad, sexo, actividad):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.actividad = actividad

    @abstractmethod
    def hacer_actividad(self):
        pass

    def presentarse(self):
        print(f"Hola me llamo {self.nombre} y tengo {self.edad} años")

class Estudiante(Persona):
    def __init__(self, nombre, edad, sexo, actividad):
        super().__init__(nombre, edad, sexo, actividad)

    def hacer_actividad(self):
        print(f"Estoy estudiando: {self.actividad}")

class Trabajador(Persona):
    def __init__(self, nombre, edad, sexo, actividad):
        super().__init__(nombre, edad, sexo, actividad)

    def hacer_actividad(self):
        print(f"Trabajo en: {self.actividad}")

#Lucas = Persona("Lucas", 23, "Hombre", "Parado") #Dara error porque Persona hereda de la clase abstracta ABC

lucas = Estudiante("Lucas", 23, "Hombre", "Teleco")
lucas.presentarse()
lucas.hacer_actividad()

marcos = Trabajador("Marcos", 21, "Hombre", "Diseño Grafico")
marcos.presentarse()
marcos.hacer_actividad()

#Al haber creado una clase abstracta de la que heredan Estudiante y Trabajdor, cada uno tiene una actividad pero son diferenetes 
#y los metodos son distintos. La clase abstracta sirve como plantilla para sus clases hijo. Las clases hijo estan obligados a tener que
#implementar los metodos de la clase abstracta, si no da error. La clase Persona no puede ser instanciada