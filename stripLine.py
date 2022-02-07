ruta_archivo_productos = ruta_archivo_productos = './data.txt'
fichero = open(ruta_archivo_productos)
lineas = fichero.readlines()
for linea in lineas:
  if linea != "\n":
    print((linea.strip()))
fichero.close()
