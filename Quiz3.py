"""
Ejercicio:
    Desarrolla un programa en Python que solicite números enteros hasta que el número ingresado sea un número negativo.
    El programa deberá de mostrar cuántos números ingresados fueron pares.

Algoritmo:
    Funcion pares(num):
        par = False
        si (num%2==0 y num>=0):
            par = True
        regresar par

    Funcion negativo(num):
        nega = False
        si (num<0):
            nega = True
        regresar nega

    Funcion main():
        contador = 0
        num = 0
        nega = negativo(num)
        mientras (nega==False):
            escribir "Ingresa un numero"
            leer num
            nega = negativo(num)
            
            par = pares(num)
            si (par==True):
                contador += 1

        escribir("Total de pares:",contador)

    inicio
        main()
    Fin

Casos de prueba:
    num     numeroDePares
    2       5
    4
    6
    8
    0
    -6
    -----------------------
    6       6
    1
    3
    7
    5
    9
    4
    12
    38
    0
    0
    9
    -1
"""
def pares(num):
    par = False
    if (num%2==0 and num>=0):
        par = True
    return par

def negativo(num):
    nega = False
    if (num<0):
        nega = True
    return nega

def main():
    contador = 0
    num = 0
    nega = negativo(num)
    
    while (nega==False):
        num = int(input("Ingresa un numero: "))
        nega = negativo(num)
        
        par = pares(num)
        if (par==True):
            contador += 1

    print("Total de pares:",contador)

main()