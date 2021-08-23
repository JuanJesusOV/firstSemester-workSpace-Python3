"""
Ejercicio 3:
    Solicita al usuario la temperatura en grados Celsius y calcula y despliega el equivalente en grados Farenheit.

Algoritmo:
    Inicio
        Escribir "Ingresa la temperatura en grados Celsius"
        Leer celsius
        Escribir "El equivalente en grados Farenheit es de: ",farenheit
    Fin

Casos de prueba:
    celsius    farenheit
    0           32
    7.6         45.68    
"""

celsius = float(input("Ingresa la temperatura en grados Celsius: "))

farenheit = (celsius * 9/5) + 32

print("{}°C = {:.1f}°F".format(celsius, farenheit))