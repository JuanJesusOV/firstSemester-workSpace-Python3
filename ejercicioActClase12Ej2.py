"""
Ejercicio:
    Escribe un programa que lea del teclado números enteros y los vaya contando y sumando. El programa se debe detener cuando 
    la suma de los números leídos sea 1000 o más. Cuando la suma sea 1000 o más, el programa debe mostrar el total de la suma, 
    y la cantidad de números que se sumaron.

Algoritmo:
    Inicio
        cuantos=0
        suma=0
        mientras suma < 1000:
            Escribir "Tecla un numero entero"
            Leer num
            suma = suma + num
            cuantos = cuantos + 1
        Escribe "suma = ",suma 
        Escribe "cantidad de numeros = ", cuantos
    Fin

Casos de prueba:
    100
    50
    200
    430
    250
    suma = 1030
    cantidad de numeros = 5
"""

cuantos=0
suma=0
while (suma < 1000):
    num = int(input("Tecla un numero entero: "))
    suma = suma + num
    cuantos = cuantos + 1
print("suma = ",suma )
print("cantidad de numeros = ", cuantos)