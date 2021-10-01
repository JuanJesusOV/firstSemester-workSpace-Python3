"""
Ejercicio:
    Deberás realizar un programa que cree una matriz de n filas y m columnas que deberá estar llena de números consecutivos  
    por renglón comenzando por el renglón 1.
        Entradas
            Dos números enteros mayores o iguales a 2 que representarán el numero de renglones n (número de listas) y 
            el número de columnas m (numero de elementos en cada lista), en ese orden.
        Salida
            Una matriz de n x m con números consecutivos comenzando en 1 y por renglón. Si alguno de los números recibidos 
            no es mayor o igual a 2, se despliega el mensaje "Error".
"""

def creaMatriz(row, column):
    matriz=[]
    dato = 1
    for r in range(row):
        lista = []
        for c in range(column):
            lista.append(dato)
            dato+=1
        matriz.append(lista)
    return matriz

def main():
    row=int(input())
    column=int(input())
    if row>=2 and column>=2:
        print(creaMatriz(row, column))
    else:
        print("Error")

main()