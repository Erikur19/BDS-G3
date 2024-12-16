ancho = 20


dic_empresas = {}

def cargar_empresas(file_name):
    file = open(file_name,'r')
    str_empresas = file.read()
    file.close()
    lista_empresas = str_empresas.splitlines()
    for str_row in lista_empresas:
        list_row = str_row.split(',')
        dic_row = {
            'nombre':list_row[1],
            'email':list_row[2]
        }
        dic_nueva_empresa = {
            list_row[0]: dic_row
        }
        dic_empresas.update(dic_nueva_empresa)

def grabar_empresas(file_name):
    str_empresas = ""
    for empresa_clave,empresa_valor in dic_empresas.items():
        str_empresa += empresa_clave + ","
        for registro_clave,registro_valor in empresa_valor.items():
            str_empresas += registro_valor
            if registro_clave != 'email':
                str_ += ','
            else:
                str_empresas += '\n'
    
    fsalida = open(file_name,'w')
    fsalida.write(str_empresas)
    fsalida.close()
    



def mostrar_mensaje(texto):
    print(texto)

def menu():
    main_menu = print([f"[1] REGISTRAR EMPRESA"]
                      [f"[2] MOSTRAR EMPRESAS"],
                      [f"[3] ACTUALIZAR EMPRESA"],
                      [f"[4] ELIMINAR EMPRESA"],
                      [f"[5] SALIR"])
    
    

def registrar():
    mostrar_mensaje("[1] REGISTRAR EMPRESA")
    RUC = input("RUC    :")
    razon_social = input("RAZONSOCIAL  :")
    email = input("EMAIL    :")
    dic_nueva_empresa = {
        RUC : {
                'razon_social': razon_social,
                'email': email
                }
    }
    dic_empresas.update(dic_nueva_empresa)

def mostrar():
    mostrar_mensaje("[2] MOSTRAR EMPRESAS")
    data = []
    for RUC,datos in dic_empresas.items():
        empresa_row = [RUC,datos['RAZONSOCIAL'],datos['email']]
        data.append(empresa_row)
    print(data)
        

def actualizar():
    mostrar_mensaje("[3] ACTUALIZAR EMPRESA")
    RUC = input("INGRESE RUC DE EMPRESA A ACTUALIZAR")
    if RUC in dic_empresas:
        print(f"EMPRESA A ACTUALIZAR  {dic_empresas[RUC]['RAZONSOCIAL']}")
        nueva_razon_social = input('RAZÓN SOCIAL : ')
        nuevo_email = input('EMAIL :')
        dic_act_empresa = {
            RUC : {
                'nombre':nueva_razon_social,
                'email':nuevo_email
            }
        }
        dic_empresas.update(dic_act_empresa)
        print("ALUMNO ACTUALIZADO CON EXITO")

def eliminar():
    mostrar_mensaje("[4] ELIMINAR EMPRESA")
    RUC = input("INGRESE EL RUC DE LA EMPRESA A ELIMINAR : ")
    if RUC in dic_empresas:
        dic_empresas.pop(RUC)
        print("EMPRESA ELIMINADA")
    else:
        print("EMPRESA NO ENCONTRADA")