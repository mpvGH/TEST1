from os import system
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
    print('Has elegido la opción 1')
    input()


def listar_trabajador():
    print('Has elegido la opción 2')
    input()


def imprimir_trabajador():
    print('Has elegido la opción 3')
    input()


def salir():
    print('Saliendo')


menu_principal()