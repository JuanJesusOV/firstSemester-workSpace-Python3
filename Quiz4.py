#Quiz 4 - Juan Jesús Ortiz - A01639936
"""
Ejercicio:
    Escribe una función llamada cuadrante que reciba un número entero que representa los grados del plano cartesiano y que regrese 
    como resultado en donde se encuentra dichos grados (la función no debe desplegar en pantalla nada), tomando en cuenta lo siguiente:
        En caso de que el grado caiga en un eje, la función regresará "eje".
        En caso de que el grado sea menor a cero o mayor a 360,  la función regresará "se excede".
        En el resto de los casos debe de regresar  “cuadrante I” o “cuadrante II” o “cuadrante III” o “cuadrante IV”
        Ahora crea un programa (main) que pida al usuario tantos números enteros como el usuario quiera y para cada número, 
        mande a llamar la función cuadrante que creaste arriba y que despliegue en pantalla el resultado que regresa la función.

Algoritmo:
    Funcion cuadrante(grados)
        numCuadrante=""
        si (grados<0 o grados>360):
            numCuadrante="excede"
        sinoSi (grados==0 o grados==90 o grados==180 o grados==270 o grados==360):
            numCuadrante="eje"
        sinoSi (grados>0 y grados<90):
            numCuadrante="cuadrante I"
        sinoSi (grados>90 y grados<180):
            numCuadrante="cuadrante II"
        sinoSi (grados>180 y grados<270):
            numCuadrante="cuadrante III"
        sinoSi (grados>270 y grados<360):
            numCuadrante="cuadrante IV"
        regresa numCuadrante

    Funcion main(numCuadrante):
        decision = 's'
        mientras decision != 'n':
            Escribir "Teclea los grados: "
            Leer grados
            numCuadrante = cuadrante(grados)
            print(grados,"se encuentra en",numCuadrante)
            Escribir "Quieres dar de alta otro (s/n)?"
            Leer decision

    Inicio
        numCuadrante=0
        main(numCuadrante)
    Fin

Casos de prueba:
    grados      numCuadrante    decision
    0           eje             s  
    90          eje             s
    180         eje             s
    270         eje             s
    360         eje             s   
    -9          excede          s
    673         excede          s
    53          cuadrante I     s
    129         cuadrante II    s
    210         cuadrante III   s
    300         cuadrante IV    n
"""
def cuadrante(grados):
    numCuadrante=""
    if (grados<0 or grados>360):
        numCuadrante="se excede"
    elif (grados==0 or grados==90 or grados==180 or grados==270 or grados==360):
        numCuadrante="eje"
    elif (grados>0 and grados<90):
        numCuadrante="cuadrante I"
    elif (grados>90 and grados<180):
        numCuadrante="cuadrante II"
    elif (grados>180 and grados<270):
        numCuadrante="cuadrante III"
    elif (grados>270 and grados<360):
        numCuadrante="cuadrante IV"
    return numCuadrante

def main(numCuadrante):
    decision = 's'
    while decision != 'n':
        grados = int(input("Teclea los grados: "))
        numCuadrante = cuadrante(grados)
        print("{} se encuentra en {}".format(grados,numCuadrante))
        decision = input("Quieres dar de alta otro (s/n)?")

numCuadrante=0
main(numCuadrante)