"""
Ejercicio:
    Escribe un programa que, dado un número, muestre en la pantalla su inverso numérico, es decir un número que tiene los mismos 
    dígitos pero en orden inverso.
    Considera un número de máximo 6 dígitos, si el número tiene 7 dígitos o más muestra el mensaje: "numero demasiado largo" 
    (sin las comillas, observa que la palabra número no tiene acento).
    Sugerencia: Usa residuos y divisiones para recorrer los dígitos

Algoritmo:
    Funcion comprobar(num):
        si num>999999 o num<-999999:
            decision = Falso
        sino:
            decision = Cierto
        regresar decision

    Funcion ordenar(num):
        ultimoDigito = 0
        listaInversa = []
        mientras num != 0:
            ultimoDigito = num % 10
            num // = 10
            listaInversa.agregar(ultimoDigito)
        # quitar las dobles comillas a la lista y juntar los valores
        regresar strLista 

    Funcion main():
        Escribir "Ingresa un numero:"
        Leer num
        decision = comprobar(num)
        si decision == Cierto:
            si num < 0:
                num *= -1
                numeroInverso = ordenar(num)
                Escribir "-",(numeroInverso)
            sino:
                numeroInverso = ordenar(num)
                Escribir (numeroInverso)
        sino:
            Escribir "numero demasiado largo"

    main()

    Casos de prueba:
        num         numInverso
        123         321
        -1653       -3561
        1234567     "numero demasiado largo"

"""
def comprobar(num):
    if num>999999 or num<-999999:
        decision = False
    else:
        decision = True
    return decision

def ordenar(num):
    ultimoDigito = 0
    listaInversa = []
    while num != 0:
        ultimoDigito = num % 10
        num //= 10
        listaInversa.append(ultimoDigito)
    strLista = "".join(map(str, listaInversa))
    return strLista 

def main():
    num = int(input("Ingresa un numero: "))
    decision = comprobar(num)
    if decision == True:
        if num < 0:
            num *= -1
            numeroInverso = ordenar(num)
            print("-{}".format(numeroInverso))
        else:
            numeroInverso = ordenar(num)
            print(numeroInverso)
    else:
        print("numero demasiado largo")

main()