"""
Ejercicio:
    Escribe un programa que use estatutos for para mostrar en la pantalla un triángulo de caracteres 
    como se muestra en el siguiente ejemplo.
        Ejemplo: 
        Si el usuario captura 5; la impresión debe de quedar de la siguiente forma:
            *   
           **  
          *** 
         ****
        *****

Algoritmo:
    Inicio
        Escribir "Ingresa un numero: "
        Leer num
        para i en rango(1,num+1,1):
            Escribir((num-i)*' ','*'*i)
    Fin

Casos de prueba:
    num     print
    5            *
                **
               ***
              ****
             *****
    
    8               *
                   **
                  ***
                 ****
                *****
               ******
              *******
             ********   

"""
num = int(input("Ingresa un numero: "))
for i in range(1,num+1,1):
    print((num-i)*' ','*'*i)