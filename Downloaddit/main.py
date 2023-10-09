import os
import time
from art import *
from modulos.pantalla import ( # Importamos mensajes en pantalla
    pantalla,
    pantalla_dupli,
    msg_descarga,
    imprimir_duplicados,
    # duplicados_terminados,
)
from modulos.descargas import ( # Funciones para las descargas
    descargar_reddit,
    descargar_lista,
)
from modulos.funciones import (
    obtener_ruta_directorio,
    crear_directorio_duplicados,
    procesar_archivos_duplicados,
    # imprimir_duplicados
)

def opcion(respuesta, opcion_valida):
    while True:
        try:
            opcion = int(input(respuesta))
            if opcion in opcion_valida: # Bucle para verificar que la opcion del usuario sea corecta...
                return opcion
            else: #... caso contrario se repite la pregunta
                pantalla()
        except ValueError:
            pantalla()

def main(): 
    while True:
        pantalla()
        opcion1 = opcion(
            "Ingresa el digito correspondiente:\n1. Un link\n2. Varios links\n3. Usar DupliTP (eliminar repetidos)\n4. Salir\n\n> ",
            [1, 2, 3, 4]
        )

        if opcion1 == 1:
            pantalla()
            url = input("Ingrese el URL (pulsa click derecho para pegar link):\n> ")
            descargar_reddit (url)
        elif opcion1 == 2:
            pantalla()
            descargar_lista()
        elif opcion1 == 3:
            pantalla_dupli()
            directory_path = obtener_ruta_directorio()

            pantalla_dupli()
            carga = "CARGANDO..."
            print(f"{carga:^71}")

            try:
                carpeta_duplicados = crear_directorio_duplicados(directory_path)
                duplicados = procesar_archivos_duplicados(directory_path, carpeta_duplicados)

                pantalla_dupli()
                print(imprimir_duplicados(duplicados))
                time.sleep(5)

            except FileNotFoundError as e:
                print(f"Error: No se encontró el archivo o directorio: {e.filename}")
            except PermissionError as e:
                print(f"Error: Permiso denegado para acceder a {e.filename}")
            except Exception as e:
                print(f"Error desconocido: {str(e)}")
        else:
            break
        
        time.sleep(2)
        pantalla()
        msg_descarga()

        respuesta = input("¿Deseas hacer otra tarea (Y/N)? ").strip().lower()
        if respuesta != 'y':
            break

if __name__ == "__main__":
    main()
