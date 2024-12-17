class Automovil:
    #Creamos el método constructor
    def __init__(self, aa, pl, col, mar):
        self.año = aa
        self.placa =pl
        self.color = col
        self.marca = mar

    #métodos
    def encender (self):
        print('encender ' + self.marca)
    
    def avanzar (self):
        print('avanzar ' + self.marca)

    def acelerar (self):
        print('acelerar ' + self.marca)
    
    def frenar (self):
        print('frenar ' + self.marca)


#creamos objetos
vw = Automovil(1978, 'CO-191', 'Verde', 'Mazda')
vw.encender()
vw.avanzar()
vw.acelerar()
vw.frenar()
print("*"*50)

tico = Automovil(1999, 'ER-200', 'Rojo', 'DAEWOO')

tico.encender()
tico.avanzar()
tico.acelerar()
tico.frenar()
print("*"*50)

lambo = Automovil(2022, 'RICH-19','Azul', 'Lamborgini' )

lambo.encender()
lambo.avanzar()
lambo.acelerar()
lambo.frenar()
print("*"*50)


         