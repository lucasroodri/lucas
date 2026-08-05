def decorador1(funcion):
    def funcion_modificada():
        print("Antes de llamar a la funcion")
        funcion()
        print("Despues de llamara a la funcion")
    return funcion_modificada

#def hola_mundo():
#    print("Hola mundo")
#
#hola_modificado = decorador(hola_mundo)
#hola_modificado()

@decorador1
def saludo():
    print("Hola mundo")

saludo()