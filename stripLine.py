import os
#os.system('awk')

ruta_archivo_productos = './dataArgenchemical.txt'
fichero = open(ruta_archivo_productos)
lineas = fichero.readlines()
for linea in lineas:
  if linea != "\n":
    producto = (linea.split())
    print(producto[0])
    print(" ".join(producto[1:]))
    pass


# ejecuto awk en python
#cantidad = os.system('awk \'{print $1}\' ./dataArgenchemical.txt')
#print(cantidad)
#producto = os.system('awk \'{print substr($0, index($0,$2))}\' ./dataArgenchemical.txt ')

fichero.close()
