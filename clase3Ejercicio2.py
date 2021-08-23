"""
Ejercicio 1:
    El área de un triángulo cuyos lados son de longitud a, b y c se calcula como: 
    área = √[s*(s−a)*(s−b)*(s−c)]          
    dónde s=(a+b+c)/2
    Escribe un programa que pida al usuario los valores a, b y c y calcule y muestre el área del triángulo usando esta fórmula.

Algoritmo:
    Inicio
        Escribir "Ingresa el valor de a: "
        Escribir "Ingresa el valor de b: "
        Escribir "Ingresa el valor de c: "
        Leer a
        Leer b
        Leer c
        s = (a+b+c)/2
        area = √(s*(s−a)*(s−b)*(s−c))
        Escribir "El area del triangulo es: ", area
    Fin

Casos de prueba:
    a       b       c       area
    5       10      15      
    5.3     8.7     9.3     
"""
from math import sqrt as raizCuadrada

a = float(input("Ingresa el valor de a: "))
b = float(input("Ingresa el valor de b: "))
c = float(input("Ingresa el valor de c: "))

s = (a+b+c)/2
area = raizCuadrada(s*(s-a)*(s-b)*(s-c))

print("El area del triangulo es de {:.2f}u^2".format(area))