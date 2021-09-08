"""
Ejercicio:
    Escribe un programa que reciba un número entero y calcule la suma: 1^2 + 2^2 + 3^2 +...+"numero^2". 
    Donde "numero" es el valor que el usuario proporcionó. Finalmente se imprime el resultado de la suma en pantalla.

Algoritmo:
    Escribir "Ingresa un numero: "
    Leer num 
    suma = 0
    para i en rango(1,num+1,1):
        suma += i**2

    Escribir(suma)

Casos de prueba:
    num     suma
    5       55
    0       0

"""
num = int(input("Ingresa un numero: "))
suma = 0

for i in range(1,num+1,1):
    suma += i**2

print(suma)