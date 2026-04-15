def sumar (a, b):
    resultado = int (a) + int (b)
    return resultado

print ("="*50)
print ("CALCULADORA")
print ("="*50)

n1 = input ("Ingrese el primer número: ")
n2 = input ("Ingrese el segundo número: ")
suma = sumar(n1,n2)
print (f"La suma de {n1} + {n2} es {suma}")
