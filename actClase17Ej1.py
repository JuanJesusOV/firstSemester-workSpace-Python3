lista=[]
n = 0
while n<=0:
    n = int(input("Teclea la cantidad de numeros que tendrá la lista: "))
for cual in range(n):
    num = int(input("Teclea el valor a ingresar: "))
    lista.insert(cual,num)
print(lista)