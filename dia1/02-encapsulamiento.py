class Usuario:
#En este caso le estoy fijando variables, no quiero que reciba
#valores, sino que el email y password sean fijos para compararlo
#contra el valor que ingrese el usuario.
#sea el método constructor
    __email = 'ecabrera@gmail.com'
    __password ='querty123'

#Aquí creo el método init pero sin mayor relevancia, no es que
#sea el método constructor
    def __init__(self):
        pass

    def set_password (self, password):
        self.__password = password

    def login(self, email, password):
        if (self.__email == email and self.__password == password):
            print (f"Bienvenido{self.__email}")
        else:
            print ('datos incorrectos')

    

print ('LOGIN DE USUARIOS')
email = input ('Ingresa el email:  ')
password = input ('Ingresa el password:  ')

user = Usuario()
user.set_password(password)
user.login (email, password)


