class FileWriter:
    def __init__(self, fileName):
        self.fileName = fileName
        self.i = open(self.fileName, "w+", "r")

    def write(self,mensaje:str):
        self.iwrite(mensaje)

    def read(self)->str:
        self.i.close()


def main():
    prueba = FileWriter("fileWriter.txt")
    prueba.write("Hola")
    prueba.close()
    prueba = FileWriter("fileWriter.txt")
    prueba.read()
    prueba.close()