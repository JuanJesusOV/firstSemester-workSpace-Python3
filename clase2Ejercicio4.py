"""
Ejercicio 4:
    Escribe un algoritmo que verifique si una persona puede obtener su licencia de conducir. 
    Para hacerlo debe ser mayor de edad (18 años o más) y traer una identificación oficial.

Algoritmo:
	Inicio
		Escribir “Teclea tu edad”
		Leer edad
		Escribir “Traes identificación oficial? (s/n)”
		Leer resp
		Si edad>=18 y resp= “s” entonces
			Escribir “SI puedes obtener licencia”
		Sino
			Escribir “No puedes obtener licencia”
    Fin

Casos de Prueba:
    edad	resp	Resultado
    18	    s	    Si puedes obtener licencia
    20	    n	    No puedes obtener licencia
    15	    s	    No puedes obtener licencia
    13	    n	    No puedes obtener licencia
"""

edad = int(input("Ingresa tu edad: "))
resp = str(input("Traes identificacion oficial? (s/n): "))
print(type(resp))

if edad>=18 and resp=="s":
    print("Si puedes obtener tu licencia")
else:
    print("No puedes obtener tu licencia")