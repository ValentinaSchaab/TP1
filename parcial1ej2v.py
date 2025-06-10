from list_ import List
from queue import Queue
from superheroes import superheroes

def order_by_name(item):
    return item.name

def order_by_real_name(item):
    return item.real_name or ""

def order_by_first_appearance(item):
    return item.first_appearance

class Superhero:
    
    def __init__(self, name, alias, real_name, short_bio, first_appearance, is_villain):
        self.name = name
        self.alias = alias
        self.real_name = real_name
        self.short_bio = short_bio
        self.first_appearance = first_appearance
        self.is_villain = is_villain
        

    def __str__(self):
        return f"{self.name}, {self.real_name} - {self.is_villain}"

list_superhero = List()
list_superhero.add_criterion('name', order_by_name)
list_superhero.add_criterion('real_name', order_by_real_name)
list_superhero.add_criterion('first_appearance', order_by_first_appearance)

for superhero in superheroes:
    hero = Superhero(
        name=superhero["name"],
        alias=superhero["alias"],
        real_name=superhero["real_name"],
        short_bio=superhero["short_bio"],
        first_appearance=superhero["first_appearance"],
        is_villain=superhero["is_villain"],
    )
    list_superhero.append(hero)

# punto 1
def ordenar(lista,criterio):
    lista.sort_by_criterion(criterio)
    lista.show()

print("listado ordenado ascendente por nombre")
ordenar(list_superhero,"name")

# punto 2
def posicion(lista,nombre):
    pos = lista.search(nombre, "name")
    print(nombre, " esta en la posicion ", pos)

posicion(list_superhero, "The Thing")
posicion(list_superhero,"Rocket Raccoon")

# punto 3
def villanos(lista):
    print("listado de villanos")
    for personaje in lista:
        if personaje.is_villain:
            print(personaje)

villanos(list_superhero)

# punto 4
def villanos_cola(lista):
    cola = Queue()

    for personaje in lista:
        if personaje.is_villain:
            cola.arrive(personaje)

    while cola.size() > 0:
        villano = cola.attention()
        if villano.first_appearance < 1980:
            print(villano)

print("villanos que aparecieron antes de 1980")
villanos_cola(list_superhero)

# punto 5
def super_iniciales(lista,letra):
    print("superheroes que comienzan con ", letra)

    for personaje in lista:
        if personaje.name.startswith(letra):
            print(personaje)

super_iniciales(list_superhero,"Bl")
super_iniciales(list_superhero,"G")
super_iniciales(list_superhero,"My")
super_iniciales(list_superhero,"W")

# punto 6
print("listado ordenado ascendente por nombre real")
ordenar(list_superhero,"real_name")

# punto 7
print("listado de superheroes ordenado por fecha de aparicion")
ordenar(list_superhero,"first_appearance")

# punto 8
def modificar(lista,rnombre,nuevor):
    for personaje in lista:
        if personaje.name == rnombre:
            personaje.real_name = nuevor

modificar(list_superhero, "Ant Man", "Scott Lang")
for p in list_superhero:
    print(p)

# punto 9
def biografia(lista):
    for personaje in lista:
        bio = personaje.short_bio.lower()
        if "time-traveling" in bio or "suit" in bio:
            print(personaje)

print("personajes que en su biografia tienen la palabra time-traveling o suit")
biografia(list_superhero)

# punto 10
def eliminar(lista, nombre):
    eliminado = lista.delete_value(nombre, "name")
    if eliminado:
        print("Personaje eliminado: ")
        print(eliminado.name," - ", eliminado.alias," - ", eliminado.real_name," - ", eliminado.short_bio," - ", eliminado.first_appearance," - ", eliminado.is_villain)
    else:
        print("No se encontró al personaje", nombre)

eliminar(list_superhero,"Electro")
eliminar(list_superhero,"Baron Zemo")