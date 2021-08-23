# Juan Jesús Ortiz Vazquez - A01639936
"""
Tarea 1:
    Un vendedor de una compañía de refrescos, vende refrescos individuales (sueltos) y obtiene un pago por esta venta 
    a razón de $100 pesos por cajas completas de refrescos, las cuales contienen 20 refrescos y $3 pesos por refrescos 
    que no completen caja. A partir de solicitar cantidad de refrescos vendidos, cantidad de refrescos por caja, comisión 
    por caja y comisión por refresco, calcula y despliega el total a pagar de comisión.

Algoritmo:
    Inicio
        Escribir: "Ingresa la cantidad de refrescos vendidos: "
        Leer refrescosVendidos
        refrescosSueltos = refrescosVendidos%20
        cantidadCajas = (refrescosVendidos - refrescosSueltos)/20
        total = (cantidadCajas*100) + (refrescosSueltos*3)
        Escribir "Cantidad de refrescos por caja:",(refrescosVendidos - refrescosSueltos)
        Escribir "Cantidad de refrescos sueltos:",refrescosSueltos
        Escribir "Comisión por caja:",cantidadCajas*100
        Escribir "Comisión por refresco:",refrescosSueltos*3
        Escribir "Comisión a pagar: ${} (${} por la(s) caja(s) y $3 por cada uno de los {} refrescos que no completan caja)".format(total, cantidadCajas*100, refrescosSueltos))
    Fin

Casos de prueba: 
    refrescosVendidos       refrescosPorCaja        refrescosSueltos        comisionPorCaja     comisionPorRefresco         comisionTotal
    25                      20                      5                       100                 15                          115
    88                      80                      8                       400                 24                          424
"""

refrescosVendidos = int(input("Ingresa la cantidad de refrescos vendidos: "))

refrescosSueltos = refrescosVendidos%20
cantidadCajas = (refrescosVendidos - refrescosSueltos)/20
total = (cantidadCajas*100) + (refrescosSueltos*3)

print("\nCantidad de refrescos por caja:",(refrescosVendidos - refrescosSueltos))
print("Cantidad de refrescos sueltos:",refrescosSueltos)
print("Comisión por caja:",cantidadCajas*100)
print("Comisión por refresco:",refrescosSueltos*3)
print("Comisión a pagar: ${} (${} por la(s) caja(s) y $3 por cada uno de los {} refrescos que no completan caja)".format(total, cantidadCajas*100, refrescosSueltos))