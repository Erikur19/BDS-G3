capitales = {
            'Perú':'Lima',
            'Ecuador': 'Quito',
            'Colombia': 'Bogota',
            'Chile' : 'Santiago'    
            }

pais = input("Ingrege el país a consultar:   ")

if pais in capitales:
    capital = capitales[pais]
    print(f'la capital de {pais} es {capital}')
else: 
    nueva_capital = input(f'País no encontrado. Ingrese la capital de {pais}:   ')
    capitales.update({pais : nueva_capital})
    print(capitales)
