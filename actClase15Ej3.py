"""
Ejercicio:
    Escribe un programa que lea un número entero positivo y que muestre en la pantalla la cantidad de dígitos que tiene.
    Sugerencia: Divide el número entre 10 repetidamente hasta que el número sea menor que 1.

Algoritmo:
    ultimoDigito = 0
    i=0
    Escribir "Ingresa un numero entero"
    Leer num 
    mientras num != 0:
        ultimoDigito = num % 10
        num //= 10
        i+=1
    Escribir "La cantidad de digitos es:",i

    Casos de prueba:
    num     cantDigitos
    356     3
    123456  6
    
"""
ultimoDigito = 0
i=0

num = int(input("Ingrese un numero entero: "))

while num != 0:
    ultimoDigito = num % 10
    num //= 10
    i+=1

print("La cantidad de digitos es:",i)