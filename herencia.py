class Persona:
    def __init__(self,nombre,edad,nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad
    
    def hablar(self):
        print("Hola")

class Empleado(Persona): #Se crea una clase hija de la clase padre Persona. Hereda metodos y atributos del padre
    def __init__(self,nombre,edad,nacionalidad,trabajo,salario):
        super().__init__(nombre,edad,nacionalidad) #Hace que herede estas propiedades del padre
        self.trabajo = trabajo
        self.salario = salario

    def hablar(self): #Sobrescribe el metodo de la clase padre
        print("NO")

#Clases jerarquicas: Cuando de una clas padre se crean varias clases hijas
class Estudiante(Persona):
    def __init__(self,nombre,edad,nacionalidad,notas,universidad):
        super().__init__(nombre,edad,nacionalidad)
        self.notas = notas
        self.universidad = universidad


class Artista():
    def __init__(self,habilidad):
        self.habilidad = habilidad

    def mostrar_habilidad(self):
        return f"Mi habilidad es: {self.habilidad}"

#Herencia multiple
class EmpleadoArtista(Persona,Artista):
    def __init__(self,nombre,edad,nacionalidad,habilidad,salario,empresa):
        Persona.__init__(self,nombre,edad,nacionalidad)
        Artista.__init__(self,habilidad)
        self.salario = salario
        self.empresa = empresa
    
    def mostrar_habilidad(self):
        print("No tengo xd")

    
    def presentarse(self):
        print(f'Hola soy: {self.nombre}, {super().mostrar_habilidad()} y trabjo en {self.empresa}') #Si se pone self.most... no es lo mismo que super().most...




lucas = Empleado("Lucas",23,"Español","ingeniero",3000)
lucas.hablar()

lucas2 =EmpleadoArtista("Lucas",22,"Argentino","Fumar",1000,"Amberleaf")
lucas2.presentarse()

herencia = issubclass(EmpleadoArtista,Persona) #Se puede comprobar si uno e subclase del otro
instancia = isinstance(lucas2,EmpleadoArtista)
print(herencia)
print(instancia)