def sinDuplicados(lista):
    listaSinDuplicados=[]
    for i in lista:
        if i not in listaSinDuplicados:
            listaSinDuplicados.append(i)
    return listaSinDuplicados

def main():
    elementos = int(input("Ingresa el numero de elementos a ingresar: "))
    lista = []

    if elementos<1:
        print("Error")
    else:
        for i in range(0,elementos):
            lista.append(input())
        print(lista)
        listaSinDuplicados = sinDuplicados(lista)
        print(listaSinDuplicados)

main()