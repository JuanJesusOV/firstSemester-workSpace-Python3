"""
Ejercicio:
    Desarrolla un programa que contenga una función en Python que reciba un número entero positivo diferente a cero que 
    representa la cantidad de términos a calcular de la serie, muestre la secuencia de términos que se van generando y regrese el 
    resultado de la serie.

Algoritmo:
    De fractions importar Fraction
    Función leibniz(n):
        lista=[]
        i=1
        suma=0
        mate=1
        mas=' + '
        menos=' - '
        bor="',\"()\\"
        Mientras len(lista)<n:
            lista.append(1/i)
            i+=2    
        Para x en rango(0,n):
            Si x!=0:
                Si x%2!=0:
                    mate=repr(mate)+repr(menos)+repr(str(Fraction(lista[x]).limit_denominator()))
                Sino:
                    mate=repr(mate)+repr(mas)+repr(str(Fraction(lista[x]).limit_denominator()))
            Sino:
                mate=repr(mate)
        Para x en rango(len(bor)):
            mate=mate.reemplazar(bor[x],"")
        Para x en rango(0,n):
            Si x%2!=0:
                lista[x]*=-1
            suma+=lista[x]
        Escribir mate,"=",f"{suma:.2f}"
    Inicio
        Escribir "Teclea un número entero positivo diferente a cero: "
        Leer num
        Si num<=0:
            Escribir "ERROR: El número debe de ser positivo y diferente a cero"
            Escribir "Teclea un número entero positivo diferente a cero: "
            Leer num
        leibniz(num)        
    Fin
Casos de Prueba:
    num   resultado
    5     1 - 1/3 + 1/5 - 1/7 + 1/9 = 0.83
    7     1 - 1/3 + 1/5 - 1/7 + 1/9 - 1/11 + 1/13 = 0.82
    3     1 - 1/3 + 1/5 = 0.87
    2     1 - 1/3 = 0.67
    1     1 = 1.00
"""
from fractions import Fraction
def leibniz(n):
    lista=[]
    i=1
    suma=0
    mate=1
    mas=' + '
    menos=' - '
    bor="',\"()\\"
    while len(lista)<n:
        lista.append(1/i)
        i+=2    
    for x in range(0,n):
        if x!=0:
            if x%2!=0:
                mate=repr(mate)+repr(menos)+repr(str(Fraction(lista[x]).limit_denominator()))
            else:
                mate=repr(mate)+repr(mas)+repr(str(Fraction(lista[x]).limit_denominator()))
        else:
            mate=repr(mate)
    for x in range(len(bor)):
        mate=mate.replace(bor[x],"")
    for x in range(0,n):
        if x%2!=0:
            lista[x]*=-1
        suma+=lista[x]
    print(mate,"=",f"{suma:.2f}")
num=int(input("Teclea un número entero positivo diferente a cero: "))
if num<=0:
    print("ERROR: El número debe de ser positivo y diferente a cero")
    num=int(input("Teclea un número entero positivo diferente a cero: "))
leibniz(num)