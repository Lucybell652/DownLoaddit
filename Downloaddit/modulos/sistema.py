import datetime as dt  # Importamos tiempo de la PC del usuario
import os

def cls():  # Funcion para limpiar consola
    os.system("cls") 

def obtener_nombre():  # Funcion para crear el nombre del archivo a descargar usando la hora del usuario
    fecha_hora_actual = dt.datetime.now()
    nombre = str(fecha_hora_actual.strftime("%d%m%y-%H%M%S"))
    return nombre

def ruta_fin_reddit():  # Funcion para definir la ruta donde se guardarán los archivos descargados
    descargas_path = os.path.join(os.path.expanduser("~"), "Downloads")
    carpeta_reddit = os.path.join(descargas_path, "Reddit")
    if not os.path.exists(carpeta_reddit):
        os.makedirs(carpeta_reddit)
    return carpeta_reddit
