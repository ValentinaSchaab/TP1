from tree import BinaryTree

# Lista de criaturas
criaturas = [
    {"name": "Ceto", "derrotado_por": None, "descripcion": "", "capturada": None},
    {"name": "Tifón", "derrotado_por": "Zeus", "descripcion": "", "capturada": None},
    {"name": "Equidna", "derrotado_por": "Argos Panoptes", "descripcion": "", "capturada": None},
    {"name": "Dino", "derrotado_por": None, "descripcion": "", "capturada": None},
    {"name": "Pefredo", "derrotado_por": None, "descripcion": "", "capturada": None},
    {"name": "Enio", "derrotado_por": None, "descripcion": "", "capturada": None},
    {"name": "Escila", "derrotado_por": None, "descripcion": "", "capturada": None},
    {"name": "Caribdis", "derrotado_por": None, "descripcion": "", "capturada": None},
    {"name": "Euríale", "derrotado_por": None, "descripcion": "", "capturada": None},
    {"name": "Esteno", "derrotado_por": None, "descripcion": "", "capturada": None},
    {"name": "Medusa", "derrotado_por": "Perseo", "descripcion": "", "capturada": None},
    {"name": "Ladón", "derrotado_por": "Heracles", "descripcion": "", "capturada": None},
    {"name": "Águila del Cáucaso", "derrotado_por": None, "descripcion": "", "capturada": None},
    {"name": "Quimera", "derrotado_por": "Belerefonte", "descripcion": "", "capturada": None},
    {"name": "Hidra de Lerna", "derrotado_por": "Heracles", "descripcion": "", "capturada": None},
    {"name": "León de Nemea", "derrotado_por": "Heracles", "descripcion": "", "capturada": None},
    {"name": "Esfinge", "derrotado_por": "Edipo", "descripcion": "", "capturada": None},
    {"name": "Dragón de la Cólquida", "derrotado_por": None, "descripcion": "", "capturada": None},
    {"name": "Cerbero", "derrotado_por": None, "descripcion": "", "capturada": None},
    {"name": "Cerda de Cromión", "derrotado_por": "Teseo", "descripcion": "", "capturada": None},
    {"name": "Ortro", "derrotado_por": "Heracles", "descripcion": "", "capturada": None},
    {"name": "Toro de Creta", "derrotado_por": "Teseo", "descripcion": "", "capturada": None},
    {"name": "Jabalí de Calidón", "derrotado_por": "Atalanta", "descripcion": "", "capturada": None},
    {"name": "Carcinos", "derrotado_por": None, "descripcion": "", "capturada": None},
    {"name": "Gerión", "derrotado_por": "Heracles", "descripcion": "", "capturada": None},
    {"name": "Cloto", "derrotado_por": None, "descripcion": "", "capturada": None},
    {"name": "Láquesis", "derrotado_por": None, "descripcion": "", "capturada": None},
    {"name": "Átropos", "derrotado_por": None, "descripcion": "", "capturada": None},
    {"name": "Minotauro de Creta", "derrotado_por": "Teseo", "descripcion": "", "capturada": None},
    {"name": "Harpías", "derrotado_por": None, "descripcion": "", "capturada": None},
    {"name": "Argos Panoptes", "derrotado_por": "Hermes", "descripcion": "", "capturada": None},
    {"name": "Aves del Estínfalo", "derrotado_por": None, "descripcion": "", "capturada": None},
    {"name": "Talos", "derrotado_por": "Medea", "descripcion": "", "capturada": None},
    {"name": "Sirenas", "derrotado_por": None, "descripcion": "", "capturada": None},
    {"name": "Pitón", "derrotado_por": "Apolo", "descripcion": "", "capturada": None},
    {"name": "Cierva de Cerinea", "derrotado_por": None, "descripcion": "", "capturada": None},
    {"name": "Basilisco", "derrotado_por": None, "descripcion": "", "capturada": None},
    {"name": "Jabalí de Erimanto", "derrotado_por": None, "descripcion": "", "capturada": None}
]


