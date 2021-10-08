"""
Desarrolla un programa en Python que contenga una función que identifique si una palabra es un palíndromo o no.
El programa debe funcionar aún cuando la frase incluya espacios entre palabras y si tiene diferencias entre mayúsculas o minúsculas.
"""
cadena = input().lower().replace(" ","")
if cadena == cadena[::-1]:
    print("Es palindromo")
else:
    print("No es palindromo")