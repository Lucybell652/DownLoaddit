# Downloaddit

Este es un programa de línea de comandos llamado "Downloaddit" que te permite descargar contenido de Reddit de manera sencilla. Puedes descargar un solo enlace o varios enlaces a la vez. A continuación, se describen los principales componentes y cómo utilizar el programa.

## Requisitos Previos

Asegúrate de tener Python 3 instalado en tu sistema y las siguientes bibliotecas Python:

- `art` para el diseño de texto.
- `RedDownloader` para la descarga de contenido de Reddit.

Puedes instalar las bibliotecas faltantes utilizando el siguiente comando:

```bash
pip install art RedDownloader
```

## Cómo Usar

1. Ejecuta el programa principal `main.py` para comenzar.

```bash
python main.py
```

2. Se mostrará un menú en la consola con las siguientes opciones:

    - **1:** Descargar un solo enlace de Reddit.
    - **2:** Descargar varios enlaces de Reddit.
    - **3:** Salir del programa.

3. Si seleccionas la opción **1**, se te pedirá que ingreses un URL de Reddit. Puedes pegar el enlace utilizando el clic derecho del mouse. El programa descargará el contenido de Reddit y lo guardará en la carpeta de descargas con un nombre generado automáticamente.

4. Si seleccionas la opción **2**, puedes ingresar varios enlaces de Reddit uno por uno. Para terminar de agregar enlaces, escribe "Fin" y el programa comenzará a descargar los contenidos de Reddit uno por uno.

5. Una vez que se complete la descarga de un enlace, se mostrará un mensaje de finalización.

6. Después de cada descarga, tendrás la opción de realizar otra descarga o salir del programa.

7. Si seleccionas la opción **3**, el programa se cerrará.

## Estructura de Archivos

- `main.py`: El archivo principal que contiene el menú y controla las opciones de descarga.
- `sistema.py`: Contiene funciones para limpiar la consola y generar nombres de archivo.
- `pantalla.py`: Contiene funciones para mostrar información en la consola con diseño.
- `descargas.py`: Contiene funciones para descargar enlaces de Reddit, ya sea uno solo o varios en una lista.

## Futuras actualizaciones

- Agregar una opcion que permita borrar archivos repetidos
- Interfaz grafica

¡Disfruta de la descarga de contenido de Reddit con Downloaddit!
