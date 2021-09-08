"""
Ejercicio:
    La secuencia de Fibonacci es una serie de números relacionados entre sí. Usualmente la serie comienza con los números 0 y 1, 
    y todo número sucesivo se calcula como la suma de los dos números anteriores. Así que los primeros 11 elementos de la serie son:
        0 1 1 2 3 5 8 13 21 34 55
    Debes escribir un programa que contenga una función llamada fibonacci_index. Esta función debe recibir como parámetro 
    el índice (o posición) que quieres conocer dentro de la serie de Fibonacci. La función debe regresar el número de Fibonacci 
    en ese índice. Tu programa debe solamente imprimir el valor devuelto por la función.

Algoritmo:
    Funcion fibonacci_index(indice):
        fibo = [0,1]
        para i en rango(2,indice+1,1):
            fibo.agregar(fibo[i-1] + fibo[i-2])
        valor = fibo[indice-1]
        regresar valor

    Escribir "Ingresa un numero: "
    Leer indice
    valor = fibonacci_index(indice)
    Escribir (valor)

Casos de prueba:
    indice      valor
    5           3
    26          75025
    11          55

"""
def fibonacci_index(indice):
    fibo = [0,1]
    for i in range(2,indice+1,1):
        fibo.append(fibo[i-1] + fibo[i-2])
    valor = fibo[indice-1]
    return valor

indice = int(input("Ingresa un numero: "))
valor = fibonacci_index(indice)
print(valor)