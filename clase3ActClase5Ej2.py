"""
    Ejercicio:
        Escribe un programa que calcule la población de una especie en un determinado número de años. Utiliza la fórmula Ni(e^rt), donde Ni es la población inicial, r es la tasa de crecimiento, la cual siempre es un número entre 0 y 1, t es el tiempo en años y e la constante de Euler.
        Entrada
        Tres números recibidos uno en cada renglón, correspondientes a: población inicial (entero positivo), tiempo en años (entero positivo) y tasa de crecimiento (flotante entre 0 y 1), en ese orden.
        Salida
        Un número entero, resultado del cálculo de la población final. IMPORTANTE: Trunca los decimales del número resultante, para que el resultado sea entero (¿Cuál es la función de la librería math de Python que te puede ayudar a truncar los decimales?).

    Algoritmo:


    Casos de prueba
        Ni       t       r
"""
import math

Ni = int(input("Ingresa la poblacion inicial: "))
if (Ni<1): 
    print("El valor de la población inicial debería ser positivo")
    exit()

t = int(input("Ingresa el tiempo en años: "))
if (t<1): 
    print("El valor del tiempo debería ser positivo")
    exit()

r = float(input("Ingresa la tasa de crecimiento: "))
if (r<0 or r>1): 
    print("La tasa de crecimiento debería ser un numero decimal entre 0 y 1 ")
    exit()

res = Ni * (math.pow(math.e,r*t))

print(res)