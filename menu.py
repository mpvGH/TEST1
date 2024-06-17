from os import system
lista_trabajador = []
def menu_principal():
    opciones = {
        '1': ('Opción 1', reg_trabajador),
        '2': ('Opción 2', listar_trabajador),
        '3': ('Opción 3', imprimir_trabajador),
        '4': ('Salir', salir)
    }

    generar_menu(opciones, '4')

def generar_menu(opciones, opcion_salida):
    opcion = None
    while opcion != opcion_salida:
        system("cls")
        mostrar_menu(opciones)
        opcion = leer_opcion(opciones)
        ejecutar_opcion(opcion, opciones)
        print() # se imprime una línea en blanco para clarificar la salida por pantalla

def mostrar_menu(opciones):
    print('Seleccione una opción:')
    for clave in sorted(opciones):
        print(f' {clave}) {opciones[clave][0]}')

def leer_opcion(opciones):
    while (a := input('Opción: ')) not in opciones:
        print('Opción incorrecta, vuelva a intentarlo.')
    return a

def ejecutar_opcion(opcion, opciones):
    opciones[opcion][1]()


def reg_trabajador():
    # Para registrar un trabajador se requiere los siguiente: Nombre y Apellido, Cargo, Sueldo bruto.
    # desc.salud 7%, desc. afp 12%, líquido = restante
    print('Has elegido la opción 1')
    dic_reg_trabajador = {}
    dic_reg_trabajador['nombre'] = input("Ingrese el nombre y apellido del usuario.")
    dic_reg_trabajador['cargo'] = input("Ingrese el cargo del usuario.")
    dic_reg_trabajador['sueldo'] = input("Ingrese el sueldo del usuario")
    dic_reg_trabajador['desc_salud'] = float(dic_reg_trabajador['sueldo'])/100*7
    dic_reg_trabajador['desc_afp'] = float(dic_reg_trabajador['sueldo'])/100*12
    dic_reg_trabajador['liquido'] = float(dic_reg_trabajador['sueldo'])-dic_reg_trabajador['desc_salud']-dic_reg_trabajador['desc_afp']
    lista_trabajador.append(dic_reg_trabajador)

    #CAMBIO CUALQUIERA
    #BLABLA


def listar_trabajador():
    print('Has elegido la opción 2')
    for i in lista_trabajador:
        print(i)
    input()


def imprimir_trabajador():
    print('Has elegido la opción 3')
    input()


def salir():
    print('Saliendo')


menu_principal()