"""
    Ejercicio 1:
        Desarrolla un programa en Python que calcule la distancia entre dos puntos del plano cartesiano.
    Entradas    
    El programa solicita el punto inicial (x1, y1) y el final (x2, y2). Todos enteros y en ese orden.
    Salida
    El valor de la distancia (numero flotante) que existe entre los dos puntos. Despliega el resultado con la palabra distancia (todo en minúsculas) y un = y el número formateado a 2 decimales (sin espacios entre caracteres y números). Por ejemplo: distancia=9.90
    
    Algoritmo:
        Inicio
            Escribir "Ingresa X1: "
            Escribir "Ingresa Y1: "
            Escribir "Ingresa X2: "
            Escribir "Ingresa Y2: "
            Leer x1
            Leer y1
            Leer x2
            Leer y2
            distancia = raizCuadrada((x2-x1)^2 + (y2-y1)^2)
            Escribir "Distancia = ", distancia
        Fin

    Casos de prueba:
        x1      x2      y1      y2      distancia
        2       -4      5       3       7.62
        7       9       -6      2       14.76
"""
import math

x1 = int(input("Ingresa X1: "))
y1 = int(input("Ingresa Y1: "))
x2 = int(input("Ingresa X2: "))
y2 = int(input("Ingresa Y2: "))

distancia = math.sqrt((math.pow((x2-x1),2)) + (math.pow((y2-y1),2)))

print("Distancia = {:.2f}".format(distancia))