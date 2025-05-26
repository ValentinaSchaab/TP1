from queue import Queue

class Personaje:
    def __init__(self, nombre, superheroe, genero):
        self.nombre = nombre
        self.superheroe = superheroe
        self.genero = genero

    def __str__(self):
        return f"Nombre:{self.nombre}, Superheroe:{self.superheroe}, Genero:{self.genero}"

personajes = Queue()

personajes.arrive(Personaje("tony stark", "iron man", "m"))
personajes.arrive(Personaje("steve rogers", "capitan america", "m"))
personajes.arrive(Personaje("natasha romanoff", "black widow", "f"))
personajes.arrive(Personaje("carol danvers", "capitana marvel", "f"))
personajes.arrive(Personaje("scott lang", "ant man", "m"))

def buscar_nombre(cola, superheroe):
    aux = Queue()

    while cola.size() > 0:
        personaje = cola.attention()
        if personaje.superheroe == superheroe:
            print("el nombre de", superheroe, "es ", personaje.nombre)
        aux.arrive(personaje)

    while aux.size() > 0:
        cola.arrive(aux.attention())


def super_genero(cola, genero):
    aux = Queue()

    while cola.size() > 0:
        personaje = cola.attention()
        if personaje.genero == genero:
            print("los nombres de superheroe ", genero, " son ", personaje.superheroe)
        aux.arrive(personaje)

    while aux.size() > 0:
        cola.arrive(aux.attention())

def nombre_genero(cola, genero):
    aux = Queue()

    while cola.size() > 0:
        personaje = cola.attention()
        if personaje.genero == genero:
            print("los nombres de los personajes ", genero, " son ", personaje.nombre)
        aux.arrive(personaje)

    while aux.size() > 0:
        cola.arrive(aux.attention())

def buscar_superheroe(cola, nombre):
    aux = Queue()

    while cola.size() > 0:
        personaje = cola.attention()
        if personaje.nombre == nombre:
            print("si se encuentra en la cola")
            print("el personaje ", nombre, "es ", personaje.superheroe)

        aux.arrive(personaje)

    while aux.size() > 0:
        cola.arrive(aux.attention())

def mostrar_s(cola):
    aux = Queue()
    while cola.size() > 0:
        personaje = cola.attention()
        if personaje.nombre[0] == "s" or personaje.superheroe[0] == "s":
            print(personaje)

        aux.arrive(personaje)

    while aux.size() > 0:
        cola.arrive(aux.attention())


# punto a
buscar_nombre(personajes, "capitana marvel")
# punto b
super_genero(personajes, "f")
# punto c
nombre_genero(personajes, "m")
# punto d
buscar_superheroe(personajes, "scott lang")
# punto e
mostrar_s(personajes)
# punto d
buscar_superheroe(personajes,"carol danvers")