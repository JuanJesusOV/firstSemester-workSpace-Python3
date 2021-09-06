"""
Ejercicio: 
    Escribe un función que reciba un entero y devuelva True si es un número primo y False si NO es un número primo.
    Ahora escribe una función main , que solicite el numero al usuario, mande llamar la función que desarrollaste arriba y 
    despliegue el siguiente mensaje
        X es un numero primo    ó
        X no es un numero primo 
        Donde X es el número que proporciono el usuario
    Asume que los números negativos pueden ser primos

Algoritmo:
    Funcion primos(num):
        primo = Falso
        divisores=0
        
        para i en rango(1,num+1,1):
            si num%i==0:
                divisores+=1

        si (divisores==2): 
            primo = Cierto

        regresar primo

    Funcion main():
        Escribir "Ingresa un numero"
        Leer num
        primo = primos(num)
        si primo==Cierto:
            Escribir num,"Es un numero primo"
        sino:
            Escribir num,"No es un numero primo"

    main()

Casos de prueba:
    num     primo?
    4       4 no es un numero primo
    123     123 no es un numero primo
    7       7 es un numero primo
"""
def primos(num):
    primo = False
    divisores=0
    
    for i in range(1,num+1,1):
        if num%i==0:
            divisores+=1

    if (divisores==2): primo = True

    return primo

def main():
    num = int(input("Ingresa un numero: "))
    primo = primos(num)
    if primo==True:
        print("{} es un numero primo".format(num))
    else:
        print("{} no es un numero primo".format(num))

main()