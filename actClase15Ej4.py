"""
Ejercicio: 
    Escribe un programa que despliegue la suma de los dígitos de un número entero, el número puede ser positivo 
    o negativo, la suma siempre será positiva.

Algoritmo: 
    suma = 0
    ultimoDigito = 0
    Escribir "Ingrese un numero entero: "
    Leer num

    si num<0:
        num = num * -1

    mientras num != 0:
        ultimoDigito = num % 10
        num // = 10
        suma + = ultimoDigito

    Escribir "La suma de los digitos es:",suma


Casos de prueba:
    num     suma
    2975    23 
    -517    13

"""
suma = 0
ultimoDigito = 0

num = int(input("Ingrese un numero entero: "))

if num<0:
    num*=-1

while num != 0:
    ultimoDigito = num % 10
    num //= 10
    suma += ultimoDigito

print("La suma de los digitos es:",suma)