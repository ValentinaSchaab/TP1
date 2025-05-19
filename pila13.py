from stack import Stack

# Clase trajes
class Traje:
    def __init__(self, modelo, pelicula, estado):
        self.modelo = modelo
        self.pelicula = pelicula
        self.estado = estado

    def __str__(self):
        return f"modelo: {self.modelo}, Película: {self.pelicula}, Estado: {self.estado}"

pila_trajes = Stack()

pila_trajes.push(Traje("mark I", "iron man", "dañado"))
pila_trajes.push(Traje("mark V","iron man 2", "destruido"))
pila_trajes.push(Traje("mark XLII","iron man 3","destruido"))
pila_trajes.push(Traje("mark L","avengers infinity mar","dañado"))
pila_trajes.push(Traje("mark LXXXV","avengers endgame","impecable"))
# punto D
pila_trajes.push(Traje("mark XLIV (Hulkbuster)", "avengers: age of ultron", "dañado"))
pila_trajes.push(Traje("mark XLIV (Hulkbuster)", "avengers: endgame", "destruido")) # modelos en mas de una peli
pila_trajes.push(Traje("mark L", "avengers: endgame", "dañado"))        # misma peli q mark LXXXV

print("trajes en la pila")
pila_trajes.show()
# punto A
def buscar_modelo(pila, modelo_buscado):
    aux = Stack()
    peliculas = []

    while pila.size()> 0:
        traje = pila.pop()
        if traje.modelo == modelo_buscado:
            peliculas.append(traje.pelicula)
        aux.push(traje)

    while aux.size()> 0:
        pila.push(aux.pop())

    return peliculas

peliculas = buscar_modelo(pila_trajes, "mark XLIV (Hulkbuster)")
if peliculas:
    print("el modelo mark XLIV (Hulkbuster) fue usado en: ")
    for peli in peliculas:
        print(" - ", peli)
else:
    print ("el modelo mark XLIV (Hulkbuster) no fue usado")

# punto B
def modelos_dañados(pila):
    aux = Stack()
    dañados = []

    while pila.size() > 0:
        traje = pila.pop()
        if traje.estado == "dañado":
            dañados.append(traje.modelo)
        aux.push(traje)

    while aux.size() > 0:
        pila.push(aux.pop())

    if dañados:
        print ("modelos dañados")
        for modelo in dañados:
            print("-", modelo)
    else:
        print("no hay modelos dañados")

modelos_dañados(pila_trajes)

# punto C
def trajes_destruidos(pila):
    aux = Stack()
    eliminados = []

    while pila.size() > 0:
        traje = pila.pop()
        if traje.estado == "destruido":
            eliminados.append(traje.modelo)
        else:
            aux.push(traje)

    while aux.size() > 0:
        pila.push(aux.pop())

    if eliminados:
        print("se eliminaron los siguientes trajes: ")
        for modelo in eliminados:
          print ("-", modelo)
    else:
         print("no habia trajes destruidos")

trajes_destruidos(pila_trajes)

#punto e
def agregar_traje(pila, modelo, pelicula, estado):
    aux = Stack()
    existe = False

    while pila.size() > 0:
        traje = pila.pop()
        if traje.modelo == modelo and traje.pelicula == pelicula:
            existe = True
        aux.push(traje)
    
    while aux.size() > 0:
        pila.push(aux.pop())

    if existe == False:
        pila.push(Traje(modelo, pelicula, estado))
        print(f"se agrego el traje: {modelo} en '{pelicula}'")
    else:
        print(f"ya existe el traje {modelo} en '{pelicula}', no se agrega")
        
agregar_traje(pila_trajes,"mark LXXXV", "avengers endgame", "impecable")

#punto f
def trajes_utilizados(pila,pelicula):
    aux = Stack()
    masutilizados = []

    while pila.size() > 0:
        traje = pila.pop()
        if traje.pelicula == "spider-man: homecoming" or traje.pelicula == "capitan america: civil war":
            masutilizados.append(traje.modelo)
        aux.push(traje)

    while aux.size() > 0:
        pila.push(aux.pop())

    if masutilizados:
        print("modelos de trajes utilizados en esas peliculas")
        for modelo in masutilizados:
            print("-", modelo)
    else:
        print("no se encontraron trajes en esas eliculas")

pelis = ["Spider-Man: Homecoming", "Capitan America: Civil War"]
trajes_utilizados(pila_trajes, pelis)