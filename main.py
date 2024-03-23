import utils
import random

utils.MontyHall()
puertas = utils.crearPuertas()
## Persona selecciona puerta
puertaSeleccionada = random.randit(0,2)
chekSeleccion = utils.chekSeleccion(puertaSeleccionada, puertas)

