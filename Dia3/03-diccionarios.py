import os
from time import sleep

capitales = {
            'Peru' : 'Lima',
            'Ecuador' : 'Quito',
            'Chile' : 'Santiago',
            'Colombia': 'Bogotá'
}

operacion = "SI"
while (operacion == "SI"):
    pais = input ('Ingrese el país: ')
    if pais in capitales:
        capital = capitales [pais]
        print (f'La capital de {pais}  es {capital}')
        eliminarCapital = input ('¿Desea eliminar capital? (SI  | NO)    ')
        if eliminarCapital == "SI":
            capitales.pop (pais)
            print (f'NUEVA LISTA DE CAPITALES: {capitales}')
        elif eliminarCapital == "NO":
            print ('=======FINALIZANDO OPERACIÓN============')
        else:
            print ('=======OPCIÓN NO VÁLIDA============')
            print ('=======FINALIZANDO OPERACIÓN============')

    else:
        print (f'No se encontró capital de {pais}')
        
        agregarCapital = input('¿Desea agregar una nueva capital?   (SI   | NO)   ')
        if agregarCapital == "SI":
            capitalNueva = input (f'Ingrese la capital de {pais}   ')
            capitales.update({pais: capitalNueva})
            print (f'NUEVA LISTA DE CAPITALES: {capitales}')
        elif agregarCapital == "NO":
            print ('=======¡ENTENDIDO! FINALIZANDO OPERACIÓN============')
        else:
            print ('=======OPCIÓN NO VÁLIDA============')
            print ('=======FINALIZANDO OPERACIÓN============')
       
    operacion = input ('¿Desea realizar otra consulta  (SI | NO)   ')
    if (operacion == "SI" or operacion == "NO"):
        pass
    else:
            print ('=======OPCIÓN NO VÁLIDA============')
            print ('=======FINALIZANDO OPERACIÓN============')
            break

    sleep (3)
    os.system('clear')     