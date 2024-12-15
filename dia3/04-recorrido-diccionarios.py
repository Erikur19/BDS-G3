capitales = {
            'Perú':'Lima',
            'Ecuador': 'Quito',
            'Colombia': 'Bogota',
            'Chile' : 'Santiago'    
            }

print("="*50 + "recorrido por claves")
for clave in capitales.keys():
    print(clave)

print("="*50)

print("="*50 + "recorrido por valores")
for valor in capitales.values():
    print(valor)

print("="*50)

print("="*50 + "recorrido por clave y valor")
for clave, valor in capitales.items():
    print(f'la capital de {clave} es {valor}')

print("="*50)