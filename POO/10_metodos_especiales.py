class Persona():
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self): #Metodo reservado para definir como mostrar por consola la clase
        return f"Persona(nombre={self.nombre}, edad={self.edad})"

    def __repr__(self): #Metodo para realizar la representacion del objeto y luego reconstruirlo. Tiene una sintaxis concreta para el return
        return f'Persona("{self.nombre}", {self.edad})'

    def __add__(self, otro): #Existen metodos para las operaciones logicas
        nuevo_valor = self.edad + otro.edad
        return Persona(self.nombre+otro.nombre, nuevo_valor) #Se define que clase va a devolver la suma de clases

lucas = Persona("Lucas", 23)
marcos = Persona("Marcos", 21)
olga = Persona("Olga", 58)

print(lucas) #Muestra el objeto

representacion = repr(lucas)
resultado = eval(representacion)

print(resultado)
print(lucas.edad)

suma = lucas + marcos
suma += olga
print(suma)
print(suma.nombre)
print(suma.edad)

#Existen muchos mas metodos reservados para diferentes operaciones logicas
#Sepodria hacer: lucas * marcos - olga. y dara una clase nueva