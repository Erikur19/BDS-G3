from tabulate import tabulate
from colorama import Fore, Back, Style

ANCHO = 50
TABLE_STYLE = "rounded_grid"
dic_alumnos = {}

def cargar_alumnos (file_name):
    file = open (file_name, 'r')
    str_alumnos = file.read ()
    file.close ()
    lista_general = str_alumnos.splitlines ()

    for fila in lista_general:
        fila_alumno = fila.split (',')
        dic_fila = {
            'nombre': fila_alumno[1],
            'email' : fila_alumno [2]
        }
        dic_alumno_nuevo = {
                fila_alumno[0]: dic_fila
                }
        dic_alumnos.update (dic_alumno_nuevo)


def mostrar_mensaje (texto):
    data = [[f'{Fore.GREEN}{texto}{Style.RESET_ALL}']]
    tabla = tabulate (data,tablefmt=TABLE_STYLE, stralign = 'center' )
    print (tabla)
    
    # print ("="*ANCHO)
    # if texto != " ":
    #     print ("="*ANCHO)
    #     print (texto)
    #     print ("="*ANCHO)


def menu ():
    data = [
            [f'{Fore.GREEN}[1] REGISTRAR ALUMNO {Style.RESET_ALL}'],
            [f'{Fore.GREEN}[2] MOSTRAR ALUMNO {Style.RESET_ALL}'],
            [f'{Fore.GREEN}[3] ACTUALIZAR ALUMNO {Style.RESET_ALL}'],
            [f'{Fore.GREEN}[4] ELIMINAR ALUMNO] {Style.RESET_ALL}'],
            [f'{Fore.GREEN}[5] SALIR {Style.RESET_ALL}']
    ]
    tabla = tabulate (data, headers = [f"{Fore.BLUE} GESTIÓN DE ALUMNOS {Style.RESET_ALL}"], tablefmt= TABLE_STYLE, stralign= 'left')
    print (tabla)



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
    mostrar_mensaje ("MOSTRAR ALUMNOS")
    data = []
    for dni, datos in dic_alumnos.items():
        alumno_fila = [dni, datos ['nombre'], datos ['email']]
        data.append (alumno_fila)

    tabla = tabulate (data, headers = ["DNI","NOMBRE", "EMAIL"], tablefmt=TABLE_STYLE, stralign = 'left')
    print (tabla)
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
    else:
            mostrar_mensaje ("NO EXISTE EL ALUMNO A ACTUALIZAR")
    return dic_alumnos
            


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

def grabar (file_name):
    str_alumnos = ""
    contador = 0
    for clave, valor in dic_alumnos.items():
        if contador > 0:
                str_alumnos += '\n'
        str_alumnos += clave
        for valor_alumno in valor.values():
                str_alumnos += ","
                str_alumnos += valor_alumno
        contador += 1
        # str_alumnos += '\n'
    f_alumnos_act = open(file_name, 'w')
    f_alumnos_act.write(str_alumnos)
    f_alumnos_act.close()

def salir ():
    mostrar_mensaje ("SALIENDO DEL PROGRAMA")
