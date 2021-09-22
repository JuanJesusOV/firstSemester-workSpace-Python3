"""
    Diseña y codifica un programa en Python en el cual el usuario ingrese la cantidad de n elementos que va a tener la lista, 
    posteriormente el programa debe leer cada uno de los n elementos, línea por línea y se van agregando a la lista. 
    El programa debe validar que n sea mayor que cero sino debe volver a pedir el valor hasta que cumpla.

    El programa debe desplegar los elementos ingresados en forma inversa, el indice mayor al menor y en el siguiente formato:
    lista[-1] = 5
    lista[-2] = 4
    lista[-3] = 3
    lista[-4] = 2
    lista[-5] = 1
    Posteriormente el programa debe desplegar el valor mayor de todos los elementos de la lista:
    Después el programa debe desplegar el valor menor de todos los elementos de la lista:
    Por último, el programa debe desplegar la lista ordenada de menor a mayor.
"""
num = int(input("Ingresa un numero: "))

while num < 0:
    print("Error. Ingresa un numero mayor a cero")
    num = int(input("Ingresa un numero: "))

lista = list(range(1,num+1))

for i in range(0,num):
    lista[i] = int(input())

for i in range (0,num):
    print("lista[-{}] = {}".format(i+1,lista[(-i)-1]))

print("Numero mayor: {}".format(max(lista)))

print("Numero menor: {}".format(min(lista)))

lista.sort()
print(lista)