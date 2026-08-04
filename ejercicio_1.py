class Estudiante:
    def __init__(self, nombre, edad, grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado

    def estudiar(self):
        print("Estudiando...")

nombre = input("Dime tu nombre: ")
edad = input("Dime tu edad: ")
grado = input("En que curso estas: ")

estudiante = Estudiante(nombre, edad, grado)

print(f"""
    DATOS DEL ESTUDIANTE: \n
    Nombre: {estudiante.nombre} \n
    Edad: {estudiante.edad} \n
    Grado: {estudiante.grado} \n
""")

while True:
    estudiar = input()
    if(estudiar.lower() == "estudiar"): #El .lower() lo convierte todo a minusculas. 
        estudiante.estudiar()