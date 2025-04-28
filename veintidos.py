def fuerza(mochila, objetos_sacados=0):

    if not mochila:
        return False, objetos_sacados
    
    objeto = mochila.pop(0)
    objetos_sacados += 1
    
    if objeto == "sable de luz":
        return True, objetos_sacados
    else:
        return fuerza(mochila, objetos_sacados)

mochila = ["botella", "comida", "ropa", "sable de luz", "piedra"]
encontro_sable, cantidad_objetos = fuerza(mochila.copy())

if encontro_sable:
    print(f"Encontramos el sable de luz sacando {cantidad_objetos} objetos")
else:
    print("No encontramos el sable de luz")
