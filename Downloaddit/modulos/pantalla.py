import os
from art import *  # Importamos "art" para los diseños to' bonitos
from modulos.sistema import cls  # Importamos funcion para limpiar consola


def pantalla():  # Creamos funcion para limpiar y mostrar informacion en consola
    cls()
    tprint("Downloaddit")
    credits()

def pantalla_dupli():
    cls()
    nombre_dupli = "DupliTP"
    tprint(f"{nombre_dupli:^35}")
    credits()

def separador():  # separador con "="
    print("=" * 70) 

def credits():
    lucy = "LUCYFER"  # Variable con mi nombre to' bonito...
    print(f"{lucy:=^71}")  #... y lo centramos usando "=" de relleno
    print()

def mensaje(): # Mensaje de espera
    mensaje = "Algunas descargas pueden tardar más de lo esperado\n♥ No cierre la consola ♥"
    lineas = mensaje.split('\n')
    for linea in lineas:
        print(f"{linea:^71}")
    print()

def imprimir_duplicados(duplicados):
    for file_hash, file_list in duplicados.items():
        if len(file_list) > 1:
            print("="*50)
            file_name = os.path.basename(file_list[0])
            print(f"Duplicados de {file_name}:")
            for file_path in file_list[1:]:
                print(f"   {os.path.basename(file_path)}")
            print("="*50)

def msg_descarga(): # Mensaje de termino de descarga
    msg_desc = "♥ Se finalizó la tarea ♥"
    print(f"{msg_desc:^71}")
    print()