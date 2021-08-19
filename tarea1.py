# Juan Jesús Ortiz Vazquez - A01639936
"""
Tarea 1:
    Realiza un programa que reciba las coordenadas de dos puntos y que calcule la pendiente de la recta que une esos dos puntos.
    La fórmula para calcular la pendiente es: m = (y2 - y1) / (x2 - x1)

Algoritmo:
    Inicio
        Escribir "Ingresa el valor de X1: "
        Leer x1
        Escribir "Ingresa el valor de Y1: "
        Leer y1
        Escribir "Ingresa el valor de X2: "
        Leer x2
        Escribir "Ingresa el valor de Y2: "
        Leer y2
        m = (y2 - y1) / (x2 - x1)
        Escribir "m = ",m
    Fin

Casos de prueba
    x1      y1      x2      y2      m
    3.6     -1.3    8.6     2.5     0.76
    -4      2       0       3       0.25
"""

x1 = float(input("Ingresa el valor de X1: "))
y1 = float(input("Ingresa el valor de Y1: "))
x2 = float(input("Ingresa el valor de X2: "))
y2 = float(input("Ingresa el valor de Y2: "))

m = (y2 - y1) / (x2 - x1)

print("m = {:.2}".format(m))