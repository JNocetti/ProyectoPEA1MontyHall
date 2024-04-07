import random

## Función que crea las puertas con un random seleccionado
def crearPuertas():
    puertas = []
    num = random.randint(0,2)
    for i in range(3):
        if (i == num):
            puertas.append(1)
        else:
            puertas.append(0)
    return puertas


def montyHall():
    puertas = crearPuertas()
    seleccion = random.randint(0, 2)
    
    print("Su selección es:", seleccion)

    puertas_sin_auto = []

    for i in range(3):
        if i != seleccion and puertas[i] == 0:
            puertas_sin_auto.append(i)

    if len(puertas_sin_auto) == 2:
        # la funcion random.choice() elige un elemento aleatorio de una lista
        puerta_abierta = random.choice(puertas_sin_auto)
    else:
        puerta_abierta = puertas_sin_auto[0]

    print("La puerta", puerta_abierta, "no tiene el premio")

    print("Desea cambiar de puerta? Responda si o no")
    eleccion = input().lower()

    if "si" in eleccion:
        for i in range(3):
            if i != seleccion and i != puerta_abierta:
                seleccion = i
                break

    if puertas[seleccion] == 1:
        print("¡Felicidades, ha ganado!")
        return True
    else:
        print("Lo siento, ha perdido")
        return False

def MontyHallCambiaPuerta():
    puertas = crearPuertas()
    seleccion = random.randint(0, 2)
    
    puertas_sin_auto = []

    for i in range(3):
        if i != seleccion and puertas[i] == 0:
            puertas_sin_auto.append(i)

    if len(puertas_sin_auto) == 2:
        # la funcion random.chocie() elige un elemento aleatorio de una lista
        puerta_abierta = random.choice(puertas_sin_auto)
    else:
        puerta_abierta = puertas_sin_auto[0]
    
    for i in range(3):
            if i != seleccion and i != puerta_abierta:
                seleccion = i
                break

    if puertas[seleccion] == 1:
        return True
    else:
        return False

    
def MontyHallNoCambiaPuerta():
    puertas = crearPuertas()
    seleccion = random.randint(0, 2)

    if puertas[seleccion] == 1:
        return True
    else:
        return False


   