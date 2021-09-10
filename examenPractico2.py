"""
Ejercicio:
    Realiza una función llamada digitoMayor que reciba como parámetro 1 número entero y regrese como valor de retorno el mayor de 
    los dígitos contenido en el numero. NOTA: La función NO despliega nada.
    Realiza ahora un programa (función main) que pida al usuario un numero entero y muestre en la pantalla el dígito mayor del número 
    ingresado por el usuario. Para hacerlo debes llamar a la función digitoMayor y desplegar el resultado que te regresa

Algoritmo:
    Funcion digitoMayor(num):
        mayor = 0
        digitos = []
        mientras num != 0:       
            ultimoDigito = num % 10
            num //= 10
            digitos.agregar(ultimoDigito)

        para i en rango(0,len(digitos),1):
            si (digitos[i] >= mayor):
                mayor = digitos[i]
        regresar mayor


    Funcion main():
        Escribir "Numero = "
        Leer num
        mayor = digitoMayor(num)
        Escribir "Digito mayor =",mayor

    Inicio
        main()
    Fin

Casos de prueba:
    num         mayor
    1234        4
    654         6
    679         9
    221         3
"""
def digitoMayor(num):
    mayor = 0
    digitos = []
    while num != 0:       
        ultimoDigito = num % 10
        num //= 10
        digitos.append(ultimoDigito)

    for i in range(0,len(digitos),1):
        if (digitos[i] >= mayor):
            mayor = digitos[i]
    return mayor


def main():
    num = int(input("Numero = "))
    mayor = digitoMayor(num)
    print("Digito mayor =",mayor)

main()