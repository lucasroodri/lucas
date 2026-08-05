class Coche():
    def __init__(self):
        self._estado = "apagado"

    def encender(self):
        self._estado = "encendido"
        print("Se ha encendido el coche")

    def conducir(self):
        if self._estado == "apagado":
            self.encender()
        print("Conduciendo el coche")

peugot = Coche()
peugot.conducir()
#La Abstraccion xonsiste en ocultar la logica y las comprobaciones del programa al usuario
#En este caso si se tiene en coche apagado y se quiere conducir, el programa lo enciende
#Al ususario solo se le da un metodo para que pueda usarlo sin necesidad de que sepa como funciona