#HARE UNA TABLA DE MULTIPLICAR DE UN NRO QUE QUIERA

#ENTRADA
print ("MI TABLA DE MULTIPLICAR")
multiplicador = input("¿De qué número deseas la tabla?")
multiplicador = int (multiplicador)

#PROCESO y SALIDA
for contador in range (1,13):
    print(f"{contador} x {multiplicador} = {contador*multiplicador}")

    
