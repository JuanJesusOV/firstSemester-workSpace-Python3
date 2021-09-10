"""
Ejercicio:
    La empresa “Siempre limpio”, ofrece servicio semestral de limpieza de hogares y desea analizar el impacto de un incremento en el 
    precio de sus servicios para enero 2022, actualmente cobra $5,430.00 por semestre. Actualmente cuenta con 210 hogares a los cuales 
    da servicio, al 10% de esos 210 hogares les da un descuento en la tarifa. El descuento consiste en un 12% de la costo semestral.

    A partir de solicitar Cantidad de hogares, Porcentaje de hogares con descto. Costo actual por semestre y Porcentaje de descuento 
    sobre costo, tu programa debe de calcular y desplegar:
        Número total de hogares a los que se les realiza descuento.
        Ingreso semestral($) de la empresa por los hogares con descuento.
        Ingresos totales($) actuales de la empresa.
        Si los ingresos totales actuales son mayores o iguales a 1,000,000 quieren aumentar un 5% en caso contrario quieren aumentar un 7%. Calcular y desplegar:
            Porcentaje a aumentar
            Ingresos nuevos ya con el aumento.

Algoritmo:
    Inicio
        Escribir "Cantidad de hogares: "
        Leer cantidadHogares
        Escribir "Porcentaje de hogares con descuento: "
        Leer porcentajeHogaresConDescto
        Escribir "Costo actual por semestre: "
        Leer costoActualSemeste
        Escribir "Porcentaje de descuento sobre costo: "
        Leer porcentjeDescuento

        totalHogaresConDescuento = cantidadHogares*(porcentajeHogaresConDescto/100)
        ingresoHogaresConDescuento = (costoActualSemeste*(100-porcentjeDescuento)/100) * totalHogaresConDescuento
        ingresosTotales = ingresoHogaresConDescuento + (cantidadHogares-totalHogaresConDescuento)*costoActualSemeste
        ingresosConAumento5 = ingresosTotales + (ingresosTotales*5/100)
        ingresosConAumento7 = ingresosTotales + (ingresosTotales*7/100)

        Escribir "Numero total de hogares a los que se les realiza descuento",totalHogaresConDescuento
        Escribir "Ingreso semestral de la empresa por los hogares con descuento: $,"ingresoHogaresConDescuento
        Escribir "Ingresos totales actuales de la empresa: $",ingresosTotales
        si ingresosTotales >= 1000000:
            Escribir "Porcentaje a aumentar: 5%"
            Escribir "Ingresos nuevos ya con aumento: $",ingresosConAumento5
        else:
            Escribir "Porcentaje a aumentar: 7%"
            Escribir "Ingresos nuevos ya con aumento: $",ingresosConAumento7
    Fin

Casos de prueba:
    -------------------------------------- PRIMERO ------------------------------------------------
    Cantidad de hogares: 210
    Porcentaje de hogares con descuento: 10
    Costo actual por semestre: 5430
    Porcentaje de descuento sobre costo: 12

    Numero total de hogares a los que se les realiza descuento 21.0
    Ingreso semestral de la empresa por los hogares con descuento: $100346.4
    Ingresos totales actuales de la empresa: $1126616.4
    Porcentaje a aumentar: 5%
    Ingresos nuevos ya con aumento: $1182947.22

    -------------------------------------- SEGUNDO -----------------------------------------------
    Cantidad de hogares: 5
    Porcentaje de hogares con descuento: 20
    Costo actual por semestre: 5430
    Porcentaje de descuento sobre costo: 18

    Numero total de hogares a los que se les realiza descuento 1.0
    Ingreso semestral de la empresa por los hogares con descuento: $4452.6
    Ingresos totales actuales de la empresa: $26172.6
    Porcentaje a aumentar: 7%
    Ingresos nuevos ya con aumento: $28004.681999999997
"""
cantidadHogares = int(input("Cantidad de hogares: "))
porcentajeHogaresConDescto = int(input("Porcentaje de hogares con descuento: "))
costoActualSemeste = float(input("Costo actual por semestre: "))
porcentjeDescuento = int(input("Porcentaje de descuento sobre costo: "))

totalHogaresConDescuento = cantidadHogares*(porcentajeHogaresConDescto/100)
ingresoHogaresConDescuento = (costoActualSemeste*(100-porcentjeDescuento)/100) * totalHogaresConDescuento
ingresosTotales = ingresoHogaresConDescuento + (cantidadHogares-totalHogaresConDescuento)*costoActualSemeste
ingresosConAumento5 = ingresosTotales + (ingresosTotales*5/100)
ingresosConAumento7 = ingresosTotales + (ingresosTotales*7/100)

print("\nNumero total de hogares a los que se les realiza descuento {}".format(totalHogaresConDescuento))
print("Ingreso semestral de la empresa por los hogares con descuento: ${}".format(ingresoHogaresConDescuento))
print("Ingresos totales actuales de la empresa: ${}".format(ingresosTotales))
if (ingresosTotales) >= 1000000:
    print("Porcentaje a aumentar: 5%")
    print("Ingresos nuevos ya con aumento: ${}".format(ingresosConAumento5))
else:
    print("Porcentaje a aumentar: 7%")
    print("Ingresos nuevos ya con aumento: ${}".format(ingresosConAumento7))