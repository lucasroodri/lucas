#LCP = Principio de Sustitucion de Liskov
#Todo lo que una clase puede hacer, lo deben de hacer tambien sus subclases

#ASI NO
#class Ave():
#    def volar(self):
#        return "Estoy volando"
#
#class Pinguino(Ave):
#    def volar(self):
#        return "No puedo volar"
#
#def hacer_volar(ave = Ave):
#    return ave.volar()
#
#print(hacer_volar(Pinguino()))

class Ave(): #Se ponen todas las caracteristicas que tengan en comun TODAS las aves
    pass

class AveVoladora(Ave): #Se ponen todas las caracteristicas exclusivas que tengan en comun de las aves voladoras
    def volar(self):
        return "Estoy volando"

class AveNoVoladora(Ave): #Se ponen todas las caracteristicas exclusivas que tengan en comun de las aves no voladoras
    pass