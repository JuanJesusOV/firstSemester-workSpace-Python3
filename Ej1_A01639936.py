def creaMatriz( ):
    m=[]
    rengCol = int(input("Teclea la cantidad de renglones y columnas de la matriz: "))
    for r in range(rengCol):
        reng=[]
        for c in range(rengCol):
            reng.append(int(input()))
        m.append(reng)
    return m

def dmenor_mayor(matriz):
    diagonal = []
    resultante = []
    
    for i in range(len(matriz)):
        diagonal.append(matriz[i][i])
    
    max = diagonal[0]
    min = diagonal[0]

    for i in range (len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] > max:
                max = matriz[i][j]
            if matriz[i][j] < min:
                min = matriz[i][j]

    resultante = [min, max]

    return resultante

def main():
    matriz = creaMatriz()
    resultante = dmenor_mayor(matriz)
    print(resultante)

main()