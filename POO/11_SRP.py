#SRP = Principio de Responsabilidad Unica

class Coche():
    def __init__(self, tanque): #Para crear el coche, primero hay que crear el atnque y pasarselo
        self.posicion = 0
        self.tanque = tanque

    def mover(self, distancia):
        if self.tanque.obtener_combustible() >= distancia / 2:
            self.posicion += distancia
            self.tanque.usar_combustible(distancia / 2)
        else:
            print("No hay suficiente combustible")

    def obtener_posicion(self):
        return self.posicion

#Se divide en 2 clase el total del coche, para que cada clase se encargue de una tarea en concreto
class TanqueCombustible():
    def __init__(self):
        self.combustible = 100

    def agregar_combustible(self, cantidad):
        self.combustible += cantidad

    def obtener_combustible(self):
        return self.combustible

    def usar_combustible(self, cantidad):
        self.combustible -= cantidad


tanque = TanqueCombustible()
coche = Coche(tanque)

print(coche.obtener_posicion())
coche.mover(20)
print(coche.obtener_posicion())
coche.mover(40)
print(coche.obtener_posicion())
coche.mover(60)
print(coche.obtener_posicion())
coche.mover(80)
print(coche.obtener_posicion())
coche.mover(100)
print(coche.obtener_posicion())