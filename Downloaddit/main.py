import time
from modulos.pantalla import ( # Importamos mensajes en pantalla
    pantalla,
    msg_descarga,
)
from modulos.descargas import ( # Funciones para las descargas
    descargar_reddit,
    descargar_lista,
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
            "Ingresa el digito correspondiente:\n1.- Un link\n2.- Varios links\n3. Salir\n\n> ",
            [1, 2, 3]
        )

        if opcion1 == 1:
            pantalla()
            url = input("Ingrese el URL (pulsa click derecho para pegar link):\n> ")
            descargar_reddit (url)
        elif opcion1 == 2:
            pantalla()
            descargar_lista()
        else:
            break
        
        time.sleep(2)
        pantalla()
        msg_descarga()

        respuesta = input("¿Deseas hacer otra descarga (Y/N)? ").strip().lower()
        if respuesta != 'y':
            break

if __name__ == "__main__":
    main()
