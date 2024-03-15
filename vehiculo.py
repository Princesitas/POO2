class Vehiculo:
    def __init__(self, ruedas:int, color:str)->None:
        self.ruedas = ruedas
        self.color = color

    def info(self)->None:
        print(self.ruedas, self.color)


if __name__ == "__main__":
    seat = Vehiculo(4, "blanco")