"""
Ejercicio:
    Escribe un programa que lea los valores a y b y muestre todos los números pares que van desde a hasta b incluyendo los límites.
    Supón que siempre a < b.
    Para este ejercicio considera el valor 0 como par.
"""
def pares(a, b):
    lista = []
    
    while a<=b:
        if (a%2==0):
            lista.append(a)
        a += 1
    return lista

def main():
    a = int(input("a: "))
    b = int(input("b: "))
    
    lista = pares(a,b)

    print(lista)

main()