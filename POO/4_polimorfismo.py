class Gato:
    def sonido(self):
        return "Miau"

class Perro:
    def sonido(self):
        return "Guau"

def hacerSonido(animal):
    print(animal.sonido())

gato = Gato()
perro = Perro()

print(gato.sonido()) #Si se cambia gato por perro hara un sonido diferente
hacerSonido(perro)   #Lo mimso aqui