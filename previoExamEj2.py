"""
Ejercicio:
    Desarrolla un programa en Python que solicite un número entero positivo diferente a cero y muestre todos los 
    números generados por la conjetura de Ulam. La conjetura Ulam o también llamada de Collatz, se genera de la siguiente manera:
    Si el número ingresado es un número par, éste se divide (división entera) por dos si no, se multiplica por 3 y se le suma 1. 
    Este se repite hasta obtener el número 1.

Algoritmo:
    Funcion Ulam(num):
        si (num%2==0):
            result = num // 2
        sino:
            result = num * 3 + 1
        regresar result

    Escribir "Ingresa un numero: "
    Leer num
    result = num
    Escribir (result)
    mientras result!=1:
        result = Ulam(num)
        num = result
        Escribir(result)

Casos de prueba:
    num     result
    6       6
            3
            10
            5
            16
            8
            4
            2
            1

"""
def Ulam(num):
    if (num%2==0):
        result = num // 2
    else:
        result = num * 3 + 1
    return result

num = int(input("Ingresa un numero: "))
result = num
print(result)
while result!=1:
    result = Ulam(num)
    num = result
    print(result)