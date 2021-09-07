"""
Ejercicio:
    Escribe un programa que calcule el promedio de una serie de números flotantes, no se sabe inicialmente la cantidad de valores 
    a promediar, así que el programa debe seguir leyendo números hasta que el usuario teclee un número negativo. Ten cuidado de no 
    considerar el número negativo dentro del promedio.    

Algoritmo:
    suma = 0
    cantidad = 0
    i=-1
    mientras cantidad >= 0:
        suma+=cantidad
        i+=1
        Escribir "Ingresa un numero: "
        Leer cantidad
    Escribir "El promedio es:",(suma/i)

Casos de prueba:
    cantidad    promedio
    2.5         4.5
    6.3
    4.7
    -1

"""
suma = 0
cantidad = 0
i=-1
while cantidad >= 0:
    suma+=cantidad
    i+=1
    cantidad = float(input("Ingresa un numero: "))
    
print("El promedio es:",(suma/i))