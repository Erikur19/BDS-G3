dias = ('lunes', 'martes', 'jueves', 'viernes')
print (dias)
print (type(dias))
#Como la tupla es inmutable, no puedo modificarla (agregar o quitar) 
#Pero sí puedo convertirla a lista

#convirtiendo a lista
dias = list(dias)
print (type(dias))

#modificando
dias.insert(2,"miércoles")
print (dias)

#convirtiendo a tupla otra vez
dias = tuple (dias)
print (type (dias))

#recorrer una tupla
for dia in dias:
    print(dia)