superheroes = [
    "Iron Man", "Hulk", "Thor", "Black Widow", "Hawkeye",
    "Capitan America", "Spider Man", "Doctor Strange", "Black Panther",
    "Ant-Man", "Wasp", "Scarlet Witch", "Vision", "Falcon", "Winter Soldier"
]

# punto 1
def buscar_superheroe(lista, nombre, index=0):
    if index >= len(lista):
        return False
    if lista[index] == nombre:
        return True
    return buscar_superheroe(lista, nombre, index + 1)

encontrado = buscar_superheroe(superheroes, "Capitan America")
if encontrado:
    print("esta capitan america en la lista")
else:
    print("no esta capitan america en la lista")

# punto 2
def listar_superheroes(lista, index=0):
    if index >= len(lista):
        return
    print(lista[index])
    listar_superheroes(lista, index + 1)

print("Listado de superhéroes:")
listar_superheroes(superheroes)