from stack import Stack

# clase personajes
class Personaje:
    def __init__(self, nombre, peliculas):
        self.nombre = nombre
        self.peliculas = peliculas

    def __srt__(self):
        return f"nombre: {self.nombre}, películas: {self.peliculas}"

pila_personajes = Stack()

pila_personajes.push(Personaje("iron man", 10))
pila_personajes.push(Personaje("captain america", 9))
pila_personajes.push(Personaje("viuda negra (black widow)", 5))
pila_personajes.push(Personaje("rocket raccoon", 8))
pila_personajes.push(Personaje("hawkeye", 6))

# punto A
def buscar_posiciones(pila, nombres_buscados):
    aux = Stack()
    posiciones = {}
    posicion_actual = 1

    while pila.size() > 0:
        personaje = pila.pop()
        if personaje.nombre == "rocket raccoon" or personaje.nombre == "groot":
            posiciones[personaje.nombre] = posicion_actual
        aux.push(personaje)
        posicion_actual +=1

    while aux.size() > 0:
        pila.push(aux.pop())

    for nombre in nombres_buscados:
        if nombre in posiciones:
             print(f"{nombre} se encuentra en la posición {posiciones[nombre]}")
        else:
            print(f"{nombre} no se encuentra en la pila")

names = ["rocket raccoon", "groot"]
buscar_posiciones(pila_personajes, names)

# punto B
def participaciones(pila):
    aux = Stack()
    maspersonajes = []
    cantidad = []

    while pila.size() > 0:
        personaje = pila.pop()
        if personaje.peliculas > 5:
            maspersonajes.append(personaje.nombre)
            cantidad.append(personaje.peliculas)
        aux.push(personaje)

    while aux.size() > 0:
        pila.push(aux.pop())

    if maspersonajes:
        print("personajes con mas de 5 peliculas: ")
        for i in range(len(maspersonajes)):
            print(f"- {maspersonajes[i]}: {cantidad[i]} películas ")
    else:
        print("no hay personajes con mas de 5 peliculas")

participaciones(pila_personajes)        

#punto C
def viudanegra(pila):
    aux = Stack()
    participo = False
    cantidad = []

    while pila.size() > 0:
        personaje = pila.pop()
        if personaje.nombre == "viuda negra (black widow)":
            participo = True
            cantidad.append(personaje.peliculas)
        aux.push(personaje)    

    while aux.size() > 0:
        pila.push(aux.pop())

    if participo == True:
        print("la viuda negra (black widow) participo en: ", cantidad, "peliculas")
    else:
        print("la viuda negra (black widow) no participo en ninguna pelicula")
    

viudanegra(pila_personajes)

#punto D
def letras(pila):
    aux = Stack()
    existe = False
    nombrescdg = []

    while pila.size()> 0:
        personaje = pila.pop()
        if personaje.nombre.startswith(('c', 'd', 'g')): # verifica si empieza con alguna de esas letras
            existe = True
            nombrescdg.append(personaje.nombre)
        aux.push(personaje)

    while aux.size()> 0:
        pila.push(aux.pop())

    if existe == True:
        print("personajes que empiezan con c d y g: ", nombrescdg)
    else:
        print("no hay personajes que empiecen con c d y g")    

letras(pila_personajes)