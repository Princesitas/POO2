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


### Ejercicio 3
def myDiv(id:str, *clas:str, contet:str)->str:
    resultado = ""
    resultado += '<div id="' + id + '

    if len(clas) != 0:
        resultado += 'class="'
        for e in clas:
            resultado += e +', '
        
        resultado += '\b\b"'

    resultado += '>' + content + '</div>'

    return resultado


### Ejercicio 5

def myScript(*src=str)->str:
Función que tiene como entrada un número indeterminado de cadenas de caracteres
y como salida de una cadena de caracteres. Probablemente transforma las entradas en la salida
