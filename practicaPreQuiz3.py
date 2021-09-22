"""
Ejercicio:
    Desarrolla el programa que determine el total de valores pares e impares de una lista de números enteros que recibirá en su entrada. 
    Los valores los captura el usuario uno por uno, se van almacenando en una lista y posteriormente se analizará la lista para 
    determinar cuantos valores pares e impares posee. Consideramos al 0 como par.
"""

num=''
lista = []

while num != '*':
    num = input("Ingresa un numero ('*' para terminar): ")
    if num == '*':
        break
    else:
        lista.append(int(num))

pares = 0
impares = 0
for i in lista:
    if i%2==0:
        pares+=1
    else:
        impares+=1

print("PARES={}".format(pares))
print("IMPARES={}".format(impares))