arbol = BinaryTree()

for criatura in criaturas:
    arbol.insert(criatura["name"], criatura)

# punto a
print("listado inorden de criaturas y quien las derroto:")

def inorden_derrotas(root):
    if root is not None:
        inorden_derrotas(root.left)
        print(f"{root.value} y derrotado por: {root.other_values['derrotado_por']}")
        inorden_derrotas(root.right)
    
inorden_derrotas(arbol.root)

# punto b.
criatura = arbol.search("Talos")
if criatura:
    criatura.other_values["descripcion"] = "Gigante de bronce"

# punto c.
print("información de Talos:")
nodo = arbol.search("Talos")
if nodo:
    print(nodo.value, nodo.other_values)
else:
    print("Talos no encontrado")

# punto d.
# Creamos un diccionario para contar cuántas criaturas derrotó cada héroe
derrotadores = {}

def contar_derrotadores(root):
    if root is not None:
        contar_derrotadores(root.left)

        # obtener quién derrotó a la criatura
        derrotado_por = root.other_values.get('derrotado_por')

        # si existe un derrotador, lo contamos
        if derrotado_por:
            if derrotado_por in derrotadores:
                derrotadores[derrotado_por] += 1
            else:
                derrotadores[derrotado_por] = 1

        contar_derrotadores(root.right)

contar_derrotadores(arbol.root)

# Convertimos el dicc en una lista ordenada por cantidad
top3 = sorted(derrotadores.items(), key=lambda x: x[1], reverse=True)[:3]

print("Los 3 héroes que derrotaron mas criaturas son:")
for nombre, cantidad in top3:
    print(f"{nombre}: {cantidad} criaturas derrotadas")

# punto e.
print("Criaturas derrotadas por Heracles:")

def derrotadas_por(root, nombre):
    if root is not None:
        derrotadas_por(root.left, nombre)
        if root.other_values["derrotado_por"] == nombre:
            print(root.value)
        derrotadas_por(root.right, nombre)

derrotadas_por(arbol.root, "Heracles")

# punto f.
print("criaturas no derrotadas:")

def no_derrotadas(root):
    if root is not None:
        no_derrotadas(root.left)
        if root.other_values["derrotado_por"] is None:
            print(root.value)
        no_derrotadas(root.right)

no_derrotadas(arbol.root)

# punto g. realizado

# punto h.
capturadas = ["Cerbero", "Toro de Creta", "Cierva de Cerinea", "Jabalí de Erimanto"]

for nombre in capturadas:
    nodo = arbol.search(nombre)
    if nodo:
        nodo.other_values["capturada"] = "Heracles"

# punto i.
def coincidencia(root, text: str):
    # Muestra las criaturas q el nombre contienen el texto
    if root is not None:
        coincidencia(root.left, text)
        if text.lower() in root.value.lower():
            print(f"{root.value} y derrotado por: {root.other_values.get('derrotado_por', 'Nadie')}")
        coincidencia(root.right, text)

texto = input("Ingrese parte del nombre de la criatura: ")
print("Resultados de búsqueda para: ", texto)
coincidencia(arbol.root, texto)

# punto j.
arbol.delete("Basilisco")
arbol.delete("Sirenas")

# punto k. modificar el nodo que contiene a las Aves del Estínfalo, agregando que Heracles derroto a varias
nodo = arbol.search("Aves del Estínfalo")
if nodo:
    nodo.other_values["derrotado_por"] = "Heracles derrotó a varias"

# punto L.
valor, otros = arbol.delete("Ladón")
if valor is not None:
    otros["name"] = "Dragón Ladón"
    arbol.insert("Dragón Ladón", otros)

# punto M.
print("listado por nivel:")
arbol.by_level()

# punto n.
def capturadas_por(root, heroe):
    if root is not None:
        capturadas_por(root.left, heroe)
        if root.other_values["capturada"] == heroe:
            print(root.value)
        capturadas_por(root.right, heroe)

print("Criaturas capturadas por Heracles:")
capturadas_por(arbol.root, "Heracles")


