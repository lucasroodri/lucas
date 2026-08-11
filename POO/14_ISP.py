#ISP = Principio de Segregacion de la Interfaz
#Un cliente no debe de utilizar interfaces que no pueda usar

from abc import ABC, abstractmethod

class Trabajador(ABC):

    @abstractmethod
    def trabajar(self):
        pass

class Comedor(ABC):

    @abstractmethod
    def comer(self):
        pass

class Durmiente(ABC):

    @abstractmethod
    def dormir(self):
        pass


#A cada subclase se le añade las clases padre que emplea
class Humano(Trabajador, Durmiente, Comedor):
    def comer(self):
        print("El humano come")

    def trabajar(self):
        print("El humano trabaja")

    def dormir(self):
        print("El humano duerme")

class Robot(Trabajador): 
    def trabajar(self):
        print("El robot trabaja")

robot = Robot()
robot.trabajar()

humano = Humano()
humano.trabajar()
humano.comer()