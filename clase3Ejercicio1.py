"""
Ejercicio 1:
    El área y volumen de una esfera se calcula con las siguientes fórmulas:
    área =  4 * π * r^2
    volumen = 4/3 * π * r^3
    Escribe un programa que pida el valor del radio y muestre su área y su volumen.

Algoritmo:
    Inicio
        Escribir "Ingresa el valor del radio: "
        Leer radio
        area = 3.1416 * radio * radio
        volumen = 4/3 * 3.1416 * radio * radio * raio
        Escribir "El area es: ", area
        Escribir "El volumen es: ", volmen
    Fin

Casos de prueba:
    radio   area        volumen
    5       78.54       523.61
    18      1017.88     24429.02
"""

import math

radio = float(input("Ingresa el valor del radio: "))

area = (math.pi) * (math.pow(radio, 2))
volumen = (4/3) * (math.pi) * (math.pow(radio, 3))

print("El area del circulo es de {:.2f}u^2, y el volumen {:.2f}u^3".format(area, volumen))