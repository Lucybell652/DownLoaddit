from RedDownloader import RedDownloader as rd
from modulos.sistema import (
    obtener_nombre,
    ruta_fin_reddit,
)
from modulos.pantalla import (
    pantalla,
    separador as sp, # Separador
    mensaje as msg, # Pantalla predeterminada
)
import time


def descarga(url, nombre):  # Funcion con comando de descarga
    try:
        rd.Download(url, output=nombre, destination = ruta_fin_reddit())  # Descarga
        print(f"Descarga exitosa: {nombre}")
    except Exception as e:
        print(f"La descarga falló para {nombre}: {str(e)}")


def descargar_reddit(url):  # Funcion para descarga individual
    try:
        pantalla()
        msg()
        sp()
        nombre = obtener_nombre()  # Pedimos el nombre que se creó en el modulo
        descarga(url, nombre)
        sp()
        time.sleep(2)
    except Exception as e:  # Si la descarga falla...
        print(f"La descarga falló: {str(e)}")  # ...indicamos cuàl fue el error


def descargar_contador(links_descarga):  # Funcion para llevar un contador en la descarga de lista
    try:
        pantalla()
        msg()
        total_links = len(links_descarga)  # Contamos cuantos links hay en la lista
        contador = 0

        for url in links_descarga:
            contador += 1
            sp()
            print(f"Descarga {contador}/{total_links}") 
            nombre = obtener_nombre()
            descarga(url, nombre)
            sp()
            time.sleep(2)
            pantalla()
    except Exception as e:
        print(f"Error general: {str(e)}")


def descargar_lista():  # Funcion de la descarga por lista
    pantalla()
    links_descarga = []  # Creamos la lista donde se guardarán los links
    try:
        print('Pegue el enlace (pulsa click derecho para pegar) y pulse "enter" para agregar\nEscriba "Fin" cuando termine:')
        while True:
            url = input("> ")  # Solicitamos al usuario los links
            if (url.lower() == "fin"):  # Verificamos si el usuario desea terminar el bucle
                break

            links_descarga.append(url)

        descargar_contador(links_descarga)
    except Exception as e:
        print(f"La descarga falló: {str(e)}")
