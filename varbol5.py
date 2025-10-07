from tree import BinaryTree
from superheroes import superheroes

arbol = BinaryTree()

for personaje in superheroes:
    arbol.insert(personaje['name'], personaje)

# punto a. campo booleano

# punto b.
print("villanos ordenados alfabeticamente:")
arbol.villain_in_order()

# punto c
print("superheroes que empiezan con C")

def heroes_con_c(root):
    if root is not None:
        heroes_con_c(root.left)  # recorremos la izquierda
        if (
            root.value.startswith('C') and # verifica nombre con c
            root.other_values['is_villain'] == False  # verifica si es heroe
        ):
            print(root.value)
        heroes_con_c(root.right)  # recorremos la derecha

# Llamamos a la función pasando la raíz del árbol
heroes_con_c(arbol.root)

# punto d
cantidad_heroes = arbol.count_heroes()
print("cantidad total de superheroes: ", cantidad_heroes)

# punto e
print("Busco a Doctor Strange:")
arbol.proximity_search('Dr')  # muestra los que empiecen con "Dr"

# Borramos y reemplazamos el nombre
value, other_value = arbol.delete('Dr Strange')
if value is not None:
    # Corregimos el nombre en el diccionario
    other_value['name'] = 'Doctor Strange'
    # Lo volvemos a insertar con el nombre corregido
    arbol.insert('Doctor Strange', other_value)
    print("Nombre corregido")
else:
    print("No se encontró Dr Strange")

# punto f, in orden pero inverso.
def in_order_descendente(root):
    if root is not None:
        in_order_descendente(root.right)
        if root.other_values['is_villain'] is False:
            print(root.value)
        in_order_descendente(root.left)

print("Superhéroes ordenados de manera descendente:")
in_order_descendente(arbol.root)

# punto g
# separar en dos arboles (heroes y villanos)
arbol_heroes = BinaryTree()
arbol_villanos = BinaryTree()

arbol.divide_tree(arbol_heroes, arbol_villanos)
# I
# contar heroes con funcion
print("cantidad de nodos en el arbol heroes:", arbol_heroes.count_heroes())
#contar villanos
def count_villains(root):
    if root is None:
        return 0
    count = 1 if root.other_values["is_villain"] else 0
    return count + count_villains(root.left) + count_villains(root.right)

print("Cantidad de nodos en el árbol de villanos:", count_villains(arbol_villanos.root))

# II
print("Arbol de heroes en orden:")
arbol_heroes.in_order()

print("arbol de villanos en orden:")
arbol_villanos.in_order()
