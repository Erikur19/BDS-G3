import os
from time import sleep


""""

CRUD
    - CREATE
    - READ
    - UPDATE
    - DELETE
"""


dic_alumnos = {
    '12345678': {
        'nombre' : 'CESAR',
        'email' : 'cesar@gmail.com'
        }
}


ANCHO = 50
opcion = 0

while (opcion < 5):
    os.system ("clear")
    print ("="*ANCHO)
    print (" "*10 + "GESTIÓN DE ALUMNOS")
    print ("="*ANCHO)
    print ("""
            [1] REGISTRAR ALUMNO
            [2] MOSTRAR ALUMNO
            [3] ACTUALIZAR ALUMNO
            [4] ELIMINAR ALUMNO
            [5] SALIR
           """)
    print ("="*ANCHO)
    opcion = int(input("Ingrese la opción que desea:  "))

    if opcion == 1:
        print("="*ANCHO)
        print ("="*10 + "REGISTRAR ALUMNO")
        print ("="*ANCHO)
    elif opcion == 2:
        print("="*ANCHO)
        print ("="*10 + "MOSTRAR ALUMNO")
        print ("="*ANCHO)
    elif opcion == 3:
        print("="*ANCHO)
        print ("="*10 + "ACTUALIZAR ALUMNO")
        print ("="*ANCHO)
    elif opcion == 5:
        print("="*ANCHO)
        print ("="*10 + "SALIR ALUMNO")
        print ("="*ANCHO)
    else:
        print ("="*ANCHO)
        print ("OPCIÓN INVÁLIDA")
        print ("="*50)

    sleep (1)
