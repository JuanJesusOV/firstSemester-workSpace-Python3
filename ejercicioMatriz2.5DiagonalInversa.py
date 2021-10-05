#Imprimir la diagonal inversa de una matriz cuadrada

def diagonal(matriz):
    lista = []
    for i in range(len(matriz),0,-1):
        #print(i)
        lista.append(matriz[i-1][i-1])

    return lista

def desplegar(matriz):
    for r in range(len(matriz)):
        for c in range(len(matriz[0])):
            print(matriz[r][c], end="\t")
        print("")            


fila=int(input())
columna=int(input())
matriz=[]

if fila==columna:
    for i in range(fila):
        lista=[]
        for j in range(columna):
            lista.append(int(input()))
        matriz.append(lista)
    
    print()
    desplegar(matriz)
    print("Diagonal:",diagonal(matriz))
else:
    print("La matriz no es cuadrada")