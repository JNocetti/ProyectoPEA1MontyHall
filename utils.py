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

def chequearSeleccion(seleccion, puertas):
    if (puertas[seleccion] == 1):
        return True
    return False

def demostrarPuerta(eleccion,seleccion,puertas):
    cont = 0
    if(eleccion):
        num = random.randint(0,1)
        for i in puertas:
            if (num == 0):
                if(i == num & i != seleccion):
                    puertas.remove(i)
                    break
            else:
                if (cont != 0 & i == 0):
                    puertas.remove(i)
                    break
                elif (i == 0):
                    cont += 1

            
            
        
        











