bandera = "SI"
while (bandera == "SI"):
    print ("================= MI CALCULADORA ================= ")
    numero1 = int(input("Número 1: "))
    numero2 = int(input("Número 2: "))
    operacion = int (input ("""¿Qué operación desea realizar?
                       1) SUMA
                       2) RESTA
                       3) MULTIPLICACION
                       4) DIVISION
                            
                        INGRESE OPCIÓN:   """))

## CONDICIONALES PARA IDENTIFICAR LA OPERACIÓN Y RESULTADO  
    if (operacion == 1):
        nomboper = "SUMA"
        resultado = numero1 + numero2
    elif (operacion == 2):
        nomboper = "RESTA"
        resultado = numero1 - numero2
    elif (operacion == 3):
        nomboper = "MULTIPLICACION"
        resultado = numero1 * numero2
    elif (operacion == 4):
        nomboper = "DIVISION"
        resultado = numero1 / numero2
    else:
        print("La operación no existe")
        
##IMPRIMIENDO RESPUESTA
    if (operacion ==1 or operacion == 2 or operacion == 3 or operacion == 4):
        print (f"La {nomboper} de {numero1} y {numero2} es {resultado}")



    
    bandera = input ("""¿Desea realizar otra operación?  
                     SI | NO
                              """)