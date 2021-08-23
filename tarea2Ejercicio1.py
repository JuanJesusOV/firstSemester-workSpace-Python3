"""
Ejercicio:
    Escribe un programa que calcule el IMC (Índice de Masa Corporal) de una persona, el cual se 
    utiliza para determinar si la proporción de peso y altura es adecuada. El IMC se puede calcular utilizando la siguiente fórmula:

    índice = peso / altura**2

    Donde el peso debe darse en kilogramos y la altura en metros. La siguiente tabla muestra cómo se 
    clasifican los diferentes rangos de índice:

    Rango de índice          Descripción
    índice < 20              'PESO BAJO'
    20 <= índice < 25        'NORMAL'
    25 <= índice < 30        'SOBREPESO'
    30 <= índice < 40        'OBESIDAD'
    40 >= índice             'OBESIDAD MORBIDA'

Algoritmo:
    Inicio
        Escribir "Ingresa tu peso"
        Leer peso
        Escribir "Ingresa tu altura"
        Leer altura
        indice = peso / altura**2
        si indice < 20
            Escribir "PESO BAJO"
        sino (indice < 25 && indice >= 20)
            Escribir "NORMAL"
        sino (indice < 30 && indice >=25)
            Escribir "SOBREPESO"
        sino (indice < 40 && indice >= 30)
            Escribir "OBESIDAD"
        sino (indice >= 40)
            Escribir "OBESIDAD MORBIDA"
    Fin

Casos de prueba:
    peso        altura      impresiónEnPantalla
    70          1.70        NORMAL
    88          1.60        OBESIDAD 
"""
peso = float(input("Ingresa tu peso (kg): "))
altura = float(input("Ingresa tu altura (m): "))

indice = peso / altura**2

if indice < 20:
    print("PESO BAJO")
elif (indice < 25 and indice >= 20):
    print("NORMAL")
elif (indice < 30 and indice >=25):
    print("SOBREPESO")
elif (indice < 40 and indice >= 30):
    print("OBESIDAD")
elif (indice >= 40):
    print("OBESIDAD MORBIDA")