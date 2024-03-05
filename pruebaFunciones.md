### Parámetro posicional
def tipicaFuncion(unpar:str, dospar:str)->None:
#def tipicaFuncion(unpar:str, dospar:str, /)->None:         # Cuidado con el caracter "/"
    pass

tipicaFuncion("3", "6")
#unpar = "3"
#dospar = "6"


### Parámetro con valor por defecto
def tipicaFuncion(unpar:str, dospar = 6:str)->None:
    pass

tipicaFunciona("3")
#unpar = "3"
#dospar = "6"


### Parámetro arbitrario
def tipicaFuncion(unpar:int, *dospar:int, content:int)->str:
    pass

tipicaFuncion(3, 6, 6, 6, content=3)


### Parámetro nominal
def tipicaFuncion(unpar:str, dospar:str)->None:
    pass

tipicaFuncion(unpar=3, dospar=6)
#unpar = 3
#dospar = 6