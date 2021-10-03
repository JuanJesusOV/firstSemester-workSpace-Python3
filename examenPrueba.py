lista=[]
for i in range(5):
    palabra=input("Ingresa una palabra: ")
    lista.append(palabra)

listaInversa = []
for i in range(len(lista),0,-1):
    listaInversa.append(i)

for i in listaInversa:
    print(i)