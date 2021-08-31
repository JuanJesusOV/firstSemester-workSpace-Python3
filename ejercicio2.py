largo = float(input("Ingresa el largo de la alberca: "))
ancho = float(input("Ingresa el ancho de la ancho: "))
profundidad = float(input("Ingresa el profundidad de la profundidad: "))
costoPintura = float(input("Ingresa el costo de la pintura por m^2: "))

base = largo*ancho
lado1 = largo*profundidad
lado2 = largo*ancho

totalArea = base+(2*lado1)+(2*lado2)
costoTotal = costoPintura*totalArea

print("El total a pagar es de ${:.2f}".format(costoTotal))
