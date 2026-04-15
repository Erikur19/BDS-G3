from tabulate import tabulate

data = [
    ["100", "erick cabrera", "ec@gmail.com"],
    ["200", "pepito juarez", "pj@gmail.com"],
    ["200", "ana salinas", "as@gmail.com"]
]

columnas = ["DNI", "NOMBRE", "EMAIL"]

tabla = tabulate (data, headers = columnas, tablefmt="rounded_grid")

# puedo tener más formatos de aquí: https://pypi.org/project/tabulate/

print (tabla)