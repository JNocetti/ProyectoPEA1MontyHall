import utils
import random

def iterarCambiaPuerta(limite):
    cantidad_ganadas = 0
    cantidad_perdidas = 0
    for i in range(limite):
        if utils.MontyHallCambiaPuerta() == True:
            cantidad_ganadas += 1
        else:
            cantidad_perdidas += 1
    print("Iteracion de", limite, "veces cambiando de puerta")
    print("Cantidad de veces que ganó:", cantidad_ganadas)
    print("Cantidad de veces que perdió:", cantidad_perdidas)

def iterarNoCambiaPuerta(limite):
    cantidad_ganadas = 0
    cantidad_perdidas = 0
    for i in range(limite):
        if utils.MontyHallNoCambiaPuerta() == True:
            cantidad_ganadas += 1
        else:
            cantidad_perdidas += 1
    print("Iteracion de", limite, "veces sin cambiar de puerta")
    print("Cantidad de veces que ganó:", cantidad_ganadas)
    print("Cantidad de veces que perdió:", cantidad_perdidas)

iterarCambiaPuerta(1000)
iterarCambiaPuerta(10000)
iterarCambiaPuerta(100000)
iterarNoCambiaPuerta(1000)
iterarNoCambiaPuerta(10000)
iterarNoCambiaPuerta(100000)

        


