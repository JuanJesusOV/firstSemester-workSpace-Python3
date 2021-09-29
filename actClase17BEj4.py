"""
nombre de la funcion: main (implicita)
descripción: muestra una lista de valores de la serie Fibonacci hasta la cantidad de elementos que el usuario indica.
parametros de entrada: -
parametros de salida: -
"""

num =int(input()) 
while num<0:
    num =int(input()) 

lista=[0,1]
for i in range(num):
    indice=lista[i]+lista[i+1]
    lista.append(indice)

print(lista[0:num])
