"""
Realiza una función que obtenga el área de un rectángulo. La función debe recibir dos parámetros 
(números decimales) que representan la base y la altura del rectángulo y debe regresar el área calculada 
(número decimal).
"""
def area(base, altura):
    area = base * altura
    return area

base = float(input("Ingresa la base: "))
altura = float(input("Ingresa la altura: "))
area = area(base,altura)
print(area)