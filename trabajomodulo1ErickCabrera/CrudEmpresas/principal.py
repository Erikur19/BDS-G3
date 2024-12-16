import os
from lib_empresas import *


cargar_empresas('empresas.txt')
op = 0

while(op < 5):
    os.system("clear")
    menu()
    op = int(input("INGRESE OPCION : "))
    os.system("clear")
    if op == 1:
        registrar()
    elif op == 2:
        mostrar()
        input("Presione por favor ENTER para continuar...")
    elif op == 3:
        actualizar()
        input("Presione por favor ENTER para continuar...")
    elif op == 4:
        eliminar()
        input("Presione por favor ENTER para continuar...")
    elif op == 5:
        grabar_empresas('empresas.txt')
        mostrar_mensaje("[5] SALIR")
    else:
        mostrar_mensaje("LA OPCIÓN NO ES VÁLIDA!")
  