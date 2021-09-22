"""
    Escribe un programa determine cuántas palabras de una lista empiezan con una determinada letra.

    Entrada
    5 palabras y una letra, en ese orden y cada una en un renglón.

    Salida
    Un número entero que represente la cantidad de palabras que empiezan con la letra ingresada. Debe contabilizar sin 
    importar si la palabra está en mayúsculas o minúsculas.
"""

lista = []

for i in range(0,5):
    palabra = input("Ingresa una palabra: ").lower()
    lista.append(palabra)

letra = input("Ingresa una letra: ").lower()

contador = 0
for i in range(0,5):
    if letra == (lista[i])[0]:
        contador += 1

print(contador)