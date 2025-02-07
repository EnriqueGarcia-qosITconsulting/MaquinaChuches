""" 
Programa de máquina expendedora de chuches.

Las funciones de la máquina son:
1.Comprar
2.Mostrar productos
3.Rellenar productos (con contraseña para acceder, que es: ME2025)
4.Apagar la máquina (muestra las ventas totales)
"""

fichero = open('chuches.txt','r')
tamañoLista = int(fichero.readline())
productos = []
precios = []
cantidad = []
productosVendidos = []

#Introduce los datos del fichero en las listas
for i in range(tamañoLista):
    productos.append(fichero.readline().rstrip().split(','))
for i in range(tamañoLista):
    fila = [float(numero) for numero in fichero.readline().strip().split(',')]
    precios.append(fila)
for i in range(tamañoLista):
    fila = [int(numero) for numero in fichero.readline().strip().split(',')]
    cantidad.append(fila)
fichero.close()
productosVendidos = [[0 for _ in range(len(productos[0]))] for _ in range(len(productos))]

#Comprueba que la posición de la chuche seleccionada sea correcta
def compruebaPosicion(posicion):
    repetir = False
    if len(posicion) < 1 or len(posicion) > 2:
        repetir = True
        return repetir
    try:
        fila = int(posicion[0])
        columna = int(posicion[1])
    except:
        repetir = True
        return repetir
    if fila < 0 or fila > 3: 
        repetir = True
        return repetir
    if columna < 0 or columna > 3: 
        repetir = True
        return repetir
    return repetir

#Se seleccionará un producto. Si hay existencias se le restará a la cantidad y aumentará un valor en los productos vendidos. De lo contrario no lo hará y volverá al menú
def pedirChuches(productos,precios,cantidad,productosVendidos):
    repetir = True
    while repetir:
        repetir = False
        print("Elija un producto")
        posicion = input()
        repetir = compruebaPosicion(posicion)
        if repetir:
            print("Posición no válida")
    fila = int(posicion[0])
    columna = int(posicion[1])
    if cantidad [fila][columna] == 0:
        print("Producto agotado")
        print()
        return
    else:
        productosVendidos[fila][columna] += 1
        cantidad[fila][columna] -= 1
        print("Has comprado",productos[fila][columna])
        print()

#Muestra los productos con su precio y posición en la máquina
def mostrarChuches(productos,precios):
    for f in range(len(productos)):
        for c in range(len(productos[f])):
            posicion = str(f)
            posicion += str(c)
            print(productos[f][c],"precio:",precios[f][c],"posición:",posicion)

#Rellena los productos de la máquina. Se selecciona una posición y la cantidad a rellenar. No se puede quitar productos
def rellenarMaquina(productos,cantidad):
    relleno = 0
    contraseña = "ME2025"
    print("Introduzca la contraseña")
    intento = input()
    if contraseña != intento:
        print("Contraseña erronea")
        return
    repetir = True
    while repetir:
        repetir = False
        print("Elija un producto")
        posicion = input()
        repetir = compruebaPosicion(posicion)
        if repetir:
            print("Posición no válida")
    fila = int(posicion[0])
    columna = int(posicion[1])
    print("Elija la cantidad a rellenar")
    try:
        relleno = int(input())
    except:
        print("Error")
    if relleno == 0:
        print("No se ha rellenado nada")
        return
    if relleno < 0:
        print("Valor negativo. No se puede quitar productos de la máquina")
        return
    cantidad[fila][columna] += relleno
    print("Se ha rellenado",relleno,productos[fila][columna])
    return
#
def apagarMaquina(productos,precios,productosVendidos):
    print("==================")
    total = 0.0
    for f in range(len(productos)):
        for c in range(len(productos[f])):
            if productosVendidos[f][c] > 0:
                print(productosVendidos[f][c],productos[f][c],":",precios[f][c]*productosVendidos[f][c])
                total += precios[f][c]*productosVendidos[f][c]
    print("\n Total :",round(total,2))
    print("==================")
    return
#Menú de la máquina con selección de opción
repetir = True
repetirOpcion = True
opcion = 0
while repetir:
    print("Introduzca una opción")
    print("1.Pedir chuches")
    print("2.Mostrar chuches")
    print("3.Rellenar chuches")
    print("4.Apagar máquina")
    repetirOpcion = True
    while repetirOpcion:
        try:
            repetirOpcion = False
            opcion = int(input(""))
        except:
            repetirOpcion = True
            print("Opción erronea")
        else:
            if opcion < 1 or opcion > 4:
                repetirOpcion = True
                print("Opción erronea")
    match opcion:
        case 1:
            pedirChuches(productos,precios,cantidad,productosVendidos)
        case 2:
            mostrarChuches(productos,precios)
        case 3:
            rellenarMaquina(productos,cantidad)
        case 4:
            apagarMaquina(productos,precios,productosVendidos)
            repetir = False