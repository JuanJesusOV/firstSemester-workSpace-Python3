"""
Ejercicio:
    Los divisores propios de un número n son aquellos divisores positivos menores que n.
    Un número entero positivo n se dice que es perfecto si la suma de sus divisores propios es igual a n.
    Realiza un programa que lea un número y muestre un mensaje indicando si es perfecto o no.

Algoritmo:
    Inicio
    
    Fin

Casos de prueba:
    
"""

def validador(num):
    divisor = 1
    suma = 0
    
    while (divisor<num):
        if (num%divisor==0):
            suma += divisor
        divisor += 1
    
    if (suma == num):
        decision = True
    else:
        decision = False

    return decision

def main():
    num = int(input("Ingresa un numero: "))
    decision = validador(num)
    
    if (decision==True):
        print("El {} es perfecto".format(num))
    else:
        print("El {} no es perfecto".format(num))

main()