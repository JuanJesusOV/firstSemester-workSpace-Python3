#Quiz 2 - Juan Jesús Ortiz - A01639936
"""
Algoritmo:
    Funcion cuadrante(angulo)
        numCuadrante=""
        si (angulo<0 o angulo>360):
            numCuadrante="excede"
        sinoSi (angulo==0 o angulo==90 o angulo==180 o angulo==270 o angulo==360):
            numCuadrante="eje"
        sinoSi (angulo>0 y angulo<90):
            numCuadrante="cuadrante I"
        sinoSi (angulo>90 y angulo<180):
            numCuadrante="cuadrante II"
        sinoSi (angulo>180 y angulo<270):
            numCuadrante="cuadrante III"
        sinoSi (angulo>270 y angulo<360):
            numCuadrante="cuadrante IV"
        regresa numCuadrante

    Funcion main(numCuadrante):
        Escribir "Ingresa el valor del angulo: "
        Leer angulo
        numCuadrante = cuadrante(angulo)
        Escribir angulo

    Inicio
        numCuadrante=0
        main(numCuadrante)
    Fin


Casos de prueba:
    angulo      numCuadrante
    0           eje
    90          eje
    180         eje
    270         eje
    360         eje
    -5          excede
    420         excede
    54          cuadrante I
    128         cuadrante II
    213         cuadrante III
    301         cuadrante IV
"""

def cuadrante(angulo):
    numCuadrante=""
    if (angulo<0 or angulo>360):
        numCuadrante="excede"
    elif (angulo==0 or angulo==90 or angulo==180 or angulo==270 or angulo==360):
        numCuadrante="eje"
    elif (angulo>0 and angulo<90):
        numCuadrante="cuadrante I"
    elif (angulo>90 and angulo<180):
        numCuadrante="cuadrante II"
    elif (angulo>180 and angulo<270):
        numCuadrante="cuadrante III"
    elif (angulo>270 and angulo<360):
        numCuadrante="cuadrante IV"
    return numCuadrante

def main(numCuadrante):
    angulo = int(input("Ingresa el valor del angulo: "))
    numCuadrante = cuadrante(angulo)
    print(numCuadrante)

numCuadrante=0
main(numCuadrante)