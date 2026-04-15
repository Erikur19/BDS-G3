#Importando Operating System
import os
from time import sleep

#Variables y constantes
respuesta = True

TC_COMPRA = 3.6
TC_VENTA = 3.7

while (respuesta == True):
    print ("""
           ========================================================
                            CONVERSOR DE DIVISAS                    
           ========================================================
           [1] CONVERTIR SOLES A DÓLARES
           [2] CONVERTIR DÓLARES A SOLES
           [3] SALIR                                                """)
    
    conv = int(input ("Indique la opción que desea: "))
    if (conv == 1):
        print ("======= CONVERSOR DE SOLES (PEN) A DÓLARES (USD) =========")
        print (f"El tipo de cambio de venta es 1 USD = {TC_VENTA} soles")
        print("""
              
              """)
        entrada = float (input("INGRESE EL MONTO EN SOLES: "))
        salida = entrada/TC_VENTA
        sal_red = round(salida,2)
        print (f"Te damos {sal_red} dólares por tus {entrada} soles ")

    elif (conv == 2):
        print ("======= CONVERSOR DE DÓLARES (USD) A SOLES (PEN) =========")
        print (f"El tipo de cambio de venta es 1 USD = {TC_COMPRA} soles")
        print("""
              
              """)
        entrada = float (input("INGRESE EL MONTO EN SOLES: "))
        salida = entrada*TC_COMPRA
        sal_red = round(salida,2)
        print (f"Te damos {sal_red} soles por tus {entrada} dólares ")

    elif (conv == 3):
        respuesta = False
        print ("""=======================================================
                            SALIENDO DEL PROGRAMA                     
                =========================================================== """)
    
    else: 
        print ("""=======================================================
                            LA OPERACIÓN NO EXISTE                      
                =========================================================== """)
        
    sleep (3)
    os.system ("clear")