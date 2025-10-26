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
        },
    '11223344' : {
        'nombre':  'PEPITO',
        'email' : 'pepe@gmail.com'
    },
    '22557788': {
        'nombre':  'JUANITO',
        'email' : 'juan@gmail.com'
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
        dni = input ("Ingrese su número de DNI  ")
        nombre = input ("Ingrese su Nombre  ")
        email = input ("Ingrese su correo electrónico  ")
        dic_alumno_nuevo = {
                    dni : {
                        'nombre': nombre,
                        'email': email, 
                    }
        }
        dic_alumnos.update (dic_alumno_nuevo)

    elif opcion == 2:
        print("="*ANCHO)
        print ("="*10 + "MOSTRAR ALUMNO")
        print ("="*ANCHO)
        for dni, datos in dic_alumnos.items():
            print ("="*ANCHO)
            print (f"DNI: {dni}")
            print (f"NOMBRE: {datos['nombre']}")
            print (f"EMAIL: {datos['email']}")
        input ("PRESIONE ENTER para continuar")
    elif opcion == 3:
        print("="*ANCHO)
        print ("="*10 + "ACTUALIZAR ALUMNO")
        print ("="*ANCHO)
        dni = input ("Ingrese DNI de alumno a actualizar: ")
        if dni in dic_alumnos:
            print (f"ALUMNO A ACTUALIZAR: {dni} || {dic_alumnos[dni]['nombre']}")
            act_nombre = input ("INGRESE NOMBRE ACTUALIZADO")
            act_email = input ("INGRESE EMAIL ACTUALIZADO")
            dic_act_alumno = {
                        dni : {
                            'nombre': act_nombre,
                            'email': act_email
                        }
            }
            dic_alumnos.update (dic_act_alumno)
        else:
            print("EL ALUMNO CONSULTADO NO EXISTE")
    elif opcion == 4:
        print("="*ANCHO)
        print ("="*10 + "ELIMINAR ALUMNO")
        print ("="*ANCHO)
        dni = input ("INGRESE DNI DEL ALUMNO A ELIMINAR:  ")
        if dni in dic_alumnos:
            print (f"ALUMNO A ELIMINAR {dni} || {dic_alumnos[dni]['nombre']}")
            confirmacion = input ("¿SEGURO DE QUE DESEA ELIMINAR ESTE ALUMNO?  SI | NO ")
            if confirmacion == "SI":
                dic_alumnos.pop (dni)
                print ("ALUMNO ELIMINADO")
            elif confirmacion == "NO":
                print ("NO SE ELIMINÓ EL ALUMNO")
            else:
                print ("RESPUESTA NO VALIDA")
        else:
            "EL ALUMNO CONSULTADO NO EXISTE"
           
    elif opcion == 5:
        print("="*ANCHO)
        print ("SALIENDO DEL PROGRAMA")
        print ("="*ANCHO)
    else:
        print ("="*ANCHO)
        print ("OPCIÓN INVÁLIDA")
        print ("="*ANCHO)

    sleep (1)
