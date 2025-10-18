## IMPRIMIENDO TÍTULO
print ("=============== CONVERSOR DE DIVISAS ==================")
respuesta = "SI"
TC_COMPRA = 3.6
TC_VENTA = 3.7
while (respuesta == "SI"):
    tipo = int(input("""¿Qué desea convertir? 
                     1) SOLES A DÓLARES
                     2) DÓLARES A SOLES
                     
                     """))

    if (tipo == 1):
        print ("======= CONVERSOR DE SOLES (PEN) A DÓLARES (USD) =========")
        print (f"El tipo de cambio de venta es 1 USD = {TC_VENTA} soles")
        print("""
              
              """)
        monto = int (input("INGRESE EL MONTO EN SOLES:  "))
        resultado = round(monto/TC_VENTA,2)
        print (f"Te damos {resultado} dólares por tus {monto} soles ")
    elif (tipo == 2):
        print ("======= CONVERSOR DE DÓLARES (USD) A SOLES (PEN) =========")
        print (f"El tipo de cambio de compra es 1 USD = {TC_COMPRA} soles")
        print("""
              
              """)        
        monto = int (input("INGRESE EL MONTO EN DÓLARES:  "))
        resultado = round(monto*TC_COMPRA,2)
        print (f"Te damos {resultado} soles por tus {monto} dólares  ")
    else: 
        print ("Esta opción no existe")


    respuesta = input ("""¿Desea realizar otra conversión?   SI  |  NO  
                       
                       
                       """)

