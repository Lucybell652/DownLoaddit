from art import *  # Importamos "art" para los diseños to' bonitos
from modulos.sistema import cls  # Importamos funcion para limpiar consola


def pantalla():  # Creamos funcion para limpiar y mostrar informacion en consola
    cls()
    tprint("Downloaddit")
    lucy = "LUCYFER"  # Variable con mi nombre to' bonito...
    print(f"{lucy:=^71}")  #... y lo centramos usando "=" de relleno
    print()


def separador():  # separador con "="
    print("=" * 70) 


def mensaje(): # Mensaje de espera
    mensaje = "Algunas descargas pueden tardar más de lo esperado\n♥ No cierre la consola ♥"
    lineas = mensaje.split('\n')
    for linea in lineas:
        print(f"{linea:^71}")
    print()


def msg_descarga(): # Mensaje de termino de descarga
    msg_desc = "Se finalizó la descarga"
    print(f"{msg_desc:^71}")
    print()