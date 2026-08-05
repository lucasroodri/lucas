class TelefonoMovil():
    marca = "Samsung"
    modelo = "S23"
    camara = "48MP"

#OBJETOS ESTATICOS
movil1 = TelefonoMovil() #Se crea un objeto que es una instancia de la clase TelefonoMovil
print(movil1)
print(movil1.marca) #Ahora mismo los atributos/propiedades son estaticos

#CLASES DINAMICAS
class Telefono:
    #Constructor
    def __init__(self, marca, modelo, camara): #Sirve para definir las propiedades iniciales del objeto
        #Se ejecuta al crear el objeto
        self.marca = marca
        self.modelo = modelo
        self.camara = camara
    
    #METODOS: Son funciones que se encuentra dentro de una clase
    def llamar(self): #Hay que poner siempre como parametro self para que haga referencia al objeto
        print(f'Estas haciendo una llamada desde un: {self.modelo}') #f stream para poder usar el modelo. LLEVA COMILLAS SIMPLES
    
    def colgar(self):
        print("Colgaste la llamada")


movil2 = Telefono("Apple", "Iphone15", "48MP")
print(movil2)
print(movil2.modelo)

movil2.llamar()
movil2.colgar()