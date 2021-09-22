"""
Ejercicio:
    Escribe un programa en el cual definas la función es_bisiesto. Esta función debe recibir como parámetro un número entero que 
    representa un año, y te debe regresar True si el año es bisiesto, y False en caso contrario.Recuerda que un año es bisiesto si 
    es divisible entre 4, excepto cuando es divisible entre 100. Aquellos años que son divisibles entre 100 no son bisiestos, a menos 
    que sean divisibles entre 400.

Algoritmo:
    Funcion es_bisiesto(año):

        bisiesto=Falso

        si año%4==0:
            bisiesto=Cierto
            si año%100==0:
                bisiesto=Falso
                si año%400==0:
                    bisiesto=Ciero

        regresar bisiesto    
    
    Inicio
        Escribir "Ingresa un año: "
        Leer año
        bisiesto = es_bisiesto(año)
        Escribir (bisiesto)
    Fin

Casos de prueba:
    año     bisiesto
    2100    False
    2020    True
    1543    False

"""
def es_bisiesto(año):

    bisiesto=False

    if año%4==0:
        bisiesto=True
        if año%100==0:
            bisiesto=False
            if año%400==0:
                bisiesto=True

    return bisiesto

año = int(input(("Ingresa un año: ")))
bisiesto = es_bisiesto(año)
print(bisiesto)