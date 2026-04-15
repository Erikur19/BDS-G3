import os
from time import sleep
from lib_alumnos import *


cargar_alumnos('alumnos.txt')
opcion = 0


while (opcion < 5):
    os.system ("clear")
    menu()
    opcion = int(input("Ingrese la opción que desea:  "))
    if opcion == 1:
        dic_alumno_nuevo = registrar ()
        dic_alumnos.update (dic_alumno_nuevo)
    elif opcion == 2:
        mostrar(dic_alumnos)
    elif opcion == 3:
         actualizar (dic_alumnos)   
    elif opcion == 4:
        eliminar (dic_alumnos)           
    elif opcion == 5:
        grabar ('alumnos.txt')
        salir ()
    else:
        mostrar_mensaje ("¡OPCIÓN NO VÁLIDA!")
        
    sleep (1)
