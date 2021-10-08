"""
Crea un programa que pida al usuario dos cadenas de caracteres como entrada e imprima la cadena con la longitud mayor en la consola. 
Si las dos cadenas tienen la misma longitud, la función debe imprimir ambas cadenas una en cada renglón.
"""
dato1 = input()
dato2 = input()

if len(dato1) > len(dato2):
    print(dato1)
elif len(dato1) < len(dato2):
    print(dato2)
else:
    print(dato1)
    print(dato2)