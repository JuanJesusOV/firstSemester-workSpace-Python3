"""
Ejercicio 1:
    Solicita al usuario 2 números y realiza la suma, resta y multiplicación de ellos.

Algoritmo:
    Inicio
        Escribir "Teclea el primer numero"
        Leer num1
        Escribir "Teclea el segundo numero"
        Leer num2
        Escribir "La suma es: ", (num1 + num2)
        Escribir "La resta es: ", (num1 - num2)
        Escribir "La multiplicación es: ", (num1 * num2)
    Fin

Casos de prueba:
    num1    num2    prueba
    4       5       La suma es: 9   
                    La resta es: -1
                    La multiplicación es: 20
    -3      6       La suma es: 3  
                    La resta es: -9
                    La multiplicación es: -18
    4.2     5.4     La suma es: 9.6  
                    La resta es: -1.2
                    La multiplicación es: 22.68
"""

num1 = float(input("Teclea el primer numero: "))
num2 = float(input("Teclea el segundo numero: "))
print("{} + {} = {:.2f}".format(num1, num2, (num1+num2)))
print(num1,"-",num2,"= {:.2f}".format(num1-num2))
print(num1,"*",num2,"= {:.2f}".format(num1*num2))
