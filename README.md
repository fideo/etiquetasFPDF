# Generación de Etiquetas
Programa en Python para generar un PDF en base a una lista de articulos cargados en un archivo de texto.

Lo generé para poder realizar de forma sencilla y rápida varias etiquetas en formato PDF para que luego sean impresas en una impresora con ribbon; en mi caso una impresora Zebra.

## Instalación
  1- Montar la variable de entorno env de virtualenv

  2- Correr pip install -r requirements.txt

  3- Para realizar el .exe en Windows ejecutar pyinstaller.exe --windowed --onefile y extraerlo del directorio dist y pegarlo en la raiz.

## Uso
Para cargar los datos debemos acceder al directorio assets y buscar el archivo data.txt

Cada linea que se ingresa en ese archivo de texto será una etiqueta nueva

Si se está usando la etiqueta que generé para la empresa donde trabajo (crea_pdfArgenchemical.py) este tomo los datos del archivo dataArgenchemical.txt donde si el nombre del producto contiene la palabra polvo este muestra la unidad de medida en K (Kilogramos) en lugar de L (Litros)

Espero que le pueda servir a alquien mas esto.

Enjoy!!
