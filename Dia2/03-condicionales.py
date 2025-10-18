print ("MI CALCULADORA")

#ENTRADA
numero1 = input ("Numero 1 : ")
numero2 = input ("Numero 2 : ")
operacion = input ("¿Qué operación matemática desea hacer? (1 SUMA | 2 RESTA | 3 MULTIPLICACION | 4 DIVISION)")

#PROCESO
if (operacion == "1"):
    resultado = int (numero1) + int (numero2)
elif (operacion == "2"):
    resultado = int (numero1) - int (numero2)
elif (operacion == "3"):
    resultado = int (numero1) * int (numero2)
elif (operacion == "4"):
    resultado = int (numero1) / int (numero2)
else:
    print ("LA OPERACION NO EXISTE")
    exit ()

#SALIDA

print (f"La {operacion} de {numero1} y {numero2} es {resultado}")