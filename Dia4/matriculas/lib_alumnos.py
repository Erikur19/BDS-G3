
ANCHO = 50

def menu ():
    print ("="*ANCHO)
    print (" "*10 + "GESTIÓN DE ALUMNOS")
    print ("="*ANCHO)
    print ("""
            [1] REGISTRAR ALUMNO
            [2] MOSTRAR ALUMNO
            [3] ACTUALIZAR ALUMNO
            [4] ELIMINAR ALUMNO
            [5] SALIR
           """)
    print ("="*ANCHO)



def registrar ():
    print("="*ANCHO)
    print ("="*10 + "REGISTRAR ALUMNO")
    print ("="*ANCHO)
    dni = input ("Ingrese su número de DNI  ")
    nombre = input ("Ingrese su Nombre  ")
    email = input ("Ingrese su correo electrónico  ")
    dic_alumno_nuevo = {
                dni : {
                    'nombre': nombre,
                    'email': email, 
                }
    }
    return dic_alumno_nuevo


def mostrar (dic_alumnos):
    print("="*ANCHO)
    print ("="*10 + "MOSTRAR ALUMNO")
    print ("="*ANCHO)
    for dni, datos in dic_alumnos.items():
        print ("="*ANCHO)
        print (f"DNI: {dni}")
        print (f"NOMBRE: {datos['nombre']}")
        print (f"EMAIL: {datos['email']}")
    input ("PRESIONE ENTER para continuar")

def actualizar (dic_alumnos):
    dni = input ("Ingrese DNI de alumno a actualizar: ")
    if dni in dic_alumnos:
        print("="*ANCHO)
        print ("="*10 + "ACTUALIZAR ALUMNO")
        print ("="*ANCHO)
        print (f"ALUMNO A ACTUALIZAR: {dni} || {dic_alumnos[dni]['nombre']}")
        act_nombre = input ("INGRESE NOMBRE ACTUALIZADO")
        act_email = input ("INGRESE EMAIL ACTUALIZADO")
        dic_act_alumno = {
                    dni : {
                        'nombre': act_nombre,
                        'email': act_email
                    }
        }
        dic_act_alumno = actualizar (dni,dic_alumnos)
        dic_alumnos.update (dic_act_alumno)
    return dic_act_alumno


def eliminar (dic_alumnos):
    dni = input ("INGRESE EL DNI DEL ALUMNO A ELIMINAR")
    print("="*ANCHO)
    print ("="*10 + "ELIMINAR ALUMNO")
    print ("="*ANCHO)
    if  dni in dic_alumnos:
        print (f"ALUMNO A ELIMINAR {dni} || {dic_alumnos[dni]['nombre']}")
        confirmacion = input ("¿SEGURO DE QUE DESEA ELIMINAR ESTE ALUMNO?  SI | NO ")
        if confirmacion == "SI":
                dic_alumnos.pop (dni)
                print ("ALUMNO ELIMINADO")
        elif confirmacion == "NO":
                print ("NO SE ELIMINÓ EL ALUMNO")
        else:
                print ("RESPUESTA NO VALIDA")
    else:
            print ("NO EXISTE EL ALUMNO QUE SE DESEA ACTUALIZAR")
def salir ():
    print("="*ANCHO)
    print ("SALIENDO DEL PROGRAMA")
    print ("="*ANCHO)

def invalido ():
    print ("="*ANCHO)
    print ("OPCIÓN INVÁLIDA")
    print ("="*ANCHO)
