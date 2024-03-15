from automovil import Automovil
from bicicleta import Bicicleta
from moto import Moto
from camion import Camion

seat = Automovil(4, "blanco")
seat.info()
trek = Bicicleta(2, "roja")
trek.info()
kawasaki = Moto(2, "roja")
kawasaki.info()
rover = Camion(6, "blanco")
rover.info()