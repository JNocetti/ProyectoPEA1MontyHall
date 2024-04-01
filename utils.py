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
    puertas  = crearPuertas()
    seleccion = random.randint(0,2)
    puertasSinAuto = []
    for i in range(3):
        if (i != seleccion & puertas[i] == 0):
            puertasSinAuto.append(i)
    puertaAbierta = random.randint(0,1)
    print("La puerta ",puertasSinAuto[puertaAbierta]," no tiene el premio")
    print("Desea cambiar de puerta?")
    eleccion = input()
    
        





            
            
        
        











