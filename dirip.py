ERRORNUMBITS      = 1
ERRORNUMBITSMSG   = "Número de bits incorrecto"

ERRORBITS      = 2
ERRORBITSMSG   = "El string contiene caracteres distintos al 0 ó 1"

BINVALUES      = [128, 64, 32, 16, 8, 4, 2, 1]

def verifyDec8bit(theInput:int)->bool:
    if 0 <= theInput and 255 >= theInput:
        return True
    return False

def verifyBinaryString(theInput:str)->int:
    if len(theInput) != 8:
        return ERRORNUMBITS

    for car in theInput:
        if car != "0" and car != "1":
            return  ERRORBITS

def convertBinDec(theInput:str)->int: #int between 0-255
    result = 0

    for i in range(len(theInput)):
        
        if theInput[i] == '1':
            result += BINVALUES[i]

    return result

entrada = int(input("Introducir un número entre 0 y 255\n"))
verifyResult = verifyDec8bit(entrada)



# entrada = input("Introducir 8 bit\n")
# verifyResult = verifyBinaryString(entrada)

# if verifyResult == ERRORNUMBITS:
#     print(ERRORNUMBITSMSG)
#     exit(-1)
# elif verifyResult == ERRORBITS:
#     print(ERRORBITSMSG)
#     exit(-2)

# print(convertBinDec(entrada))

# print(entrada)