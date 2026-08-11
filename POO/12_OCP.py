#OCP = Principio de Abierto Cerrado
#Una clase debe estar abierta a añadir mas contenido, sin modificar su codigo fuente (cerrado)
#Se separa el programa en partes mas pqueñas para no tner que modificar una clase entear al meter algo nuevo

class Notificador():
    def __init__(self, usuario, mensaje):
        self.usuario = usuario
        self.mensaej = mensaje

    def notificar(self):
        raise NotImplementedError #Devuelve un error avisando de que el metodo no ha sido implementado. Se pone para
                                  #indicar funcionalidades que se implementaran en el futuro

class NotificadorEmail(Notificador):
    def notificar(self):
        print(f"Enviando mensaje por correo electronico a {self.usuario.email}")

class NotificadorSMS(Notificador):
    def notificar(self):
        print(f"Enviando mensaje por SMS a {self.usuario.sms}")