"""
Ejercicio:
    Desarrolla un programa que contenga una función en Python que reciba dos números enteros positivos 
    diferentes a cero que representan los límites de un rango y despliegue los números pares que se encuentran en 
    el rango de menor a mayor (se incluyen los dos límites).

Algoritmo:
Funcion validador(a,b):
    decision = Falso
    if (a>0 y b>0):
        decision = Cierto
    regresar decision

Funcion menor(a,b):
    si a>b:
        inf = b 
        sup = a
    sino:
        inf = a   
        sup = b
    regresar inf, sup

Funcion numerosEnRango(inf, sup):
    listaRango = []
    para i en rango (inf,sup+1,1):
        listaRango.agregar(i)
    regresar listaRango

Funcion paresEnLista(listaRango):
    listaPares = []
    para i en listaRango:
        si i%2==0:
            listaPares.agregar(i)
    si listaPares==[]:
        listaPares.agregar('No hay pares') 
    regresar listaPares

Funcion main():
    Escribir "Ingresa un numero"
    Leer a
    Escribir "Ingresa un numero"
    Leer b
    
    decision = validador(a,b)
    si decision == cierto:
        inf, sup = menor(a,b)
        listaRango = numerosEnRango(inf, sup)
        listaPares = paresEnLista(listaRango)
        Escribir (listaPares)
    sino:
        escribir "Ingresa valores enteros positivos"
    
main()

Casos de prueba:
    a   b   listaPares
    0   9   "Ingresa valores enteros positivos"
    7   7   "No hay pares"
    19  1   [2, 4, 6, 8, 10, 12, 14, 16, 18]
    6   22  [6, 8, 10, 12, 14, 16, 18, 20, 22]
"""
def validador(a,b):
    decision = False
    if (a>0 and b>0):
        decision = True
    return decision

def menor(a,b):
    if a>b:
        inf = b 
        sup = a
    else:
        inf = a   
        sup = b
    return inf, sup

def numerosEnRango(inf, sup):
    listaRango = []
    for i in range (inf,sup+1,1):
        listaRango.append(i)
    return listaRango

def paresEnLista(listaRango):
    listaPares = []
    for i in listaRango:
        if i%2==0:
            listaPares.append(i)
    if listaPares==[]:
        listaPares.append('No hay pares') 
    return listaPares

def main():
    a = int(input("Ingresa un numero: "))
    b = int(input("Ingresa un numero: "))
    
    decision = validador(a,b)
    if decision == True:
        inf, sup = menor(a,b)
        listaRango = numerosEnRango(inf, sup)
        listaPares = paresEnLista(listaRango)
        print(listaPares)
    else:
        print("Ingresa valores enteros positivos")
    
main()

