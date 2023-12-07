import os
import time
from art import *
from modulos.sistema import cls


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
    lucy = "LUCYFER"
    print(f"{lucy:=^71}")  #centramos usando "=" de relleno
    print()

def mensaje(): # Mensaje de espera
    mensaje = "Algunas descargas pueden tardar más de lo esperado\n♥ No cierre la consola ♥"
    lineas = mensaje.split('\n') #Uso \n como separador...
    for linea in lineas:
        print(f"{linea:^71}") #...para centrar el texto dividido en lineas.
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

def barraProgreso(segmento, total, longitud):
    porcentaje = segmento/total
    completado = int(porcentaje * longitud)
    restante = longitud - completado
    barra = f"[{"#" * completado}{"·" * restante}{porcentaje:.2%}]"
    return barra
