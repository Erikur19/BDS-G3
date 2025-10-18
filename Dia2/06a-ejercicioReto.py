## IMPRIMIENDO TÍTULO
print ("=============== CONVERSOR DE DIVISAS ==================")
respuesta = "SI"
TC = 3.6
while (respuesta == "SI"):
    tipo = int(input("""¿Qué desea convertir? 
                     1) SOLES A DÓLARES
                     2) DÓLARES A SOLES
                     
                     """))

    if (tipo == 1):
        print ("======= CONVERSOR DE SOLES (PEN) A DÓLARES (USD) =========")
        print (""" El tipo de cambio es 1 USD =  3.6 PEN"""
           
           )
        monto = int (input("INGRESE EL MONTO EN SOLES:  "))
        resultado = round(monto*TC,2)
        print (f"{monto} soles equivalen a {resultado} dólares ")
    elif (tipo == 2):
        print ("======= CONVERSOR DE DÓLARES (USD) A SOLES (PEN) =========")
        print (""" El tipo de cambio es 1 PEN = 0.28 USD"""
            
            )
        monto = int (input("INGRESE EL MONTO EN DÓLARES:  "))
        resultado = round(monto*TC,2)
        print (f"{monto} dólares equivalen a {resultado} soles ")
    else: 
        print ("Esta opción no existe")


    respuesta = input ("""¿Desea realizar otra conversión?   SI  |  NO  
                       
                       
                       """)

