"""
Ejercicio:
    Escribe un programa que primero lea el valor n, que es la cantidad de números que se van a promediar.
    Después debe leer los n números positivos (flotantes), promediarlos y mostrar el promedio.

Algoritmo:
    Inicio
        Escribir "Ingresa el numero de numeros a promediar: "
        Leer n
        i = 0
        suma = 0
        mientras i<n: 
            i = i + 1
            Escribir "Ingresa un numero: "
            Leer cantidad
            suma = suma + cantidad
        Escribir "El promedio es", (suma/n)
    Fin

Casos de prueba:
    n       cantidad       promedio
    3       2.5             3.63
            3.8
            4.6
"""
n = int(input("Ingresa el numero de numeros a promediar: "))
i = 0
suma = 0
while i<n: 
    i+=1
    cantidad = float(input("Ingresa un numero: "))
    suma += cantidad
print("El promedio es",(suma/n))
