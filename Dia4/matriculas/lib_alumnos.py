
ANCHO = 50

def mostrar_mensaje (texto):
    print ("="*ANCHO)
    if texto != " ":
        print ("="*ANCHO)
        print (texto)
        print ("="*ANCHO)


def menu ():
    mostrar_mensaje ("GESTIÓN DE ALUMNOS")
    print ("""
            [1] REGISTRAR ALUMNO
            [2] MOSTRAR ALUMNO
            [3] ACTUALIZAR ALUMNO
            [4] ELIMINAR ALUMNO
            [5] SALIR
           """)
    mostrar_mensaje(" ")



def registrar ():
    mostrar_mensaje ("REGISTRAR ALUMNO")
    dni = input ("Ingrese su número de DNI  ")
    nombre = input ("Ingrese su Nombre  ")
    email = input ("Ingrese su correo electrónico  ")
    dic_alumno_nuevo = {
                dni : {
                    'nombre': nombre,
                    'email': email, 
                }
    }
    mostrar_mensaje(" ")

    return dic_alumno_nuevo

def mostrar (dic_alumnos):
    mostrar_mensaje ("MOSTRAR ALUMNO")
    for dni, datos in dic_alumnos.items():
        print ("="*ANCHO)
        print (f"DNI: {dni}")
        print (f"NOMBRE: {datos['nombre']}")
        print (f"EMAIL: {datos['email']}")
    mostrar_mensaje(" ")
    input ("PRESIONE ENTER para continuar...")

def actualizar (dic_alumnos):
    dni = input ("Ingrese DNI de alumno a actualizar: ")
    if dni in dic_alumnos:
        mostrar_mensaje ("ACTUALIZAR ALUMNO")
        print (f"ALUMNO A ACTUALIZAR: {dni} || {dic_alumnos[dni]['nombre']}")
        act_nombre = input ("INGRESE NOMBRE ACTUALIZADO   ")
        act_email = input ("INGRESE EMAIL ACTUALIZADO   ")
        dic_act_alumno = {
                    dni : {
                        'nombre': act_nombre,
                        'email': act_email
                    }
        }
        dic_alumnos.update (dic_act_alumno)
    mostrar_mensaje(" ")
    return dic_act_alumno


def eliminar (dic_alumnos):
    mostrar_mensaje ("ELIMINAR ALUMNO")
    dni = input ("INGRESE EL DNI DEL ALUMNO A ELIMINAR  ")
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
    mostrar_mensaje(" ")

def salir ():
    mostrar_mensaje ("SALIENDO DEL PROGRAMA")
