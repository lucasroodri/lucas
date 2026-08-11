class Personaje():
    def __init__(self, nombre, fuerza, velocidad):
        self.nombre = nombre
        self.fuerza = fuerza
        self.velocidad = velocidad

    def __repr__(self):
        return f"{self.nombre} (Fuerza: {self.fuerza}, Velocidad: {self.velocidad})"

    def __add__(self, otro_personaje):
        nuevo_nombre = self.nombre + otro_personaje.nombre
        nueva_fuerza = round(((self.fuerza + otro_personaje.fuerza)/2)**1.5)
        nueva_velocidad = round(((self.velocidad + otro_personaje.velocidad)/2)**1.5)
        return Personaje(nuevo_nombre, nueva_fuerza, nueva_velocidad)

######################################
personajes = []
menu = 0

while menu != 4:
    print("1. Crear Personaje")
    print("2. Fusionar Personaje")
    print("3. Mostrar Personajes")
    print("4. Salir")
    menu = int(input("Elige una opción: "))

    if menu not in (1, 2, 3, 4):
        while menu not in (1, 2, 3, 4):
            print("1. Crear Personaje")
            print("2. Fusionar Personaje")
            print("3. Mostrar Personajes")
            print("4. Salir")   
            menu = int(input("Elige una opción: "))

    if menu == 1:
        print("CREAR PERSONAJE")
        nombre = input("Nombre de Personaje: ")
        fuerza = input("Fuerza del personaje: ")
        if not fuerza.isdigit():
            while not fuerza.isdigit():
                fuerza = input("Fuerza del personaje: ")
        velocidad = input("Velocidad del personaje: ")
        if not velocidad.isdigit():
                while not velocidad.isdigit():
                    velocidad = input("Velocidad del personaje: ")

        pers = Personaje(nombre, int(fuerza), int(velocidad))
        personajes.append(pers)
        print(pers)

    if menu == 2:
        print("FUSION DE PERSONAJES")
        num1 = int(input("Numero de personajes a fusionar: "))
        print(personajes[num1-1])
        num2 = int(input("Numero de personajes a fusionar: "))
        print(personajes[num2-1])
        if num1 > len(personajes) or num2 > len(personajes):
            print("No existe ese personaje. Intenta de nuevo o crea mas personajes")
            num1 = input("Numero de personaje a fusionar: ")
            num2 = input("Numero de personaje a fusionar: ")
        pers = personajes[num1-1] + personajes[num2 -1]
        print(pers)
        personajes.append(pers)

    if menu == 3:
        print("MOSTRAR PERSONAJES")
        for personaje in personajes:
            print(personaje)
