capitales = {
            'Peru' : 'Lima',
            'Ecuador' : 'Quito',
            'Chile' : 'Santiago',
            'Colombia' : 'Bogotá'
}

print ('='*25 + "RECORRIDO POR CLAVES" + "="*25)
#recorrido por claves
for clave in capitales.keys():
    print (clave)

print('='*25+"RECORRIDO POR VALORES"  + "="*25)
#recorrido por valores
for valor in capitales.values():
    print(valor)

print("="*25 + "RECORRIDO POR CLAVE, VALOR" + "="*25)
#recorrido por clave, valor
for clave, valor in capitales.items():
    print(f'la capital de {clave} es {valor}')
