"""
Algoritmo:
    Funcion calculo_grado(calificacion):
        si (calificacion>0.9):
            nota = "A"
        sinoSi (calificacion>0.8):
            nota="B"
        sinoSi (calificacion>0.7):
            nota="C"
        sinoSi (calificacion>0.6):
            nota="D"
        sino:
            nota="F"

        regresar nota
        
    Funcion main():
        Escribir "Ingresa tu calificación"
        Leer calificacion
        si (calificacion>=0 y calificacion<=1):
            nota = calculo_grado(calificacion)
            Escribir nota
        sino:
            Escribir "score incorrecto"

    main()

Casos de prueba:
    calificación    nota
    0.9             B
    0.6             F   
    10              score incorrecto
"""
def calculo_grado(calificacion):
    if (calificacion>0.9):
        nota = "A"
    elif (calificacion>0.8):
        nota="B"
    elif (calificacion>0.7):
        nota="C"
    elif (calificacion>0.6):
        nota="D"
    else:
        nota="F"

    return nota
    
def main():
    calificacion = float(input())
    if (calificacion>=0 and calificacion<=1):
        nota = calculo_grado(calificacion)
        print(nota)
    else:
        print("score incorrecto")

main()