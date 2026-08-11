#DIP = Principio de Inversion de Dependencias
#Los modulos de alto nivel no tiene que depender de los modulos de bajo nivel
#La sclases de alto nivel deben de ser independientes de las de bajo nivel

# class Diccionario():
#     def verificar_palabra(self, palabra):
#         #Logica para verificar palabras
#         pass

# class CorrectorOrtografico(): #CorrectorOrtografico depende de diccionario
#     def __init__(self):
#         self.diccionario = Diccionario()

#     def corregir_texto(self, texto):
#         #Usamos el diccionario para corregir el texto
#         pass

from abc import ABC, abstractmethod

class VerificadorOrtografico():
    @abstractmethod
    def verificar_palabra(self, palabra):
        #Logica de verificacion de palabras
        pass

class Diccionario(VerificadorOrtografico):
    def verificar_palabra(self, palabra):
        #Logica de verificacion de palabras
        pass

class ServicioOnline(VerificadorOrtografico):
    def verificar_palabra(self, palabra):
        #Logica de verificacion de palbras online
        pass

class CorrectorOrtografico():
    def __init__(self, verificador):
        self.verificador = verificador

    def corregir_texto(self, texto):
        #Logica de corrrecion de palabras
        pass


corrector_offline = CorrectorOrtografico(Diccionario())
corrector_online = CorrectorOrtografico(ServicioOnline())