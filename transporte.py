class Transporte:
    
    def __init__(self, *, ruedas:int, asientos:int):
        self.ruedas = ruedas
        self.asientos = asientos
        

    def desplazar(self, x:int, y:int) -> None:
        print("Desplazando a:", x, y)

    def informacion(ruedas:int, asientos:int):
        print(ruedas, asientos)