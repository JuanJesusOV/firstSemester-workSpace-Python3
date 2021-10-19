lista1 = []
lista2 = []
lista3 = []

cantlista1 = int(input("Candidad de elementos de la lista 1: "))
for i in range(0,cantlista1):
    num = int(input())
    lista1.append(num)
print(lista1)

cantlista2 = int(input("\nCandidad de elementos de la lista 2: "))
for i in range(0,cantlista2):
    num = int(input())
    lista2.append(num)
print(lista2)

for i in range (len(lista1)):
	if lista1[i] not in lista2: lista3.append(lista1[i])

print("\nLos elementos que estan en la lista1 pero no en la lista 2 =",lista3)