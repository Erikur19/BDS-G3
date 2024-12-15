###Tuplas: son iguales que las listas pero son inmutables (no pueden cambiar sus valores). Se usa para guardar constantes
###que no cambiarán

dias = ('lunes', 'martes', 'miércoles', 'jueves')

#PARA AGREGAR DATOS A LA TUPLA
dias = list(dias)
print(type (dias))
dias.append('viernes')
dias = tuple(dias)
print(dias)
print(type (dias))