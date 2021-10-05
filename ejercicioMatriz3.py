"""
Desarrolla una función en Python que reciba  una matriz de números enteros de tamaño 2x2 y calcule su determinante.
"""
a = [[],[]]
a[0] = input()
a[0] = a[0].split(' ')
a[1] = input()
a[1] = a[1].split(' ')

if (len(a[0]) or len(a[1])) != 2:
    print("La matriz no es una matriz de 2x2")
else:
    """a00 = int(a[0][0])
    a11 = int(a[1][1])
    a10 = int(a[1][0])
    a01 = int(a[0][1])
    det = (a00*a11)-(a01*a10)
    print(det)"""
    
    for i in range (len(a)):
        for j in range(len(a[i])):
            a[i][j] = int(a[i][j])

    det = (a[0][0]*a[1][1])-(a[0][1]*a[1][0])
    print(det)
