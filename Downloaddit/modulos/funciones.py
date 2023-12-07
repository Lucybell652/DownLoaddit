import os
import hashlib
import shutil

def calcular_hash(file_path):
    sha256 = hashlib.sha256()
    with open(file_path, "rb") as f:
        while True:
            data = f.read(65536)
            if not data:
                break
            sha256.update(data)
    return sha256.hexdigest()

def obtener_ruta_directorio():
    print("Ingrese la ruta del directorio que desea analizar: ")
    directory_path = input("> ")
    if not isinstance(directory_path, str):
        raise ValueError("Error: La ruta ingresada no es una cadena válida.")
    if not os.path.isdir(directory_path):
        raise ValueError("Error: La ruta no es un directorio válido.")
    return directory_path

def crear_directorio_duplicados(directory_path):
    carpeta_duplicados = os.path.join(directory_path, "duplicados")
    if not os.path.exists(carpeta_duplicados):
        os.makedirs(carpeta_duplicados)
    return carpeta_duplicados

def procesar_archivos_duplicados(directory_path, carpeta_duplicados):
    duplicados = {}
    for root, dirs, files in os.walk(directory_path):
        for filename in files:
            file_path = os.path.join(root, filename)
            file_hash = calcular_hash(file_path)

            if file_hash in duplicados:
                duplicados[file_hash].append(file_path)
            else:
                duplicados[file_hash] = [file_path]

    for file_hash, file_list in duplicados.items():
        if len(file_list) > 1:
            for file_path in file_list[1:]:
                mover_a_duplicados(file_path, carpeta_duplicados)
    return duplicados

def mover_a_duplicados(file_path, carpeta_duplicados):
    duplicate_path = os.path.join(carpeta_duplicados, os.path.basename(file_path))
    shutil.move(file_path, duplicate_path)
