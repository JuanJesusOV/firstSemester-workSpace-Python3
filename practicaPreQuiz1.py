"""
Ejercicio: 
    Diseña y codifica un programa en Python en el cual el usuario ingrese la cantidad de elementos que 
    va a ingresar a la lista, posteriormente el programa debe leer cada uno de los elementos de la lista, 
    uno por línea y se van agregando a la lista.

    Importante: El programa debe validar que el número de elementos a ingresar sea mayor que cero, 
    sino debe volver a pedir el valor hasta que cumpla..

    El programa debe desplegar los elementos ingresados en la siguiente forma:
    lista[0] = 1
    lista[1] = 2
    lista[2] = 3
    lista[3] = 4
    lista[4] = 5
    Posteriormente el programa debe desplegar el último elemento.
    Después el programa debe desplegar la suma de todos los elementos de la lista.
    Por último, el programa debe desplegar el promedio de todos los elementos de la lista.
"""

num = int(input("Ingresa un numero: "))

lista = list(range(1,num+1))

while num < 0:
    print("Error. Ingresa un numero mayor a cero")
    num = int(input("Ingresa un numero: "))

for i in range(0,num):
    lista[i] = int(input())


for i in range (0,num):
    print("lista[{}] = {}".format(i,lista[i]))

print("Ultimo elemento:",lista[-1])

suma = 0
for i in range (0,num):
    suma += lista[i]
print("Suma:",suma)

print("Promedio:",suma/len(lista))