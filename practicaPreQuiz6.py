"""
Ejercicio: 
    Desarrolla un programa que permita realizar la suma elemento a elemento de dos listas de números enteros y 
    con la misma cantidad de elementos.

    Entradas
        Un número entero que indica cuántos elementos tendrá cada lista. El número debe ser mayor a 0. Posteriormente el 
        ingreso de los números enteros correspondientes a los elementos de las dos listas. Por ejemplo, si en la primera 
        entrada se ingresa un 5, después del 5 se reciben 10 números más (uno en cada renglón) 5 para conformar cada lista.

    Salida
        Si el número inicial ingresado es 0 o menor, deberá desplegar el mensaje "Error"
        Una lista donde los elementos corresponde a la suma de los elementos de las dos listas de acuerdo con su posición, 
        es decir los elementos de la posición 0 de las dos listas se suman y se ponen en la posición 0 de la lista resultado 
        y así consecutivamente para todos los datos de la lista.
"""
num = int(input("Ingresa un numero: "))

if num < 0:
    print("Error")
    exit()

lista1 = []
lista2 = []
suma = []

for i in range(0,num):
    cantidad = int(input())
    lista1.append(cantidad)

for i in range(0,num):
    cantidad = int(input())
    lista2.append(cantidad)

for i in range(0,num):
    suma.append(lista1[i] + lista2[i])

print(suma)