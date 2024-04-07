import utils
import random

def simularJuegoCambiandoDePuerta(veces):
    cantidad_ganadas = 0
    cantidad_perdidas = 0
    for i in range(veces):
        if utils.MontyHallCambiaPuerta() == True:
            cantidad_ganadas += 1
        else:
            cantidad_perdidas += 1

    
    print("\nIteracion ", veces)
    print("Cantidad de veces que ganó:", cantidad_ganadas, ", Frecuencia relativa = ",cantidad_ganadas/veces, ", Porcentaje de ganar: ",int(cantidad_ganadas/veces*100),"%")
    print("Cantidad de veces que perdió:", cantidad_perdidas, ", Frecuencia relativa = ",cantidad_perdidas/veces, ", Porcentaje de perder: ",int(cantidad_perdidas/veces*100),"%")
   

def simularJuegoSinCambiarDePuerta(veces):
    cantidad_ganadas = 0
    cantidad_perdidas = 0
    for i in range(veces):
        if utils.MontyHallNoCambiaPuerta() == True:
            cantidad_ganadas += 1
        else:
            cantidad_perdidas += 1
    

    print("\nIteracion de", veces)
    print("Cantidad de veces que ganó:", cantidad_ganadas, ", Frecuencia relativa = ",cantidad_ganadas/veces, ", Porcentaje de ganar: ",int(cantidad_ganadas/veces*100),"%")
    print("Cantidad de veces que perdió:", cantidad_perdidas, ", Frecuencia relativa = ",cantidad_perdidas/veces, ", Porcentaje de perder: ",int(cantidad_perdidas/veces*100),"%")
   

print("Simulación de Monty Hall cambiando de puerta \n")
simularJuegoCambiandoDePuerta(1000)
simularJuegoCambiandoDePuerta(10000)
simularJuegoCambiandoDePuerta(100000)
print("-------------------------------------------------------------------------------------------------")
print("\nSimulación de Monty Hall sin cambiar de puerta \n")
simularJuegoSinCambiarDePuerta(1000)
simularJuegoSinCambiarDePuerta(10000)
simularJuegoSinCambiarDePuerta(100000)

        


