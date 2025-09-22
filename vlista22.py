from list_ import List

class Jedi:
    def __init__(self, nombre, maestros, colores, especie):
        self.nombre = nombre
        self.maestros = maestros          # lista de nombres
        self.colores = colores            # lista de colores de sable
        self.especie = especie

    def __str__(self):
        return (f"nombre:{self.nombre}, especie:{self.especie}, maestros:{self.maestros}, colores:{self.colores}")

# criterios de ordenamiento
def order_by_name(jedi):
    return jedi.nombre

def order_by_especie(jedi):
    return jedi.especie

# lista y criterio principal
lista_jedi = List()
lista_jedi.add_criterion('nombre', order_by_name)
lista_jedi.add_criterion('especie', order_by_especie)

lista_jedi.append(Jedi("Ahsoka Tano", ["Anakin Skywalker"], ["Verde", "Azul", "Blanco"], "Togruta"))
lista_jedi.append(Jedi("Kit Fisto", ["Yoda"], ["Verde"], "Nautolano"))
lista_jedi.append(Jedi("Luke Skywalker", ["Obi-Wan Kenobi", "Yoda"], ["Verde"], "Humano"))
lista_jedi.append(Jedi("Yoda", [], ["Verde"], "Desconocida"))
lista_jedi.append(Jedi("Anakin Skywalker", ["Obi-Wan Kenobi"], ["Azul"], "Humano"))
lista_jedi.append(Jedi("Qui-Gon Jin", ["Conde Dooku"], ["Verde"], "Humano"))
lista_jedi.append(Jedi("Mace Windu", ["Cyslin Myr"], ["Violeta"], "Humano"))
lista_jedi.append(Jedi("Luminara Unduli", ["Yoda"], ["Verde"], "Mirialana"))
lista_jedi.append(Jedi("Barriss Offee", ["Luminara Unduli"], ["Azul"], "Mirialana"))
lista_jedi.append(Jedi("Aayla Secura", ["Quinlan Vos"], ["Azul"], "Twi'lek"))
lista_jedi.append(Jedi("Rey", ["Leia Organa"], ["Azul", "Amarillo"], "Humano"))
lista_jedi.append(Jedi("Ezra Bridger", ["Kanan Jarrus"], ["Azul", "Verde"], "Humano"))

print("lista completa:")
lista_jedi.show()

# punto a 
def listado_ordenado(lista):
    print("listado ordenado por nombre:")
    lista.sort_by_criterion("nombre")
    lista.show()

    print("listado ordenado por especie:")
    lista.sort_by_criterion("especie")
    lista.show()

listado_ordenado(lista_jedi)

# punnto b 
def mostrar_info(lista, nombre):
    print("info de ", nombre)
    indice = lista.search(nombre, "nombre")
    if indice is not None:
        print(lista[indice])
    else:
        print("no se encontro")

mostrar_info(lista_jedi, "Ahsoka Tano")
mostrar_info(lista_jedi, "Kit Fisto")

# punto c
def mostrar_padawans(lista, maestro):
    print("Padawans de ", maestro)
    encontrados = False
    for jedi in lista:
        if maestro in jedi.maestros:
            print(jedi.nombre)
            encontrados = True
    if not encontrados:
        print("no tiene padawans en la lista")

mostrar_padawans(lista_jedi, "Yoda")
mostrar_padawans(lista_jedi, "Luke Skywalker")

# punto d
def humanos_twi(lista):
    print("jedi humanos o twi'lek:")
    for jedi in lista:
        if jedi.especie.lower() in ["humano", "twi'lek"]:
            print(jedi.nombre, "-", jedi.especie)

humanos_twi(lista_jedi)

# punto e
def comienza_a(lista):
    print("jedi que comienzan con A:")
    for jedi in lista:
        if jedi.nombre.startswith("A"):
            print(jedi.nombre)

comienza_a(lista_jedi)

# punto f
def mas_deun_color(lista):
    print("jedi con más de un color de sable:")
    for jedi in lista:
        if len(jedi.colores) > 1:
            print(jedi.nombre, "-", jedi.colores)

mas_deun_color(lista_jedi)

# punto g
def amarillo_violeta(lista):
    print("jedi que usaron amarillo o violeta:")
    for jedi in lista:
        colores_lower = [c.lower() for c in jedi.colores]
        if "amarillo" in colores_lower or "violeta" in colores_lower:
            print(jedi.nombre, "-", jedi.colores)

amarillo_violeta(lista_jedi)

# punto h
def padawans(lista, maestro):
    print("padawans de ", maestro)
    encontrados = False
    for jedi in lista:
        if maestro in jedi.maestros:
            print(jedi.nombre)
            encontrados = True
    if not encontrados:
        print("no tuvo padawans en la lista.")

padawans(lista_jedi, "Qui-Gon Jin")
padawans(lista_jedi, "Mace Windu")