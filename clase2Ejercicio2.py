"""
Ejercicio 2:
	Escribe un algoritmo que muestre la velocidad promedio de un automóvil dadas la 
    distancia recorrida en kilómetros y el tiempo que se tardó en recorrer esa distancia dado en horas.

Algoritmo:
	Inicio
		Escribir “Teclea la distancia en kilómetros”
		Leer distancia
        Escribir “Teclea el tiempo que tardaste en recorrer esa distancia”
		Leer tiempo
		Calcular velocidad = distancia/tiempo
		Escribir “La velocidad del automóvil es”, velocidad
    Fin

Casos de Prueba:
    Distancia	Tiempo	velocidad
    100	        2	    50
    120	        1	    120
"""

distancia = float(input("Teclea la distancia en kilometros: "))
#print(type(distancia)) #saber el tipo de dato de la variable distancia
tiempo = float(input("Teclea el total de horas tardaste en recorrer esa distancia: "))

velocidad = distancia / tiempo

print("La velocidad del auto es de", velocidad,"km/h")