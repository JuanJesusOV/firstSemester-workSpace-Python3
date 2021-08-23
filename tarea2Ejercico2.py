"""
Ejercicio:
    Escribe un programa que pida una distancia en centímetros y que escriba esa distancia 
    en su equivalente en kilómetros, metros y centímetros (escribiendo solamente las unidades necesarias).

Algoritmo:
    Inicio
        Escribir "Ingresa una distancia: "
        Leer num
        si num>=100000
            km = num // 100000
            Escribir km,"km"
            num = num - km*100000
        si num>=100 && num!=0
            m = num // 100
            Escribir m,"m"
            num = num - m*100
        si num!=0
            cm = num
            Escribir cm,"cm"
    Fin

Casos de prueba:
    num         km      m       cm
    5907800     59      78
    3306904     33      69      4
"""
num = int(input("Ingresa una distancia (cm): "))

if num >= 100000:
    km = num // 100000
    print(km,"km")
    num -= km*100000

if num >= 100 and num!=0:
    m = num // 100
    print(m,"m")
    num -= m*100

if num!=0:
    cm = num
    print(cm,"cm")
