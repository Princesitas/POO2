class Transporte:
    def __init__(self, *, ruedas:int, asientos:int) -> None:
        self.ruedas = ruedas
        self.asientos = asientos

    def desplazar(self, x:int, y:int = 0) -> None:
        print("Desplazando a: ", x, y)

    def informacion(self) -> None:
        print("Ruedas: ", self.ruedas, " Asientos: ", self.asientos)