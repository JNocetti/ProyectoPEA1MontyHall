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

    print("--------------")
    print("Iteracion de", limite, "veces cambiando de puerta")
    print("Cantidad de veces que ganó:", cantidad_ganadas, ", Frecuencia relativa = ",cantidad_ganadas/limite, ", Porcentaje: ",int(cantidad_ganadas/limite*100),"%")
    print("Cantidad de veces que perdió:", cantidad_perdidas, ", Frecuencia relativa = ",cantidad_perdidas/limite, ", Porcentaje: ",int(cantidad_perdidas/limite*100),"%")
    print("--------------")

def iterarNoCambiaPuerta(limite):
    cantidad_ganadas = 0
    cantidad_perdidas = 0
    for i in range(limite):
        if utils.MontyHallNoCambiaPuerta() == True:
            cantidad_ganadas += 1
        else:
            cantidad_perdidas += 1
    
    print("--------------")
    print("Iteracion de", limite, "veces sin cambiar de puerta")
    print("Cantidad de veces que ganó:", cantidad_ganadas, ", Frecuencia relativa = ",cantidad_ganadas/limite, ", Porcentaje: ",int(cantidad_ganadas/limite*100),"%")
    print("Cantidad de veces que perdió:", cantidad_perdidas, ", Frecuencia relativa = ",cantidad_perdidas/limite, ", Porcentaje: ",int(cantidad_perdidas/limite*100),"%")
    print("--------------")

iterarCambiaPuerta(1000)
iterarCambiaPuerta(10000)
iterarCambiaPuerta(100000)
iterarNoCambiaPuerta(1000)
iterarNoCambiaPuerta(10000)
iterarNoCambiaPuerta(100000)

        


