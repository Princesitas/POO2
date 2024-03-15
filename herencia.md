## Ejercicio 1
```mermaid
classDiagram
    note "Vehículos de Transporte"
    Transporte <|-- Guagua
    
    Transporte : +int ruedas
    Transporte : +int asientos
    Transporte: +desplazar()
    Transporte: +informacion()
```

- intercity = Guagua
- lanzaroteBus = Guagua

## Ejercicio 2
```mermaid
classDiagram
    note "Vehículo"
    Vehículo <|-- Automovil
    Automovil <|-- Camión
    Vehículo <|-- Bicicleta
    Bicicleta <|-- moto
    
    Vehículo : +int ruedas
    Vehículo : +str color
    Vehículo: +info()
```

## Ejercicio 3
Escribir una clase que convierta un número entero en número romano

opción b: número romano a número entero