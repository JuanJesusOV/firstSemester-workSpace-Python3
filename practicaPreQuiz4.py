"""
Ejercicio: 
    Escribe un programa que reciba del usuario un número entero que representa la cantidad de números que va a ingresar. 
    El programa deberá recibir esa cantidad de números enteros, los colocará en una lista y la desplegará a pantalla. 
    Posteriormente deberá construir una nueva lista, con el cuadrado de cada uno de los elementos de la lista del usuario.
"""
num = int(input("Ingresa un numero: "))

if num < 0: num = 0

lista = list(range(1,num+1))   

for i in range(0,num):
    lista[i] = int(input())

print(lista)
for i in range(0,num):
    lista[i] **= 2 
print(lista)