"""
Ejercicio:
    Desarrolla una función llamada divideLista, que reciba una lista que contenga números enteros, la función debe de crear 
    una lista (listaPar) con los números pares de la lista recibida y otra lista (listaImp) con los números impares y desplegarlas 
    de la siguiente forma:
        
        Si la función recibe Lista=[1,2,3,4,5] deberá desplegar:
            LISTA PARES= [2,4]
            LISTA IMPARES= [1.3.5]
    
    Ahora desarrolla el programa principal, reciba números enteros, tantos como el usuario quiera, hasta que reciba un “*” 
    indicará que ya no quiere ingresar números y mande llamar a la función divideLista.
"""

def divideLista(lista):
    listaPar = []
    listaImp = []
    
    for i in lista:
        if i%2==0:
            listaPar.append(i)
        else:
            listaImp.append(i)
    
    print("LISTA PARES = {}\nLISTA IMPARES = {}".format(listaPar, listaImp))


def main():
    lista = []
    num = input()
    while num!="*":
        lista.append(int(num))
        num = input()

    divideLista(lista)

main()