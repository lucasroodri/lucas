class A:
    def hablar(self):
        print("Hola desde A")

class B(A):
    def hablar(self):
        print("Hola desde B")

class C(A):
    def hablar(self):
        print("Hola desde C")

class D(B,C):
    pass

d = D()

d.hablar()
#Si hay metodos con el mismo nombre primero ejecutara siempre el suyo propio
#Si B y C tienen el mismo metodo, ejecutara primero el de B porque es su primera herencia
#Busca metodos de abajo a arriba de herencia

class E:
    def hablar(self):
        print("Hola desde E")

class F:
    def hablar(self):
        print("Hola desde F")

class G(E):
    pass

class H(F):
    pass

class I(G,H):
    pass

i = I()

i.hablar()

#En caso de que las clases padres sean de diferentes padres, se da prioridad a los que sean primeras herencias. 
#En este caso se mira primero la herencia entera de G hasta arriba del todo (hasta E y si no lo tiene va a H)

print(I.mro()) #Te dice cual es el orden del MRO de cada objeto

A.hablar(d) #Ejecuta el hablar pero con el objeto d (puedes usar metodos que estan muy arriba en la herencia en un objeto mas bajo)
