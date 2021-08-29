def comparadorFracciones(num1, den1, num2, den2):
    fraccionMayor = 0
    mayorNum = 0
    mayorDen = 0
    fraccion1 = num1 / den1
    fraccion2 = num2 / den2
    
    if (fraccion1>=fraccionMayor):
        fraccionMayor=fraccion1
        mayorNum=num1
        mayorDen=den1
    if (fraccion2>=fraccionMayor):
        fraccionMayor=fraccion2
        mayorNum=num2
        mayorDen=den2

    return mayorNum, mayorDen

def main(mayorNum, mayorDen):
    print("---Fraccion 1---")
    num1 = int(input("Numerador:   "))
    den1 = int(input("Denominador: "))
    print("---Fraccion 2---")
    num2 = int(input("Numerador:   "))
    den2 = int(input("Denominador: "))
    mayorNum, mayorDen = comparadorFracciones(num1, den1, num2, den2)
    #print(mayorNum, mayorDen)
    print("---Fraccion 3---")
    num3 = int(input("Numerador:   "))
    den3 = int(input("Denominador: "))
    mayorNum, mayorDen = comparadorFracciones(mayorNum, mayorDen, num3, den3)
    print("\nLa fraccion más grande es: {}/{}\n".format(mayorNum, mayorDen))

mayorNum = 0
mayorDen = 0
main(mayorNum, mayorDen)