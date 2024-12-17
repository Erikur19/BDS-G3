class Persona:
    def __init__ (self, dni, nom, ema):
        self.dni = dni
        self.nombre = nom
        self.email = ema
    
    def mostrar(self):
        print("*"*30)
        print(f"DNI: {self.dni}")
        print(f"NOMBRE: {self.nombre}")
        print(f"EMAIL: {self.email}")


class Alumno (Persona):
    def __init__ (self, dni, nom, ema, nota):
        super().__init__(dni, nom, ema)
        self.nota = nota
    def mostrar (self):
        super().mostrar()
        print(f"NOTA: {self.nota}")


class Profesor (Persona):

    def __init__(self, dni, nom, ema, esp):
        super().__init__(dni, nom, ema)
        self.especialidad = esp
    
    def mostrar (self):
        super().mostrar()
        print(f"ESPECIALIDAD : {self.especialidad}")


class Empleado (Persona):
    pass


alumno1 = Alumno("1111", "JUAN PEREZ", "jp@gmail.com", 20)
print ("DATOS ALUMNO" + "*"*40)
alumno1.mostrar()
print ("*"*50)

profesor1 = Profesor("2222", "CARLOS GARCIA", "cg@gmail.com", "MACHINE LEARNING")
print ("DATOS PROFESOR" + "*"*40)
profesor1.mostrar()
print ("*"*50)

empleado1 = Empleado("4444","JOSE CALMET", "jc@gmail.com")
print ("DATOS EMPLEADO" + "*"*40)
empleado1.mostrar()
print ("*"*50)



