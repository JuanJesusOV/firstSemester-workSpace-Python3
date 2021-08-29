"""
Ejercicio: 
    - Escribe una función llamada areaRect que reciba como parámetro el largo y ancho de un rectángulo y que regresa como valor de retorno el área del rectángulo.
    - Escribe una función llamada perimetroRect que reciba como parámetro el largo y ancho de un rectángulo y que regresa como valor de retorno el perímetro del rectángulo.
    - Observa que dentro de las funciones no mostrarás nada, solo regresarás el valor calculado usando return.
    - Escribe ahora una función main que pregunte al usuario el largo y ancho del rectángulo y después pregunte si quiere calcular 
    el área o el perímetro del rectángulo (puedes pedir una clave a para área y p para perímetro) y después muestre el valor 
    correspondiente al cálculo que pidió el usuario.

Algoritmo:


Casos de prueba:

"""

def areaRect(largo, ancho):
    area = largo * ancho
    return area

def perimetroRect(largo, ancho):
    perimetro = largo + largo + ancho + ancho
    return perimetro

def main(area, perimetro):
    largo = float(input("Ingresa el largo del rectangulo: "))
    ancho = float(input("Ingresa el ancho del rectangulo: "))
    operacion = input("Que valor desea calcular? perimetro(p) o area(a): ")
    
    if (operacion == 'p'):
        perimetro = perimetroRect(largo,ancho)
        print("Perimetro: {:.2f}u".format(perimetro))
    elif (operacion == 'a'):
        area = areaRect(largo, ancho)
        print("Area: {:.2f}u^2".format(area))
    else:
        print("Operación no valida")
        exit()

area = 0
perimetro = 0
main(area, perimetro)