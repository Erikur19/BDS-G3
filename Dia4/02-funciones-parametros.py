#parametros args y kwargs
def suma_infinita (args):
    resultado = 0
    for n in args:
        resultado = resultado + n
    return resultado

suma1 = suma_infinita ([1,2,3,4])
print (suma1)

suma2 = suma_infinita ([1,2])
print (suma2)

#operando con kwargs

def calculadora(**kwargs):
    ope = kwargs['ope']
    n1 = kwargs ['n1']
    n2 = kwargs ['n2']

    if ope == "suma":
        resultado = n1 + n2
        print (f"La {ope} de {n1} y {n2} es {resultado}")
    elif ope == "resta":
        resultado = n1-n2
        print (f"La {ope} de {n1} y {n2} es {resultado}")
    elif ope == "multiplicación":
        resultado = n1*n2
        print (f"La {ope} de {n1} y {n2} es {resultado}")
    elif ope == "división":
        resultado = n1/n2
        print (f"La {ope} de {n1} y {n2} es {resultado}")
    else:
        print ("No existe la operación indicada")

suma3 = calculadora(n1=5, n2=3, ope = 'suma')
resta1 = calculadora(n2 = 10, n1= 22, ope = 'resta')
multip1 = calculadora(n1=20, n2=10,ope= "multiplicación")
division1 = calculadora(ope='división', n2=25, n1=5)
