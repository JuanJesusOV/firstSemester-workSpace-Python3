"""
Ejercicio:
    Escribe un programa que utilice estatutos for para mostrar una secuencia como la que se muestra en el ejemplo:
    Si el usuario teclea el número 5
    El programa mostrará lo siguiente:
    1 = 1
    1+2 = 3
    1+2+3 = 6
    1+2+3+4 = 10
    1+2+3+4+5 = 15
    La suma de la serie hasta el número 5 es: 35

Algoritmo:
    Escribir "Ingres un numero: "
    Leer num
    cadena = "1"
    suma = 1
    acumulador = 0

    para i en rango(2, num+2, 1):
        Escribir ("",cadena," = ",suma)
        acumulador += suma
        suma += i
        cadena += ('+',i)

    Escribir ("La suma de la serie hasta el número",num,"es:",acumulador)

Casos de prueba:
    num     impresión en pantalla
    5       1 = 1
            1+2 = 3
            1+2+3 = 6
            1+2+3+4 = 10
            1+2+3+4+5 = 15
            La suma de la serie hasta el número 5 es: 35

    2       1 = 1
            1+2 = 3
            La suma de la serie hasta el número 2 es: 4

"""
num = int(input("Ingresa un numero: "))
cadena = "1"
suma = 1
acumulador = 0

for i in range(2, num+2, 1):
    print("{} = {}".format(cadena,suma))
    acumulador += suma
    suma += i
    cadena += ('+'+str(i))

print("La suma de la serie hasta el número {} es: {}".format(num,acumulador))