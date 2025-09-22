from list_ import List

class Superhero:
    def __init__(self, name, year, casa, bio):
        self.name = name
        self.year = year
        self.casa = casa
        self.bio = bio

    def __str__(self):
        return f"name:{self.name}, year: {self.year}, casa:{self.casa}, bio:{self.bio}"
    
def order_by_name(hero):
    return hero.name

# lista y criterio principal
lista_superheroes = List()
lista_superheroes.add_criterion('name', order_by_name)

lista_superheroes.append(Superhero("Batman", 1939, "DC", "Dark Knight"))
lista_superheroes.append(Superhero("Iron Man", 1963, "Marvel", "Armadura"))
lista_superheroes.append(Superhero("Linterna Verde", 1940, "DC", "Green Power"))
lista_superheroes.append(Superhero("Star-lord", 1962, "Marvel", "Araña"))
lista_superheroes.append(Superhero("Wolverine", 1974, "Marvel", "Mutante con garras"))
lista_superheroes.append(Superhero("Dr Strange", 1960, "DC", "Mutante con garras"))
lista_superheroes.append(Superhero("Capitana marvel", 1965, "Marvel", "Mutante con garras"))
lista_superheroes.append(Superhero("Mujer maravilla", 1980, "DC", "hola traje"))
lista_superheroes.append(Superhero("Flash", 1950, "DC", "haaaaa"))


print("lista completa")
lista_superheroes.show()

# punto a
def eliminar(lista):
    eliminar = lista.delete_value("Linterna Verde", "name")
    print("eliminado", eliminar)


print("lista despues de eliminar linterna verde")
eliminar(lista_superheroes)
lista_superheroes.show()

#punto b
def mostrar_aparicion(lista):
    indice = lista.search("Wolverine","name")

    if indice is not None:
        print("año de aparicion de wolverine:", lista[indice].year)
    else:
        print("wolverine no esta en la lista")

mostrar_aparicion(lista_superheroes)

# punto c
def cambiar_casa(lista):

    indice = lista.search("Dr Strange", "name")

    if indice is not None:
        lista[indice].casa = "Marvel"
    else:
        print("no se encuentra el personaje")

cambiar_casa(lista_superheroes)
lista_superheroes.show()

# punto d
def mostrar_traje_armadura(lista):
    print("superheroes con traje o armadura en su biografia")

    for heroe in lista:
        bio = heroe.bio.lower()
        if "traje" in bio or "armadura" in bio:
            print(heroe.name)

mostrar_traje_armadura(lista_superheroes)

# punto e
def aparicion(lista):
    print("nombre y casa de superheroes con aparición anterior a 1963")
    encontrados = False 

    for heroe in lista:

        if heroe.year < 1963:
            print(heroe.name, heroe.casa)
            encontrados = True

    if encontrados == False:
        print("no hay superheroes con fecha menor")
    
aparicion(lista_superheroes)

# punto f
def puntof(lista,super):
    print("casa de ", super)

    indice = lista.search(super, "name")

    if indice is not None:
        print("casa a la que pertenece:", lista[indice].casa)
    else:
        print("no se encontro ", super)

puntof(lista_superheroes,"Capitana marvel")
puntof(lista_superheroes,"Mujer maravilla")

# punto g
def mostrar_info(lista,superheroe):
    print("info completa de ", superheroe)

    indice = lista.search(superheroe,"name")

    if indice is not None:
        print(lista[indice])
    else:
        print("no se encontro ", superheroe)

mostrar_info(lista_superheroes,"Flash")
mostrar_info(lista_superheroes,"Star-lord")

# punto h
def listabms(lista):
    print("superheroes que comienzan con B M o S")

    for heroe in lista:
        if heroe.name.startswith(("B","M","S")):
            print(heroe.name)

listabms(lista_superheroes)

# punto i
def cant_casas(lista):
    contadorMARVEL = 0
    contadorDC = 0

    for heroe in lista:
        if heroe.casa == "Marvel":
            contadorMARVEL +=1
        else:
            contadorDC +=1

    print("cantidad de superheroes en marvel:", contadorMARVEL)
    print("cantidad de superheroes en DC:", contadorDC)


cant_casas(lista_superheroes)