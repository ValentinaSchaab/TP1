from queue import Queue
from stack import Stack

class Notificaciones:
    def __init__(self, hora, aplicacion, mensaje):
        self.hora = hora
        self.aplicacion = aplicacion
        self.mensaje = mensaje

    def __str__(self):
        return f"Hora: {self.hora}, App: {self.aplicacion}, Mensaje: {self.mensaje}"

def cargar_notificaciones():
    cola_notif = Queue()

    cola_notif.arrive(Notificaciones("10:30", "Facebook", "Solicitud")) 
    cola_notif.arrive(Notificaciones("11:45", "Instagram", "Historia"))
    cola_notif.arrive(Notificaciones("14:00", "Facebook", "repost"))
    cola_notif.arrive(Notificaciones("17:35", "Twitter", "Python"))
    return cola_notif                  

def eliminar(cola_notif):
    print("eliminar facebook")
    aux = Queue()

    while cola_notif.size() > 0:
        notif = cola_notif.attention()
        if notif.aplicacion != "Facebook":
            aux.arrive(notif)
    
    while aux.size() > 0:
        cola_notif.arrive(aux.attention())

    while cola_notif.size() > 0:
        print(cola_notif.attention())   

# cola_notif = cargar_notificaciones()
#print('cola sin notificaciones de facebook')
#eliminar(cola_notif)

def mostrar_tw_py(cola_notif):
    print("mostrar twitter con python")
    aux = Queue()
    while cola_notif.size() > 0:
        notif = cola_notif.attention()
        if notif.aplicacion == "Twitter" and "Python" in notif.mensaje:
            print(notif)
        aux.arrive(notif)

    while aux.size()> 0:
        cola_notif.arrive(aux.attention())

#cola_notif = cargar_notificaciones()
#print('notificaciones de tw con mensaje python')
#mostrar_tw_py(cola_notif)

def notif_temp(cola_notif):
    print("notificaciones entre 11:43 y 15:57")
    aux = Queue()
    pila = Stack()
    contador = 0

    while cola_notif.size() > 0:
        notif = cola_notif.attention()
        if "11:43" < notif.hora < "15:57":
            pila.push(notif)
            contador += 1
            print(notif)

        aux.arrive(notif)

    while aux.size() > 0:
        cola_notif.arrive(aux.attention())
    
    print(f'notificaciones entre las 11:43 y las 15:57: {contador} ')
    return pila

cola = cargar_notificaciones()
eliminar(cola)

cola = cargar_notificaciones()
mostrar_tw_py(cola)

cola = cargar_notificaciones()
notif_temp(cola)