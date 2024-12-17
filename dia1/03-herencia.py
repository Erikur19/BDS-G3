class Persona:
    def __init__ (self, dni, nom, ema):
        self.dni = dni
        self.nombre = nom
        self.email = ema
    
    def mostrar(self):
        print(f"DNI: {self.dni}")
        print(f"NOMBRE: {self.nombre}")
        print(f"EMAIL: {self.email}")


class Alumno (Persona):
    pass


class Profesor (Persona):

    def __init__(self, dni, nom, ema, esp):
        super().__init__(dni, nom, ema)
        self.especialidad = esp
    
    def mostrar (self):
        print(f"DNI: {self.dni}")
        print(f"NOMBRE: {self.nombre}")
        print(f"EMAIL: {self.email}")
        print(f"ESPECIALIDAD : {self.especialidad}")


alumno1 = Alumno("1111", "JUAN PEREZ", "jp@gmail.com")
print ("*"*20 + "DATOS ALUMNO" + "*"*20)
alumno1.mostrar()
print ("*"*50)

profesor1 = Profesor("2222", "CARLOS GARCIA", "cg@gmail.com", "MACHINE LEARNING")
print ("*"*20 + "DATOS PROFESOR" + "*"*20)
profesor1.mostrar()
print ("*"*50)



