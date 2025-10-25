dias = ['lunes', 'martes', 'miércoles']
print(dias)
print (dias[-1])
print (dias[1:3])


#agregar valores a la lista

dias.append('jueves')
dias.append('viernes')
print (dias)

#eliminar un valor de la lista
dias.pop(3)
print (dias)
del dias[2:4]
print (dias)


#agregar una lista al final (no solo un valor)
dias.extend (['miércoles', 'viernes'])
print(dias)
#agregar un valor en una posición específica.
dias.insert (3, 'jueves')
print(dias)

#actualizar un valor
dias[2] = "mié_act"
print (dias)

dias[2] = "miércoles"
print (dias)

#recorrer una lista

#forma1 (más larga)
for contador in range (len(dias)):
    print(dias[contador])

print ("===============================")

#forma2 (más corta)
for dia in dias:
    print (dia)