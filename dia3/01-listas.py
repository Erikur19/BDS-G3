dias = ['lunes', 'martes', 'miércoles']
print(dias[1])
print(dias[1:3])
print(dias[-1])
print(dias[:])

#Agregar valores a la lista
dias.append('jueves')
dias.append('viernes')
print (dias)

dias.pop(3)
print (dias)
print(dias[0])
print (dias[1])
print(dias[2])

del dias[0:2]   
print(dias)
 
dias[1] ='act'
print(dias)

dias[1] = 'viernes'
print(dias)

dias.insert(0, 'lunes')
print(dias)
dias.insert(1, 'martes')
print(dias)
dias.insert(3, 'jueves')
print(dias)
dias. insert(5, 'sábado')
print(dias)

for contador in range(len(dias)):
    print(dias[contador])

print("Con otro método")
for dia in dias:
    print(dia)

